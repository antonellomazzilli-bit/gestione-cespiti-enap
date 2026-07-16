
Gemini
Nuova chat
Cerca nelle chat
Video
Raccolta
Gem
Nuovo notebook
Statuto+ C.C.N.L. + CODICE CIVILE
2013 Bylaws of the En.A.P. Puglia Association
Tutti i notebook
Ammortamento: Criteri Civili e Fiscali
Allestire Laboratorio Estetista per Accreditamento
Richiesta Manutenzione Muffa e Infiltrazioni
Gestione Finanziaria Azienda Agricola con Streamlit
Olio EVO: Analisi Digitale e Fisica
Calcolo Tasso Netto Investimento
Mi crei il logo un'immagine per la mia azienda agricola che si chiama loro di San Vittore azienda agricola prettamente di che si occupa di olive e olio.
Modello Verbale CdA Legale e Formale
Analisi Pignoramento e Piano d'Azione
Trani-Tricase: Distanza e Tempo di Viaggio
Relazione Comportamento Dipendente Aggressivo
VBA per spalmare importo su righe visibili
Registrazione Operazioni Contabili in Partita Doppia
Contestazione Disciplinare per Ritardo Dipendente
Ricerca Dati con Criteri Multipli Excel
Aggiornamento Saldi Bancari da PDF a Excel
Reclamo per Mancata Manutenzione Piscina
Comunicazioni aziendali: canali ufficiali obbligatori
Richiamo Disciplinare Dipendente: Richiesta Dettagli
Accordo Aziendale Dipendenti: Bozza e Guida
App Gestione Ore e Spese Aziendali
Generazione Ricevute da Google Sheets
Comunicazione Cambio Proprietà e Arretrati
Applicativo Gestione Finanziaria Azienda Agricola
Richiesta Mail Dimissioni CdA
Analisi Documento Tecnico Immobiliare
Crea un avatar da questa immagine
Ruolo RLS: Guida Normativa e Operativa
Guida alla Pensione con 30 Contributi
Analisi Estratto Conto e Risparmio
Presidente e Straordinario Senza Board
Dimissioni Consigliere CdA: Procedura e Sostituzione
Unire File Excel con Python e Pandas
Dimissioni PEC per Tutela Legale
Accorpare file Excel con Python
Creare App Python per Richieste Ferie
Mobbing: Cause, Strategie e Prove
Richiesta App per Attività Commerciale
Analisi Statuto En.A.P. e Criticità Legali
Richiesta Smart Working Dettagliata e Inattaccabile
Operare con la Liquidità Forex
Investire 5000 Euro: Portafoglio 5 Anni
Progetto Valutazione Formazione Professionale
Gestire un Ente di Formazione Professionale
Coordinatore Formazione: Attività Post-Corso
Unire Tabelle Excel: Metodi e Consigli
Guida Corso Obbligo Formativo Puglia
Gestione Finanziaria Progetti 5 Sedi
Ricerca Testo in Stringhe Excel
VBA per Distribuzione Importo Prioritaria
Richiesta Offerta Acquisto PC e Licenze
Aliquote Ammortamento Fiscale Beni Strumentali
Percorso Obbligo Formativo: Fasi Chiave
Monitoraggio Spese Impegnate e Rendicontate
Metodo Proiezioni di Spesa Finanziaria
Bilancio Ente Formazione Professionale: Guida
CCNL Formazione: Livelli, Mansioni e Retribuzioni
Funzioni e capacità di Gemini

Attività
Corato BA, Italia
In base ai tuoi luoghi (lavoro)
Aggiorna posizione
Conversazione con Gemini
dobbiamo prevedere di poter utilizzare il software da qualsiasi pc

Ragionamento Interno Sintetico

Analisi dell'obiettivo: L'esigenza è trasformare un applicativo desktop locale (vincolato alla presenza di Python e file .bat su una specifica macchina) in una piattaforma universale, accessibile da qualsiasi dispositivo (Windows, Mac, tablet) senza alcuna configurazione pre-esistente. L'attuale affidamento alla sincronizzazione delle cartelle di lavoro mostra limiti strutturali quando si richiede mobilità totale.

Confronto di 3 Alternative:

Creazione di un eseguibile stand-alone (.exe) con PyInstaller: Converte il codice Python in un unico file cliccabile. (Scartata: Streamlit gestisce malissimo la conversione in .exe, risultando in file enormi, lenti all'avvio e spesso bloccati dagli antivirus aziendali).

Hosting su Server Locale (Intranet): Eseguire il programma su un singolo computer o server fisico sempre acceso in sede, rendendolo accessibile agli altri PC tramite l'indirizzo IP locale (es. 192.168.1.50:8501). (Scartata come prima scelta: funziona solo se si è fisicamente connessi alla rete del medesimo ufficio, vanificando il concetto di "qualsiasi PC" se si lavora in smart working o da un'altra sede).

Distribuzione Cloud (Streamlit Community Cloud / Render): Trasformare l'applicativo in una vera e propria Web App accessibile tramite un semplice indirizzo internet (URL) da qualsiasi browser. (Scelta ottimale: azzera i tempi di configurazione tecnica sui PC degli operatori, garantisce che tutti usino l'ultima versione aggiornata del codice e ottimizza il massimo impatto operativo).

Azione: Strutturare il piano di migrazione verso il Cloud, evidenziando le implicazioni sulla privacy dei dati (fatture XML) e proponendo l'infrastruttura necessaria.

Per rendere il software utilizzabile da qualsiasi postazione senza dover mai più installare Python, lanciare terminali o preoccuparsi delle configurazioni locali, dobbiamo trasformarlo in una Web App. In questo modo, per usare il classificatore basterà aprire Chrome o Edge e digitare un link (es. ammortamenti-ente.streamlit.app).

Ecco il piano d'azione per eseguire questa transizione.

Il Piano Concreto e Priorità
Priorità 1: Creazione del "Motore Remoto" (Repository)
Affinché il cloud possa far girare il tuo programma, il codice non può più risiedere solo nei tuoi documenti locali, ma deve essere ospitato su un deposito online.

Azione: Creare un account gratuito su GitHub (lo standard globale per il codice sorgente).

Caricamento: Creare un nuovo progetto (Repository) privato o pubblico e caricare al suo interno esclusivamente due file: il tuo app_ammortamenti.py e un nuovo file di testo chiamato requirements.txt.

Configurazione dipendenze: Il file requirements.txt dovrà contenere solo due parole, essenziali per dire al server cloud cosa installare:

Plaintext
streamlit
pandas
Priorità 2: Collegamento e Messa in Rete (Deploy)

Azione: Creare un account su Streamlit Community Cloud (completamente gratuito e nativamente integrato con la libreria che stiamo usando).

Collegamento: Collegare l'account Streamlit al profilo GitHub creato al passo precedente.

Lancio: Con tre clic, Streamlit leggerà il tuo file Python, installerà in automatico i requisiti e genererà un link web stabile.

Priorità 3: Ottimizzazione del Codice per il Cloud
Il codice attuale è già eccellente per il web, ma andrà testato il comportamento della funzione di stampa (CTRL+P). I browser gestiscono le finestre di stampa delle pagine web pubbliche in modo leggermente diverso rispetto alle applicazioni lanciate da un terminale locale.

Rischi, Errori Potenziali e Come Evitarli
Rischio Privacy e Trattamento Dati (GDPR): Caricando i file XML tramite una pagina web pubblica, i dati fiscali dell'ente transitano per un server cloud esterno (generalmente ospitato negli Stati Uniti).

Come evitarlo: Il codice che abbiamo scritto non salva i file XML (li elabora nella memoria volatile "RAM" del server e li distrugge appena chiudi la pagina web). Tuttavia, dal punto di vista normativo, devi assicurarti che l'amministrazione approvi il transito di fatture non anonimizzate su infrastrutture cloud esterne. In alternativa, si può optare per un hosting Cloud basato in Europa (es. Render o server VPS aziendali in Germania/Italia).

Correlazioni Nascoste nei Dati
Analizzando l'infrastruttura, emerge una correlazione inversa tra l'accessibilità universale e la sicurezza passiva. Mantenendo i file su una rete locale, la lentezza operativa fa da scudo naturale contro le dispersioni. Spostando l'applicativo su un URL globale, l'efficienza schizza al 100%, ma il rischio di accesso improprio cresce proporzionalmente. Se il link viene condiviso per errore, chiunque potrebbe utilizzare lo strumento aziendale.

Identificazione di ciò che manca e cosa aggiungere
Ciò che manca attualmente per un passaggio al Cloud aziendale sicuro è un sistema di autenticazione.
Cosa aggiungere: Prima di pubblicare la pagina, dovremo aggiungere circa 10 righe di codice all'inizio del file app_ammortamenti.py per creare una barriera d'accesso. Un semplice modulo di login che richieda una password fissa (es. una password concordata tra gli operatori amministrativi) bloccherà l'interfaccia a chiunque clicchi sul link senza autorizzazione.

Vogliamo procedere con la predisposizione per il Cloud esterno (creando il deposito su GitHub e l'autenticazione con password), oppure per questioni di rigida privacy sui file XML preferisci esplorare la configurazione di un "Server Interno" ospitato su una macchina fissa della vostra rete?

lo facciamo dopo, adesso per ogni fattura mi devi scrivere ogni songolo articolo presente magari con una note se può essere scartato

Ragionamento Interno Sintetico

Analisi dell'obiettivo: Accantoniamo temporaneamente il Cloud. L'obiettivo attuale è garantire la massima trasparenza visiva: il report deve elencare analiticamente ogni singolo articolo della fattura e applicare una "nota esplicita" che indichi a colpo d'occhio se quel prodotto/servizio viene scartato (non patrimonializzato) e perché.

Soluzione tecnica:

Confermo la struttura riga per riga per mostrare ogni singolo dettaglio dell'XML.

Aggiungo una colonna denominata "Azione Libro Cespiti (Note)".

Programmo una regola semantica: se l'algoritmo rileva un'aliquota dello 0% (es. manodopera, canoni, ecc.), stamperà la nota "❌ SCARTATO (Spesa Corrente)". Se rileva un'aliquota > 0, stamperà "✔️ DA ISCRIVERE".

Ottimizzazione: Integro questa nuova colonna nell'impaginazione del foglio A4, calibrando le larghezze per non "schiacciare" le descrizioni degli articoli.

Ricevuto. Lasciamo il Cloud in sospeso per il momento e concentriamoci sulla precisione analitica del report cartaceo.

Ho modificato il codice affinché ogni singolo articolo presente nel file XML venga stampato sulla sua riga dedicata. Inoltre, ho aggiunto una nuova colonna finale chiamata "Azione Libro Cespiti (Note)": il programma scriverà esplicitamente "❌ SCARTATO" per i servizi di esercizio e "✔️ DA ISCRIVERE" per i beni ammortizzabili, togliendo qualsiasi dubbio all'operatore che legge la stampa.

Il Codice Aggiornato
Fai CTRL+A all'interno del tuo file app_ammortamenti.py, premi CANC per pulire e incolla questa versione definitiva:

Python
import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import html 

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- INIEZIONE CSS: IMPAGINAZIONE AVANZATA PER LA STAMPA ---
st.markdown("""
    <style>
        .titolo-fattura {
            background-color: #f8fafc;
            padding: 12px 15px;
            border-left: 5px solid #2563eb;
            border-radius: 6px 6px 0 0;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .fattura-container {
            background-color: white;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            margin-bottom: 30px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            page-break-inside: avoid !important; 
        }
        
        table.custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        
        table.custom-table th, table.custom-table td {
            padding: 8px 10px;
            border-bottom: 1px solid #e2e8f0;
            text-align: right;
            vertical-align: middle;
        }
        
        table.custom-table td:first-child, table.custom-table th:first-child {
            text-align: left; 
            width: 35%;
        }
        
        table.custom-table th {
            background-color: #f1f5f9;
            font-weight: bold;
            color: #0f172a;
        }
        
        @media print {
            header, footer, .stDeployButton, [data-testid="stFileUploader"], .no-print { 
                display: none !important; 
            }
            
            body, .stApp, .main, .block-container, div {
                background-color: transparent !important;
                background-image: none !important;
                color: black !important;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
            }
            
            .block-container { 
                padding: 0 !important;
                max-width: 100% !important;
            }
            
            table.custom-table th, table.custom-table td {
                border: 1px solid #94a3b8 !important;
            }
            
            table.custom-table th {
                background-color: #cbd5e1 !important; 
                -webkit-print-color-adjust: exact !important; 
                print-color-adjust: exact !important;
            }
            
            .titolo-fattura {
                background-color: transparent !important;
                border-left: none !important;
                border-bottom: 2px solid #000 !important;
                box-shadow: none !important;
                padding: 0 0 8px 0 !important;
            }
            
            .fattura-container {
                border: none !important;
                box-shadow: none !important;
                margin-bottom: 40px !important;
            }
            
            .print-header {
                display: block !important;
                text-align: center;
                border-bottom: 3px solid #000;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .print-header h2 { margin: 0; font-size: 24px; text-transform: uppercase; }
            .print-header p { margin: 5px 0 0 0; font-size: 14px; color: #555; }
        }
        
        .print-header { display: none; }
    </style>
""", unsafe_allow_html=True)

# --- FUNZIONI DI FORMATTAZIONE EUROPEA ---
def formatta_euro(valore):
    return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatta_decimale(valore):
    val_formattato = f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if val_formattato.endswith(",00"): return val_formattato[:-3]
    return val_formattato

def formatta_anni(valore):
    return str(valore).replace(".", ",")

# 1. DATABASE CESPITI E FILTRI PAROLE CHIAVE
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "manutenzione", "noleggio", "energia", "assicurazione", "servizio", "lavori", "pitturazione", "cartongesso", "manodopera"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups "]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo):
    if not descrizione: return "Sconosciuto", 0.0
    desc_lower = descrizione.lower()
    
    if any(parola in desc_lower for parola in cluster_servizi_pesanti): return "Spesa Corrente / Servizio non ammortizzabile", 0.0
    
    if any(parola in desc_lower for parola in cluster_sollevamento): categoria, aliquota = "AA2 - Impianti e mezzi di sollevamento (Sottosp. 4)", 7.5
    elif any(parola in desc_lower for parola in cluster_hardware): categoria, aliquota = "AA4 - Elaboratori elettronici e sistemi hardware (Sottosp. 41)", 33.33
    elif any(parola in desc_lower for parola in cluster_software): categoria, aliquota = "AA1 - Diritti di utilizzazione delle opere dell'ingegno / Software (Sottosp. 42)", 50.0
    elif any(parola in desc_lower for parola in cluster_macchine_uff): categoria, aliquota = "AA8 - Macchine d'ufficio elettroniche (Sottosp. 13)", 20.0
    elif any(parola in desc_lower for parola in cluster_impianti): categoria, aliquota = "AA2 - Impianti generici di condizionamento, allarme e cablaggio (Sottosp. 44)", 16.66
    elif any(parola in desc_lower for parola in cluster_mobili): categoria, aliquota = "AA7 - Mobili e arredi ordinari d'ufficio (Sottosp. 43)", 12.50
    elif any(parola in desc_lower for parola in cluster_laboratorio): categoria, aliquota = "AA8 - Macchinari, apparecchi e attrezzature di laboratorio (Sottosp. 5)", 15.0
    elif any(parola in desc_lower for parola in cluster_accessori): return "Spesa Corrente / Servizio accessorio", 0.0
    else: categoria, aliquota = "AA3 - Attrezzatura Generica (Da Verificare)", 15.0
    
    if prezzo <= 516.46 and aliquota > 0:
        return "AA9 - Beni ammortizzabili meno di 1 anno (Sottosp. 35)", 100.0
        
    return categoria, aliquota

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
    totale_imponibile_globale = 0.0
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
                        if 'Denominazione' in figlio.tag and fornitore == "Non specificato":
                            fornitore = figlio.text
                            
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
                                
                    if prezzo_totale > 0:
                        prezzo_finale = prezzo_totale
                    else:
                        prezzo_finale = prezzo_unitario * quantita
                    
                    if descrizione and prezzo_finale > 0:
                        iva_calcolata = prezzo_finale * (aliquota_iva_riga / 100.0)
                        categoria, aliquota = classifica_voce(descrizione, prezzo_finale)
                        anni = 0.0 if aliquota == 0 else (1.0 if aliquota == 100 else round(100 / aliquota, 1))
                        
                        # --- GENERAZIONE DELLA NOTA DI SCARTO ---
                        if aliquota == 0:
                            nota_azione = "❌ SCARTATO (Spesa Corrente)"
                        else:
                            nota_azione = "✔️ DA ISCRIVERE"
                        
                        righe_estratte.append({
                            "Descrizione": descrizione,
                            "Valore_num": prezzo_finale,
                            "IVA_num": iva_calcolata,
                            "Esito Fiscale": categoria,
                            "Aliquota_num": aliquota,
                            "Anni_num": anni,
                            "Nota_Azione": nota_azione
                        })
            
            if importo_totale_doc == 0.0 and (imponibile_riepilogo > 0 or importo_iva_totale > 0):
                importo_totale_doc = imponibile_riepilogo + importo_iva_totale
                
            if righe_estratte:
                df_calc = pd.DataFrame(righe_estratte)
                totale_spese = df_calc["Valore_num"].sum()
                totale_iva_righe = df_calc["IVA_num"].sum()
                
                cespiti_puri = df_calc[df_calc["Aliquota_num"] > 0]["Valore_num"].sum()
                totale_non_ammesso_riga = totale_spese - cespiti_puri
                
                totale_imponibile_globale += totale_spese
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
                <th>Esito Fiscale (Aziendale / Normativo)</th>
                <th>Aliquota Amm. (%)</th>
                <th>Azione Libro Cespiti (Note)</th>
            </tr>
        </thead>
        <tbody>
"""
                
                for riga in righe_estratte:
                    stile_cella = "color: #b91c1c; font-weight: 500;" if riga['Aliquota_num'] == 0 else "color: #1e293b;"
                    
                    # Evidenziazione colore specifico per la colonna Note
                    colore_nota = "#b91c1c" if riga['Aliquota_num'] == 0 else "#047857"
                    
                    html_fattura += f"""
            <tr>
                <td style="{stile_cella}">{riga['Descrizione']}</td>
                <td style="{stile_cella}">{formatta_euro(riga['Valore_num'])}</td>
                <td style="{stile_cella}">{formatta_euro(riga['IVA_num'])}</td>
                <td style="{stile_cella}"><b>{riga['Esito Fiscale']}</b></td>
                <td style="{stile_cella}">{formatta_decimale(riga['Aliquota_num'])}</td>
                <td style="color: {colore_nota}; font-weight: bold;">{riga['Nota_Azione']}</td>
            </tr>
"""
                    
                html_fattura += f"""
            <tr style="background-color: #f1f5f9; font-weight: bold; color: #0f172a; border-top: 2px solid #94a3b8;">
                <td style="text-align: right; color: #0f172a;">TOTALE RIGHE</td>
                <td style="color: #0f172a;">{formatta_euro(totale_spese)}</td>
                <td style="color: #0f172a;">{formatta_euro(totale_iva_righe)}</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
    <div style="text-align: right; padding: 8px 12px; background-color: #ffffff; border-radius: 0 0 6px 6px; font-size: 14px;">
        <b>Imponibile Riga:</b> € {formatta_euro(totale_spese)} &nbsp;&nbsp;|&nbsp;&nbsp; 
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
            
    if totale_imponibile_globale > 0:
        st.markdown('<hr style="border: 2px solid #000; margin-top: 40px;" class="no-print">', unsafe_allow_html=True)
        st.markdown(f"""
            <div style="page-break-inside: avoid; border: 2px solid #1e293b; padding: 20px; border-radius: 8px; margin-top: 20px;">
                <h3 style="margin-top:0; text-align:center;">📊 RIEPILOGO GLOBALE REPORT</h3>
                <div style="display: flex; justify-content: space-around; margin-top: 15px;">
                    <div style="text-align: center;">
                        <p style="margin:0; font-size: 16px; color: #475569;">Totale Imponibile Caricato</p>
                        <h2 style="margin:0; color: #0f172a;">€ {formatta_euro(totale_imponibile_globale)}</h2>
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
ritorniamo al streamlite

Ragionamento Interno Sintetico

Analisi: L'esigenza è riprendere il processo di migrazione dell'applicativo dal server locale (PC fisico tramite file .bat) all'infrastruttura web universale (Streamlit Community Cloud). L'obiettivo è generare un indirizzo web (URL) accessibile da qualsiasi computer senza dover configurare Python o l'ambiente di sviluppo.

Alternative valutate (per il trasferimento del codice):

Uso della riga di comando (Git Bash). (Scartata: richiede l'installazione del motore Git e la conoscenza dei comandi di gestione repository, allungando i tempi).

Utilizzo del software GitHub Desktop. (Scartata: costringe all'installazione di un ulteriore programma sul PC aziendale).

Caricamento manuale (Drag & Drop) tramite interfaccia web di GitHub. (Scelta ottimale: non richiede alcuna installazione locale, l'impatto visivo azzera gli errori di digitazione e l'esecuzione è immediata).

Scelta: Procedo con l'alternativa 3. Ottimizzo i passaggi per arrivare alla pubblicazione online nel minor tempo possibile.

Il Piano Concreto e Priorità
Per trasformare il file Python in una Web App pubblica e utilizzabile da qualsiasi dispositivo, dobbiamo completare l'allineamento tra due piattaforme gratuite: GitHub (che farà da cassaforte per il codice) e Streamlit Cloud (che farà da motore per farlo funzionare).

Priorità 1 - Creazione del Deposito (GitHub)

Vai su github.com e registra un account gratuito.

In alto a sinistra o in alto a destra, clicca sul pulsante "New" o "+" per creare un nuovo Repository.

Inserisci un nome (es. gestione-cespiti-enap).

Seleziona l'opzione "Private" (fondamentale per non rendere il tuo codice e le logiche aziendali visibili al pubblico).

Spunta la casella "Add a README file" (aiuta a inizializzare la cartella).

Clicca su "Create repository".

Priorità 2 - Caricamento dei file essenziali
Ora che hai la tua "cartella cloud", devi inserirci dentro il motore.

Nella pagina del tuo nuovo repository, clicca sul pulsante "Add file" e scegli "Upload files".

Trascina all'interno della finestra il tuo file aggiornato app_ammortamenti.py.

Clicca sul pulsante verde "Commit changes" per salvare.

Ripeti l'operazione (Add file -> Create new file) per creare direttamente online un file chiamato esattamente requirements.txt.

All'interno di questo file, scrivi solo queste due righe (servono a dire al server cosa installare):

Plaintext
streamlit
pandas
Clicca di nuovo su "Commit changes".

Priorità 3 - Il Lancio su Streamlit Cloud (Deploy)

Vai su share.streamlit.io e accedi cliccando su "Continue with GitHub".

Autorizza Streamlit a leggere i tuoi repository.

Clicca sul pulsante "New app".

Seleziona "Yep, I have an app" (oppure usa il modulo di ricerca rapida).

Compila i tre campi richiesti:

Repository: seleziona dal menu a tendina gestione-cespiti-enap (o il nome che gli hai dato).

Branch: lascia main.

Main file path: scrivi app_ammortamenti.py.

Clicca su "Deploy!".

Rischi, Errori Potenziali e Come Evitarli
Rischio di stallo in fase di caricamento (Baking): Durante il primissimo deploy, potresti vedere un'icona di caricamento (un "forno" che cuoce) che dura svariati minuti. Se il sistema si blocca in questa fase, spesso è per un errore di battitura nel file dei requisiti.

Come evitarlo: Assicurati che il file caricato su GitHub si chiami esattamente requirements.txt (tutto minuscolo e con la "s" finale) e che al suo interno non ci siano spazi o simboli strani oltre ai nomi delle librerie streamlit e pandas.

Correlazioni Nascoste nei Dati
Eseguendo questo trasferimento, si slega completamente la potenza di calcolo dall'hardware locale. Anche se l'operatore caricasse 50 fatture XML pesanti da un vecchio tablet con scarse prestazioni, la velocità di calcolo della tabella e dell'IVA rimarrebbe altissima, perché lo sforzo di elaborazione viene assorbito dai server di Streamlit e non dal dispositivo fisico che visualizza la pagina.

Identificazione di ciò che manca e cosa aggiungere
Attualmente, chiunque in possesso dell'URL generato da Streamlit Cloud potrebbe aprire la pagina. Essendo l'interfaccia usata per caricare dati finanziari e fiscali dell'ente, manca un sistema di autenticazione.
Cosa aggiungere: Appena avrai verificato che l'interfaccia web si apre e funziona correttamente al link generato, il passaggio successivo sarà aggiungere un blocco di sicurezza (Login) all'inizio del file app_ammortamenti.py. Integreremo un campo dove l'utente dovrà digitare una password aziendale per far apparire il modulo di caricamento delle fatture.

non riesco ad importare l'app da

Ragionamento Interno Sintetico

Analisi: Il tuo messaggio si è interrotto ("da..."), ma trovandoci nella fase 3 del piano (Il Lancio su Streamlit Cloud), è altamente probabile che il blocco riguardi il tentativo di far "leggere" a Streamlit il codice caricato su GitHub.

Alternative valutate sulle cause del blocco:

Permessi per Repository Privati: Streamlit Cloud, di default, legge solo i progetti pubblici. Se hai impostato il progetto come "Private" (come consigliato), Streamlit non lo trova nel menu a tendina.

Sincronizzazione account mancante: L'accesso a Streamlit è stato fatto con una mail diversa da quella di GitHub.

Percorso file errato: Il sistema chiede il nome esatto del file principale, ma non lo trova nella cartella principale di GitHub.

Scelta: Poiché l'opzione 1 è la causa del 90% degli stalli in questa fase, focalizzo il piano d'emergenza sullo sblocco dei permessi di sicurezza, chiedendoti contestualmente di completare la frase per darti la soluzione esatta.

Il tuo messaggio si è tagliato, ma immagino tu ti sia bloccato nella schermata di Streamlit dove devi selezionare il progetto.

Il blocco più comune in questa fase avviene perché Streamlit non riesce a vedere i progetti privati di GitHub finché non gli diamo il permesso esplicito.

Piano di Sblocco Rapido (Priorità)
Se non vedi il tuo progetto gestione-cespiti-enap nel menu a tendina di Streamlit, fai così:

Autorizza i progetti privati: Nella schermata di Streamlit dove ti chiede di creare la nuova app, guarda in alto a destra o vicino al menu a tendina. Dovresti vedere un link o un pulsante con scritto "Paste GitHub URL" oppure un avviso per aggiustare i "GitHub permissions".

Usa il link diretto: Vai sulla pagina del tuo progetto su GitHub, copia l'intero indirizzo web in alto (es. [https://github.com/tuonome/gestione-cespiti-enap](https://github.com/tuonome/gestione-cespiti-enap)) e incollalo in Streamlit cliccando su "Paste GitHub URL".

Se ti chiede di confermare l'accesso a repository privati, acconsenti.

Identificazione di ciò che manca
Per darti la soluzione millimetrica, mi manca un pezzo del tuo messaggio. Cosa stavi scrivendo esattamente dopo il "da"?

Hai ricevuto una scritta d'errore rossa su Streamlit (es. "App does not exist" o "ModuleNotFoundError") oppure non riesci proprio a far dialogare i due siti? Dimmi cosa vedi a schermo e lo risolviamo in un istante.

L'immagine parla chiaro! Non preoccuparti, sei a un millimetro dal traguardo. Ci sono due ostacoli ben precisi che Streamlit ti sta segnalando in rosso, ma si risolvono in un istante.

1. Il nome del file è predefinito (Terza casella)
Streamlit inserisce in automatico il nome standard streamlit_app.py nella casella "Main file path", ed è per questo che dice che non lo trova.

Azione: Clicca su quell'ultima casella rossa, cancella il testo e digita il nome esatto del tuo file: app_ammortamenti.py

2. Streamlit non "vede" la tua cartella privata (Prima casella)
Dato che hai creato il repository su GitHub in modalità "Privata" (fondamentale per proteggere i dati contabili), Streamlit attualmente è bloccato fuori. Finché non gli dai le chiavi, ti dirà "This repository does not exist".

Ecco come sbloccare i permessi:

Il Metodo dalle Impostazioni (Consigliato):

Esci da questa schermata cliccando sulla freccia blu "<- Back".

Nella schermata principale di Streamlit, clicca in alto a destra o a sinistra sull'icona del tuo profilo (o le impostazioni dell'area di lavoro) e vai su Settings (Impostazioni).

Cerca la sezione Linked Accounts (Account collegati) o GitHub.

Troverai un'opzione per gestire i permessi. Devi autorizzare Streamlit ad accedere anche ai Private repositories (Repository privati).

Clicca per autorizzare (si aprirà una finestrella di GitHub per confermare la password o dare l'ok).

Il Metodo Rapido (Alternativo):

Rimanendo nella schermata della tua foto, clicca sulla piccola scritta azzurra "Paste GitHub URL" (appena sopra la prima casella rossa).

Vai nella scheda di GitHub (vedo dal browser che ce l'hai aperta in alto), apri il tuo file app_ammortamenti.py e copia l'intero indirizzo web in alto (es. [https://github.com/antonellomazzilli-bit/.../app_ammortamenti.py](https://github.com/antonellomazzilli-bit/.../app_ammortamenti.py)).

Incollalo in Streamlit. Se non avevi dato i permessi, questa azione forza l'apertura automatica del pop-up di autorizzazione per i repository privati.

Non appena darai il permesso per i progetti privati e sistemerai il nome del file in app_ammortamenti.py, le caselle diventeranno blu e il tasto Deploy! in basso si attiverà.

l'iva per noi è un costo quindi va inserito nell'ammortamento

Ragionamento Interno Sintetico

Analisi dell'obiettivo: L'inclusione dell'IVA nel calcolo dell'ammortamento (IVA indetraibile considerata come costo) è una regola contabile fondamentale. Questo cambia radicalmente la base di calcolo patrimoniale: il valore del bene non è più l'imponibile, ma il lordo (Imponibile + IVA).

Soluzione tecnica:

Calcolare il prezzo_lordo sommando il netto all'IVA di riga.

Passare il prezzo_lordo (non più il netto) alla funzione di classificazione. Questo è vitale perché un bene da 450€ netti con IVA al 22% (99€) diventa un bene da 549€ lordi, superando così la soglia di sbarramento dei 516,46€ e passando dall'ammortamento in un solo anno (100%) all'ammortamento pluriennale.

Aggiungere la colonna "Valore Lordo (€)" nella tabella per garantire totale trasparenza contabile.

Aggiornare i contatori globali per sommare i valori lordi.

Piano Concreto e Priorità
Priorità 1 - Patrimonializzazione dell'IVA
Ho modificato il motore matematico. Ora il programma prende il valore netto, calcola l'IVA e genera il Valore Lordo. È quest'ultimo valore che viene inviato al Libro Cespiti e analizzato per capire se supera la soglia normativa dei 516,46€.

Priorità 2 - Aggiornamento Visivo
Ho aggiunto la colonna "Valore Lordo (€)" all'interno della tabella HTML. In questo modo, in fase di stampa, chi revisiona il documento vedrà l'esatta progressione matematica: Netto + IVA = Lordo da Ammortizzare.

Fai il solito CTRL+A all'interno del file app_ammortamenti.py, cancella tutto con CANC e incolla questa versione aggiornata:

Python
import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import html 

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- INIEZIONE CSS: IMPAGINAZIONE AVANZATA PER LA STAMPA ---
st.markdown("""
    <style>
        .titolo-fattura {
            background-color: #f8fafc;
            padding: 12px 15px;
            border-left: 5px solid #2563eb;
            border-radius: 6px 6px 0 0;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .fattura-container {
            background-color: white;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            margin-bottom: 30px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            page-break-inside: avoid !important; 
        }
        
        table.custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        
        table.custom-table th, table.custom-table td {
            padding: 8px 10px;
            border-bottom: 1px solid #e2e8f0;
            text-align: right;
            vertical-align: middle;
        }
        
        table.custom-table td:first-child, table.custom-table th:first-child {
            text-align: left; 
            width: 30%;
        }
        
        table.custom-table th {
            background-color: #f1f5f9;
            font-weight: bold;
            color: #0f172a;
        }
        
        @media print {
            header, footer, .stDeployButton, [data-testid="stFileUploader"], .no-print { 
                display: none !important; 
            }
            
            body, .stApp, .main, .block-container, div {
                background-color: transparent !important;
                background-image: none !important;
                color: black !important;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
            }
            
            .block-container { 
                padding: 0 !important;
                max-width: 100% !important;
            }
            
            table.custom-table th, table.custom-table td {
                border: 1px solid #94a3b8 !important;
            }
            
            table.custom-table th {
                background-color: #cbd5e1 !important; 
                -webkit-print-color-adjust: exact !important; 
                print-color-adjust: exact !important;
            }
            
            .titolo-fattura {
                background-color: transparent !important;
                border-left: none !important;
                border-bottom: 2px solid #000 !important;
                box-shadow: none !important;
                padding: 0 0 8px 0 !important;
            }
            
            .fattura-container {
                border: none !important;
                box-shadow: none !important;
                margin-bottom: 40px !important;
            }
            
            .print-header {
                display: block !important;
                text-align: center;
                border-bottom: 3px solid #000;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .print-header h2 { margin: 0; font-size: 24px; text-transform: uppercase; }
            .print-header p { margin: 5px 0 0 0; font-size: 14px; color: #555; }
        }
        
        .print-header { display: none; }
    </style>
""", unsafe_allow_html=True)

# --- FUNZIONI DI FORMATTAZIONE EUROPEA ---
def formatta_euro(valore):
    return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatta_decimale(valore):
    val_formattato = f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if val_formattato.endswith(",00"): return val_formattato[:-3]
    return val_formattato

def formatta_anni(valore):
    return str(valore).replace(".", ",")

# 1. DATABASE CESPITI E FILTRI PAROLE CHIAVE
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "manutenzione", "noleggio", "energia", "assicurazione", "servizio", "lavori", "pitturazione", "cartongesso", "manodopera"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups "]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo_lordo):
    if not descrizione: return "Sconosciuto", 0.0
    desc_lower = descrizione.lower()
    
    if any(parola in desc_lower for parola in cluster_servizi_pesanti): return "Spesa Corrente / Servizio non ammortizzabile", 0.0
    
    if any(parola in desc_lower for parola in cluster_sollevamento): categoria, aliquota = "AA2 - Impianti e mezzi di sollevamento (Sottosp. 4)", 7.5
    elif any(parola in desc_lower for parola in cluster_hardware): categoria, aliquota = "AA4 - Elaboratori elettronici e sistemi hardware (Sottosp. 41)", 33.33
    elif any(parola in desc_lower for parola in cluster_software): categoria, aliquota = "AA1 - Diritti di utilizzazione delle opere dell'ingegno / Software (Sottosp. 42)", 50.0
    elif any(parola in desc_lower for parola in cluster_macchine_uff): categoria, aliquota = "AA8 - Macchine d'ufficio elettroniche (Sottosp. 13)", 20.0
    elif any(parola in desc_lower for parola in cluster_impianti): categoria, aliquota = "AA2 - Impianti generici di condizionamento, allarme e cablaggio (Sottosp. 44)", 16.66
    elif any(parola in desc_lower for parola in cluster_mobili): categoria, aliquota = "AA7 - Mobili e arredi ordinari d'ufficio (Sottosp. 43)", 12.50
    elif any(parola in desc_lower for parola in cluster_laboratorio): categoria, aliquota = "AA8 - Macchinari, apparecchi e attrezzature di laboratorio (Sottosp. 5)", 15.0
    elif any(parola in desc_lower for parola in cluster_accessori): return "Spesa Corrente / Servizio accessorio", 0.0
    else: categoria, aliquota = "AA3 - Attrezzatura Generica (Da Verificare)", 15.0
    
    # Lo sbarramento viene ora calcolato sul COSTO LORDO (inclusa IVA indetraibile)
    if prezzo_lordo <= 516.46 and aliquota > 0:
        return "AA9 - Beni ammortizzabili meno di 1 anno (Sottosp. 35)", 100.0
        
    return categoria, aliquota

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
                        if 'Denominazione' in figlio.tag and fornitore == "Non specificato":
                            fornitore = figlio.text
                            
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
                                
                    if prezzo_totale > 0:
                        prezzo_netto = prezzo_totale
                    else:
                        prezzo_netto = prezzo_unitario * quantita
                    
                    if descrizione and prezzo_netto > 0:
                        iva_calcolata = prezzo_netto * (aliquota_iva_riga / 100.0)
                        
                        # --- CALCOLO DEL LORDO (IL VERO COSTO DEL BENE) ---
                        prezzo_lordo = prezzo_netto + iva_calcolata
                        
                        categoria, aliquota = classifica_voce(descrizione, prezzo_lordo)
                        anni = 0.0 if aliquota == 0 else (1.0 if aliquota == 100 else round(100 / aliquota, 1))
                        
                        if aliquota == 0:
                            nota_azione = "❌ SCARTATO (Spesa Corrente)"
                        else:
                            nota_azione = "✔️ DA ISCRIVERE (Lordo)"
                        
                        righe_estratte.append({
                            "Descrizione": descrizione,
                            "Valore_Netto": prezzo_netto,
                            "IVA_num": iva_calcolata,
                            "Valore_Lordo": prezzo_lordo,
                            "Esito Fiscale": categoria,
                            "Aliquota_num": aliquota,
                            "Anni_num": anni,
                            "Nota_Azione": nota_azione
                        })
            
            if importo_totale_doc == 0.0 and (imponibile_riepilogo > 0 or importo_iva_totale > 0):
                importo_totale_doc = imponibile_riepilogo + importo_iva_totale
                
            if righe_estratte:
                df_calc = pd.DataFrame(righe_estratte)
                totale_netto_spese = df_calc["Valore_Netto"].sum()
                totale_iva_righe = df_calc["IVA_num"].sum()
                totale_lordo_spese = df_calc["Valore_Lordo"].sum()
                
                # Il calcolo del libro cespiti ora somma i VALORI LORDI
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
                <td style="color: {colore_nota}; font-weight: bold;">{riga['Nota_Azione']}</td>
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
Rischi, Errori Potenziali e Come Evitarli
Rischio di sforamento della soglia (L'Effetto 516,46€): Includendo l'IVA nel costo, alcuni articoli che prima risultavano deducibili integralmente nell'anno (perché il loro imponibile era di 450€), ora supereranno la soglia di 516,46€ per effetto dell'imposta.

Come evitarlo: Contabilmente non c'è nulla da evitare, questo è esattamente l'effetto legale corretto quando l'IVA è indetraibile. Il programma è stato istruito per controllare il superamento del limite dopo aver aggiunto l'imposta, impedendo decurtazioni fiscali scorrette.

Correlazioni Nascoste nei Dati
Con il passaggio al regime del Valore Lordo, tutti i riepiloghi globali a fondo pagina (i 3 box colorati) mostreranno importi nettamente più alti, poiché l'IVA non è più un numero "parallelo", ma è stata fusa all'interno dei costi di struttura. La somma verde (Cespiti) e la somma rossa (Spese Correnti) spaccheranno al centesimo il totale del Costo Lordo Inserito.

spiega la motivazione dello scarto

Ragionamento Interno Sintetico

Analisi dell'obiettivo: Attualmente il programma etichetta i servizi con un generico "❌ SCARTATO (Spesa Corrente)". L'obiettivo è rendere l'algoritmo parlante, costringendolo a dichiarare esplicitamente quale parola chiave (es. "pitturazione", "canone", "noleggio") ha innescato la regola di esclusione per quella specifica riga.

Confronto di 3 Alternative:

Creare una colonna aggiuntiva "Motivazione". (Scartata: aggiungere un'ulteriore colonna stringerebbe troppo lo spazio per la descrizione principale, rendendo illeggibile la tabella in fase di stampa A4).

Sostituire l'Esito Fiscale con il Motivo. (Scartata: l'esito fiscale serve a indicare la natura della spesa ai fini di bilancio).

Integrare dinamicamente la parola chiave intercettata all'interno della cella "Azione Libro Cespiti", scrivendola in piccolo sotto la nota principale. (Scelta ottimale: massimizza la precisione informativa mantenendo il foglio di stampa elegante e compatto).

Piano d'Azione: Modificare la funzione di classificazione affinché, invece di cercare solo se una parola è presente, estragga l'esatta parola trovata (motivo_scarto) e la restituisca per la stampa a video.

Il Piano Concreto e il Codice Definitivo
Ho potenziato il motore di classificazione. Da ora in poi, quando il sistema scarta una voce, leggerai esattamente quale parola ha bloccato l'ammortamento (es. Motivo: Rilevato servizio di tipo 'pitturazione'). Allo stesso modo, per i beni agevolati ti indicherà se sono stati dedotti integralmente per via della regola dei 516€.

Fai CTRL+A all'interno del file app_ammortamenti.py, premi CANC per pulire e incolla questa versione integrale:

Python
import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import html 

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- INIEZIONE CSS: IMPAGINAZIONE AVANZATA PER LA STAMPA ---
st.markdown("""
    <style>
        .titolo-fattura {
            background-color: #f8fafc;
            padding: 12px 15px;
            border-left: 5px solid #2563eb;
            border-radius: 6px 6px 0 0;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .fattura-container {
            background-color: white;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            margin-bottom: 30px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            page-break-inside: avoid !important; 
        }
        
        table.custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        
        table.custom-table th, table.custom-table td {
            padding: 8px 10px;
            border-bottom: 1px solid #e2e8f0;
            text-align: right;
            vertical-align: middle;
        }
        
        table.custom-table td:first-child, table.custom-table th:first-child {
            text-align: left; 
            width: 30%;
        }
        
        table.custom-table th {
            background-color: #f1f5f9;
            font-weight: bold;
            color: #0f172a;
        }
        
        @media print {
            header, footer, .stDeployButton, [data-testid="stFileUploader"], .no-print { 
                display: none !important; 
            }
            
            body, .stApp, .main, .block-container, div {
                background-color: transparent !important;
                background-image: none !important;
                color: black !important;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
            }
            
            .block-container { 
                padding: 0 !important;
                max-width: 100% !important;
            }
            
            table.custom-table th, table.custom-table td {
                border: 1px solid #94a3b8 !important;
            }
            
            table.custom-table th {
                background-color: #cbd5e1 !important; 
                -webkit-print-color-adjust: exact !important; 
                print-color-adjust: exact !important;
            }
            
            .titolo-fattura {
                background-color: transparent !important;
                border-left: none !important;
                border-bottom: 2px solid #000 !important;
                box-shadow: none !important;
                padding: 0 0 8px 0 !important;
            }
            
            .fattura-container {
                border: none !important;
                box-shadow: none !important;
                margin-bottom: 40px !important;
            }
            
            .print-header {
                display: block !important;
                text-align: center;
                border-bottom: 3px solid #000;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .print-header h2 { margin: 0; font-size: 24px; text-transform: uppercase; }
            .print-header p { margin: 5px 0 0 0; font-size: 14px; color: #555; }
        }
        
        .print-header { display: none; }
    </style>
""", unsafe_allow_html=True)

# --- FUNZIONI DI FORMATTAZIONE EUROPEA ---
def formatta_euro(valore):
    return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatta_decimale(valore):
    val_formattato = f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if val_formattato.endswith(",00"): return val_formattato[:-3]
    return val_formattato

def formatta_anni(valore):
    return str(valore).replace(".", ",")

# 1. DATABASE CESPITI E FILTRI PAROLE CHIAVE
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "manutenzione", "noleggio", "energia", "assicurazione", "servizio", "lavori", "pitturazione", "cartongesso", "manodopera"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups "]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo_lordo):
    if not descrizione: return "Sconosciuto", 0.0, "Nessuna descrizione"
    desc_lower = descrizione.lower()
    
    # Estrazione dinamica della parola che innesca lo scarto
    motivo_pesante = next((p for p in cluster_servizi_pesanti if p in desc_lower), None)
    if motivo_pesante: return "Spesa Corrente / Servizio non ammortizzabile", 0.0, f"Rilevato servizio di tipo: '{motivo_pesante}'"
    
    categoria = ""
    aliquota = 0.0
    
    if any(parola in desc_lower for parola in cluster_sollevamento): categoria, aliquota = "AA2 - Impianti e mezzi di sollevamento (Sottosp. 4)", 7.5
    elif any(parola in desc_lower for parola in cluster_hardware): categoria, aliquota = "AA4 - Elaboratori elettronici e sistemi hardware (Sottosp. 41)", 33.33
    elif any(parola in desc_lower for parola in cluster_software): categoria, aliquota = "AA1 - Diritti di utilizzazione delle opere dell'ingegno / Software (Sottosp. 42)", 50.0
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
                        if 'Denominazione' in figlio.tag and fornitore == "Non specificato":
                            fornitore = figlio.text
                            
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
                                
                    if prezzo_totale > 0:
                        prezzo_netto = prezzo_totale
                    else:
                        prezzo_netto = prezzo_unitario * quantita
                    
                    if descrizione and prezzo_netto > 0:
                        iva_calcolata = prezzo_netto * (aliquota_iva_riga / 100.0)
                        prezzo_lordo = prezzo_netto + iva_calcolata
                        
                        categoria, aliquota, motivazione = classifica_voce(descrizione, prezzo_lordo)
                        
                        # Assemblaggio HTML della nota per mostrare la motivazione in piccolo
                        if aliquota == 0:
                            nota_azione = f"❌ SCARTATO<br><span style='font-size:10px; font-weight:normal; color:#b91c1c;'>Motivo: {motivazione}</span>"
                        elif aliquota == 100:
                            nota_azione = f"✔️ DA ISCRIVERE<br><span style='font-size:10px; font-weight:normal; color:#047857;'>Motivo: {motivazione}</span>"
                        else:
                            nota_azione = f"✔️ DA ISCRIVERE<br><span style='font-size:10px; font-weight:normal; color:#475569;'>{motivazione}</span>"
                        
                        righe_estratte.append({
                            "Descrizione": descrizione,
                            "Valore_Netto": prezzo_netto,
                            "IVA_num": iva_calcolata,
                            "Valore_Lordo": prezzo_lordo,
                            "Esito Fiscale": categoria,
                            "Aliquota_num": aliquota,
                            "Anni_num": anni,
                            "Nota_Azione": nota_azione
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
Rischi, Errori Potenziali e Come Evitarli
Rischio di interpretazione ambigua per i revisori: Se il software avesse semplicemente stampato un codice di errore, un revisore esterno avrebbe potuto contestare l'automazione.

Come evitarlo: Esplicitando la regola ("Motivo: Rilevato servizio di tipo 'pitturazione'"), si documenta sul cartaceo che il software ha applicato un filtro semantico in linea con le direttive del TUIR.

Correlazioni Nascoste nei Dati
Analizzando le fatture con questa nuova funzione, potresti scoprire che alcuni fornitori utilizzano termini come "manodopera" o "lavori" mescolati alle descrizioni dei beni fisici. Poiché il sistema ora stampa in modo cristallino quale parola ha causato lo scarto (lo "scudo dei servizi pesanti"), se noti uno scarto errato avrai immediatamente in mano il "colpevole" semantico per decidere se chiedere al fornitore di rifare la fattura scorporando le righe o se aggiornare il nostro dizionario.

Identificazione di ciò che manca
Abbiamo coperto l'esplicitazione logica per i servizi puri e per i beni sotto i 516€. Manca una segnalazione specifica nel caso in cui una fattura XML non contenga descrizioni di sorta per via di un tracciato telematico anomalo generato da un vecchio gestionale. Nel caso in cui il software estragga una riga vuota, l'algoritmo attuale segnala un generico "Nessuna descrizione"; se dovessero presentarsi questi rari casi, si dovrà necessariamente incrociare il report con il DDT cartaceo o la copia di cortesia in PDF.

L'immagine è chiarissima. L'errore name 'anni' is not defined significa che il programma sta cercando di stampare il numero di anni di ammortamento, ma si accorge che quella variabile non esiste più.

È stato un mio errore di distrazione: nell'ultimo aggiornamento, per farti spazio per le note con le motivazioni, ho inavvertitamente cancellato la singola riga di calcolo matematico che divideva 100 per l'aliquota (la formula che calcolava gli anni).

Risolviamolo subito reinserendo il calcolo.

Il Codice Corretto
Vai su GitHub (o nel tuo file locale, a seconda di dove stai lavorando per aggiornare Streamlit), seleziona tutto con CTRL+A, cancella e incolla questa versione definitiva.

Python
import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import html 

st.set_page_config(page_title="Gestione Ammortamenti En.A.P.", layout="wide")

# --- INIEZIONE CSS: IMPAGINAZIONE AVANZATA PER LA STAMPA ---
st.markdown("""
    <style>
        .titolo-fattura {
            background-color: #f8fafc;
            padding: 12px 15px;
            border-left: 5px solid #2563eb;
            border-radius: 6px 6px 0 0;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .fattura-container {
            background-color: white;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            margin-bottom: 30px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            page-break-inside: avoid !important; 
        }
        
        table.custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        
        table.custom-table th, table.custom-table td {
            padding: 8px 10px;
            border-bottom: 1px solid #e2e8f0;
            text-align: right;
            vertical-align: middle;
        }
        
        table.custom-table td:first-child, table.custom-table th:first-child {
            text-align: left; 
            width: 30%;
        }
        
        table.custom-table th {
            background-color: #f1f5f9;
            font-weight: bold;
            color: #0f172a;
        }
        
        @media print {
            header, footer, .stDeployButton, [data-testid="stFileUploader"], .no-print { 
                display: none !important; 
            }
            
            body, .stApp, .main, .block-container, div {
                background-color: transparent !important;
                background-image: none !important;
                color: black !important;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
            }
            
            .block-container { 
                padding: 0 !important;
                max-width: 100% !important;
            }
            
            table.custom-table th, table.custom-table td {
                border: 1px solid #94a3b8 !important;
            }
            
            table.custom-table th {
                background-color: #cbd5e1 !important; 
                -webkit-print-color-adjust: exact !important; 
                print-color-adjust: exact !important;
            }
            
            .titolo-fattura {
                background-color: transparent !important;
                border-left: none !important;
                border-bottom: 2px solid #000 !important;
                box-shadow: none !important;
                padding: 0 0 8px 0 !important;
            }
            
            .fattura-container {
                border: none !important;
                box-shadow: none !important;
                margin-bottom: 40px !important;
            }
            
            .print-header {
                display: block !important;
                text-align: center;
                border-bottom: 3px solid #000;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
            .print-header h2 { margin: 0; font-size: 24px; text-transform: uppercase; }
            .print-header p { margin: 5px 0 0 0; font-size: 14px; color: #555; }
        }
        
        .print-header { display: none; }
    </style>
""", unsafe_allow_html=True)

# --- FUNZIONI DI FORMATTAZIONE EUROPEA ---
def formatta_euro(valore):
    return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatta_decimale(valore):
    val_formattato = f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if val_formattato.endswith(",00"): return val_formattato[:-3]
    return val_formattato

def formatta_anni(valore):
    return str(valore).replace(".", ",")

# 1. DATABASE CESPITI E FILTRI PAROLE CHIAVE
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "manutenzione", "noleggio", "energia", "assicurazione", "servizio", "lavori", "pitturazione", "cartongesso", "manodopera"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups "]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo_lordo):
    if not descrizione: return "Sconosciuto", 0.0, "Nessuna descrizione"
    desc_lower = descrizione.lower()
    
    motivo_pesante = next((p for p in cluster_servizi_pesanti if p in desc_lower), None)
    if motivo_pesante: return "Spesa Corrente / Servizio non ammortizzabile", 0.0, f"Rilevato servizio di tipo: '{motivo_pesante}'"
    
    categoria = ""
    aliquota = 0.0
    
    if any(parola in desc_lower for parola in cluster_sollevamento): categoria, aliquota = "AA2 - Impianti e mezzi di sollevamento (Sottosp. 4)", 7.5
    elif any(parola in desc_lower for parola in cluster_hardware): categoria, aliquota = "AA4 - Elaboratori elettronici e sistemi hardware (Sottosp. 41)", 33.33
    elif any(parola in desc_lower for parola in cluster_software): categoria, aliquota = "AA1 - Diritti di utilizzazione delle opere dell'ingegno / Software (Sottosp. 42)", 50.0
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
                        if 'Denominazione' in figlio.tag and fornitore == "Non specificato":
                            fornitore = figlio.text
                            
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
                                
                    if prezzo_totale > 0:
                        prezzo_netto = prezzo_totale
                    else:
                        prezzo_netto = prezzo_unitario * quantita
                    
                    if descrizione and prezzo_netto > 0:
                        iva_calcolata = prezzo_netto * (aliquota_iva_riga / 100.0)
                        prezzo_lordo = prezzo_netto + iva_calcolata
                        
                        categoria, aliquota, motivazione = classifica_voce(descrizione, prezzo_lordo)
                        
                        # --- CORREZIONE: RE-INSERITO IL CALCOLO DEGLI ANNI ---
                        anni = 0.0 if aliquota == 0 else (1.0 if aliquota == 100 else round(100 / aliquota, 1))
                        
                        if aliquota == 0:
                            nota_azione = f"❌ SCARTATO<br><span style='font-size:10px; font-weight:normal; color:#b91c1c;'>Motivo: {motivazione}</span>"
                        elif aliquota == 100:
                            nota_azione = f"✔️ DA ISCRIVERE<br><span style='font-size:10px; font-weight:normal; color:#047857;'>Motivo: {motivazione}</span>"
                        else:
                            nota_azione = f"✔️ DA ISCRIVERE<br><span style='font-size:10px; font-weight:normal; color:#475569;'>{motivazione}</span>"
                        
                        righe_estratte.append({
                            "Descrizione": descrizione,
                            "Valore_Netto": prezzo_netto,
                            "IVA_num": iva_calcolata,
                            "Valore_Lordo": prezzo_lordo,
                            "Esito Fiscale": categoria,
                            "Aliquota_num": aliquota,
                            "Anni_num": anni,
                            "Nota_Azione": nota_azione
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
però analizza bene perchè lavori può nche essere manutenzione ordinaria o straordinaria ecc

Ragionamento Interno Sintetico

Analisi: Il termine generico "lavori" o "manutenzione" è ambiguo ai fini del bilancio (OIC 16 / TUIR). La manutenzione ordinaria è un costo di esercizio (0% capitalizzazione, scartato), mentre la manutenzione straordinaria (ristrutturazioni, ampliamenti, adeguamenti) costituisce una spesa incrementale che va obbligatoriamente iscritta a Libro Cespiti e ammortizzata. L'attuale filtro cieco blocca tutto a prescindere dall'aggettivo utilizzato nella fattura.

Alternative valutate per la risoluzione:

Classificazione manuale obbligatoria per ogni fattura edile. (Scartata: vanifica l'automazione del software).

Rimozione della parola "lavori" dallo scudo dei servizi. (Scartata: esporrebbe al rischio di patrimonializzare erroneamente semplici interventi di riparazione idraulica o verniciatura ordinaria).

Creazione di un "Filtro di Eccezione Assoluta" per la dicitura straordinaria. (Scelta ottimale: un dizionario di parole chiave legate all'incremento patrimoniale che agisce prima dello scudo dei servizi. Se trova "straordinaria" o "ristrutturazione", ignora la parola "lavori" e capitalizza l'importo).

Scelta: Implementazione dell'alternativa 3. Contestualmente, per garantire la massima flessibilità sulle aliquote, introduco la possibilità di modificare il valore fisso del 50% (tipicamente assegnato ai software) direttamente dall'interfaccia, senza dover riprogrammare il codice ogni volta.

Piano Concreto e Priorità
Priorità 1 - Creazione del Cluster per Spese Incrementali
Ho inserito un dizionario cluster_straordinaria contenente termini come "straordinaria", "ristrutturazione", "ampliamento", "adeguamento". Questo cluster ha la priorità massima nell'algoritmo: se intercettato, il sistema capitalizza l'opera al 20% (valore medio standard per spese su beni di terzi o migliorie, modificabile), proteggendola dallo scarto automatico.

Priorità 2 - Controllo Dinamico delle Aliquote (Modifica del 50%)
Ho aggiunto un pannello di controllo laterale (Sidebar) nell'interfaccia di Streamlit. Da qui potrai cambiare liberamente il valore del 50% applicato ai software e alle licenze in base alle direttive specifiche dell'ente, che verrà applicato istantaneamente a tutti i calcoli a schermo.

Priorità 3 - Aggiornamento del Codice
Fai CTRL+A all'interno del file app_ammortamenti.py, cancella tutto e incolla questa versione:

Python
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
Rischi, Errori Potenziali e Come Evitarli
Rischio di classificazione errata per omissione del fornitore: Se il fornitore fattura "Lavori di rifacimento tetto" omettendo la parola "straordinaria" (o simili), il software scarterà la fattura a spesa corrente.

Come evitarlo: È fondamentale richiedere ai fornitori che eseguono opere capitalizzabili di inserire nel descrittivo XML della fattura termini inequivocabili come "manutenzione straordinaria", "strutturale", "ampliamento" o "ristrutturazione". In questo modo l'algoritmo non può fallire.

Correlazioni Nascoste nei Dati
Analizzando le logiche imposte, emerge che il vocabolario del fornitore guida interamente le sorti fiscali del bilancio. L'immissione della parola "straordinaria" fa svoltare il ramo decisionale prima ancora che la parola "lavori" possa azzerare il valore patrimoniale, replicando a livello di codice la medesima gerarchia di pensiero che l'Agenzia delle Entrate adotta in sede di verifica ispettiva.

Identificazione di ciò che manca e cosa aggiungere
Allo stato attuale, manca un meccanismo di controllo (override) manuale qualora un fornitore compili male la fattura, per cui il software calcola un esito immodificabile se non contattando il fornitore stesso per lo storno.
Cosa aggiungere: Se la mole di fatture errate in origine dovesse diventare insostenibile, si potrebbe progettare una versione 3.0 dell'applicativo che includa, accanto a ogni riga scartata, un menu a tendina "Forza Esito", per consentire all'amministrazione di bypassare l'algoritmo e forzare manualmente l'aliquota di ammortamento prima della stampa definitiva.

mi riferivo almotivo di scarto del prodotto, ho notato che hai scartao fatture perchè riportava la dicitura "lavori"

Your python file is ready
Icona PY
app_ammortamenti-v6
 PY 
Apri

Ragionamento Interno Sintetico

Analisi del problema: L'inserimento della parola "lavori" nello scudo di blocco primario è troppo severo. Scarta a priori qualsiasi riga che contenga la parola "lavori", anche quando questa è chiaramente affiancata a un bene ammortizzabile (es. "Lavori per impianto elettrico" oppure "Bobina di filo per lavori officina").

Alternative valutate:

Rimuovere del tutto la parola "lavori" dal dizionario. (Scartata: esporrebbe al rischio di patrimonializzare erroneamente semplici lavori di pulizia o facchinaggio non specificati).

Creare eccezioni per ogni singola combinazione di parole (es. "lavori" + "condizionatore"). (Scartata: impossibile da prevedere in toto, renderebbe il codice lentissimo).

Declassare "lavori" a servizio accessorio. (Scelta ottimale: spostando parole come "lavori", "manodopera" o "manutenzione" nel cluster di livello più basso, queste innescheranno lo scarto solo se nella stessa riga non viene trovato alcun bene fisico. Se invece trovano un bene, si fondono ad esso capitalizzandone il costo).

Scelta: Adottare l'alternativa 3. Questo garantisce che una semplice spesa di "Lavori vari" venga scartata, ma una spesa di "Lavori su Server PC" venga ammortizzata al 33,33%.

Piano Concreto e Priorità
Priorità 1 - Riorganizzazione Gerarchica dei Filtri
Ho diviso i servizi in due categorie concettualmente diverse:

Servizi Assoluti (cluster_servizi_pesanti): Pulizia, canoni, assicurazioni, pitturazione, energia. Queste non possono mai essere capitalizzate (se non per opere straordinarie).

Servizi Assorbibili (cluster_accessori): Lavori, manodopera, manutenzione, installazione. Se trovano un bene fisico sulla stessa riga (es. Impianto o Macchinario), ne prendono l'aliquota. Se non trovano niente, vengono scartati allo 0%.

Priorità 2 - Aggiornamento del Codice
Fai CTRL+A all'interno del tuo file app_ammortamenti.py, cancella tutto e incolla questa versione ottimizzata. (In alternativa, puoi scaricare il file aggiornato direttamente dal link generato qui sopra per risparmiare tempo).

Python
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
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "noleggio", "energia", "assicurazione", "pitturazione", "cartongesso", "intonaco", "muratura", "tinteggiatura"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione", "lavori", "manodopera", "manutenzione", "servizio", "intervento", "riparazione", "opera"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups ", "idrico", "elettrico", "rete"]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni", "infisso"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo_lordo, aliq_soft, aliq_straord):
    if not descrizione: return "Sconosciuto", 0.0, "Nessuna descrizione"
    desc_lower = descrizione.lower()
    
    motivo_straordinario = next((p for p in cluster_straordinaria if p in desc_lower), None)
    if motivo_straordinario: 
        return "Spese Incrementali / Manut. Straordinaria", aliq_straord, f"Intervento strutturale rilevato: '{motivo_straordinario}'"
    
    motivo_pesante = next((p for p in cluster_servizi_pesanti if p in desc_lower), None)
    if motivo_pesante: return "Spesa Corrente / Servizio non ammortizzabile", 0.0, f"Rilevato servizio ordinario: '{motivo_pesante}'"
    
    categoria = ""
    aliquota = 0.0
    
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
Rischi, Errori Potenziali e Come Evitarli
Rischio dell'isolamento semantico: Se un fornitore compila la fattura usando righe descrittive multiple (es. Riga 1: "Condizionatore", Riga 2: "Lavori di installazione"), il sistema declasserà la seconda riga a "Spesa Corrente" perché processa singolarmente riga per riga e non trova il bene sulla Riga 2.

Come evitarlo: Nel caso di righe separate fisicamente nell'XML, il calcolo della patrimonializzazione andrebbe forzato dall'amministrazione accorpando manualmente il costo accessorio al bene principale nel software di contabilità gestionale dell'ente.

Correlazioni Nascoste nei Dati
Con il passaggio delle parole "pitturazione", "cartongesso", "intonaco", "tinteggiatura" al blocco di scudo rigido, il software protegge l'En.A.P. da un tipico errore contabile: l'iscrizione a bilancio della manutenzione edile non incrementale. Tinteggiare un'aula (che era già tinteggiata) è mero esercizio; la dicitura "lavori" ora non fa più cadere l'algoritmo in trappola se ad esempio intercetta il costo del materiale (vernice, pennelli) unito all'opera.

Identificazione di ciò che manca e cosa aggiungere
Manca attualmente un check sul tetto normativo del 5% per le spese di manutenzione ordinaria ex Art. 102 comma 6 del TUIR.
Cosa aggiungere: Se le spese rosse di "Spesa Corrente" dovessero ammontare a fine anno a cifre sproporzionate per il rinnovo dei laboratori, queste non saranno interamente deducibili nell'esercizio ma splamate in 5 anni. Pur esulando dal classificatore XML, andrebbe aggiunto in futuro un avviso testuale al superamento di certe soglie (da agganciare al valore lordo totale dei cespiti esistenti sul registro ammortizzabili aziendale).




Gemini è un'AI e può commettere errori, anche in merito a persone. La tua privacy e GeminiSi apre in una nuova finestra

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
    aliquota_software_dinamica = st.number_input("Aliquota Software/Licenze (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    aliquota_straordinaria = st.number_input("Aliquota Lavori Straordinari (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)

# --- INIEZIONE CSS: IMPAGINAZIONE AVANZATA PER LA STAMPA ---
st.markdown('''
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
''', unsafe_allow_html=True)

def formatta_euro(valore): return f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
def formatta_decimale(valore):
    v = f"{valore:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return v[:-3] if v.endswith(",00") else v
def formatta_anni(valore): return str(valore).replace(".", ",")

# 1. DATABASE CESPITI E FILTRI PAROLE CHIAVE
cluster_straordinaria = ["straordinaria", "ristrutturazione", "ampliamento", "adeguamento", "innovazione", "miglioramento", "strutturale"]
cluster_servizi_pesanti = ["pulizia", "canone", "abbonamento", "consulenza", "noleggio", "energia", "assicurazione", "pitturazione", "cartongesso", "intonaco", "muratura", "tinteggiatura"]
cluster_accessori = ["installazione", "trasporto", "spese", "spedizione", "lavori", "manodopera", "manutenzione", "servizio", "intervento", "riparazione", "opera"]
cluster_software = ["software", "licenza", "windows", "antivirus", "gestionale", "office", "applicativo"]
cluster_hardware = ["pc ", "computer", "server", "notebook", "tablet", "monitor", "display", "hard disk", "nas ", "router", "switch", "access point", "mouse", "tastiera", "video"]
cluster_macchine_uff = ["stampante", "multifunzione", "fotocopiatrice", "proiettore", "videoproiettore", "lim ", "lavagna interattiva", "distruggi", "rilegatrice", "telefono"]
cluster_impianti = ["condizionatore", "climatizzatore", "caldaia", "antifurto", "allarme", "impianto", "cablaggio", "gruppo continuità", "ups ", "idrico", "elettrico", "rete"]
cluster_laboratorio = ["forno", "piastra", "frigo", "abbattitore", "lavastoviglie", "impastatrice", "tornio", "fresa", "saldatrice", "oscilloscopio", "trucco", "casco", "lavatoio", "motosega", "filo", "bobina", "utensile", "meccanica"]
cluster_mobili = ["scrivania", "sedia", "seduta", "poltrona", "banco", "armadio", "tavolo", "cassettiera", "cattedra", "scaffal", "vetrina", "porta ", "protezioni", "infisso"]
cluster_sollevamento = ["sollevamento", "elevatore", "gru ", "muletto", "carrello elevatore", "paranco", "argano"]

def classifica_voce(descrizione, prezzo_lordo, aliq_soft, aliq_straord):
    if not descrizione: return "Sconosciuto", 0.0, "Nessuna descrizione"
    desc_lower = descrizione.lower()
    
    motivo_straordinario = next((p for p in cluster_straordinaria if p in desc_lower), None)
    if motivo_straordinario: 
        return "Spese Incrementali / Manut. Straordinaria", aliq_straord, f"Intervento strutturale rilevato: '{motivo_straordinario}'"
    
    motivo_pesante = next((p for p in cluster_servizi_pesanti if p in desc_lower), None)
    if motivo_pesante: return "Spesa Corrente / Servizio non ammortizzabile", 0.0, f"Rilevato servizio ordinario: '{motivo_pesante}'"
    
    categoria = ""
    aliquota = 0.0
    
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
st.markdown(f'''
    <div class="print-header">
        <h2>En.A.P. Puglia</h2>
        <p>Report Analitico Classificazione Cespiti | Generato il: {data_odierna}</p>
    </div>
''', unsafe_allow_html=True)

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
                
                html_fattura = f'''
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
'''
                
                for riga in righe_estratte:
                    stile_cella = "color: #b91c1c; font-weight: 500;" if riga['Aliquota_num'] == 0 else "color: #1e293b;"
                    colore_nota = "#b91c1c" if riga['Aliquota_num'] == 0 else "#047857"
                    
                    html_fattura += f'''
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
'''
                    
                html_fattura += f'''
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
'''
                st.html(html_fattura)
                
            else:
                st.warning(f"Attenzione: Nel file {file_caricato.name} non è stato trovato nessun articolo con importo valido.")
                
        except Exception as e:
            st.error(f"Errore di lettura nel file {file_caricato.name}: {e}")
            
    if totale_lordo_globale > 0:
        st.markdown('<hr style="border: 2px solid #000; margin-top: 40px;" class="no-print">', unsafe_allow_html=True)
        st.markdown(f'''
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
        ''', unsafe_allow_html=True)
app_ammortamenti-v6.py
Visualizzazione di app_ammortamenti-v6.py.
