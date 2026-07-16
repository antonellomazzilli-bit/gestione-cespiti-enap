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

def classifica_voce(desc, prezzo, aliq_soft, aliq_straord):
    """Analizza la descrizione e determina la classificazione fiscale"""
    desc_l = desc.lower()
    
    # 1. PRIORITÀ MASSIMA: Beni fisici (Prevalgono su qualsiasi filtro lavori/servizi)
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
    for f in files:
        try:
            radice = ET.parse(f).getroot()
            
            # --- ESTRAZIONE INTESTAZIONE ---
            try:
                fornitore = radice.find('.//CedentePrestatore/DatiAnagrafici/Anagrafica/Denominazione').text
            except:
                fornitore = "Non specificato"
                
            try:
                tot_fattura = float(radice.find('.//DatiGeneraliDocumento/ImportoTotaleDocumento').text)
            except:
                tot_fattura = 0.0
                
            tot_iva = sum([float(i.find('Imposta').text) for i in radice.iter('DatiRiepilogo') if i.find('Imposta') is not None])
            
            st.subheader(f"📄 Fattura: {f.name} | Fornitore: {fornitore}")
            st.markdown(f"**Totale Fattura:** € {fmt(tot_fattura)} | **Totale IVA:** € {fmt(tot_iva)}")
            
            # --- ANALISI RIGHE ---
            dati = []
            for linea in radice.iter('DettaglioLinee'):
                desc = linea.findtext('Descrizione')
                prezzo = float(linea.findtext('PrezzoTotale') or 0)
                
                cat, aliq, quota, motivo = classifica_voce(desc, prezzo, aliquota_soft, aliquota_straord)
                
                dati.append({
                    "Descrizione": desc, 
                    "Valore (€)": fmt(prezzo), 
                    "Aliquota (%)": aliq, 
                    "Quota Amm. (€)": fmt(quota), 
                    "Motivo": motivo
                })
            
            if dati:
                st.table(pd.DataFrame(dati))
            else:
                st.warning("Nessuna linea trovata nel file.")
                
        except Exception as e:
            st.error(f"Errore nella lettura del file {f.name}: {e}")
