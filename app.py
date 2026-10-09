import streamlit as st
import datetime

# Configuração da página
st.set_page_config(page_title="Para a Isabela ❤️", page_icon="❤️", layout="centered")

# CSS personalizado para o tema romântico
st.markdown("""
    <style>
    .stApp { background-color: #fff0f3; }
    h1 { color: #c9184a; text-align: center; }
    .counter-box {
        background: white; padding: 15px; border-radius: 15px; text-align: center;
        color: #ff4d6d; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    .section-title { color: #800f2f; text-align: center; font-size: 1.2rem; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("UM PRESENTE PARA A ISABELA ❤️")

# Cálculo dos dias
data_inicio = datetime.date(2023, 1, 15)
dias_juntos = (datetime.date.today() - data_inicio).days

st.markdown(f"""
    <div class='counter-box'>
        <h2>🥰 Juntos há {dias_juntos} dias!</h2>
        <p style='color: #666; margin: 0;'>E cada segundo ao seu lado vale a pena.</p>
    </div>
""", unsafe_allow_html=True)

# Primeira Conversa
st.markdown("<div class='section-title'>📱 ONDE EU JÁ ESTAVA APAIXONADO POR VOCÊ</div>", unsafe_allow_html=True)
st.image("https://i.imgur.com/TRos5qS.jpeg", use_container_width=True)

st.divider()

# Abas interativas
tab1, tab2, tab3 = st.tabs(["🎵 Nossa Música", "📸 Nossas Fotos", "💌 O Nosso Momento"])

with tab1:
    st.subheader("🎵 Nossa Trilha Sonora")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

with tab2:
    st.subheader("📸 Nossas Memórias")
    fotos = [
        {"url": "https://i.imgur.com/5GyZcKH.jpeg", "legenda": "NOSSA PRIMEIRA FOTO MESMO PECANDO EM NAO TIRAR MUITAS KK TODAS QUE TEMOS JUNTOS SAO LINDAS!"},
        {"url": "https://i.imgur.com/ddswIGR.jpeg", "legenda": "NOSSA PRIMEIRA VIAGEM AINDA POR CIMA ACOMPANHADOS DA JUJU ❤️"},
        {"url": "https://i.imgur.com/eghAih2.jpeg", "legenda": "Foto da JUJU nosso carro alugado que nos acompanhou na viagem 🚗"},
        {"url": "https://i.imgur.com/Pw0LPcV.jpeg", "legenda": "NOSSO 'PRIMEIRO' SHOW DE MUITOS 🤘"},
        {"url": "https://i.imgur.com/RHE34zE.jpeg", "legenda": "NOSSO FUTURO ❤️"}
    ]
    
    for item in fotos:
        st.image(item["url"], use_container_width=True)
        st.caption(f"**{item['legenda']}**")
        st.write("---")

with tab3:
    st.subheader("💌 O Momento Mais Especial")
    st.write("""
    **NOSSO MOMENTO ONDE ESCOLHEMOS NOSSO 'BEM' MAIS PRECIOSO, ONDE EU JÁ ESTAVA DECIDIDO SOBRE O QUE QUERIA PARA MINHA VIDA...**

    **VOCÊ! PARA SEMPRE...**

    **VOCÊ.**
    """)
    st.error("### EU TE AMO MUITÃO ❤️")
