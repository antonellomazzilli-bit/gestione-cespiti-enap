import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import html 

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- PANNELLO LATERALE ---
with st.sidebar:
    st.header("⚙️ Impostazioni")
    aliquota_soft = st.number_input("Aliquota Software (%)", value=50.0)
    aliquota_straord = st.number_input("Aliquota Straordinaria (%)", value=20.0)

# --- CSS E FUNZIONI ---
st.markdown("""
    <style>
        .fattura-container { background-color: white; border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 30px; padding: 15px; }
        .custom-table { width: 100%; border-collapse: collapse; font-size: 12px; }
        .custom-table th, .custom-table td { padding: 8px; border-bottom: 1px solid #e2e8f0; text-align: right; }
    </style>
""", unsafe_allow_html=True)

def formatta_euro(v): return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def classifica_voce(descrizione, prezzo_lordo, aliq_soft, aliq_straord):
    desc = descrizione.lower()
    
    # 1. ECCEZIONE PRIORITARIA: Beni fisici salvano la riga
    if any(p in desc for p in ["porta", "copricassonetto", "infisso", "sedia", "scrivania", "pc", "computer"]):
        return "AA7 - Arredi/Beni (Priorità fisica)", 12.5, "Bene fisico rilevato: capitalizzazione forzata"
    
    # 2. SCUDO SERVIZI
    if any(p in desc for p in ["straordinaria", "ristrutturazione", "adeguamento"]):
        return "Spese Incrementali", aliq_straord, "Intervento strutturale rilevato"
    if any(p in desc for p in ["pulizia", "canone", "pitturazione", "lavori"]):
        return "Spesa Corrente", 0.0, "Servizio ordinario rilevato"
        
    return "AA3 - Attrezzatura Generica", 15.0, "Ammortamento ordinario"

st.title("Classificatore Fatture XML")
files = st.file_uploader("Carica XML", accept_multiple_files=True)

if files:
    for f in files:
        radice = ET.parse(f).getroot()
        righe = []
        # [Logica di estrazione linee semplificata per brevità]
        for linea in radice.iter('DettaglioLinee'):
            desc = linea.findtext('Descrizione')
            prezzo = float(linea.findtext('PrezzoTotale') or 0)
            cat, aliq, motivo = classifica_voce(desc, prezzo, aliquota_soft, aliquota_straord)
            righe.append({"Desc": desc, "Prezzo": prezzo, "Cat": cat, "Motivo": motivo})
        
        # Rendering della tabella
        st.write(f"### Fattura {f.name}")
        df = pd.DataFrame(righe)
        st.table(df)
