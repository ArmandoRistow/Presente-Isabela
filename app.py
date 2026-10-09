<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Para o Meu Amor ❤️</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
      background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #333;
      padding: 20px;
    }

    .container {
      background: rgba(255, 255, 255, 0.9);
      padding: 30px;
      border-radius: 20px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
      max-width: 500px;
      width: 100%;
      text-align: center;
    }

    h1 {
      color: #e63946;
      margin-bottom: 10px;
    }

    p.subtitle {
      color: #666;
      margin-bottom: 25px;
      font-size: 0.95rem;
    }

    /* Menu de Abas */
    .menu {
      display: flex;
      justify-content: space-around;
      margin-bottom: 20px;
      border-bottom: 2px solid #ffe5ec;
    }

    .tab-btn {
      background: none;
      border: none;
      padding: 10px 15px;
      font-size: 1rem;
      font-weight: bold;
      color: #888;
      cursor: pointer;
      transition: 0.3s;
    }

    .tab-btn.active {
      color: #e63946;
      border-bottom: 3px solid #e63946;
    }

    /* Conteúdo das Abas */
    .tab-content {
      display: none;
      animation: fadeIn 0.5s ease;
    }

    .tab-content.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Galeria de Fotos */
    .photo-frame {
      width: 100%;
      height: 280px;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
      margin-bottom: 15px;
    }

    .photo-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* Botão de Música */
    .music-btn {
      background: #e63946;
      color: white;
      border: none;
      padding: 12px 24px;
      border-radius: 25px;
      font-size: 1rem;
      cursor: pointer;
      margin-top: 15px;
      box-shadow: 0 4px 10px rgba(230, 57, 70, 0.3);
      transition: 0.2s;
    }

    .music-btn:hover {
      transform: scale(1.05);
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Para o Meu Amor ❤️</h1>
    <p class="subtitle">Um cantinho especial só nosso</p>

    <!-- Menu Interativo -->
    <div class="menu">
      <button class="tab-btn active" onclick="openTab('fotos')">Nossa Galeria</button>
      <button class="tab-btn" onclick="openTab('carta')">Minha Carta</button>
      <button class="tab-btn" onclick="openTab('motivos')">Por que te amo?</button>
    </div>

    <!-- Aba 1: Fotos -->
    <div id="fotos" class="tab-content active">
      <div class="photo-frame">
        <img id="current-photo" src="https://picsum.photos/400/300?random=1" alt="Foto Nossa">
      </div>
      <button class="music-btn" style="background: #4a4e69;" onclick="nextPhoto()">Próxima Foto 📸</button>
    </div>

    <!-- Aba 2: Carta -->
    <div id="carta" class="tab-content">
      <p style="text-align: left; line-height: 1.6; font-size: 0.95rem;">
        Escreva aqui sua mensagem especial... <br><br>
        Obrigado por cada momento ao meu lado, por todo sorriso e por deixar minha vida muito mais leve e feliz. Te amo!
      </p>
    </div>

    <!-- Aba 3: Motivos -->
    <div id="motivos" class="tab-content">
      <ul style="text-align: left; margin-left: 20px; line-height: 2;">
        <li>Seu sorriso que ilumina meu dia.</li>
        <li>O jeito como você cuida de mim.</li>
        <li>Nossas risadas e piadas internas.</li>
        <li>Construir um futuro ao seu lado.</li>
      </ul>
    </div>

    <!-- Música de Fundo -->
    <audio id="bg-music" loop>
      <!-- Substitua o link abaixo pela sua música favorita (link direto .mp3) -->
      <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    
    <button class="music-btn" onclick="toggleMusic()">🎵 <span id="music-text">Tocar Música</span></button>
  </div>

  <script>
    // Navegação do Menu Interativo
    function openTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      
      document.getElementById(tabId).classList.add('active');
      event.currentTarget.classList.add('active');
    }

    // Carrossel de Fotos Simples
    const photos = [
      "foto1.jpg", // Substitua pelo caminho das suas fotos
      "foto2.jpg",
      "foto3.jpg"
    ];
    let photoIndex = 0;

    function nextPhoto() {
      photoIndex = (photoIndex + 1) % photos.length;
      document.getElementById('current-photo').src = photos[photoIndex];
    }

    // Controle de Áudio (Navegadores bloqueiam reprodução automática sem clique prévio)
    const music = document.getElementById('bg-music');
    const musicText = document.getElementById('music-text');

    function toggleMusic() {
      if (music.paused) {
        music.play();
        musicText.innerText = "Pausar Música";
      } else {
        music.pause();
        musicText.innerText = "Tocar Música";
      }
    }
  </script>
</body>
</html>
