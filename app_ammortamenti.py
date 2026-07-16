import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import html 

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- PANNELLO LATERALE: IMPOSTAZIONI ALIQUOTE DINAMICHE ---
with st.sidebar:
    st.header("⚙️ Impostazioni Fiscali")
    st.markdown("Modifica le aliquote standard applicate dall'algoritmo.")
    # Permette di variare dinamicamente il 50% assegnato ai software
    aliquota_software_dinamica = st.number_input("Aliquota Software/Licenze (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    aliquota_straordinaria = st.number_input("Aliquota Lavori Straordinari (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)

# --- INIEZIONE CSS: IMPAGINAZIONE AVANZATA PER LA STAMPA ---
st.markdown("""
    <style>
        .titolo-fattura { background-color: #f8fafc; padding: 12px 15px; border-left: 5px solid #2563eb; border-radius: 6px 6px 0 0; border-bottom: 1px solid #e2e8f0; }
        .fattura-container { background-color: white; border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 30px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); page-break-inside: avoid !important; }
        table.custom-table { width: 100%; border-collapse: collapse; font-size: 12px; }
        table.custom-table th, table.custom-table td { padding: 8px 10px; border-bottom: 1px solid #e2e8f0; text-align: right; vertical-align: middle; }
        table.custom-table td:first-child, table.custom-table th:first-child { text-align: left; width: 30%; }
        table.custom-table th { background-color: #f1f5f9; font-weight: bold; color: #0f172a; }
        @media print {
            header, footer, .stDeployButton, [data-testid="stFileUploader"], [data-testid="stSidebar"], .no-print { display: none !important; }
            body, .stApp, .main, .block-container, div { background-color: transparent !important; color: black !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important; }
            .block-container { padding: 0 !important; max-width: 100% !important; }
            table.custom-table th, table.custom-table td { border: 1px solid #94a3b8 !important; }
            table.custom-table th { background-color: #cbd5e1 !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
            .fattura-container { border: none !important; box-shadow: none !important; margin-bottom: 40px !important; }
            .print-header { display: block !important; text-align: center; border-bottom: 3px solid #000; padding-bottom: 10px; margin-bottom: 20px; }
            .print-header h2 { margin: 0; font-size: 24px; text-transform: uppercase; }
            .print-header p { margin: 5px 0 0 0; font-size: 14px; color: #555; }
        }
        .print-header { display: none; }
    </style>
""", unsafe_allow_html=True)

def formatta_euro(valore): return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
def formatta_decimale(valore):
    v = f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return v[:-3] if v.endswith(",00") else v
def formatta_anni(valore): return str(valore).replace(".", ",")

# 1. DATABASE CESPITI E FILTRI PAROLE CHIAVE
cluster_straordinaria = ["straordinaria", "ristrutturazione", "ampliamento", "adeguamento", "innovazione", "miglioramento", "strutturale"]
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "manutenzione", "noleggio", "energia", "assicurazione", "servizio", "lavori", "pitturazione", "cartongesso", "manodopera"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups "]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo_lordo, aliq_soft, aliq_straord):
    if not descrizione: return "Sconosciuto", 0.0, "Nessuna descrizione"
    desc_lower = descrizione.lower()
    
    # 1. ECCEZIONE ASSOLUTA: Manutenzione Straordinaria (Batte tutti gli altri filtri)
    motivo_straordinario = next((p for p in cluster_straordinaria if p in desc_lower), None)
    if motivo_straordinario: 
        return "Spese Incrementali / Manut. Straordinaria", aliq_straord, f"Intervento strutturale rilevato: '{motivo_straordinario}'"
    
    # 2. SCUDO SERVIZI ORDINARI
    motivo_pesante = next((p for p in cluster_servizi_pesanti if p in desc_lower), None)
    if motivo_pesante: return "Spesa Corrente / Servizio non ammortizzabile", 0.0, f"Rilevato servizio ordinario: '{motivo_pesante}'"
    
    categoria = ""
    aliquota = 0.0
    
    # 3. RICERCA BENI
    if any(parola in desc_lower for parola in cluster_sollevamento): categoria, aliquota = "AA2 - Impianti e mezzi di sollevamento (Sottosp. 4)", 7.5
    elif any(parola in desc_lower for parola in cluster_hardware): categoria, aliquota = "AA4 - Elaboratori elettronici e sistemi hardware (Sottosp. 41)", 33.33
    elif any(parola in desc_lower for parola in cluster_software): categoria, aliquota = "AA1 - Diritti di utilizzazione delle opere dell'ingegno / Software (Sottosp. 42)", aliq_soft
    elif any(parola in desc_lower for parola in cluster_macchine_uff): categoria, aliquota = "AA8 - Macchine d'ufficio elettroniche (Sottosp. 13)", 20.0
    elif any(parola in desc_lower for parola in cluster_impianti): categoria, aliquota = "AA2 - Impianti generici di condizionamento, allarme e cablaggio (Sottosp. 44)", 16.66
    elif any(parola in desc_lower for parola in cluster_mobili): categoria, aliquota = "AA7 - Mobili e arredi ordinari d'ufficio (Sottosp. 43)", 12.50
    elif any(parola in desc_lower for parola in cluster_laboratorio): categoria, aliquota = "AA8 - Macchinari, apparecchi e attrezzature di laboratorio (Sottosp. 5)", 15.0
    
    if not categoria:
        motivo_accessorio = next((p for p in cluster_accessori if p in desc_lower), None)
        if motivo_accessorio: return "Spesa Corrente / Servizio accessorio", 0.0, f"Costo accessorio isolato: '{motivo_accessorio}'"
        categoria, aliquota = "AA3 - Attrezzatura Generica (Da Verificare)", 15.0
    
    if prezzo_lordo <= 516.46 and aliquota > 0:
        return "AA9 - Beni ammortizzabili meno di 1 anno (Sottosp. 35)", 100.0, "Art. 102 TUIR (Beni < 516,46€)"
        
    return categoria, aliquota, "Ammortamento ordinario"

st.title("Classificatore Fatture XML (Database 2025)")

data_odierna = datetime.now().strftime("%d/%m/%Y")
st.markdown(f"""
    <div class="print-header">
        <h2>En.A.P. Puglia</h2>
        <p>Report Analitico Classificazione Cespiti | Generato il: {data_odierna}</p>
    </div>
""", unsafe_allow_html=True)

# 2. Upload Multiplo
st.markdown('<p class="no-print" style="font-size: 16px;">Carica gli <b>XML</b> per generare il report impaginato.</p>', unsafe_allow_html=True)
file_caricati = st.file_uploader("Scegli i file XML", type=["xml", "p7m"], accept_multiple_files=True)

if file_caricati:
    totale_lordo_globale = 0.0
    totale_cespiti_globale = 0.0
    totale_non_ammesso_globale = 0.0
    
    for file_caricato in file_caricati:
        try:
            albero = ET.parse(file_caricato)
            radice = albero.getroot()
            
            fornitore, numero_fattura, data_fattura = "Non specificato", "N/D", "N/D"
            importo_totale_doc = 0.0
            importo_iva_totale = 0.0
            imponibile_riepilogo = 0.0
            righe_estratte = []
            
            for elemento in radice.iter():
                if 'CedentePrestatore' in elemento.tag:
                    for figlio in elemento.iter():
                        if 'Denominazione' in figlio.tag and fornitore == "Non specificato": fornitore = figlio.text
                            
                elif 'DatiGeneraliDocumento' in elemento.tag:
                    for figlio in elemento.iter():
                        if 'Numero' in figlio.tag: numero_fattura = figlio.text
                        elif 'Data' in figlio.tag:
                            d = figlio.text
                            if d and len(d) >= 10: data_fattura = f"{d[8:10]}/{d[5:7]}/{d[0:4]}"
                        elif 'ImportoTotaleDocumento' in figlio.tag:
                            try: importo_totale_doc = float(figlio.text)
                            except ValueError: pass
                            
                elif 'DatiRiepilogo' in elemento.tag:
                    for figlio in elemento:
                        if 'Imposta' in figlio.tag:
                            try: importo_iva_totale += float(figlio.text)
                            except ValueError: pass
                        elif 'ImponibileImporto' in figlio.tag:
                            try: imponibile_riepilogo += float(figlio.text)
                            except ValueError: pass
                            
                elif 'DettaglioLinee' in elemento.tag:
                    descrizione = ""
                    prezzo_unitario = 0.0
                    prezzo_totale = 0.0
                    aliquota_iva_riga = 0.0
                    quantita = 1.0  
                    
                    for figlio in elemento:
                        if 'Descrizione' in figlio.tag: descrizione = html.escape(str(figlio.text))
                        elif 'PrezzoUnitario' in figlio.tag:
                            try: prezzo_unitario = float(figlio.text)
                            except ValueError: pass
                        elif 'PrezzoTotale' in figlio.tag:
                            try: prezzo_totale = float(figlio.text)
                            except ValueError: pass
                        elif 'Quantita' in figlio.tag:
                            try: quantita = float(figlio.text)
                            except ValueError: pass
                        elif 'AliquotaIVA' in figlio.tag:
                            try: aliquota_iva_riga = float(figlio.text)
                            except ValueError: pass
                                
                    if prezzo_totale > 0: prezzo_netto = prezzo_totale
                    else: prezzo_netto = prezzo_unitario * quantita
                    
                    if descrizione and prezzo_netto > 0:
                        iva_calcolata = prezzo_netto * (aliquota_iva_riga / 100.0)
                        prezzo_lordo = prezzo_netto + iva_calcolata
                        
                        # Passaggio delle aliquote dinamiche dalla sidebar
                        categoria, aliquota, motivazione = classifica_voce(descrizione, prezzo_lordo, aliquota_software_dinamica, aliquota_straordinaria)
                        
                        anni = 0.0 if aliquota == 0 else (1.0 if aliquota == 100 else round(100 / aliquota, 1))
                        
                        if aliquota == 0:
                            nota_azione = f"❌ SCARTATO<br><span style='font-size:10px; font-weight:normal; color:#b91c1c;'>Motivo: {motivazione}</span>"
                        elif aliquota == 100:
                            nota_azione = f"✔️ DA ISCRIVERE<br><span style='font-size:10px; font-weight:normal; color:#047857;'>Motivo: {motivazione}</span>"
                        else:
                            nota_azione = f"✔️ DA ISCRIVERE<br><span style='font-size:10px; font-weight:normal; color:#475569;'>{motivazione}</span>"
                        
                        righe_estratte.append({
                            "Descrizione": descrizione, "Valore_Netto": prezzo_netto, "IVA_num": iva_calcolata,
                            "Valore_Lordo": prezzo_lordo, "Esito Fiscale": categoria, "Aliquota_num": aliquota,
                            "Anni_num": anni, "Nota_Azione": nota_azione
                        })
            
            if importo_totale_doc == 0.0 and (imponibile_riepilogo > 0 or importo_iva_totale > 0):
                importo_totale_doc = imponibile_riepilogo + importo_iva_totale
                
            if righe_estratte:
                df_calc = pd.DataFrame(righe_estratte)
                totale_netto_spese = df_calc["Valore_Netto"].sum()
                totale_iva_righe = df_calc["IVA_num"].sum()
                totale_lordo_spese = df_calc["Valore_Lordo"].sum()
                
                cespiti_puri = df_calc[df_calc["Aliquota_num"] > 0]["Valore_Lordo"].sum()
                totale_non_ammesso_riga = totale_lordo_spese - cespiti_puri
                
                totale_lordo_globale += totale_lordo_spese
                totale_cespiti_globale += cespiti_puri
                totale_non_ammesso_globale += totale_non_ammesso_riga
                
                html_fattura = f"""
<div class="fattura-container">
    <div class="titolo-fattura">
        <h4 style="margin:0; color:#1e3a8a;">📄 FATTURA N. {html.escape(str(numero_fattura))} del {html.escape(str(data_fattura))}</h4>
        <p style="margin:6px 0 0 0; font-size:15px; color:#334155;">
            <b>Fornitore:</b> {html.escape(str(fornitore))} &nbsp;&nbsp;|&nbsp;&nbsp;
            <span style="color:#0f172a;"><b>Totale Fattura:</b> € {formatta_euro(importo_totale_doc)}</span> &nbsp;&nbsp;|&nbsp;&nbsp;
            <span style="color:#0f172a;"><b>Totale IVA Documento:</b> € {formatta_euro(importo_iva_totale)}</span>
        </p>
    </div>
    <table class="custom-table">
        <thead>
            <tr>
                <th>Descrizione Articolo / Servizio</th>
                <th>Valore Netto (€)</th>
                <th>IVA (€)</th>
                <th style="background-color: #e2e8f0;">Valore Lordo (€)</th>
                <th>Esito Fiscale (Aziendale / Normativo)</th>
                <th>Aliquota Amm. (%)</th>
                <th>Anni</th>
                <th>Azione Libro Cespiti</th>
            </tr>
        </thead>
        <tbody>
"""
                
                for riga in righe_estratte:
                    stile_cella = "color: #b91c1c; font-weight: 500;" if riga['Aliquota_num'] == 0 else "color: #1e293b;"
                    colore_nota = "#b91c1c" if riga['Aliquota_num'] == 0 else "#047857"
                    
                    html_fattura += f"""
            <tr>
                <td style="{stile_cella}">{riga['Descrizione']}</td>
                <td style="{stile_cella}">{formatta_euro(riga['Valore_Netto'])}</td>
                <td style="{stile_cella}">{formatta_euro(riga['IVA_num'])}</td>
                <td style="{stile_cella}; background-color: #f8fafc;"><b>{formatta_euro(riga['Valore_Lordo'])}</b></td>
                <td style="{stile_cella}"><b>{riga['Esito Fiscale']}</b></td>
                <td style="{stile_cella}">{formatta_decimale(riga['Aliquota_num'])}</td>
                <td style="{stile_cella}">{formatta_anni(riga['Anni_num'])}</td>
                <td style="color: {colore_nota}; font-weight: bold; line-height: 1.3;">{riga['Nota_Azione']}</td>
            </tr>
"""
                    
                html_fattura += f"""
            <tr style="background-color: #f1f5f9; font-weight: bold; color: #0f172a; border-top: 2px solid #94a3b8;">
                <td style="text-align: right; color: #0f172a;">TOTALE RIGHE</td>
                <td style="color: #0f172a;">{formatta_euro(totale_netto_spese)}</td>
                <td style="color: #0f172a;">{formatta_euro(totale_iva_righe)}</td>
                <td style="color: #0f172a; background-color: #e2e8f0;">{formatta_euro(totale_lordo_spese)}</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
    <div style="text-align: right; padding: 8px 12px; background-color: #ffffff; border-radius: 0 0 6px 6px; font-size: 14px;">
        <b>Costo Totale Lordo:</b> € {formatta_euro(totale_lordo_spese)} &nbsp;&nbsp;|&nbsp;&nbsp; 
        <span style="color: #047857; font-size: 14px;"><b>Da Iscrivere a Libro Cespiti:</b> € {formatta_euro(cespiti_puri)}</span> &nbsp;&nbsp;|&nbsp;&nbsp;
        <span style="color: #b91c1c; font-size: 14px;"><b>Spese Correnti / Non Ammesse:</b> € {formatta_euro(totale_non_ammesso_riga)}</span>
    </div>
</div>
"""
                st.html(html_fattura)
                
            else:
                st.warning(f"Attenzione: Nel file {file_caricato.name} non è stato trovato nessun articolo con importo valido.")
                
        except Exception as e:
            st.error(f"Errore di lettura nel file {file_caricato.name}: {e}")
            
    if totale_lordo_globale > 0:
        st.markdown('<hr style="border: 2px solid #000; margin-top: 40px;" class="no-print">', unsafe_allow_html=True)
        st.markdown(f"""
            <div style="page-break-inside: avoid; border: 2px solid #1e293b; padding: 20px; border-radius: 8px; margin-top: 20px;">
                <h3 style="margin-top:0; text-align:center;">📊 RIEPILOGO GLOBALE REPORT (VALORI LORDI)</h3>
                <div style="display: flex; justify-content: space-around; margin-top: 15px;">
                    <div style="text-align: center;">
                        <p style="margin:0; font-size: 16px; color: #475569;">Totale Costo Lordo Inserito</p>
                        <h2 style="margin:0; color: #0f172a;">€ {formatta_euro(totale_lordo_globale)}</h2>
                    </div>
                    <div style="text-align: center;">
                        <p style="margin:0; font-size: 16px; color: #475569;">Totale Ammortizzabile (Beni)</p>
                        <h2 style="margin:0; color: #047857;">€ {formatta_euro(totale_cespiti_globale)}</h2>
                    </div>
                    <div style="text-align: center;">
                        <p style="margin:0; font-size: 16px; color: #475569;">Totale Spese Correnti (Servizi)</p>
                        <h2 style="margin:0; color: #b91c1c;">€ {formatta_euro(totale_non_ammesso_globale)}</h2>
                    </div>
                </div>
            </div>
            
            <div class="no-print" style="text-align: center; margin-top: 30px; padding: 20px; background-color: #eff6ff; border: 2px dashed #2563eb; border-radius: 8px;">
                <h4 style="color: #1e3a8a; margin: 0 0 10px 0; font-size: 18px;">🖨️ REPORT PRONTO PER LA STAMPA</h4>
                <p style="color: #334155; font-size: 16px; margin: 0;">
                    Il sistema di sicurezza impedisce l'avvio automatico.<br>
                    Per impaginare e stampare il documento ufficiale, premi <b>CTRL + P</b> sulla tastiera.
                </p>
            </div>
        """, unsafe_allow_html=True)
