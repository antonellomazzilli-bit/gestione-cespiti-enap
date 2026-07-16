import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET

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

def classifica_voce(desc, prezzo_lordo, aliq_soft, aliq_straord):
    """Analizza la descrizione e determina la classificazione fiscale sul valore LORDO"""
    desc_l = desc.lower()
    
    # 1. PRIORITÀ MASSIMA: Beni fisici (Prevalgono su qualsiasi filtro lavori/servizi)
    if any(p in desc_l for p in ["porta", "copricassonetto", "infisso", "sedia", "scrivania", "pc", "computer"]):
        aliq = 12.5
        return "AA7 - Arredi/Beni", aliq, prezzo_lordo * (aliq/100), "Bene fisico rilevato: capitalizzazione forzata"
    
    # 2. Straordinaria
    if any(p in desc_l for p in ["straordinaria", "ristrutturazione", "adeguamento"]):
        return "Spese Incrementali", aliq_straord, prezzo_lordo * (aliq_straord/100), "Intervento strutturale rilevato"
        
    # 3. Servizi ordinari (Scudo)
    if any(p in desc_l for p in ["pulizia", "canone", "pitturazione", "lavori", "manodopera", "manutenzione"]):
        return "Spesa Corrente", 0.0, 0.0, "Servizio ordinario rilevato"
        
    # 4. Default
    return "AA3 - Generica", 15.0, prezzo_lordo * 0.15, "Ammortamento ordinario"

st.title("Classificatore Fatture XML")
files = st.file_uploader("Carica XML", accept_multiple_files=True)

if files:
    for f in files:
        try:
            radice = ET.parse(f).getroot()
            
            # --- ESTRAZIONE INTESTAZIONE E DATI FATTURA ---
            fornitore = radice.findtext('.//CedentePrestatore/DatiAnagrafici/Anagrafica/Denominazione') or "Non specificato"
            numero_fattura = radice.findtext('.//DatiGeneraliDocumento/Numero') or "N/D"
            
            # Estrazione e formattazione Data (da YYYY-MM-DD a DD/MM/YYYY)
            data_raw = radice.findtext('.//DatiGeneraliDocumento/Data') or "N/D"
            if data_raw != "N/D" and len(data_raw) >= 10:
                data_fattura = f"{data_raw[8:10]}/{data_raw[5:7]}/{data_raw[0:4]}"
            else:
                data_fattura = data_raw
                
            try:
                tot_fattura = float(radice.findtext('.//DatiGeneraliDocumento/ImportoTotaleDocumento') or 0.0)
            except:
                tot_fattura = 0.0
                
            tot_iva = sum([float(i.findtext('Imposta') or 0.0) for i in radice.iter('DatiRiepilogo') if i.find('Imposta') is not None])
            
            # --- VISUALIZZAZIONE INTESTAZIONE PERSONALIZZATA ---
            st.subheader(f"📄 FATTURA N. {numero_fattura} del {data_fattura}")
            st.markdown(f"""
                <div style="font-size: 18px; color: #334155; margin-bottom: 5px;">
                    <b>Fornitore:</b> {fornitore}
                </div>
                <div style="font-size: 24px; font-weight: bold; color: #1e3a8a; margin-bottom: 20px;">
                    Totale Fattura: € {fmt(tot_fattura)} &nbsp;&nbsp;|&nbsp;&nbsp; Totale IVA: € {fmt(tot_iva)}
                </div>
            """, unsafe_allow_html=True)
            
            # --- ANALISI RIGHE ---
            dati = []
            for linea in radice.iter('DettaglioLinee'):
                desc = linea.findtext('Descrizione') or ""
                
                prezzo_netto = float(linea.findtext('PrezzoTotale') or 0)
                try:
                    aliquota_iva_riga = float(linea.findtext('AliquotaIVA') or 0)
                except:
                    aliquota_iva_riga = 0.0
                
                iva_calcolata = prezzo_netto * (aliquota_iva_riga / 100.0)
                prezzo_lordo = prezzo_netto + iva_calcolata
                
                cat, aliq, quota, motivo = classifica_voce(desc, prezzo_lordo, aliquota_soft, aliquota_straord)
                
                dati.append({
                    "Descrizione": desc, 
                    "Imponibile (€)": fmt(prezzo_netto),
                    "IVA (€)": fmt(iva_calcolata),
                    "Imponibile + IVA (€)": fmt(prezzo_lordo),
                    "Aliquota (%)": aliq, 
                    "Quota Amm. (€)": fmt(quota), 
                    "Motivo": motivo
                })
            
            if dati:
                st.table(pd.DataFrame(dati))
            else:
                st.warning("Nessuna linea trovata nel file.")
                
        except Exception as e:
            st.error(f"Errore nella lettura del file: {e}")
