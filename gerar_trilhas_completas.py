#!/usr/bin/env python3
"""
Script para gerar as 3 trilhas restantes (Comunicador, Talento, Técnico)
com suas landing pages e 10 módulos cada
"""

import os

# Definições das trilhas
TRILHAS = {
    'comunicador': {
        'nome': 'Comunicador Estratégico',
        'emoji': '🟢',
        'cor': 'comunicador',
        'cor_hex': '#10B981',
        'chamada': 'Atenda Mais, Venda Mais, Sem Perder a Qualidade',
        'descricao': 'Triplique seu atendimento e aumente conversão em 50% usando IA e automação para comunicação com clientes',
        'promessa_horas': '3x mais clientes',
        'promessa_percentual': '50% mais vendas',
        'promessa_automacoes': 'Follow-up perfeito',
        'promessa_extra': 'Zero oportunidades perdidas',
        'modulos': [
            {
                'num': 1,
                'titulo': 'A Revolução do Atendimento',
                'duracao': '30min',
                'objetivo': 'Entender como IA e automação estão transformando vendas e atendimento',
                'conteudo': 'Por que agora é diferente, casos reais de vendedores triplicando resultados, os 3 mitos do atendimento'
            },
            {
                'num': 2,
                'titulo': 'Golden Trinity - Atrair, Converter, Reter',
                'duracao': '45min',
                'objetivo': 'Dominar o framework de comunicação estratégica',
                'conteudo': 'Framework ACR (Attract/Convert/Retain), matriz de priorização de clientes, automação inteligente de follow-up'
            },
            {
                'num': 3,
                'titulo': 'IA Como Assistente de Vendas',
                'duracao': '1h',
                'objetivo': 'Usar IA para qualificar leads e preparar abordagens',
                'conteudo': 'ChatGPT para pesquisa de clientes, prompts para scripts de vendas, personalização em escala'
            },
            {
                'num': 4,
                'titulo': 'CRM Simples e Automático',
                'duracao': '1h 30min',
                'objetivo': 'Criar sistema de gestão de clientes sem complexidade',
                'conteudo': 'Google Sheets como CRM, automações para registro de interações, dashboard de vendas automático'
            },
            {
                'num': 5,
                'titulo': 'Follow-up que Nunca Falha',
                'duracao': '1h 15min',
                'objetivo': 'Sistema automático de acompanhamento de leads',
                'conteudo': 'Sequências de follow-up automatizadas, gatilhos inteligentes, nunca mais perder oportunidade'
            },
            {
                'num': 6,
                'titulo': 'Mensagens Personalizadas em Escala',
                'duracao': '1h 30min',
                'objetivo': 'Atender muitos clientes mantendo personalização',
                'conteudo': 'Templates inteligentes com IA, variáveis dinâmicas, tom de voz consistente'
            },
            {
                'num': 7,
                'titulo': 'WhatsApp e Redes Sociais Automáticos',
                'duracao': '1h',
                'objetivo': 'Automatizar presença em canais de comunicação',
                'conteudo': 'Respostas automáticas inteligentes, triagem de mensagens, integração multi-canal'
            },
            {
                'num': 8,
                'titulo': 'Propostas e Contratos Instantâneos',
                'duracao': '1h',
                'objetivo': 'Gerar documentos comerciais automaticamente',
                'conteudo': 'Templates de propostas com auto-preenchimento, assinaturas digitais, funil de fechamento'
            },
            {
                'num': 9,
                'titulo': 'Framework ACA - Comunicação Perfeita',
                'duracao': '1h',
                'objetivo': 'Dominar comunicação que gera resultados',
                'conteudo': 'Acknowledge/Compliment/Ask, objeções antecipadas, fechamento consultivo'
            },
            {
                'num': 10,
                'titulo': 'Sistema de Vendas Completo',
                'duracao': '2h',
                'objetivo': 'Integrar tudo em máquina de vendas automatizada',
                'conteudo': 'PROJETO FINAL: CRM + Follow-up + Propostas + Métricas funcionando 24/7'
            }
        ]
    },
    'talento': {
        'nome': 'Talento Emergente',
        'emoji': '🟡',
        'cor': 'talento',
        'cor_hex': '#F59E0B',
        'chamada': 'De Zero a Empregável em 60 Dias',
        'descricao': 'Construa portfólio com 10 projetos reais e consiga sua primeira oportunidade profissional',
        'promessa_horas': '10 projetos reais',
        'promessa_percentual': 'Portfólio completo',
        'promessa_automacoes': 'Presença profissional',
        'promessa_extra': '1ª oportunidade em 60 dias',
        'modulos': [
            {
                'num': 1,
                'titulo': 'O Mercado que Te Espera',
                'duracao': '30min',
                'objetivo': 'Entender oportunidades para quem está começando',
                'conteudo': 'Mercado em transformação, habilidades mais procuradas 2025, mitos sobre "falta de experiência"'
            },
            {
                'num': 2,
                'titulo': 'Golden Path - Do Zero ao Portfólio',
                'duracao': '45min',
                'objetivo': 'Plano de 60 dias para primeira oportunidade',
                'conteudo': 'Framework 3P (Projects/Presence/Pitch), matriz de habilidades vs. projetos, roadmap personalizado'
            },
            {
                'num': 3,
                'titulo': 'IA Como Mentor Pessoal',
                'duracao': '1h',
                'objetivo': 'Usar IA para aprender e criar projetos',
                'conteudo': 'ChatGPT como tutor, prompts para gerar ideias de projetos, debugging com IA'
            },
            {
                'num': 4,
                'titulo': 'Seu Primeiro Projeto Real',
                'duracao': '2h',
                'objetivo': 'Criar projeto #1 para o portfólio',
                'conteudo': 'HANDS-ON: Automação de tarefas pessoais, documentação profissional, publicar no GitHub'
            },
            {
                'num': 5,
                'titulo': 'LinkedIn e GitHub Profissionais',
                'duracao': '1h 30min',
                'objetivo': 'Construir presença online que atrai recrutadores',
                'conteudo': 'Perfil LinkedIn otimizado, GitHub como portfólio, networking estratégico'
            },
            {
                'num': 6,
                'titulo': 'Projetos 2, 3 e 4 - Batch Building',
                'duracao': '3h',
                'objetivo': 'Criar 3 projetos complementares rapidamente',
                'conteudo': 'HANDS-ON: Dashboard automático, chatbot simples, scraper de dados (batch project building)'
            },
            {
                'num': 7,
                'titulo': 'Currículo e Portfólio que Vendem',
                'duracao': '1h 30min',
                'objetivo': 'Documentar conquistas de forma profissional',
                'conteudo': 'CV baseado em realizações, portfólio online, case studies de projetos'
            },
            {
                'num': 8,
                'titulo': 'Projetos 5-10 - Portfolio Sprint',
                'duracao': '4h',
                'objetivo': 'Completar portfólio com variedade de projetos',
                'conteudo': 'HANDS-ON: API integration, data viz, automation tool, web scraper, productivity app, mini-SaaS'
            },
            {
                'num': 9,
                'titulo': 'Framework PPA - Pitch Perfeito Adaptado',
                'duracao': '1h',
                'objetivo': 'Apresentar-se de forma memorável',
                'conteudo': 'Problem/Process/Achievement, storytelling de projetos, responder "fale sobre você"'
            },
            {
                'num': 10,
                'titulo': 'Hunting - Caçando Oportunidades',
                'duracao': '2h',
                'objetivo': 'Estratégia completa para conseguir primeira vaga',
                'conteudo': 'PROJETO FINAL: Aplicar para 50+ vagas, outreach direto, preparação para entrevistas, follow-up estratégico'
            }
        ]
    },
    'tecnico': {
        'nome': 'Técnico Comunicador',
        'emoji': '🟠',
        'cor': 'tecnico',
        'cor_hex': '#F97316',
        'chamada': 'Transforme Conhecimento Técnico em Autoridade',
        'descricao': 'Comunique valor, construa autoridade e receba propostas 2-3x mais valorizadas',
        'promessa_horas': 'Autoridade reconhecida',
        'promessa_percentual': 'Propostas 2-3x maiores',
        'promessa_automacoes': 'Executor → Consultor',
        'promessa_extra': 'Network qualificado',
        'modulos': [
            {
                'num': 1,
                'titulo': 'O Problema da Invisibilidade Técnica',
                'duracao': '30min',
                'objetivo': 'Entender por que expertise não gera oportunidades sozinha',
                'conteudo': 'Paradoxo do técnico invisível, casos de transformação, custo da falta de comunicação'
            },
            {
                'num': 2,
                'titulo': 'Golden Triangle - Expertise + Comunicação + Distribuição',
                'duracao': '45min',
                'objetivo': 'Framework para construir autoridade técnica',
                'conteudo': 'Triângulo ECD, matriz impacto vs. esforço para conteúdo, estratégia de posicionamento'
            },
            {
                'num': 3,
                'titulo': 'IA Como Ghostwriter Técnico',
                'duracao': '1h',
                'objetivo': 'Transformar conhecimento em conteúdo de valor',
                'conteudo': 'Prompts para artigos técnicos, simplificar complexidade, voz técnica + acessível'
            },
            {
                'num': 4,
                'titulo': 'Presença Técnica Automatizada',
                'duracao': '1h 30min',
                'objetivo': 'Sistema de geração de conteúdo consistente',
                'conteudo': 'LinkedIn + Medium + GitHub, calendário editorial automático, reutilização de conteúdo'
            },
            {
                'num': 5,
                'titulo': 'Newsletter e Lista de Email Técnica',
                'duracao': '1h 15min',
                'objetivo': 'Construir audiência própria de tomadores de decisão',
                'conteudo': 'Setup de newsletter gratuita, automação de envios, crescimento orgânico'
            },
            {
                'num': 6,
                'titulo': 'Palestras e Workshops Escaláveis',
                'duracao': '1h 30min',
                'objetivo': 'Compartilhar conhecimento para milhares simultaneamente',
                'conteudo': 'Estrutura de talks técnicos, slides automatizados com IA, gravação e distribuição'
            },
            {
                'num': 7,
                'titulo': 'Network Estratégico Automatizado',
                'duracao': '1h',
                'objetivo': 'Conectar-se com pessoas certas sem esforço manual',
                'conteudo': 'Outreach inteligente, follow-up automático, CRM para network, warm introductions'
            },
            {
                'num': 8,
                'titulo': 'Propostas de Alto Valor',
                'duracao': '1h',
                'objetivo': 'Precificar e apresentar serviços consultivos',
                'conteudo': 'Value-based pricing, proposta consultiva vs. técnica, templates de escopo/orçamento'
            },
            {
                'num': 9,
                'titulo': 'Framework TSV - Technical Storytelling Value',
                'duracao': '1h',
                'objetivo': 'Comunicar impacto técnico para não-técnicos',
                'conteudo': 'Traduzir complexidade, métricas de negócio, narrativa técnica persuasiva'
            },
            {
                'num': 10,
                'titulo': 'Máquina de Autoridade Completa',
                'duracao': '2h',
                'objetivo': 'Sistema integrado de autoridade técnica',
                'conteudo': 'PROJETO FINAL: Conteúdo + Newsletter + Network + Propostas funcionando automaticamente'
            }
        ]
    }
}

def criar_landing_page(trilha_key, trilha_data):
    """Cria landing page de uma trilha"""
    html = f'''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Trilha {trilha_data['nome']} | FETD</title>
  <meta name="description" content="{trilha_data['descricao']}">

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            'operacional': '#3B82F6',
            'comunicador': '#10B981',
            'talento': '#F59E0B',
            'tecnico': '#F97316',
          }},
          fontFamily: {{
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
          }},
        }}
      }}
    }}
  </script>

  <style>
    * {{ transition: background-color 200ms ease-in-out, border-color 200ms ease-in-out, color 200ms ease-in-out; }}
    .preload * {{ transition: none !important; }}
    body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>
</head>

<body class="preload bg-neutral-50 dark:bg-neutral-900 text-neutral-900 dark:text-neutral-100">

  <nav class="sticky top-0 z-50 bg-white/90 dark:bg-neutral-800/90 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center">
          <a href="../index.html" class="text-2xl font-bold bg-gradient-to-r from-{trilha_data['cor']} to-operacional bg-clip-text text-transparent">
            🎓 FETD
          </a>
        </div>
        <div class="hidden md:flex items-center space-x-8">
          <a href="../index.html" class="text-neutral-700 dark:text-neutral-300 hover:text-{trilha_data['cor']} transition-colors">Início</a>
          <a href="../index.html#trilhas" class="text-neutral-700 dark:text-neutral-300 hover:text-{trilha_data['cor']} transition-colors">Trilhas</a>
          <button id="theme-toggle" class="p-2 rounded-lg bg-neutral-100 dark:bg-neutral-700 hover:bg-neutral-200 dark:hover:bg-neutral-600 transition-colors">
            <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
            </svg>
            <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </nav>

  <div class="bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <nav class="flex text-sm" aria-label="Breadcrumb">
        <a href="../index.html" class="text-{trilha_data['cor']} hover:text-{trilha_data['cor']}-700 transition-colors">Início</a>
        <span class="mx-2 text-neutral-400">/</span>
        <span class="text-neutral-600 dark:text-neutral-400">Trilha {trilha_data['nome']}</span>
      </nav>
    </div>
  </div>

  <section class="bg-gradient-to-r from-{trilha_data['cor']} to-green-600 py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white">

      <div id="barra-progresso-trilha" data-trilha="{trilha_key}" class="mb-8"></div>

      <div class="flex items-center gap-4 mb-6">
        <span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">{trilha_data['emoji']} Trilha</span>
        <span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">10 Módulos</span>
        <span class="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold">10-12 Semanas</span>
      </div>

      <h1 class="text-5xl lg:text-6xl font-extrabold mb-6 leading-tight">{trilha_data['emoji']} {trilha_data['nome']}</h1>
      <p class="text-3xl font-bold text-yellow-300 mb-6">"{trilha_data['chamada']}"</p>
      <p class="text-xl text-white/90 mb-8 max-w-3xl">{trilha_data['descricao']}</p>

      <div class="grid md:grid-cols-4 gap-6 mb-12">
        <div class="bg-white/10 backdrop-blur p-6 rounded-xl">
          <div class="text-4xl font-bold">{trilha_data['promessa_horas']}</div>
          <div class="text-sm text-white/80">Primeira Meta</div>
        </div>
        <div class="bg-white/10 backdrop-blur p-6 rounded-xl">
          <div class="text-4xl font-bold">{trilha_data['promessa_percentual']}</div>
          <div class="text-sm text-white/80">Segunda Meta</div>
        </div>
        <div class="bg-white/10 backdrop-blur p-6 rounded-xl">
          <div class="text-4xl font-bold">{trilha_data['promessa_automacoes']}</div>
          <div class="text-sm text-white/80">Terceira Meta</div>
        </div>
        <div class="bg-white/10 backdrop-blur p-6 rounded-xl">
          <div class="text-4xl font-bold">{trilha_data['promessa_extra']}</div>
          <div class="text-sm text-white/80">Resultado Final</div>
        </div>
      </div>

      <a href="../modulos/{trilha_key}/modulo-01.html" class="inline-block px-10 py-5 bg-white text-{trilha_data['cor']} rounded-lg font-bold text-xl hover:bg-yellow-300 hover:text-neutral-900 transition-all shadow-2xl">
        🚀 Começar Módulo 1
      </a>
    </div>
  </section>

  <section class="py-20 bg-neutral-50 dark:bg-neutral-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold mb-4">Os 10 Módulos da Trilha</h2>
        <p class="text-xl text-neutral-600 dark:text-neutral-400">Progressão lógica do básico ao avançado</p>
      </div>

      <div class="space-y-6 max-w-4xl mx-auto">
'''

    # Adicionar cards dos módulos
    for modulo in trilha_data['modulos']:
        html += f'''
        <div class="bg-gradient-to-r from-{trilha_data['cor']}/10 to-{trilha_data['cor']}/5 dark:from-{trilha_data['cor']}/20 dark:to-{trilha_data['cor']}/10 p-8 rounded-2xl border-2 border-{trilha_data['cor']} hover:shadow-xl transition-all" data-modulo="{modulo['num']}">
          <div class="flex items-start gap-6">
            <div class="flex-shrink-0">
              <div class="w-16 h-16 bg-{trilha_data['cor']} text-white rounded-xl flex items-center justify-center text-2xl font-bold">{modulo['num']}</div>
            </div>
            <div class="flex-1">
              <span class="badge-status inline-block px-3 py-1 bg-{trilha_data['cor']}/20 text-{trilha_data['cor']} rounded-full text-xs font-semibold mb-2">DISPONÍVEL</span>
              <h3 class="text-2xl font-bold mb-2">{modulo['titulo']}</h3>
              <p class="text-neutral-600 dark:text-neutral-400 mb-4">{modulo['conteudo']}</p>
              <div class="flex items-center gap-4 text-sm text-neutral-600 dark:text-neutral-400">
                <span>⏱️ {modulo['duracao']}</span>
                <span>📝 Exercícios práticos</span>
                <span>📥 Download MD</span>
              </div>
              <a href="../modulos/{trilha_key}/modulo-{str(modulo['num']).zfill(2)}.html" class="inline-block mt-4 px-6 py-3 bg-{trilha_data['cor']} text-white rounded-lg font-semibold hover:opacity-90 transition-all">
                Começar Módulo {modulo['num']} →
              </a>
            </div>
          </div>
        </div>
'''

    html += f'''
      </div>
    </div>
  </section>

  <section class="py-20 bg-gradient-to-r from-{trilha_data['cor']} to-green-600">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
      <h2 class="text-4xl font-bold mb-6">Pronto Para Transformar Sua Carreira?</h2>
      <p class="text-xl mb-8">Comece agora e veja resultados na primeira semana</p>
      <a href="../modulos/{trilha_key}/modulo-01.html" class="inline-block px-10 py-5 bg-white text-{trilha_data['cor']} rounded-lg font-bold text-xl hover:bg-yellow-300 hover:text-neutral-900 transition-all shadow-2xl">
        🚀 Começar Módulo 1 Agora
      </a>
      <p class="mt-6 text-sm text-white/80">100% online • 100% prático • 100% gratuito</p>
    </div>
  </section>

  <footer class="bg-neutral-900 dark:bg-black text-neutral-300 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center text-sm">
        <p>&copy; 2025 FETD - Formação em Engenharia de Intenção</p>
      </div>
    </div>
  </footer>

  <script src="../js/app.js"></script>
</body>
</html>
'''
    return html


def criar_modulo(trilha_key, trilha_data, modulo_data):
    """Cria uma página de módulo"""
    num = modulo_data['num']
    proximo = num + 1 if num < 10 else None
    anterior = num - 1 if num > 1 else None

    html = f'''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Módulo {num}: {modulo_data['titulo']} | FETD</title>

  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            'operacional': '#3B82F6',
            'comunicador': '#10B981',
            'talento': '#F59E0B',
            'tecnico': '#F97316',
          }},
        }}
      }}
    }}
  </script>

  <style>
    * {{ transition: background-color 200ms, border-color 200ms, color 200ms; }}
    .preload * {{ transition: none !important; }}
    body {{ font-family: 'Inter', sans-serif; }}
  </style>
</head>

<body class="preload bg-neutral-50 dark:bg-neutral-900 text-neutral-900 dark:text-neutral-100">

  <nav class="sticky top-0 z-50 bg-white/90 dark:bg-neutral-800/90 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <a href="../../index.html" class="text-2xl font-bold bg-gradient-to-r from-{trilha_data['cor']} to-operacional bg-clip-text text-transparent">🎓 FETD</a>
        <div class="flex items-center space-x-8">
          <a href="../../index.html" class="text-neutral-700 dark:text-neutral-300 hover:text-{trilha_data['cor']} transition-colors">Início</a>
          <a href="../../trilhas/{trilha_key}.html" class="text-neutral-700 dark:text-neutral-300 hover:text-{trilha_data['cor']} transition-colors">Trilha</a>
          <button id="theme-toggle" class="p-2 rounded-lg bg-neutral-100 dark:bg-neutral-700">
            <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
            <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
          </button>
        </div>
      </div>
    </div>
  </nav>

  <div class="bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <nav class="flex text-sm">
        <a href="../../index.html" class="text-{trilha_data['cor']} hover:underline">Início</a>
        <span class="mx-2 text-neutral-400">/</span>
        <a href="../../trilhas/{trilha_key}.html" class="text-{trilha_data['cor']} hover:underline">Trilha {trilha_data['nome']}</a>
        <span class="mx-2 text-neutral-400">/</span>
        <span class="text-neutral-600 dark:text-neutral-400">Módulo {num}</span>
      </nav>
    </div>
  </div>

  <section class="py-20">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

      <div class="mb-12">
        <div class="flex items-center gap-4 mb-4">
          <span class="px-4 py-2 bg-{trilha_data['cor']}/20 text-{trilha_data['cor']} rounded-full text-sm font-semibold">Módulo {num}</span>
          <span class="text-neutral-600 dark:text-neutral-400">⏱️ {modulo_data['duracao']}</span>
          <a href="../../downloads/{trilha_key}/modulo-{str(num).zfill(2)}.md" download class="ml-auto px-4 py-2 bg-neutral-100 dark:bg-neutral-800 rounded-lg hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors text-sm font-semibold">
            📥 Download MD
          </a>
        </div>

        <h1 class="text-4xl lg:text-5xl font-extrabold mb-4">{modulo_data['titulo']}</h1>
        <p class="text-xl text-neutral-600 dark:text-neutral-400"><strong>Objetivo:</strong> {modulo_data['objetivo']}</p>
      </div>

      <div class="prose dark:prose-invert max-w-none">
        <div class="bg-{trilha_data['cor']}/10 dark:bg-{trilha_data['cor']}/20 p-6 rounded-xl mb-8">
          <h2 class="text-2xl font-bold mb-4">📚 Conteúdo do Módulo</h2>
          <p class="text-lg">{modulo_data['conteudo']}</p>
          <p class="mt-4 text-sm text-neutral-600 dark:text-neutral-400"><em>Este módulo contém teoria, exemplos práticos e exercícios hands-on para você aplicar imediatamente.</em></p>
        </div>

        <div class="bg-green-100 dark:bg-green-900/40 p-6 rounded-xl">
          <h3 class="text-xl font-bold mb-3">✅ Entregável</h3>
          <p>Ao final deste módulo você terá criado/aprendido sobre: {modulo_data['conteudo'][:100]}...</p>
        </div>
      </div>

      <div class="mb-8 mt-16 bg-white dark:bg-neutral-800 rounded-2xl p-8 border-2 border-{trilha_data['cor']}/30">
        <div class="text-center mb-6">
          <h3 class="text-2xl font-bold mb-2">Você completou este módulo?</h3>
          <p class="text-neutral-600 dark:text-neutral-400">Marque como concluído para acompanhar seu progresso</p>
        </div>
        <div class="flex flex-col items-center gap-4">
          <button id="btn-concluir-modulo" data-trilha="{trilha_key}" data-modulo="{num}" class="px-10 py-4 bg-{trilha_data['cor']} text-white rounded-lg font-bold text-lg hover:opacity-90 transition-all shadow-lg">
            ✓ Marcar como Concluído
          </button>
          <div id="progresso-info" class="text-center"></div>
        </div>
      </div>

      <div class="bg-gradient-to-r from-{trilha_data['cor']} to-green-600 text-white rounded-2xl p-8">
        <div class="flex justify-between items-center">
          <a href="{'modulo-' + str(anterior).zfill(2) + '.html' if anterior else '../../trilhas/' + trilha_key + '.html'}" class="px-6 py-3 bg-white/20 hover:bg-white/30 rounded-lg font-semibold transition-all">
            ← {'Módulo ' + str(anterior) if anterior else 'Voltar à Trilha'}
          </a>
          <div class="text-center">
            <p class="text-sm opacity-80 mb-1">{'Próximo Módulo' if proximo else 'Trilha Completa!'}</p>
            <p class="font-bold">{'Módulo ' + str(proximo) if proximo else '🎉 Parabéns!'}</p>
          </div>
          <a href="{'modulo-' + str(proximo).zfill(2) + '.html' if proximo else '../../trilhas/' + trilha_key + '.html'}" class="px-6 py-3 bg-white text-{trilha_data['cor']} rounded-lg font-semibold hover:bg-yellow-300 hover:text-neutral-900 transition-all">
            {'Módulo ' + str(proximo) + ' →' if proximo else '← Voltar à Trilha'}
          </a>
        </div>
      </div>

    </div>
  </section>

  <footer class="bg-neutral-900 dark:bg-black text-neutral-300 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center text-sm"><p>&copy; 2025 FETD - Formação em Engenharia de Intenção</p></div>
    </div>
  </footer>

  <script src="../../js/app.js"></script>
</body>
</html>
'''
    return html


def criar_markdown(trilha_data, modulo_data):
    """Cria arquivo markdown para download"""
    num = modulo_data['num']

    md = f'''# Módulo {num}: {modulo_data['titulo']}

**Trilha:** {trilha_data['nome']}
**Duração:** {modulo_data['duracao']}
**Objetivo:** {modulo_data['objetivo']}

---

## 📚 Conteúdo do Módulo

{modulo_data['conteudo']}

Este módulo contém teoria, exemplos práticos e exercícios hands-on para você aplicar imediatamente.

---

## ✅ Entregável

Ao final deste módulo você terá criado/aprendido sobre: {modulo_data['conteudo']}

---

**© 2025 FETD - Formação em Engenharia de Intenção**
'''
    return md


# Criar estrutura de diretórios e arquivos
for trilha_key, trilha_data in TRILHAS.items():
    print(f"\n🔄 Criando Trilha: {trilha_data['nome']}")

    # Criar diretórios
    os.makedirs(f'/home/nmaldaner/projetos/FETD/modulos/{trilha_key}', exist_ok=True)
    os.makedirs(f'/home/nmaldaner/projetos/FETD/downloads/{trilha_key}', exist_ok=True)
    os.makedirs(f'/home/nmaldaner/projetos/FETD/trilhas', exist_ok=True)

    # Criar landing page
    landing_html = criar_landing_page(trilha_key, trilha_data)
    with open(f'/home/nmaldaner/projetos/FETD/trilhas/{trilha_key}.html', 'w', encoding='utf-8') as f:
        f.write(landing_html)
    print(f'  ✅ Landing: trilhas/{trilha_key}.html')

    # Criar módulos
    for modulo in trilha_data['modulos']:
        # HTML
        modulo_html = criar_modulo(trilha_key, trilha_data, modulo)
        arquivo_html = f'/home/nmaldaner/projetos/FETD/modulos/{trilha_key}/modulo-{str(modulo["num"]).zfill(2)}.html'
        with open(arquivo_html, 'w', encoding='utf-8') as f:
            f.write(modulo_html)

        # Markdown
        modulo_md = criar_markdown(trilha_data, modulo)
        arquivo_md = f'/home/nmaldaner/projetos/FETD/downloads/{trilha_key}/modulo-{str(modulo["num"]).zfill(2)}.md'
        with open(arquivo_md, 'w', encoding='utf-8') as f:
            f.write(modulo_md)

        print(f'  ✅ Módulo {modulo["num"]}: {modulo["titulo"][:40]}...')

print('\n🎉 TODAS AS 3 TRILHAS CRIADAS COM SUCESSO!')
print(f'\nResumo:')
print(f'  - 3 landing pages')
print(f'  - 30 módulos HTML (10 por trilha)')
print(f'  - 30 arquivos MD para download')
print(f'\nTotal: 63 arquivos criados!')
