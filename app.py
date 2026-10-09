import streamlit as st
import datetime

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="UM PRESENTE PARA A ISABELA ❤️",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------------------------------------------------------
# ESTILIZAÇÃO CUSTOMIZADA (CSS) - Visual solicitado
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Fundo da aplicação */
    .stApp {
        background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 50%, #ffe5ec 100%) !important;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Forçar textos a ficarem com cor legível */
    p, span, div, label, h1, h2, h3, h4 {
        color: #4a0e17 !important;
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
        color: #800f2f !important;
        font-size: 2rem;
        margin: 0;
        font-weight: bold;
    }

    /* Moldura de Celular para o Print da Conversa */
    .phone-frame {
        border: 2px dashed #b7094c;
        border-radius: 25px;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.5);
        text-align: center;
        margin-bottom: 10px;
    }
    
    .phone-screen {
        border: 4px solid #a4133c;
        border-radius: 20px;
        background-color: #ffffff;
        padding: 10px;
        max-width: 340px;
        margin: 0 auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    .phone-header {
        font-size: 0.85rem;
        color: #666 !important;
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-bottom: 12px;
        font-weight: bold;
    }

    .section-title {
        color: #590d22 !important;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    .sub-caption {
        text-align: center;
        color: #800f2f !important;
        font-size: 0.9rem;
        font-weight: bold;
        margin-top: 10px;
    }
    
    .carta-box {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #ffb3c1;
        text-align: center;
        font-size: 1.1rem;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DADOS E CÁLCULO DE DIAS
# -----------------------------------------------------------------------------
DATA_INICIO = datetime.date(2023, 1, 15)
dias_juntos = (datetime.date.today() - DATA_INICIO).days

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
    st.caption("E cada segundo ao seu lado vale a pena 🥰")

# --- COLUNA DA DIREITA: Conteúdo dinâmico baseado no menu ---
with col_conteudo:
    
    # OPÇÃO 1: PRIMEIRA CONVERSA (Com a moldura no estilo celular)
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
            
            # Exibe o print da conversa foto1.jpeg
            try:
                st.image("foto1.jpeg", use_container_width=True)
            except Exception:
                st.error("Imagem `foto1.jpeg` não encontrada no GitHub.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<p class="sub-caption">ONDE EU JA ESTAVA APAIXONADO POR VOCE</p>', unsafe_allow_html=True)

    # OPÇÃO 2: MÚSICA
    elif opcao == "🎵 Uma Música":
        st.markdown('<div class="section-title">Nossa Trilha Sonora 🎵</div>', unsafe_allow_html=True)
        st.write("Dê o play para ouvir a nossa música especial enquanto navega:")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    # OPÇÃO 3: FOTOS
    elif opcao == "📸 Nossas Fotos":
        st.markdown('<div class="section-title">Nossos Melhores Momentos 📸</div>', unsafe_allow_html=True)
