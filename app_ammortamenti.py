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
    aliquota_straord = st.number_input("Aliquota Lavori Straord./Oneri (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# --- FUNZIONI DI FORMATTAZIONE E LOGICA ---
def fmt(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def classifica_voce(desc, aliq_soft, aliq_straord):
    desc_l = desc.lower()
    
    # 1. SOFTWARE (50.0%)
    if any(p in desc_l for p in ["software", "licenza", "windows", "office", "antivirus"]):
        return "42 - Software", aliq_soft, "Licenze e Applicativi"
    
    # 2. HARDWARE E MACCHINE D'UFFICIO (33.33%)
    if any(p in desc_l for p in ["pc", "computer", "notebook", "server", "monitor", "stampante", "multifunzione", "lavagna", "proiettore", "nas", "router", "switch", "ups"]):
        return "41 - Hardware", 33.33, "Attrezzatura informatica"
        
    # 3. IMPIANTI GENERICI (16.66%)
    if any(p in desc_l for p in ["condizionatore", "climatizzatore", "caldaia", "antifurto", "impianto", "allarme"]):
        return "44 - Impianti Generici", 16.66, "Impiantistica"
    
    # 4. MOBILI E ARREDI (12.50%)
    if any(p in desc_l for p in ["porta", "infisso", "sedia", "scrivania", "armadio", "banco", "poltrona", "tavolo", "divano"]):
        return "43 - Mobili", 12.50, "Mobilio e Arredi"
    
    # 5. ONERI PLURIENNALI / STRAORDINARIA (20.0%)
    if any(p in desc_l for p in ["straordinaria", "ristrutturazione", "adeguamento", "allestimento"]):
        return "34 - Altri oneri pluriennali", aliq_straord, "Intervento strutturale/Allestimento"
        
    # 6. SPESA CORRENTE (Nessun ammortamento)
    if any(p in desc_l for p in ["pulizia", "canone", "pitturazione", "lavori", "manodopera", "manutenzione ordinaria", "riparazione"]):
        return "Spesa Corrente", 0.0, "Servizio ordinario rilevato"
        
    # 7. DEFAULT - MACCHINARI E ATTREZZATURE VARIE (15.0%)
    return "05 - Macchinari/Attrezzature", 15.0, "Ammortamento generico"

# --- FUNZIONE CREAZIONE PDF CON CONTROLLO IMPAGINAZIONE ---
def genera_pdf(lista_fatture):
    pdf = FPDF(orientation='L') 
    pdf.add_page()
    
    data_ora = datetime.now().strftime("%d/%m/%Y alle %H:%M")
    pdf.set_font("helvetica", style="I", size=8)
    pdf.cell(0, 5, f"Documento generato il {data_ora}", align="R", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(0, 10, "Riepilogo Classificazione Cespiti", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    headers = ["Rif. Fattura", "Descrizione", "Lordo Riga", "Tot. Fattura", "Aliq. %", "Motivo"]
    
    for fattura in lista_fatture:
        altezza_blocco = 27 + (len(fattura['righe']) * 6)
        spazio_rimanente = 210 - 15 - pdf.get_y()
        
        if altezza_blocco > spazio_rimanente:
            if altezza_blocco <= 180 or spazio_rimanente < 40:
                pdf.add_page()
                
        pdf.set_font("helvetica", style="B", size=10)
        titolo = f"FATTURA N. {fattura['numero_fattura']} del {fattura['data_fattura']} | Fornitore: {fattura['fornitore']}"
        pdf.cell(0, 6, titolo.encode('latin-1', 'replace').decode('latin-1'), new_x="LMARGIN", new_y="NEXT")
        
        sottotitolo = f"Totale Fattura: EUR {fmt(fattura['tot_fattura'])} | Totale IVA: EUR {fmt(fattura['tot_iva'])}"
        pdf.set_font("helvetica", style="", size=9)
        pdf.cell(0, 6, sottotitolo.encode('latin-1', 'replace').decode('latin-1'), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

        pdf.set_font("helvetica", style="B", size=8)
        col_widths = [pdf.get_string_width(h) + 6 for h in headers]
        
        for riga in fattura['righe']:
            valori = [
                str(riga['Rif. Fattura']),
                str(riga['Descrizione'])[:60].encode('latin-1', 'replace').decode('latin-1'),
                str(riga['Lordo Riga (€)']).replace("€", "EUR"),
                str(riga['Tot. Fattura (€)']).replace("€", "EUR"),
                str(riga['Aliquota (%)']),
                str(riga['Motivo']).encode('latin-1', 'replace').decode('latin-1')
            ]
            for i, val in enumerate(valori):
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
        for riga in fattura['righe']:
            valori = [
                str(riga['Rif. Fattura']),
                str(riga['Descrizione'])[:60].encode('latin-1', 'replace').decode('latin-1'),
                str(riga['Lordo Riga (€)']).replace("€", "EUR"),
                str(riga['Tot. Fattura (€)']).replace("€", "EUR"),
                str(riga['Aliquota (%)']),
                str(riga['Motivo']).encode('latin-1', 'replace').decode('latin-1')
            ]
            for i, testocella in enumerate(valori):
                while pdf.get_string_width(testocella) > col_widths[i] - 2 and len(testocella) > 0:
                    testocella = testocella[:-1]
                align_cell = 'R' if i in [2, 3] else ('C' if i == 4 else 'L')
                pdf.cell(col_widths[i], 6, testocella, border=1, align=align_cell)
            pdf.ln()
        
        pdf.ln(5)
        
    return bytes(pdf.output())

st.title("Classificatore Fatture XML")
files = st.file_uploader("Carica XML", accept_multiple_files=True)

if files:
    # --- CREAZIONE CONTENITORE VUOTO IN CIMA ---
    contenitore_pulsanti = st.container()
    
    dati_globali_excel = []
    dati_pdf_global = []
    
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
                rif_fattura_visivo = f"N. {numero_fattura} del {data_fattura}" if indice_riga == 0 else ""
                
                aliq_formattata = f"{aliq:.2f}%" if aliq > 0 else "0.0%"
                
                dati_visivi.append({
                    "Rif. Fattura": rif_fattura_visivo,
                    "Descrizione": desc, 
                    "Lordo Riga (€)": fmt(prezzo_lordo),
                    "Tot. Fattura (€)": totale_da_mostrare,
                    "Aliquota (%)": aliq_formattata, 
                    "Motivo": motivo
                })
                
                dati_globali_excel.append({
                    "Fornitore": fornitore,
                    "Numero Fattura": numero_fattura,
                    "Data Fattura": data_fattura,
                    "File XML": f.name,
                    "Descrizione Bene/Servizio": desc,
                    "Valore Lordo Riga": prezzo_lordo,
                    "Totale Documento": tot_fattura,
                    "Aliquota Amm. (%)": aliq,
                    "Categoria Fiscale": cat,
                    "Motivazione Classificazione": motivo
                })
            
            if dati_visivi:
                dati_pdf_global.append({
                    "fornitore": fornitore,
                    "numero_fattura": numero_fattura,
                    "data_fattura": data_fattura,
                    "tot_fattura": tot_fattura,
                    "tot_iva": tot_iva,
                    "righe": dati_visivi
                })
                
                df_visivo = pd.DataFrame(dati_visivi)
                col_order = ["Rif. Fattura", "Descrizione", "Lordo Riga (€)", "Tot. Fattura (€)", "Aliquota (%)", "Motivo"]
                st.dataframe(df_visivo[col_order], use_container_width=True, hide_index=True)
            else:
                st.warning("Nessuna linea trovata nel file.")
                
        except Exception as e:
            st.error(f"Errore nella lettura del file {f.name}: {e}")
            
    # --- RIEMPIMENTO DEL CONTENITORE IN CIMA ALLA FINE DEL CALCOLO ---
    if dati_globali_excel:
        with contenitore_pulsanti:
            st.subheader("📥 Esportazione Dati")
            
            col1, col2 = st.columns(2)
            
            df_excel = pd.DataFrame(dati_globali_excel).drop(columns=['File XML'])
            
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
                
            pdf_bytes = genera_pdf(dati_pdf_global)
            
            with col2:
                st.download_button(
                    label="📄 Scarica Riepilogo in PDF",
                    data=pdf_bytes,
                    file_name="Riepilogo_Ammortamenti.pdf",
                    mime="application/pdf"
                )
            
            st.markdown("---")
