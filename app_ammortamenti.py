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

def classifica_voce(desc, aliq_soft, aliq_straord):
    desc_l = desc.lower()
    
    if any(p in desc_l for p in ["porta", "copricassonetto", "infisso", "sedia", "scrivania", "pc", "computer"]):
        return "AA7 - Arredi/Beni", 12.5, "Bene fisico rilevato: capitalizzazione forzata"
    
    if any(p in desc_l for p in ["straordinaria", "ristrutturazione", "adeguamento"]):
        return "Spese Incrementali", aliq_straord, "Intervento strutturale rilevato"
        
    if any(p in desc_l for p in ["pulizia", "canone", "pitturazione", "lavori", "manodopera", "manutenzione"]):
        return "Spesa Corrente", 0.0, "Servizio ordinario rilevato"
        
    return "AA3 - Generica", 15.0, "Ammortamento ordinario"

# --- FUNZIONE CREAZIONE PDF CON CALCOLO LARGHEZZA DINAMICA ---
def genera_pdf(dati):
    pdf = FPDF(orientation='L') 
    pdf.add_page()
    
    data_ora = datetime.now().strftime("%d/%m/%Y alle %H:%M")
    pdf.set_font("helvetica", style="I", size=8)
    pdf.cell(0, 5, f"Documento generato il {data_ora}", align="R", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(0, 10, "Riepilogo Classificazione Cespiti", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    headers = ["Fornitore", "Descrizione Articolo", "Tot. Fattura", "Lordo Riga", "Aliq. %", "Categoria Fiscale"]
    
    pdf.set_font("helvetica", style="B", size=8)
    col_widths = [pdf.get_string_width(h) + 6 for h in headers] 
    
    dati_stampabili = []
    fattura_corrente = None
    pdf.set_font("helvetica", size=8)
    
    for row in dati:
        forn = str(row['Fornitore'])[:50].encode('latin-1', 'replace').decode('latin-1')
        desc = str(row['Descrizione Bene/Servizio'])[:80].encode('latin-1', 'replace').decode('latin-1')
        
        if row['File XML'] != fattura_corrente:
            tot_doc = f"{row['Totale Documento']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            fattura_corrente = row['File XML']
        else:
            tot_doc = "" 
            
        lordo = f"{row['Valore Lordo Riga']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        aliq = f"{row['Aliquota Amm. (%)']:.1f}%"
        cat = str(row['Categoria Fiscale']).encode('latin-1', 'replace').decode('latin-1')
        
        riga = [forn, desc, tot_doc, lordo, aliq, cat]
        dati_stampabili.append(riga)
        
        for i, val in enumerate(riga):
            w = pdf.get_string_width(val) + 4 
            if w > col_widths[i]:
                col_widths[i] = w

    max_page_width = 277.0
    tot_width = sum(col_widths)
    
    if tot_width > max_page_width:
        fattore = max_page_width / tot_width
        col_widths = [w * fattore for w in col_widths]
    
    pdf.set_font("helvetica", style="B", size=8)
    for i, header in enumerate(headers):
        align_header = 'C' if i in [2, 3, 4] else 'L'
        pdf.cell(col_widths[i], 8, header, border=1, align=align_header)
    pdf.ln()
    
    pdf.set_font("helvetica", size=8)
    for riga in dati_stampabili:
        for i, testocella in enumerate(riga):
            while pdf.get_string_width(testocella) > col_widths[i] - 2 and len(testocella) > 0:
                testocella = testocella[:-1]
                
            align_cell = 'R' if i in [2, 3] else ('C' if i == 4 else 'L')
            pdf.cell(col_widths[i], 6, testocella, border=1, align=align_cell)
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
            
            numero_fattura = radice.findtext('.//DatiGeneraliDocumento/Numero') or "N/D"
            data_raw = radice.findtext('.//DatiGeneraliDocumento/Data') or "N/D"
            if data_raw != "N/D" and len(data_raw) >= 10:
                data_fattura = f"{data_raw[8:10]}/{data_raw[5:7]}/{data_raw[0:4]}"
            else:
                data_fattura = data_raw
                
            try: tot_fattura = float(radice.find('.//DatiGeneraliDocumento/ImportoTotaleDocumento').text)
            except: tot_fattura = 0.0
                
            tot_iva = sum([float(i.find('Imposta').text) for i in radice.iter('DatiRiepilogo') if i.find('Imposta') is not None])
            
            st.subheader(f"📄 FATTURA N. {numero_fattura} del {data_fattura}")
            st.markdown(f"**Fornitore:** {fornitore} | **Totale Fattura:** € {fmt(tot_fattura)} | **Totale IVA:** € {fmt(tot_iva)}")
            
            dati_visivi = []
            
            for indice_riga, linea in enumerate(radice.iter('DettaglioLinee')):
                desc = linea.findtext('Descrizione') or "Nessuna descrizione"
                
                prezzo_netto = float(linea.findtext('PrezzoTotale') or 0)
                try:
                    aliquota_iva_riga = float(linea.findtext('AliquotaIVA') or 0)
                except:
                    aliquota_iva_riga = 0.0
                
                iva_calcolata = prezzo_netto * (aliquota_iva_riga / 100.0)
                prezzo_lordo = prezzo_netto + iva_calcolata
                
                cat, aliq, motivo = classifica_voce(desc, aliquota_soft, aliquota_straord)
                
                totale_da_mostrare = fmt(tot_fattura) if indice_riga == 0 else ""
                
                dati_visivi.append({
                    "Descrizione": desc, 
                    "Imponibile (€)": fmt(prezzo_netto),
                    "IVA (€)": fmt(iva_calcolata),
                    "Lordo Riga (€)": fmt(prezzo_lordo),
                    "Tot. Fattura (€)": totale_da_mostrare,
                    "Aliquota (%)": aliq, 
                    "Motivo": motivo
                })
                
                dati_globali_excel.append({
                    "Fornitore": fornitore,
                    "Numero Fattura": numero_fattura,
                    "Data Fattura": data_fattura,
                    "File XML": f.name,
                    "Descrizione Bene/Servizio": desc,
                    "Valore Netto Riga": prezzo_netto,
                    "Aliquota IVA (%)": aliquota_iva_riga,
                    "IVA Calcolata Riga": iva_calcolata,
                    "Valore Lordo Riga": prezzo_lordo,
                    "Totale Documento": tot_fattura,
                    "Aliquota Amm. (%)": aliq,
                    "Categoria Fiscale": cat,
                    "Motivazione Classificazione": motivo
                })
            
            if dati_visivi:
                st.dataframe(pd.DataFrame(dati_visivi), use_container_width=True, hide_index=True)
            else:
                st.warning("Nessuna linea trovata nel file.")
                
        except Exception as e:
            st.error(f"Errore nella lettura del file {f.name}: {e}")
            
    # --- GENERAZIONE PULSANTI DOWNLOAD ---
    if dati_globali_excel:
        st.markdown("---")
        st.subheader("📥 Esportazione Dati")
        
        col1, col2 = st.columns(2)
        
        df_excel = pd.DataFrame(dati_globali_excel)
        buffer_excel = io.BytesIO()
        with pd.ExcelWriter(buffer_excel, engine='openpyxl') as writer:
            df_excel.to_excel(writer, index=False, sheet_name='Cespiti Elaborati')
            
            worksheet = writer.sheets['Cespiti Elaborati']
            for column_cells in worksheet.columns:
                max_length = max((len(str(cell.value)) for cell in column_cells if cell.value is not None), default=10)
                worksheet.column_dimensions[column_cells[0].column_letter].width = min(max_length + 2, 80)
            
        with col1:
            st.download_button(
                label="📊 Scarica Riepilogo in Excel",
                data=buffer_excel.getvalue(),
                file_name="Riepilogo_Ammortamenti.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
        pdf_bytes = genera_pdf(dati_globali_excel)
        
        with col2:
            st.download_button(
                label="📄 Scarica Riepilogo in PDF",
                data=pdf_bytes,
                file_name="Riepilogo_Ammortamenti.pdf",
                mime="application/pdf"
            )
