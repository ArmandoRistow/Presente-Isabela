import streamlit as st
import datetime

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="UM PRESENTE PARA MEU MOZÃO ❤️",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------------------------------------------------------
# ESTILIZAÇÃO CUSTOMIZADA (CSS) - Réplica do visual da imagem
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Fundo da aplicação */
    .stApp {
        background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 50%, #ffe5ec 100%);
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Faixa de Cabeçalho Superior */
    .top-header {
        background-color: #f7cad0;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    .top-header h1 {
        color: #800f2f;
        font-size: 2rem;
        margin: 0;
        font-weight: bold;
    }

    /* Moldura de Celular para o Print da Conversa */
    .phone-frame {
        border: 2px dashed #b7094c;
        border-radius: 25px;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.4);
        text-align: center;
        margin-bottom: 10px;
    }
    
    .phone-screen {
        border: 4px solid #a4133c;
        border-radius: 30px;
        background-color: #ffffff;
        padding: 15px;
        max-width: 320px;
        margin: 0 auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    .phone-header {
        font-size: 0.8rem;
        color: #666;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-bottom: 12px;
    }

    .section-title {
        color: #590d22;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    .sub-caption {
        text-align: center;
        color: #800f2f;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DADOS PERSONALIZÁVEIS
# -----------------------------------------------------------------------------
# 1. Altere para a data em que vocês se conheceram/começaram a namorar (ANO, MÊS, DIA)
DATA_INICIO = datetime.date(2023, 1, 15)
dias_juntos = (datetime.date.today() - DATA_INICIO).days

# 2. Seu print da primeira conversa (Cole a URL do Imgur ou o caminho da imagem local)
URL_PRINT_CONVERSA = "https://i.imgur.com/SEU_PRINT_AQUI.jpg"  # Exemplo: "print_chat.png"

# 3. Lista de fotos para a galeria
FOTOS = [
    {"url": "https://picsum.photos/600/400?random=1", "legenda": "Nosso primeiro encontro ❤️"},
    {"url": "https://picsum.photos/600/400?random=2", "legenda": "Aquela viagem inesquecível ✈️"},
    {"url": "https://picsum.photos/600/400?random=3", "legenda": "Sempre juntos 🥰"}
]

# -----------------------------------------------------------------------------
# CABEÇALHO DO SITE
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="top-header">
        <h1>UM PRESENTE PARA MEU MOZÃO ❤️</h1>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LAYOUT EM COLUNAS: CARDÁPIO (ESQUERDA) E CONTEÚDO PRINCIPAL (DIREITA)
# -----------------------------------------------------------------------------
col_menu, col_conteudo = st.columns([1, 2.5], gap="large")

# --- COLUNA DA ESQUERDA: Cardápio de Momentos ---
with col_menu:
    st.subheader("📋 Cardápio de Momentos")
    
    opcao = st.radio(
        label="Navegue pelas opções:",
        options=[
            "💬 Primeira Conversa",
            "🎵 Uma Música", 
            "📸 Nossas Fotos",
            "💌 Minha Carta"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown(f"🗓️ **Juntos há {dias_juntos} dias!**")

# --- COLUNA DA DIREITA: Conteúdo dinâmico baseado no menu ---
with col_conteudo:
    
    # OPÇÃO 1: PRIMA CONVERSA (Com a moldura no estilo print/celular)
    if opcao == "💬 Primeira Conversa":
        st.markdown('<div class="section-title">AQUI ONDE TODO MEU AMOR COMEÇOU</div>', unsafe_allow_html=True)
        
        col_texto, col_celular = st.columns([1, 1.2])
        
        with col_texto:
            st.markdown("### 📱 Nossos Primeiros Passos")
            st.write(f"""
            Foi no dia **{DATA_INICIO.strftime('%d/%m/%Y')}** que demos o primeiro passo dessa jornada linda.
            
            Cada mensagem trocada, cada "oi" tímido e cada risada pelo celular já mostravam que isso se transformaria no maior amor da minha vida! ❤️
            """)
        
        with col_celular:
            st.markdown('<div class="phone-frame">', unsafe_allow_html=True)
            st.markdown("""
                <div class="phone-screen">
                    <div class="phone-header">💬 Chat com o Meu Mozão</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Exibe o print da conversa ou um placeholder se a URL não for alterada
            try:
                st.image(URL_PRINT_CONVERSA, use_container_width=True)
            except Exception:
                st.info("📌 Cole aqui o print da conversa substituindo a variável `URL_PRINT_CONVERSA` no código!")
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<p class="sub-caption">Sua foto do print aparecerá aqui.</p>', unsafe_allow_html=True)

    # OPÇÃO 2: MÚSICA
    elif opcao == "🎵 Uma Música":
        st.markdown('<div class="section-title">Nossa Trilha Sonora 🎵</div>', unsafe_allow_html=True)
        st.write("Dê o play para ouvir a nossa música especial enquanto navega:")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    # OPÇÃO 3: FOTOS
    elif opcao == "📸 Nossas Fotos":
        st.markdown('<div class="section-title">Nossos Melhores Momentos 📸</div>', unsafe_allow_html=True)
        
        for foto in FOTOS:
            st.image(foto["url"], caption=foto["legenda"], use_container_width=True)

    # OPÇÃO 4: CARTA
    elif opcao == "💌 Minha Carta":
        st.markdown('<div class="section-title">Minha Carta Para Você 💌</div>', unsafe_allow_html=True)
        st.write("""
        Meu amor,

        Escrevo isso para te lembrar o quanto você é especial na minha vida. Obrigado por cada gargalhada, por todo o carinho e por deixar meu mundo muito mais feliz.

        Te amo infinitamente! ❤️
        """)
