import re
import google.generativeai as genai
import streamlit as st  # Importa Streamlit per l'interfaccia

# Configura la tua API key Gemini
GOOGLE_API_KEY = "AIzaSyAEyjnSEt4p8ov_1JcgfLfOknu9Vye5wDs"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


# Funzione per generare una risposta dal modello di Gemini
def analyze_scenarios(scenario1, scenario2):
    # Costruisci il messaggio da inviare al modello
    prompt = (
        "You are a decision-making expert, and your task is to help me compare two important scenarios to support me in making a choice. Analyze each scenario and provide me with a hypothetical vision of how my day or life might change if I were to pursue one of these options. Consider both short-term and long-term effects, emotional and practical aspects, and their impact on my well-being and personal fulfillment. Conclude by providing a summary of the main advantages and disadvantages of each choice."
        "Respond with a balanced analysis, based on plausible assumptions, that helps me clearly and realistically see the possible consequences of the decisions\n\n"
        f"Scenario 1: {scenario1}\nScenario 2: {scenario2}"
    )

    try:
        # Esegui una chiamata al modello di Gemini
        response = model.generate_content(prompt)
        # Restituisci il testo generato
        return response.text  # Adatta se il formato della risposta è diverso
    except Exception as e:
        # Gestione degli errori
        return f"Error occurred: {e}"


# Imposta la configurazione della pagina
st.set_page_config(page_title="What If?", page_icon="🌟", layout="wide")


# Imposta il colore di sfondo personalizzato con un gradiente viola
def add_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #8A2BE2; /* Colore di sfondo viola */
        }
        .stApp h1 {
            color: white; /* Colore del testo del titolo */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


add_custom_css()


def extract_scenarios(text):
    # Estrai il testo fino a "Summary of Advantages and Disadvantages"
    summary_position = re.search(r"Summary of Advantages and Disadvantages", text)
    if summary_position:
        text = text[:summary_position.start()].strip()  # Truncate the text at the summary section

    # Estrai il primo scenario
    scenario1_text = re.search(r'Scenario 1:(.*?)(Scenario 2:|$)', text, re.DOTALL)
    # Estrai il secondo scenario
    scenario2_text = re.search(r'Scenario 2:(.*)', text, re.DOTALL)

    # Restituisci i due scenari separati
    return (scenario1_text.group(1).strip() if scenario1_text else "",
            scenario2_text.group(1).strip() if scenario2_text else "")


# Layout a colonne per affiancare il logo e il titolo
col1, col2 = st.columns([0.2, 4])  # Puoi regolare i numeri per la larghezza

with col1:
    st.image("logo.png", width=100)  # Sostituisci "logo.png" con il nome del tuo logo o il percorso completo del file

with col2:
    st.title("What if...")

# Layout a colonne per gli input
col1, col2, col3 = st.columns([1, 0.2, 1])

with col1:
    scenario1 = st.text_area("Case 1: Describe the first option", height=100)

with col2:
    st.markdown("<h3 style='text-align: center;'>OR</h3>", unsafe_allow_html=True)

with col3:
    scenario2 = st.text_area("Case 2: Describe the second option", height=100)

# Layout a colonne per il bottone di invio
col1, col2, col3 = st.columns([2, 1, 2])

if st.button("Send"):
    if scenario1.strip() and scenario2.strip():
        with st.spinner("Analyzing options..."):
            result = analyze_scenarios(scenario1, scenario2)

        # Estrazione dei due scenari
        scenario1_text, scenario2_text = extract_scenarios(result)

        # Layout a colonne per visualizzare i due scenari affiancati
        col1, col2 = st.columns(2)

        # Visualizza il primo scenario nella prima colonna
        with col1:
            st.subheader("Scenario 1:")
            st.write(scenario1_text)

        # Visualizza il secondo scenario nella seconda colonna
        with col2:
            st.markdown("<div style='border-left: 2px solid #000; height: 100%;'></div>",
                        unsafe_allow_html=True)  # Linea verticale
            st.subheader("Scenario 2:")
            st.write(scenario2_text)

    else:
        st.warning("Write both the cases!")
