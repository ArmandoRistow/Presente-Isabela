import streamlit as st
import datetime

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA (ESTILO LOVEPANDA)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Armando & Isabela ❤️",
    page_icon="🐼",
    layout="centered"
)

# -----------------------------------------------------------------------------
# CSS CUSTOMIZADO (RECRIAÇÃO DO DESIGN DO LOVEPANDA)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Fundo suave em gradiente do LovePanda */
    .stApp {
        background: linear-gradient(180deg, #ffb5a7 0%, #fcd5ce 40%, #f8edeb 100%) !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }

    /* Ocultar elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Cores gerais de texto */
    p, span, div, label, h1, h2, h3, h4 {
        color: #6b705c !important;
    }

    /* Cartão Principal Flutuante */
    .main-card {
        background-color: rgba(255, 255, 255, 0.92);
        border-radius: 24px;
        padding: 30px 20px;
        box-shadow: 0 12px 30px rgba(157, 129, 137, 0.2);
        text-align: center;
        margin-bottom: 25px;
        border: 1px solid #fec5bb;
    }

    /* Título do Casal */
    .couple-title {
        font-family: 'Georgia', serif;
        color: #b7094c !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #f4acb7 !important;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Contador de Tempo em Destaque */
    .time-counter {
        background: #ffe5ec;
        border-radius: 16px;
        padding: 15px;
        margin: 20px 0;
        border: 1px dashed #ffb3c1;
    }
    .time-counter h3 {
        color: #c9184a !important;
        font-size: 1.5rem;
        margin: 0;
        font-weight: bold;
    }

    /* Titulo das Seções */
    .section-header {
        color: #a4133c !important;
        font-size: 1.4rem;
        font-weight: 700;
        text-align: center;
        margin: 30px 0 15px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Caixas de Texto da Carta */
    .letter-card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 25px;
        border-left: 5px solid #ff4d6d;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        font-size: 1.05rem;
        line-height: 1.8;
        text-align: center;
        margin-top: 15px;
    }

    /* Moldura de Foto */
    .photo-caption {
        text-align: center;
        font-weight: 600;
        color: #800f2f !important;
        margin-top: 8px;
        margin-bottom: 25px;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CÁLCULO DE DIAS JUNTOS
# -----------------------------------------------------------------------------
DATA_INICIO = datetime.date(2023, 1, 15)
dias_juntos = (datetime.date.today() - DATA_INICIO).days

# -----------------------------------------------------------------------------
# CARD PRINCIPAL DE ENTRADA (ESTILO LOVEPANDA)
# -----------------------------------------------------------------------------
st.markdown(f"""
    <div class="main-card">
        <div class="couple-title">Armando & Isabela 🐼❤️</div>
        <div class="subtitle">Um pedacinho da nossa história de amor</div>
        
        <div class="time-counter">
            <h3>🥰 Juntos há {dias_juntos} dias!</h3>
            <p style="margin: 5px 0 0 0; font-size: 0.9rem;">E cada segundo ao seu lado continua sendo inesquecível.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PLAYER DE MÚSICA FIXO EM DESTAQUE
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header">🎵 Nossa Trilha Sonora</div>', unsafe_allow_html=True)
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

st.divider()

# -----------------------------------------------------------------------------
# SEÇÃO 1: PRIMEIRA CONVERSA (FOTO1)
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header">💬 Onde Tudo Começou</div>', unsafe_allow_html=True)
try:
    st.image("foto1.jpeg", use_container_width=True)
    st.markdown('<div class="photo-caption">ONDE EU JA ESTAVA APAIXONADO POR VOCE</div>', unsafe_allow_html=
    
