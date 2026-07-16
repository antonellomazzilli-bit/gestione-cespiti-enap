import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import html

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# Funzioni di formattazione IT
def fmt(valore):
    return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Logica di classificazione con calcolo quota
def classifica_voce(descrizione, prezzo_lordo, aliq_soft, aliq_straord):
    desc = descrizione.lower()
    
    # 1. Beni fisici (Priorità)
    if any(p in desc for p in ["porta", "copricassonetto", "infisso", "sedia", "scrivania", "pc", "computer"]):
        aliq = 12.5
        quota = prezzo_lordo * (aliq / 100)
        return "AA7 - Arredi/Beni", aliq, quota, "Bene fisico rilevato"
    
    # 2. Straordinaria
    if any(p in desc for p in ["straordinaria", "ristrutturazione", "adeguamento"]):
        quota = prezzo_lordo * (aliq_straord / 100)
        return "Spese Incrementali", aliq_straord, quota, "Intervento strutturale"
        
    # 3. Servizi
    if any(p in desc for p in ["pulizia", "canone", "pitturazione", "lavori"]):
        return "Spesa Corrente", 0.0, 0.0, "Servizio ordinario"
        
    return "AA3 - Generica", 15.0, prezzo_lordo * 0.15, "Ammortamento ordinario"

st.title("Classificatore Fatture XML")
files = st.file_uploader("Carica XML", accept_multiple_files=True)

if files:
    for f in files:
        radice = ET.parse(f).getroot()
        dati = []
        for linea in radice.iter('DettaglioLinee'):
            desc = linea.findtext('Descrizione')
            prezzo = float(linea.findtext('PrezzoTotale') or 0)
            
            # Calcolo
            cat, aliq, quota, motivo = classifica_voce(desc, prezzo, 50.0, 20.0)
            
            dati.append({
                "Descrizione": desc,
                "Valore (€)": fmt(prezzo),
                "Aliquota (%)": aliq,
                "Quota Amm. (€)": fmt(quota),
                "Motivo": motivo
            })
        
        st.write(f"### Fattura {f.name}")
        st.table(pd.DataFrame(dati))
