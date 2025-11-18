// ============================================
// FETD - Main JavaScript
// ============================================

// Remove preload class after page loads
window.addEventListener('load', function() {
  document.body.classList.remove('preload');
});

// ============================================
// Dark Mode Toggle
// ============================================

const themeToggle = document.getElementById('theme-toggle');
const html = document.documentElement;
const darkIcon = document.getElementById('theme-toggle-dark-icon');
const lightIcon = document.getElementById('theme-toggle-light-icon');

// Load saved theme or detect system preference
const currentTheme = localStorage.getItem('theme');

if (currentTheme === 'dark') {
  html.classList.add('dark');
  darkIcon.classList.remove('hidden');
} else if (currentTheme === 'light') {
  html.classList.remove('dark');
  lightIcon.classList.remove('hidden');
} else {
  // System preference
  if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    html.classList.add('dark');
    darkIcon.classList.remove('hidden');
    localStorage.setItem('theme', 'dark');
  } else {
    lightIcon.classList.remove('hidden');
    localStorage.setItem('theme', 'light');
  }
}

// Toggle theme on click
themeToggle.addEventListener('click', function() {
  const isDark = html.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');

  // Toggle icons
  darkIcon.classList.toggle('hidden');
  lightIcon.classList.toggle('hidden');
});

// ============================================
// Mobile Menu Toggle
// ============================================

const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuBtn.addEventListener('click', function() {
  mobileMenu.classList.toggle('hidden');
});

// Close mobile menu when clicking a link
const mobileLinks = mobileMenu.querySelectorAll('a');
mobileLinks.forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
  });
});

// ============================================
// Quiz Logic
// ============================================

const quizData = [
  {
    question: "Como é seu dia de trabalho?",
    options: [
      { text: "Faço muitas tarefas repetitivas e administrativas", trilha: "operacional", emoji: "📊" },
      { text: "Converso com clientes o dia todo", trilha: "comunicador", emoji: "💬" },
      { text: "Estou começando, sem experiência profissional ainda", trilha: "talento", emoji: "🌟" },
      { text: "Trabalho técnico complexo (desenvolvimento, engenharia, etc)", trilha: "tecnico", emoji: "💻" }
    ]
  },
  {
    question: "Qual sua maior dor hoje?",
    options: [
      { text: "Falta de tempo, sobrecarga com trabalho manual", trilha: "operacional", emoji: "⏱️" },
      { text: "Muitos clientes para atender, poucas conversões", trilha: "comunicador", emoji: "📉" },
      { text: "Falta de portfólio e experiência comprovada", trilha: "talento", emoji: "📋" },
      { text: "Dificuldade de comunicar meu valor técnico", trilha: "tecnico", emoji: "🗣️" }
    ]
  },
  {
    question: "O que você mais quer conseguir?",
    options: [
      { text: "Produtividade e organização, trabalhar menos horas", trilha: "operacional", emoji: "✅" },
      { text: "Vender mais e atender melhor meus clientes", trilha: "comunicador", emoji: "💰" },
      { text: "Conseguir minha primeira oportunidade profissional", trilha: "talento", emoji: "🎯" },
      { text: "Evoluir na carreira e ser reconhecido", trilha: "tecnico", emoji: "📈" }
    ]
  },
  {
    question: "Como você aprende melhor?",
    options: [
      { text: "Passo a passo prático e direto ao ponto", trilha: "operacional", emoji: "📝" },
      { text: "Casos reais e exemplos do dia a dia", trilha: "comunicador", emoji: "💡" },
      { text: "Fazendo projetos do zero e praticando", trilha: "talento", emoji: "🛠️" },
      { text: "Entendendo conceitos profundos e arquitetura", trilha: "tecnico", emoji: "🧠" }
    ]
  },
  {
    question: "Em 3 meses você quer ter:",
    options: [
      { text: "15 horas/semana livres e reconhecimento no trabalho", trilha: "operacional", emoji: "⭐" },
      { text: "3x mais clientes atendidos e vendas aumentadas", trilha: "comunicador", emoji: "🚀" },
      { text: "Portfólio completo e primeira oportunidade", trilha: "talento", emoji: "🎓" },
      { text: "Autoridade na área e propostas de alto valor", trilha: "tecnico", emoji: "👑" }
    ]
  }
];

// Quiz state
let currentQuestion = 0;
let answers = {
  operacional: 0,
  comunicador: 0,
  talento: 0,
  tecnico: 0
};
let selectedOption = null;

// Quiz elements
const quizContainer = document.getElementById('quiz-container');
const quizResult = document.getElementById('quiz-result');
const questionNumber = document.getElementById('question-number');
const questionText = document.getElementById('question-text');
const quizOptions = document.getElementById('quiz-options');
const quizPrev = document.getElementById('quiz-prev');
const quizNext = document.getElementById('quiz-next');
const progressDots = document.querySelectorAll('.quiz-progress');

// Render current question
function renderQuestion() {
  const data = quizData[currentQuestion];

  questionNumber.textContent = currentQuestion + 1;
  questionText.textContent = data.question;

  // Clear options
  quizOptions.innerHTML = '';

  // Render options
  data.options.forEach((option, index) => {
    const optionEl = document.createElement('div');
    optionEl.className = 'quiz-option p-4 bg-neutral-50 dark:bg-neutral-700 rounded-xl border-2 border-transparent hover:border-operacional';
    optionEl.innerHTML = `
      <div class="flex items-center gap-3">
        <div class="text-2xl">${option.emoji}</div>
        <div class="flex-1 font-medium">${option.text}</div>
      </div>
    `;

    optionEl.addEventListener('click', () => selectOption(index, optionEl));
    quizOptions.appendChild(optionEl);
  });

  // Update progress dots
  progressDots.forEach((dot, index) => {
    if (index < currentQuestion) {
      dot.classList.remove('bg-neutral-300', 'dark:bg-neutral-600');
      dot.classList.add('bg-operacional');
    } else if (index === currentQuestion) {
      dot.classList.remove('bg-neutral-300', 'dark:bg-neutral-600');
      dot.classList.add('bg-operacional');
    } else {
      dot.classList.remove('bg-operacional');
      dot.classList.add('bg-neutral-300', 'dark:bg-neutral-600');
    }
  });

  // Update navigation buttons
  quizPrev.disabled = currentQuestion === 0;
  quizNext.disabled = selectedOption === null;

  if (currentQuestion === quizData.length - 1) {
    quizNext.innerHTML = 'Ver Resultado →';
  } else {
    quizNext.innerHTML = 'Próxima →';
  }

  selectedOption = null;
}

// Select option
function selectOption(index, element) {
  // Remove previous selection
  const options = quizOptions.querySelectorAll('.quiz-option');
  options.forEach(opt => {
    opt.classList.remove('selected', 'border-operacional');
    opt.classList.add('border-transparent');
  });

  // Add selection
  element.classList.add('selected', 'border-operacional');
  element.classList.remove('border-transparent');

  selectedOption = index;
  quizNext.disabled = false;

  // Record answer
  const trilha = quizData[currentQuestion].options[index].trilha;
  answers[trilha]++;
}

// Next question
quizNext.addEventListener('click', () => {
  if (selectedOption === null) return;

  if (currentQuestion < quizData.length - 1) {
    currentQuestion++;
    renderQuestion();
  } else {
    showResult();
  }
});

// Previous question
quizPrev.addEventListener('click', () => {
  if (currentQuestion > 0) {
    // Decrement answer count
    const prevData = quizData[currentQuestion];
    if (selectedOption !== null) {
      const trilha = prevData.options[selectedOption].trilha;
      answers[trilha]--;
    }

    currentQuestion--;
    renderQuestion();
  }
});

// Show result
function showResult() {
  // Find winning trilha
  let maxScore = 0;
  let winningTrilha = 'operacional';

  for (const [trilha, score] of Object.entries(answers)) {
    if (score > maxScore) {
      maxScore = score;
      winningTrilha = trilha;
    }
  }

  // Define trilha data
  const trilhaData = {
    operacional: {
      name: 'Operacional Produtivo',
      color: 'operacional',
      emoji: '🔵',
      chamada: 'Pare de Perder Tempo com Tarefas Manuais',
      descricao: 'Você passa muito tempo em tarefas repetitivas e administrativas. Sua trilha ideal vai te ensinar a automatizar 80% do seu trabalho e recuperar 15-20 horas por semana.',
      resultados: [
        'Automatizar 80% das tarefas repetitivas',
        'Recuperar 15-20 horas por semana',
        'Criar 10+ automações funcionando sozinhas',
        'Ganhar reconhecimento e promoção'
      ],
      link: 'trilhas/operacional.html'
    },
    comunicador: {
      name: 'Comunicador Estratégico',
      color: 'comunicador',
      emoji: '🟢',
      chamada: 'Atenda Mais, Venda Mais, Sem Perder a Qualidade',
      descricao: 'Você lida com clientes diariamente e perde oportunidades por falta de tempo. Sua trilha ideal vai te ensinar a atender 3x mais clientes e aumentar conversão em 50%.',
      resultados: [
        'Atender 3x mais clientes no mesmo tempo',
        'Aumentar suas vendas em 50%',
        'Sistema de follow-up que nunca esquece',
        'Nunca mais perder oportunidades'
      ],
      link: 'trilhas/comunicador.html'
    },
    talento: {
      name: 'Talento Emergente',
      color: 'talento',
      emoji: '🟡',
      chamada: 'De Zero a Empregável em 60 Dias',
      descricao: 'Você está começando sua carreira e precisa de portfólio e experiência. Sua trilha ideal vai te ensinar a construir 10 projetos reais e conseguir sua primeira oportunidade.',
      resultados: [
        'Construir portfólio com 10 projetos reais',
        'Presença profissional no LinkedIn/GitHub',
        'Dominar as habilidades mais procuradas',
        'Conseguir primeira oportunidade profissional'
      ],
      link: 'trilhas/talento.html'
    },
    tecnico: {
      name: 'Técnico Comunicador',
      color: 'tecnico',
      emoji: '🟠',
      chamada: 'Transforme Conhecimento Técnico em Autoridade',
      descricao: 'Você é excelente tecnicamente mas tem dificuldade de comunicar valor. Sua trilha ideal vai te ensinar a construir autoridade e receber propostas 2-3x mais valorizadas.',
      resultados: [
        'Comunicar valor técnico de forma clara',
        'Construir autoridade reconhecida na área',
        'Receber propostas 2-3x mais valorizadas',
        'Transição: Executor → Consultor/Líder'
      ],
      link: 'trilhas/tecnico.html'
    }
  };

  const trilha = trilhaData[winningTrilha];

  // Hide quiz, show result
  quizContainer.classList.add('hidden');
  quizResult.classList.remove('hidden');

  // Render result
  quizResult.innerHTML = `
    <div class="text-center mb-8">
      <div class="text-6xl mb-4">${trilha.emoji}</div>
      <h3 class="text-3xl font-bold mb-2">Sua Trilha Ideal:</h3>
      <div class="text-4xl font-extrabold text-${trilha.color} mb-4">${trilha.name}</div>
      <p class="text-xl text-${trilha.color} font-semibold italic">"${trilha.chamada}"</p>
    </div>

    <div class="bg-${trilha.color}/10 dark:bg-${trilha.color}/20 p-6 rounded-xl mb-8">
      <p class="text-lg text-neutral-700 dark:text-neutral-300">
        ${trilha.descricao}
      </p>
    </div>

    <div class="mb-8">
      <h4 class="text-xl font-bold mb-4">Em 10 semanas você vai:</h4>
      <ul class="space-y-3">
        ${trilha.resultados.map(resultado => `
          <li class="flex items-start gap-3">
            <span class="text-${trilha.color} text-xl">✓</span>
            <span class="text-neutral-700 dark:text-neutral-300">${resultado}</span>
          </li>
        `).join('')}
      </ul>
    </div>

    <div class="flex flex-col sm:flex-row gap-4">
      <a href="${trilha.link}" class="flex-1 text-center px-8 py-4 bg-${trilha.color} text-white rounded-lg font-bold text-lg hover:opacity-90 transition-all">
        🚀 Começar Trilha ${trilha.name}
      </a>
      <button onclick="restartQuiz()" class="px-8 py-4 bg-neutral-200 dark:bg-neutral-700 text-neutral-800 dark:text-neutral-200 rounded-lg font-semibold hover:bg-neutral-300 dark:hover:bg-neutral-600 transition-all">
        🔄 Refazer Quiz
      </button>
    </div>

    <div class="mt-8 text-center text-sm text-neutral-600 dark:text-neutral-400">
      <p>💡 Não concorda com o resultado? Explore todas as <a href="#trilhas" class="text-${trilha.color} font-semibold hover:underline">4 trilhas disponíveis</a></p>
    </div>
  `;

  // Scroll to result
  quizResult.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Restart quiz
function restartQuiz() {
  currentQuestion = 0;
  answers = {
    operacional: 0,
    comunicador: 0,
    talento: 0,
    tecnico: 0
  };
  selectedOption = null;

  quizContainer.classList.remove('hidden');
  quizResult.classList.add('hidden');

  renderQuestion();

  // Scroll to quiz
  quizContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Initialize quiz
renderQuestion();

// ============================================
// Sistema de Progresso com LocalStorage
// ============================================

// Salvar módulo como concluído
function marcarModuloConcluido(trilha, modulo) {
  let progresso = JSON.parse(localStorage.getItem('fetd_progresso') || '{}');

  if (!progresso[trilha]) {
    progresso[trilha] = [];
  }

  if (!progresso[trilha].includes(modulo)) {
    progresso[trilha].push(modulo);
  }

  localStorage.setItem('fetd_progresso', JSON.stringify(progresso));

  // Atualizar UI
  atualizarUIProgresso(trilha, modulo);

  // Mostrar mensagem de sucesso
  mostrarMensagemSucesso(trilha, modulo);
}

// Verificar se módulo está concluído
function moduloConcluido(trilha, modulo) {
  let progresso = JSON.parse(localStorage.getItem('fetd_progresso') || '{}');
  return progresso[trilha]?.includes(modulo) || false;
}

// Calcular % de conclusão de uma trilha
function calcularProgresso(trilha) {
  let progresso = JSON.parse(localStorage.getItem('fetd_progresso') || '{}');
  let concluidos = progresso[trilha]?.length || 0;
  return {
    concluidos: concluidos,
    total: 10,
    percentual: Math.round((concluidos / 10) * 100)
  };
}

// Obter próximo módulo não concluído
function proximoModulo(trilha) {
  let progresso = JSON.parse(localStorage.getItem('fetd_progresso') || '{}');
  let concluidos = progresso[trilha] || [];

  for (let i = 1; i <= 10; i++) {
    if (!concluidos.includes(i)) {
      return i;
    }
  }

  return null; // Todos concluídos
}

// Atualizar UI após marcar módulo como concluído
function atualizarUIProgresso(trilha, modulo) {
  // Atualizar botão de conclusão
  const btnConcluir = document.getElementById('btn-concluir-modulo');
  if (btnConcluir) {
    btnConcluir.innerHTML = '✓ Módulo Concluído!';
    btnConcluir.classList.remove('bg-operacional', 'hover:bg-blue-700');
    btnConcluir.classList.add('bg-green-600', 'cursor-not-allowed');
    btnConcluir.disabled = true;
  }

  // Atualizar info de progresso
  const progressoInfo = document.getElementById('progresso-info');
  if (progressoInfo) {
    const prog = calcularProgresso(trilha);
    progressoInfo.innerHTML = `
      <div class="text-sm text-neutral-600 dark:text-neutral-400">
        Progresso na trilha: <strong class="text-operacional">${prog.percentual}%</strong> (${prog.concluidos}/${prog.total} módulos)
      </div>
    `;
  }
}

// Mostrar mensagem de sucesso ao concluir módulo
function mostrarMensagemSucesso(trilha, modulo) {
  const prog = calcularProgresso(trilha);
  const proximo = proximoModulo(trilha);

  // Criar overlay de sucesso
  const overlay = document.createElement('div');
  overlay.className = 'fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4';
  overlay.innerHTML = `
    <div class="bg-white dark:bg-neutral-800 rounded-2xl p-8 max-w-md w-full text-center animate-scale-in">
      <div class="text-6xl mb-4">🎉</div>
      <h3 class="text-2xl font-bold mb-2">Parabéns!</h3>
      <p class="text-neutral-600 dark:text-neutral-400 mb-6">
        Você concluiu o <strong>Módulo ${modulo}</strong>!<br>
        Progresso: <strong class="text-operacional">${prog.percentual}%</strong> (${prog.concluidos}/${prog.total})
      </p>
      ${proximo ? `
        <a href="modulo-${String(proximo).padStart(2, '0')}.html" class="inline-block px-8 py-3 bg-operacional text-white rounded-lg font-semibold hover:bg-blue-700 transition-all mb-3">
          Ir para Módulo ${proximo} →
        </a>
        <br>
      ` : `
        <div class="text-green-600 font-bold text-lg mb-3">
          ✓ Trilha 100% Completa!
        </div>
      `}
      <button onclick="this.parentElement.parentElement.remove()" class="px-6 py-2 bg-neutral-200 dark:bg-neutral-700 rounded-lg font-semibold hover:bg-neutral-300 dark:hover:bg-neutral-600 transition-all">
        Fechar
      </button>
    </div>
  `;

  document.body.appendChild(overlay);

  // Fechar ao clicar no overlay
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) {
      overlay.remove();
    }
  });
}

// Inicializar UI de progresso ao carregar página de módulo
function inicializarProgressoModulo() {
  const btnConcluir = document.getElementById('btn-concluir-modulo');
  if (!btnConcluir) return;

  const trilha = btnConcluir.dataset.trilha;
  const modulo = parseInt(btnConcluir.dataset.modulo);

  // Verificar se já está concluído
  if (moduloConcluido(trilha, modulo)) {
    btnConcluir.innerHTML = '✓ Módulo Concluído!';
    btnConcluir.classList.remove('bg-operacional', 'hover:bg-blue-700');
    btnConcluir.classList.add('bg-green-600', 'cursor-not-allowed');
    btnConcluir.disabled = true;
  }

  // Atualizar info de progresso
  const progressoInfo = document.getElementById('progresso-info');
  if (progressoInfo) {
    const prog = calcularProgresso(trilha);
    progressoInfo.innerHTML = `
      <div class="text-sm text-neutral-600 dark:text-neutral-400">
        Progresso na trilha: <strong class="text-operacional">${prog.percentual}%</strong> (${prog.concluidos}/${prog.total} módulos)
      </div>
    `;
  }

  // Adicionar evento de clique
  btnConcluir.addEventListener('click', () => {
    if (!btnConcluir.disabled) {
      marcarModuloConcluido(trilha, modulo);
    }
  });
}

// Inicializar barra de progresso na landing page
function inicializarBarraProgresso() {
  const barraProgresso = document.getElementById('barra-progresso-trilha');
  if (!barraProgresso) return;

  const trilha = barraProgresso.dataset.trilha;
  const prog = calcularProgresso(trilha);

  barraProgresso.innerHTML = `
    <div class="mb-6">
      <div class="flex justify-between items-center mb-2">
        <span class="text-sm font-semibold text-neutral-700 dark:text-neutral-300">Seu Progresso</span>
        <span class="text-sm font-bold text-operacional">${prog.percentual}%</span>
      </div>
      <div class="w-full bg-neutral-200 dark:bg-neutral-700 rounded-full h-3 overflow-hidden">
        <div class="bg-gradient-to-r from-operacional to-blue-600 h-full transition-all duration-500" style="width: ${prog.percentual}%"></div>
      </div>
      <div class="mt-2 text-xs text-neutral-600 dark:text-neutral-400">
        ${prog.concluidos} de ${prog.total} módulos concluídos
      </div>
    </div>
  `;
}

// Marcar módulos concluídos visualmente na landing page
function marcarModulosConcluidosLanding() {
  const trilha = 'operacional'; // Por enquanto só temos essa trilha
  const progresso = JSON.parse(localStorage.getItem('fetd_progresso') || '{}');
  const concluidos = progresso[trilha] || [];

  concluidos.forEach(modulo => {
    const card = document.querySelector(`[data-modulo="${modulo}"]`);
    if (card) {
      // Adicionar badge de concluído
      const badge = card.querySelector('.badge-status');
      if (badge) {
        badge.textContent = 'CONCLUÍDO';
        badge.classList.remove('bg-operacional/20', 'text-operacional');
        badge.classList.add('bg-green-600/20', 'text-green-600');
      }

      // Adicionar ícone de check
      const titulo = card.querySelector('h3');
      if (titulo && !titulo.querySelector('.check-icon')) {
        const check = document.createElement('span');
        check.className = 'check-icon text-green-600 ml-2';
        check.textContent = '✓';
        titulo.appendChild(check);
      }
    }
  });
}

// Inicializar quando página carregar
document.addEventListener('DOMContentLoaded', () => {
  inicializarProgressoModulo();
  inicializarBarraProgresso();
  marcarModulosConcluidosLanding();
});

// ============================================
// Smooth Scroll for Anchor Links
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});
