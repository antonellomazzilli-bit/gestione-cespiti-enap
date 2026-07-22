import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import io

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- PANNELLO LATERALE: IMPOSTAZIONI ALIQUOTE DINAMICHE ---
with st.sidebar:
    st.header("⚙️ Impostazioni Fiscali")
    aliquota_soft = st.number_input("Aliquota Software (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    aliquota_straord = st.number_input("Aliquota Lavori Straordinari (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# --- FUNZIONI DI FORMATTAZIONE E LOGICA ---
def fmt(v):
    """Formatta i numeri nel formato italiano: 1.234,56"""
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def classifica_voce(desc, prezzo, aliq_soft, aliq_straord):
    """Analizza la descrizione e determina la classificazione fiscale"""
    desc_l = desc.lower()
    
    # 1. PRIORITÀ MASSIMA: Beni fisici
    if any(p in desc_l for p in ["porta", "copricassonetto", "infisso", "sedia", "scrivania", "pc", "computer"]):
        aliq = 12.5
        return "AA7 - Arredi/Beni", aliq, prezzo * (aliq/100), "Bene fisico rilevato: capitalizzazione forzata"
    
    # 2. Straordinaria
    if any(p in desc_l for p in ["straordinaria", "ristrutturazione", "adeguamento"]):
        return "Spese Incrementali", aliq_straord, prezzo * (aliq_straord/100), "Intervento strutturale rilevato"
        
    # 3. Servizi ordinari (Scudo)
    if any(p in desc_l for p in ["pulizia", "canone", "pitturazione", "lavori", "manodopera", "manutenzione"]):
        return "Spesa Corrente", 0.0, 0.0, "Servizio ordinario rilevato"
        
    # 4. Default
    return "AA3 - Generica", 15.0, prezzo * 0.15, "Ammortamento ordinario"

st.title("Classificatore Fatture XML")
files = st.file_uploader("Carica XML", accept_multiple_files=True)

if files:
    dati_globali_excel = []  # Contenitore cumulativo per l'esportazione finale
    
    for f in files:
        try:
            radice = ET.parse(f).getroot()
            
            # --- ESTRAZIONE INTESTAZIONE ---
            try: fornitore = radice.find('.//CedentePrestatore/DatiAnagrafici/Anagrafica/Denominazione').text
            except: fornitore = "Non specificato"
                
            try: tot_fattura = float(radice.find('.//DatiGeneraliDocumento/ImportoTotaleDocumento').text)
            except: tot_fattura = 0.0
                
            tot_iva = sum([float(i.find('Imposta').text) for i in radice.iter('DatiRiepilogo') if i.find('Imposta') is not None])
            
            st.subheader(f"📄 Fattura: {f.name} | Fornitore: {fornitore}")
            st.markdown(f"**Totale Fattura:** € {fmt(tot_fattura)} | **Totale IVA:** € {fmt(tot_iva)}")
            
            # --- ANALISI RIGHE ---
            dati_visivi = []
            for linea in radice.iter('DettaglioLinee'):
                desc = linea.findtext('Descrizione')
                prezzo = float(linea.findtext('PrezzoTotale') or 0)
                
                cat, aliq, quota, motivo = classifica_voce(desc, prezzo, aliquota_soft, aliquota_straord)
                
                # 1. Dati formattati per la visualizzazione a schermo
                dati_visivi.append({
                    "Descrizione": desc, 
                    "Valore (€)": fmt(prezzo), 
                    "Aliquota (%)": aliq, 
                    "Quota Amm. (€)": fmt(quota), 
                    "Motivo": motivo
                })
                
                # 2. Dati grezzi per l'elaborazione del file Excel
                dati_globali_excel.append({
                    "Fornitore": fornitore,
                    "File XML": f.name,
                    "Descrizione Bene/Servizio": desc,
                    "Valore Netto": prezzo,
                    "Aliquota (%)": aliq,
                    "Quota Ammortamento": quota,
                    "Categoria Fiscale": cat,
                    "Motivazione Classificazione": motivo
                })
            
            if dati_visivi:
                st.table(pd.DataFrame(dati_visivi))
            else:
                st.warning("Nessuna linea trovata nel file.")
                
        except Exception as e:
            st.error(f"Errore nella lettura del file {f.name}: {e}")
            
    # --- GENERAZIONE PULSANTE EXCEL ---
    if dati_globali_excel:
        st.markdown("---")
        st.subheader("📥 Esportazione Dati")
        
        # Converte la lista globale in un DataFrame Pandas
        df_excel = pd.DataFrame(dati_globali_excel)
        
        # Scrive il DataFrame in memoria (buffer) in formato Excel
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df_excel.to_excel(writer, index=False, sheet_name='Cespiti Elaborati')
        
        # Crea il pulsante di download interattivo
        st.download_button(
            label="📊 Scarica Riepilogo Globale in Excel",
            data=buffer.getvalue(),
            file_name="Riepilogo_Ammortamenti.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
