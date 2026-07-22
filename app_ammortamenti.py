import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import io
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- PANNELLO LATERALE: IMPOSTAZIONI ALIQUOTE DINAMICHE ---
with st.sidebar:
    st.header("⚙️ Impostazioni Fiscali")
    aliquota_soft = st.number_input("Aliquota Software (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    aliquota_straord = st.number_input("Aliquota Lavori Straordinari (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# --- FUNZIONI DI FORMATTAZIONE E LOGICA ---
def fmt(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def classifica_voce(desc, prezzo, aliq_soft, aliq_straord):
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

# --- FUNZIONE CREAZIONE PDF CON ALIQUOTA ---
def genera_pdf(dati):
    pdf = FPDF(orientation='L') # Impaginazione orizzontale
    pdf.add_page()
    
    # Intestazione con Data e Ora
    data_ora = datetime.now().strftime("%d/%m/%Y alle %H:%M")
    pdf.set_font("helvetica", style="I", size=8)
    pdf.cell(0, 5, f"Documento generato il {data_ora}", align="R", new_x="LMARGIN", new_y="NEXT")
    
    # Titolo
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(0, 10, "Riepilogo Classificazione Cespiti", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    # Intestazioni Tabella (Spazio totale distribuito: 275)
    pdf.set_font("helvetica", style="B", size=9)
    col_widths = [45, 90, 25, 20, 25, 70]
    headers = ["Fornitore", "Descrizione Articolo", "Lordo (EUR)", "Aliq. %", "Quota (EUR)", "Categoria Fiscale"]
    
    for i, header in enumerate(headers):
        align_header = 'C' if i in [2, 3, 4] else 'L'
        pdf.cell(col_widths[i], 8, header, border=1, align=align_header)
    pdf.ln()
    
    # Inserimento Dati
    pdf.set_font("helvetica", size=8)
    for row in dati:
        # Pulizia e troncamento per evitare sforamenti
        forn = str(row['Fornitore'])[:25].encode('latin-1', 'replace').decode('latin-1')
        desc = str(row['Descrizione Bene/Servizio'])[:55].encode('latin-1', 'replace').decode('latin-1')
        lordo = f"{row['Valore Netto']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        aliq = f"{row['Aliquota (%)']:.1f}%"
        quota = f"{row['Quota Ammortamento']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        cat = str(row['Categoria Fiscale'])[:40].encode('latin-1', 'replace').decode('latin-1')
        
        pdf.cell(col_widths[0], 6, forn, border=1)
        pdf.cell(col_widths[1], 6, desc, border=1)
        pdf.cell(col_widths[2], 6, lordo, border=1, align='R')
        pdf.cell(col_widths[3], 6, aliq, border=1, align='C')
        pdf.cell(col_widths[4], 6, quota, border=1, align='R')
        pdf.cell(col_widths[5], 6, cat, border=1)
        pdf.ln()
        
    return bytes(pdf.output())

st.title("Classificatore Fatture XML")
files = st.file_uploader("Carica XML", accept_multiple_files=True)

if files:
    dati_globali_excel = []
    
    for f in files:
        try:
            radice = ET.parse(f).getroot()
            
            try: fornitore = radice.find('.//CedentePrestatore/DatiAnagrafici/Anagrafica/Denominazione').text
            except: fornitore = "Non specificato"
                
            try: tot_fattura = float(radice.find('.//DatiGeneraliDocumento/ImportoTotaleDocumento').text)
            except: tot_fattura = 0.0
                
            tot_iva = sum([float(i.find('Imposta').text) for i in radice.iter('DatiRiepilogo') if i.find('Imposta') is not None])
            
            st.subheader(f"📄 Fattura: {f.name} | Fornitore: {fornitore}")
            st.markdown(f"**Totale Fattura:** € {fmt(tot_fattura)} | **Totale IVA:** € {fmt(tot_iva)}")
            
            dati_visivi = []
            for linea in radice.iter('DettaglioLinee'):
                desc = linea.findtext('Descrizione') or "Nessuna descrizione"
                prezzo = float(linea.findtext('PrezzoTotale') or 0)
                
                cat, aliq, quota, motivo = classifica_voce(desc, prezzo, aliquota_soft, aliquota_straord)
                
                dati_visivi.append({
                    "Descrizione": desc, 
                    "Valore (€)": fmt(prezzo), 
                    "Aliquota (%)": aliq, 
                    "Quota Amm. (€)": fmt(quota), 
                    "Motivo": motivo
                })
                
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
            
    # --- GENERAZIONE PULSANTI DOWNLOAD ---
    if dati_globali_excel:
        st.markdown("---")
        st.subheader("📥 Esportazione Dati")
        
        col1, col2 = st.columns(2)
        
        # 1. Pulsante EXCEL
        df_excel = pd.DataFrame(dati_globali_excel)
        buffer_excel = io.BytesIO()
        with pd.ExcelWriter(buffer_excel, engine='openpyxl') as writer:
            df_excel.to_excel(writer, index=False, sheet_name='Cespiti Elaborati')
            
        with col1:
            st.download_button(
                label="📊 Scarica Riepilogo in Excel",
                data=buffer_excel.getvalue(),
                file_name="Riepilogo_Ammortamenti.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
        # 2. Pulsante PDF
        pdf_bytes = genera_pdf(dati_globali_excel)
        
        with col2:
            st.download_button(
                label="📄 Scarica Riepilogo in PDF",
                data=pdf_bytes,
                file_name="Riepilogo_Ammortamenti.pdf",
                mime="application/pdf"
            )
