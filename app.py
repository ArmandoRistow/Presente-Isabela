import streamlit as st
import datetime

# Configuração da página
st.set_page_config(page_title="Para a Isabela ❤️", page_icon="❤️", layout="centered")

# Título Principal
st.title("UM PRESENTE PARA A ISABELA ❤️")

# Cálculo dos dias de namoro
data_inicio = datetime.date(2023, 1, 15)
dias_juntos = (datetime.date.today() - data_inicio).days

# Caixa do Contador de Dias
st.info(f"🥰 **Juntos há {dias_juntos} dias!** \n\nE cada segundo ao seu lado vale a pena.")

st.write("---")

# Primeira Conversa
st.subheader("📱 ONDE EU JÁ ESTAVA APAIXONADO POR VOCÊ")
st.image("foto1.jpeg", use_container_width=True)

st.write("---")

# Abas do Menu
tab1, tab2, tab3 = st.tabs(["🎵 Nossa Música", "📸 Nossas Fotos", "💌 O Nosso Momento"])

with tab1:
    st.subheader("🎵 Nossa Trilha Sonora")
    st.write("Esta música sempre me faz lembrar do quanto amo você...")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

with tab2:
    st.subheader("📸 Nossas Memórias")
    
    galeria = [
        {
            "arquivo": "foto2.jpeg", 
            "legenda": "NOSSA PRIMEIRA FOTO MESMO PECANDO EM NAO TIRAR MUITAS KK TODAS QUE TEMOS JUNTOS SAO LINDAS!"
        },
        {
            "arquivo": "foto3.jpeg", 
            "legenda": "NOSSO 'PRIMEIRO' SHOW DE MUITOS 🤘"
        },
        {
            "arquivo": "foto4.jpeg", 
            "legenda": "NOSSA PRIMEIRA VIAGEM AINDA POR CIMA ACOMPANHADOS DA JUJU ❤️"
        },
        {
            "arquivo": "foto5.jpeg", 
            "legenda": "A vista incrível da praia que marcou a nossa viagem ❤️"
        },
        {
            "arquivo": "foto7.jpeg", 
            "legenda": "NOSSO FUTURO ❤️"
        }
    ]
    
    for item in galeria:
        st.image(item["arquivo"], use_container_width=True)
        st.caption(f"**{item['legenda']}**")
        st.write("---")

with tab3:
    st.subheader("💌 O Nosso Momento Especial")
    
    # Foto das Alianças (foto6.jpeg)
    st.image("foto6.jpeg", use_container_width=True)
    
    st.markdown("""
    **NOSSO MOMENTO ONDE ESCOLHEMOS NOSSO 'BEM' MAIS PRECIOSO, ONDE EU JÁ ESTAVA DECIDIDO SOBRE O QUE QUERIA PARA MINHA VIDA...**

    **VOCÊ! PARA SEMPRE...**

    **VOCÊ.**
    """)
    st.error("### EU TE AMO MUITÃO ❤️")
