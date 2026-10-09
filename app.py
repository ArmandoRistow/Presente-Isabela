<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Um Presente Especial ❤️</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 50%, #ffb3c1 100%);
      min-height: 100vh;
      overflow-x: hidden;
    }

    .font-cursive {
      font-family: 'Dancing Script', cursive;
    }

    /* Floating Hearts Background */
    .heart-particle {
      position: fixed;
      color: rgba(230, 57, 70, 0.4);
      animation: floatUp linear infinite;
      pointer-events: none;
      z-index: 0;
    }

    @keyframes floatUp {
      0% {
        transform: translateY(100vh) scale(0.5) rotate(0deg);
        opacity: 1;
      }
      100% {
        transform: translateY(-10vh) scale(1.2) rotate(360deg);
        opacity: 0;
      }
    }

    /* Glassmorphism Cards */
    .glass-card {
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0 10px 30px rgba(230, 57, 70, 0.15);
    }

    .glass-menu-item {
      background: rgba(255, 255, 255, 0.9);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .glass-menu-item:hover {
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 12px 20px rgba(229, 56, 84, 0.25);
    }

    /* Smooth Fade Transitions */
    .screen-fade {
      transition: opacity 0.6s ease-in-out, transform 0.6s ease-in-out;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #fff0f3;
    }
    ::-webkit-scrollbar-thumb {
      background: #ff758f;
      border-radius: 4px;
    }

    /* Pulsing Glow Effect */
    .pulse-glow {
      animation: pulseGlow 2s infinite alternate;
    }

    @keyframes pulseGlow {
      0% {
        box-shadow: 0 0 15px rgba(230, 57, 70, 0.4);
      }
      100% {
        box-shadow: 0 0 30px rgba(230, 57, 70, 0.8), 0 0 10px rgba(255, 182, 193, 0.6);
      }
    }
  </style>
</head>
<body class="relative text-gray-800">

  <div id="hearts-container" class="fixed inset-0 pointer-events-none z-0"></div>

  <!-- Top Audio Control Widget -->
  <div id="audio-widget" class="fixed top-4 right-4 z-50 transition-all duration-500 opacity-0 transform translate-y-[-20px]">
    <div class="glass-card flex items-center gap-3 px-4 py-2.5 rounded-full border border-pink-200 shadow-lg">
      <button id="play-pause-btn" onclick="toggleAudio()" class="w-10 h-10 bg-rose-500 hover:bg-rose-600 text-white rounded-full flex items-center justify-center transition shadow-md">
        <i id="play-icon" class="fa-solid fa-play text-sm"></i>
      </button>
      <div class="text-xs">
        <p id="song-title" class="font-semibold text-rose-700 truncate max-w-[120px] sm:max-w-[160px]">Nossa Música ❤️</p>
        <p id="song-artist" class="text-gray-500 text-[10px]">Trilha Sonora do Amor</p>
      </div>
      <i class="fa-solid fa-music text-rose-400 text-sm animate-bounce ml-1"></i>
    </div>
  </div>

  <!-- Audio Element (Troque o link do áudio para a sua música preferida) -->
  <audio id="bg-music" loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
  </audio>

  <!-- 1. TELA INICIAL (LANDING PAGE) -->
  <section id="welcome-screen" class="min-h-screen flex flex-col items-center justify-center p-6 text-center relative z-10 screen-fade">
    <div class="glass-card max-w-lg w-full p-8 md:p-12 rounded-3xl border-2 border-pink-200 shadow-2xl relative overflow-hidden">
      <div class="absolute -top-10 -right-10 w-32 h-32 bg-pink-300 rounded-full blur-2xl opacity-50"></div>
      <div class="absolute -bottom-10 -left-10 w-32 h-32 bg-rose-400 rounded-full blur-2xl opacity-40"></div>

      <div class="relative z-10">
        <div class="inline-block p-4 bg-rose-100 rounded-full mb-6 text-rose-500 animate-pulse">
          <i class="fa-solid fa-gift text-4xl"></i>
        </div>
        <h1 class="font-cursive text-5xl sm:text-6xl text-rose-600 font-bold mb-4 drop-shadow-sm">
          Um Presente Para o Meu Mozão ❤️
        </h1>
        <p class="text-gray-600 text-sm sm:text-base mb-8 leading-relaxed">
          Preparei este cantinho especial com todo carinho do mundo para celebrar o nosso amor e guardar nossas melhores memórias!
        </p>

        <button onclick="openGift()" class="pulse-glow bg-gradient-to-r from-rose-500 to-pink-500 hover:from-rose-600 hover:to-pink-600 text-white font-bold py-4 px-8 rounded-full text-lg shadow-xl transform hover:scale-105 transition-all duration-300 flex items-center justify-center gap-3 mx-auto">
          <span>Clique para Abrir ❤️</span>
          <i class="fa-solid fa-sparkles"></i>
        </button>
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT CONTAINER (Oculto Inicialmente) -->
  <main id="main-content" class="hidden min-h-screen pb-16 pt-6 px-4 max-w-4xl mx-auto relative z-10 opacity-0 transition-opacity duration-700">

    <!-- Header com Banner -->
    <header class="text-center mb-10">
      <h2 class="font-cursive text-4xl sm:text-5xl text-rose-600 font-bold mb-2">Cardápio de Momentos 📜</h2>
      <p class="text-rose-400 text-sm sm:text-base">Uma degustação especial de tudo o que vivemos juntos</p>
    </header>

    <!-- CONTADOR DE TEMPO JUNTOS -->
    <section class="glass-card rounded-2xl p-6 mb-10 text-center border border-pink-200">
      <h3 class="text-rose-600 text-lg font-semibold mb-3 flex items-center justify-center gap-2">
        <i class="fa-solid fa-clock"></i> Juntos Para Sempre
      </h3>
      
      <!-- GRID DO CONTADOR -->
      <div id="counter-grid" class="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-lg mx-auto">
        <div class="bg-rose-50/80 p-3 rounded-xl border border-rose-100">
          <span id="counter-days" class="block font-bold text-2xl sm:text-3xl text-rose-600">0</span>
          <span class="text-xs text-gray-500 font-medium">Dias</span>
        </div>
        <div class="bg-rose-50/80 p-3 rounded-xl border border-rose-100">
          <span id="counter-hours" class="block font-bold text-2xl sm:text-3xl text-rose-600">0</span>
          <span class="text-xs text-gray-500 font-medium">Horas</span>
        </div>
        <div class="bg-rose-50/80 p-3 rounded-xl border border-rose-100">
          <span id="counter-minutes" class="block font-bold text-2xl sm:text-3xl text-rose-600">0</span>
          <span class="text-xs text-gray-500 font-medium">Minutos</span>
        </div>
        <div class="bg-rose-50/80 p-3 rounded-xl border border-rose-100">
          <span id="counter-seconds" class="block font-bold text-2xl sm:text-3xl text-rose-600">0</span>
          <span class="text-xs text-gray-500 font-medium">Segundos</span>
        </div>
      </div>
      <p id="start-date-text" class="text-xs text-rose-400 mt-3 font-medium">Desde o dia em que nossa história começou! ❤️</p>
    </section>

    <!-- MENU TIPO CARDÁPIO ROMÂNTICO -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">

      <!-- ENTRADA -->
      <div onclick="scrollToSection('secao-entrada')" class="glass-menu-item p-6 rounded-2xl border border-pink-200 cursor-pointer relative overflow-hidden group">
        <div class="flex items-start justify-between">
          <div>
            <span class="inline-block bg-rose-100 text-rose-600 text-xs px-3 py-1 rounded-full font-bold uppercase tracking-wider mb-2">Entrada</span>
            <h4 class="text-xl font-bold text-gray-800 group-hover:text-rose-600 transition">Primeiras Memórias 🥂</h4>
            <p class="text-sm text-gray-500 mt-1">Onde tudo começou e nossos primeiros passos juntos.</p>
          </div>
          <span class="text-3xl">✨</span>
        </div>
      </div>

      <!-- PRATO PRINCIPAL -->
      <div onclick="scrollToSection('secao-prato-principal')" class="glass-menu-item p-6 rounded-2xl border border-pink-200 cursor-pointer relative overflow-hidden group">
        <div class="flex items-start justify-between">
          <div>
            <span class="inline-block bg-rose-100 text-rose-600 text-xs px-3 py-1 rounded-full font-bold uppercase tracking-wider mb-2">Prato Principal</span>
            <h4 class="text-xl font-bold text-gray-800 group-hover:text-rose-600 transition">Galeria & Viagens 📸</h4>
            <p class="text-sm text-gray-500 mt-1">Os melhores cliques, passeios e sorrisos compartilhados.</p>
          </div>
          <span class="text-3xl">🌹</span>
        </div>
      </div>

      <!-- SOBREMESA -->
      <div onclick="scrollToSection('secao-sobremesa')" class="glass-menu-item p-6 rounded-2xl border border-pink-200 cursor-pointer relative overflow-hidden group">
        <div class="flex items-start justify-between">
          <div>
            <span class="inline-block bg-rose-100 text-rose-600 text-xs px-3 py-1 rounded-full font-bold uppercase tracking-wider mb-2">Sobremesa</span>
            <h4 class="text-xl font-bold text-gray-800 group-hover:text-rose-600 transition">Razões Te Amo 🍓</h4>
            <p class="text-sm text-gray-500 mt-1">Pequenos detalhes cotidianos que me fazem te amar tanto.</p>
          </div>
          <span class="text-3xl">🍰</span>
        </div>
      </div>

      <!-- CARTA ESPECIAL -->
      <div onclick="scrollToSection('secao-carta')" class="glass-menu-item p-6 rounded-2xl border border-pink-200 cursor-pointer relative overflow-hidden group">
        <div class="flex items-start justify-between">
          <div>
            <span class="inline-block bg-rose-100 text-rose-600 text-xs px-3 py-1 rounded-full font-bold uppercase tracking-wider mb-2">Carta Especial</span>
            <h4 class="text-xl font-bold text-gray-800 group-hover:text-rose-600 transition">Mensagem do Coração 💌</h4>
            <p class="text-sm text-gray-500 mt-1">Uma declaração sincera escrita especialmente para você.</p>
          </div>
          <span class="text-3xl">🎁</span>
        </div>
      </div>

    </div>

    <!-- DETALHES DO CARDÁPIO (SEÇÕES COMPLETA DE CONTEÚDO) -->

    <!-- SEÇÃO 1: ENTRADA -->
    <section id="secao-entrada" class="glass-card rounded-3xl p-6 sm:p-8 mb-10 border border-pink-200">
      <div class="flex items-center gap-3 mb-6 border-b border-pink-100 pb-4">
        <span class="text-3xl">🥂</span>
        <div>
          <h3 class="font-cursive text-3xl text-rose-600 font-bold">Entrada: Primeiras Memórias</h3>
          <p class="text-xs text-gray-500">Nossos primeiros momentos e a mágica do início</p>
        </div>
      </div>

      <div class="space-y-4">
        <div class="bg-white/70 p-4 rounded-xl border border-pink-100 flex gap-4 items-center">
          <div class="w-12 h-12 bg-rose-100 text-rose-500 rounded-full flex items-center justify-center shrink-0 text-xl">
            <i class="fa-solid fa-comments"></i>
          </div>
          <div>
            <h5 class="font-bold text-gray-800">A Primeira Conversa</h5>
            <p class="text-sm text-gray-600">Aquele frio na barriga quando começamos a conversar e percebi o quanto você era incrível!</p>
          </div>
        </div>

        <div class="bg-white/70 p-4 rounded-xl border border-pink-100 flex gap-4 items-center">
          <div class="w-12 h-12 bg-rose-100 text-rose-500 rounded-full flex items-center justify-center shrink-0 text-xl">
            <i class="fa-solid fa-heart"></i>
          </div>
          <div>
            <h5 class="font-bold text-gray-800">O Primeiro Encontro</h5>
            <p class="text-sm text-gray-600">O momento em que te vi pessoalmente e tive a certeza de que ali começava algo lindo.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 2: PRATO PRINCIPAL (GALERIA DE FOTOS) -->
    <section id="secao-prato-principal" class="glass-card rounded-3xl p-6 sm:p-8 mb-10 border border-pink-200">
      <div class="flex items-center gap-3 mb-6 border-b border-pink-100 pb-4">
        <span class="text-3xl">📸</span>
        <div>
          <h3 class="font-cursive text-3xl text-rose-600 font-bold">Prato Principal: Nossas Fotos</h3>
          <p class="text-xs text-gray-500">Mural de fotos dos nossos momentos inesquecíveis</p>
        </div>
      </div>

      <!-- CARROSSEL / GRADE DE FOTOS -->
      <!-- DICA: Altere as URLs e legendas no array JavaScript "FOTOS_LISTA" para usar suas próprias fotos! -->
      <div id="gallery-container" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <!-- As fotos serão injetadas dinamicamente via JS -->
      </div>
    </section>

    <!-- SEÇÃO 3: SOBREMESA (MOTIVOS) -->
    <section id="secao-sobremesa" class="glass-card rounded-3xl p-6 sm:p-8 mb-10 border border-pink-200">
      <div class="flex items-center gap-3 mb-6 border-b border-pink-100 pb-4">
        <span class="text-3xl">🍓</span>
        <div>
          <h3 class="font-cursive text-3xl text-rose-600 font-bold">Sobremesa: Razões Pelas Quais Te Amo</h3>
          <p class="text-xs text-gray-500">Alguns dos infinitos motivos que me fazem apaixonar todos os dias</p>
        </div>
      </div>

      <ul id="reasons-list" class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <!-- Injetado dinamicamente -->
      </ul>
    </section>

    <!-- SEÇÃO 4: CARTA ESPECIAL -->
    <section id="secao-carta" class="glass-card rounded-3xl p-6 sm:p-10 mb-10 border border-pink-200 relative overflow-hidden">
      <div class="absolute top-0 right-0 p-6 text-pink-200 opacity-30 text-8xl pointer-events-none">
        <i class="fa-solid fa-envelope-open-text"></i>
      </div>

      <div class="flex items-center gap-3 mb-6 border-b border-pink-100 pb-4">
        <span class="text-3xl">💌</span>
        <div>
          <h3 class="font-cursive text-3xl text-rose-600 font-bold">Carta Aberta do Meu Coração</h3>
          <p class="text-xs text-gray-500">Palavras sinceras de quem te ama incondicionalmente</p>
        </div>
      </div>

      <!-- TEXTO DA CARTA (Edite aqui se desejar!) -->
      <div id="carta-conteudo" class="prose max-w-none text-gray-700 leading-relaxed text-sm sm:text-base space-y-4 bg-white/60 p-6 rounded-2xl border border-pink-100">
        <p>Meu amor,</p>
        <p>
          Escrevo esta mensagem para te lembrar o quanto você transforma meus dias em algo mais leve, doce e especial. Estar ao seu lado é viver em um constante porto seguro de paz e alegria.
        </p>
        <p>
          Agradeço por cada gargalhada, por cada abraço aconchegante nos dias difíceis e por me apoiar em cada sonho. Você não é apenas minha namorada, é minha melhor amiga e meu grande amor.
        </p>
        <p>
          Prometo continuar cuidando do nosso amor todos os dias com carinho, admiração e muito respeito. Te amo daqui até o infinito!
        </p>
        <p class="font-cursive text-2xl text-rose-600 text-right mt-6">Com todo o meu amor, para sempre. ❤️</p>
      </div>
    </section>

    <!-- FOOTER ROMÂNTICO -->
    <footer class="text-center py-6 text-xs text-rose-500">
      Feito com amor ❤️ especialmente para você!
    </footer>

  </main>

  <!-- MODAL DE VISUALIZAÇÃO DA FOTO (ZOOM) -->
  <div id="photo-modal" class="fixed inset-0 bg-black/80 z-50 hidden items-center justify-center p-4 backdrop-blur-sm" onclick="closePhotoModal()">
    <div class="max-w-3xl w-full bg-white rounded-2xl overflow-hidden shadow-2xl relative" onclick="event.stopPropagation()">
      <button onclick="closePhotoModal()" class="absolute top-3 right-3 bg-rose-500 text-white w-9 h-9 rounded-full flex items-center justify-center z-10 hover:bg-rose-600">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <img id="modal-img" src="" alt="Foto expandida" class="w-full max-h-[75vh] object-contain bg-black">
      <div class="p-4 bg-white text-center">
        <p id="modal-caption" class="text-sm font-semibold text-rose-600"></p>
      </div>
    </div>
  </div>

  <script>
    /* ====================================================================
       CONFIGURAÇÕES DO USUÁRIO (Facilmente personalizável aqui)
       ==================================================================== */
    
    // 1. DATA DE INÍCIO DO NAMORO / RELACIONAMENTO (Ano, Mês - 1, Dia, Hora, Minuto)
    // Nota: Mês começa do 0 (Janeiro = 0, Fevereiro = 1, Março = 2, etc)
    const DATA_INICIO_NAMORO = new Date(2023, 0, 15, 18, 0, 0); // Exemplo: 15 de Janeiro de 2023 às 18:00

    // 2. LISTA DE FOTOS PARA A GALERIA
    // Dica: Substitua pelas URLs reais das fotos do casal ou caminhos como "foto1.jpg"
    const FOTOS_LISTA = [
      {
        url: "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&w=600&q=80",
        legenda: "Aquele nosso momento inesquecível! ❤️"
      },
      {
        url: "https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=600&q=80",
        legenda: "Nosso passeio perfeito num dia especial ✨"
      },
      {
        url: "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?auto=format&fit=crop&w=600&q=80",
        legenda: "Sorrisos que amo ver todos os dias 😊"
      },
      {
        url: "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=600&q=80",
        legenda: "Sempre juntos em qualquer aventura 🚗"
      },
      {
        url: "https://images.unsplash.com/photo-1494774157365-9e04c6720e47?auto=format&fit=crop&w=600&q=80",
        legenda: "O abraço onde encontro minha paz 🌹"
      },
      {
        url: "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80",
        legenda: "Mais uma página da nossa história 🥂"
      }
    ];

    // 3. MOTIVOS PELOS QUAIS TE AMO
    const MOTIVOS_LISTA = [
      "Seu sorriso iluminado que transforma meu dia.",
      "O carinho e paciência que você tem comigo.",
      "Sua risada contagiante que é minha música favorita.",
      "Como você se preocupa e cuida dos mínimos detalhes.",
      "Nossos planos de futuro e os sonhos compartilhados.",
      "O conforto inigualável do seu abraço no fim do dia."
    ];

    /* ====================================================================
       LÓGICA E INTERATIVIDADE DO SITE
       ==================================================================== */

    let isPlaying = false;
    const audio = document.getElementById('bg-music');
    const playIcon = document.getElementById('play-icon');

    // Inicialização ao carregar
    window.onload = function() {
      createFloatingHearts();
      initGallery();
      initReasons();
      startRelationshipCounter();
    };

    // Efeito de partículas de corações
    function createFloatingHearts() {
      const container = document.getElementById('hearts-container');
      const heartIcons = ['❤️', '💖', '💕', '💗', '🌹'];
      
      setInterval(() => {
        const heart = document.createElement('div');
        heart.className = 'heart-particle';
        heart.innerText = heartIcons[Math.floor(Math.random() * heartIcons.length)];
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = (Math.random() * 4 + 4) + 's';
        heart.style.fontSize = (Math.random() * 12 + 16) + 'px';
        container.appendChild(heart);

        setTimeout(() => {
          heart.remove();
        }, 8000);
      }, 500);
    }

    // Ação do Botão "Clique para Abrir ❤️"
    function openGift() {
      // Efeito de Confetes
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#e63946', '#ffb3c1', '#ff758f']
      });

      // Transição Suave
      const welcomeScreen = document.getElementById('welcome-screen');
      const mainContent = document.getElementById('main-content');
      const audioWidget = document.getElementById('audio-widget');

      welcomeScreen.style.opacity = '0';
      welcomeScreen.style.transform = 'scale(0.95)';

      setTimeout(() => {
        welcomeScreen.classList.add('hidden');
        mainContent.classList.remove('hidden');
        
        // Exibir widget de áudio
        audioWidget.classList.remove('opacity-0', 'translate-y-[-20px]');
        
        // Tentar áudio automático
        toggleAudio();

        setTimeout(() => {
          mainContent.classList.remove('opacity-0');
        }, 50);
      }, 600);
    }

    // Controle do Player de Áudio
    function toggleAudio() {
      if (isPlaying) {
        audio.pause();
        playIcon.className = 'fa-solid fa-play text-sm';
      } else {
        audio.play().then(() => {
          playIcon.className = 'fa-solid fa-pause text-sm';
        }).catch(err => {
          console.log("Autoplay bloqueado pelo navegador, aguardando clique do usuário.");
        });
      }
      isPlaying = !isPlaying;
    }

    // Contador de Tempo de Relacionamento
    function startRelationshipCounter() {
      function updateCounter() {
        const now = new Date();
        const diff = now - DATA_INICIO_NAMORO;

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        document.getElementById('counter-days').innerText = days;
        document.getElementById('counter-hours').innerText = hours;
        document.getElementById('counter-minutes').innerText = minutes;
        document.getElementById('counter-seconds').innerText = seconds;
      }

      updateCounter();
      setInterval(updateCounter, 1000);
    }

    // Renderizar Galeria de Fotos
    function initGallery() {
      const container = document.getElementById('gallery-container');
      container.innerHTML = '';

      FOTOS_LISTA.forEach((foto, index) => {
        const card = document.createElement('div');
        card.className = 'bg-white rounded-2xl overflow-hidden shadow-md border border-pink-100 hover:shadow-xl transition transform hover:-translate-y-1 cursor-pointer';
        card.onclick = () => openPhotoModal(foto.url, foto.legenda);

        card.innerHTML = `
          <div class="h-48 overflow-hidden relative">
            <img src="${foto.url}" alt="${foto.legenda}" class="w-full h-full object-cover transition duration-500 hover:scale-110">
            <div class="absolute top-2 right-2 bg-white/80 backdrop-blur-xs px-2 py-1 rounded-full text-xs text-rose-500">
              <i class="fa-solid fa-heart"></i>
            </div>
          </div>
          <div class="p-3 text-center">
            <p class="text-xs text-gray-600 font-medium truncate">${foto.legenda}</p>
          </div>
        `;
        container.appendChild(card);
      });
    }

    // Renderizar Lista de Motivos
    function initReasons() {
      const container = document.getElementById('reasons-list');
      container.innerHTML = '';

      MOTIVOS_LISTA.forEach((motivo, index) => {
        const li = document.createElement('li');
        li.className = 'bg-white/70 p-3.5 rounded-xl border border-pink-100 flex items-start gap-3 text-sm text-gray-700';
        li.innerHTML = `
          <span class="text-rose-500 font-bold shrink-0">#${index + 1}</span>
          <span>${motivo}</span>
        `;
        container.appendChild(li);
      });
    }

    // Rolar Suavemente para Seção
    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    // Zoom da Foto
    function openPhotoModal(url, legenda) {
      document.getElementById('modal-img').src = url;
      document.getElementById('modal-caption').innerText = legenda;
      const modal = document.getElementById('photo-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }

    function closePhotoModal() {
      const modal = document.getElementById('photo-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  </script>
</body>
</html>
