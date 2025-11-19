#!/usr/bin/env python3
"""
Conversor de Markdown para HTML ULTRA RICO
Versão 2.0 - Layout mais visual e atraente
Baseado nos melhores elementos das trilhas existentes
"""

import re
import os
from pathlib import Path

# Mapeamento de cores por trilha
CORES_TRILHAS = {
    'operacional': {'cor': 'operacional', 'hex': '#3B82F6', 'emoji': '🔵'},
    'comunicador': {'cor': 'comunicador', 'hex': '#10B981', 'emoji': '🟢'},
    'talento': {'cor': 'talento', 'hex': '#F59E0B', 'emoji': '🟡'},
    'tecnico': {'cor': 'tecnico', 'hex': '#F97316', 'emoji': '🟠'},
}

NOMES_TRILHAS = {
    'operacional': 'Operacional Produtivo',
    'comunicador': 'Comunicador Estratégico',
    'talento': 'Talento Emergente',
    'tecnico': 'Técnico Comunicador',
}

def extrair_metadados_md(conteudo_md):
    """Extrai título, duração e objetivo do Markdown"""
    titulo_match = re.search(r'^#\s+(.+?)$', conteudo_md, re.MULTILINE)
    titulo = titulo_match.group(1) if titulo_match else "Módulo"

    duracao_match = re.search(r'\*\*Duração:\*\*\s+(.+?)$', conteudo_md, re.MULTILINE)
    duracao = duracao_match.group(1) if duracao_match else "60 minutos"

    objetivo_match = re.search(r'\*\*Objetivo:\*\*\s+(.+?)$', conteudo_md, re.MULTILINE)
    objetivo = objetivo_match.group(1) if objetivo_match else ""

    return titulo, duracao, objetivo

def converter_markdown_para_html_corpo(conteudo_md, trilha, objetivo=""):
    """Converte o corpo do Markdown para HTML ultra rico"""
    cor = CORES_TRILHAS[trilha]['cor']

    html_parts = []

    # Adiciona box de objetivo no topo se houver
    if objetivo:
        html_parts.append(f'''
      <!-- Objetivo do Módulo -->
      <div class="bg-{cor}/10 dark:bg-{cor}/20 border-l-4 border-{cor} p-6 rounded-lg mb-12 shadow-lg">
        <h3 class="text-xl font-bold text-{cor} mb-2 flex items-center gap-2">
          <span class="text-2xl">🎯</span>
          <span>Objetivo deste Módulo</span>
        </h3>
        <p class="text-neutral-700 dark:text-neutral-300 text-lg">
          {objetivo}
        </p>
      </div>
''')

    # Remove metadados do topo
    conteudo_md = re.sub(r'^#[^#].*?\n---\n', '', conteudo_md, flags=re.MULTILINE | re.DOTALL, count=1)

    # Divide o conteúdo em seções por ##
    secoes = re.split(r'\n## ', conteudo_md)

    for i, secao in enumerate(secoes):
        if not secao.strip():
            continue

        # Se não começa com ##, adiciona
        if i > 0:
            secao = '## ' + secao

        # Processa seção
        html_secao = processar_secao(secao, cor)
        html_parts.append(html_secao)

    return '\n\n'.join(html_parts)

def processar_secao(secao, cor):
    """Processa uma seção (##) individual com layout rico"""
    html_parts = []

    # Extrai título da seção (##)
    titulo_match = re.match(r'##\s+(.+?)$', secao, re.MULTILINE)
    if titulo_match:
        titulo = titulo_match.group(1)

        # Remove emojis especiais do título para comentário
        titulo_limpo = re.sub(r'^[🎯💡📊🔍✅❌⚡🚀📝🎨🔧💰📈🎓💼🌟]+\s*', '', titulo)

        # Adiciona gradient e ícone ao título da seção
        html_parts.append(f'''
      <!-- Seção: {titulo_limpo} -->
      <div class="mb-16">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 pb-4 border-b-2 border-{cor}/20 bg-gradient-to-r from-{cor}/10 to-transparent -mx-4 px-4 py-4 rounded-lg">{titulo}</h2>
''')

        # Remove título da seção do conteúdo
        conteudo = re.sub(r'^##\s+.+?$', '', secao, count=1, flags=re.MULTILINE)
    else:
        conteudo = secao

    # Processa subseções (###)
    partes = re.split(r'\n### ', conteudo)

    for j, parte in enumerate(partes):
        if not parte.strip():
            continue

        if j > 0:
            parte = '### ' + parte

        html_parte = processar_subsecao(parte, cor)
        html_parts.append(html_parte)

    html_parts.append('      </div>')

    return '\n'.join(html_parts)

def processar_subsecao(subsecao, cor):
    """Processa uma subseção (###) individual com cards visuais"""
    html_parts = []

    # Extrai título da subseção
    titulo_match = re.match(r'###\s+(.+?)$', subsecao, re.MULTILINE)
    if titulo_match:
        titulo = titulo_match.group(1)

        # Detecta se é um card especial (mito, exemplo, caso, etc)
        e_mito = bool(re.search(r'❌|MITO|Mito', titulo))
        e_verdade = bool(re.search(r'✅|VERDADE|Verdade', titulo))
        e_exemplo = bool(re.search(r'Exemplo|Case|Caso', titulo, re.IGNORECASE))
        e_importante = bool(re.search(r'💡|Importante|Atenção|Nota', titulo, re.IGNORECASE))
        e_dados = bool(re.search(r'📊|Dados|Números|Estatísticas', titulo, re.IGNORECASE))

        if e_mito:
            html_parts.append(f'''
        <div class="bg-red-50 dark:bg-red-900/20 border-l-4 border-red-500 p-6 rounded-lg mb-8 shadow-md hover:shadow-lg transition-shadow">
          <h3 class="text-xl font-bold text-red-700 dark:text-red-400 mb-4 flex items-center gap-2">
            <span class="text-2xl">❌</span>
            <span>{titulo}</span>
          </h3>
''')
        elif e_verdade:
            html_parts.append(f'''
        <div class="bg-green-50 dark:bg-green-900/20 border-l-4 border-green-500 p-6 rounded-lg mb-8 shadow-md hover:shadow-lg transition-shadow">
          <h3 class="text-xl font-bold text-green-700 dark:text-green-400 mb-4 flex items-center gap-2">
            <span class="text-2xl">✅</span>
            <span>{titulo}</span>
          </h3>
''')
        elif e_exemplo:
            html_parts.append(f'''
        <div class="bg-{cor}/10 dark:bg-{cor}/20 border-2 border-{cor}/30 p-6 rounded-xl mb-8 shadow-lg hover:shadow-xl transition-all">
          <h3 class="text-xl font-bold text-{cor} mb-4 flex items-center gap-2">
            <span class="text-2xl">💼</span>
            <span>{titulo}</span>
          </h3>
''')
        elif e_importante:
            html_parts.append(f'''
        <div class="bg-yellow-50 dark:bg-yellow-900/20 border-l-4 border-yellow-500 p-6 rounded-lg mb-8 shadow-md">
          <h3 class="text-xl font-bold text-yellow-700 dark:text-yellow-400 mb-4 flex items-center gap-2">
            <span class="text-2xl">💡</span>
            <span>{titulo}</span>
          </h3>
''')
        elif e_dados:
            html_parts.append(f'''
        <div class="bg-blue-50 dark:bg-blue-900/20 border-l-4 border-blue-500 p-6 rounded-lg mb-8 shadow-md">
          <h3 class="text-xl font-bold text-blue-700 dark:text-blue-400 mb-4 flex items-center gap-2">
            <span class="text-2xl">📊</span>
            <span>{titulo}</span>
          </h3>
''')
        else:
            html_parts.append(f'''
        <div class="mb-8">
          <h3 class="text-2xl font-semibold mb-4 text-{cor}">{titulo}</h3>
''')

        # Remove título do conteúdo
        conteudo = re.sub(r'^###\s+.+?$', '', subsecao, count=1, flags=re.MULTILINE)
    else:
        conteudo = subsecao
        html_parts.append('        <div class="mb-6">')

    # Processa o conteúdo (parágrafos, listas, tabelas, etc)
    html_conteudo = processar_conteudo(conteudo, cor)
    html_parts.append(html_conteudo)

    html_parts.append('        </div>')

    return '\n'.join(html_parts)

def processar_conteudo(conteudo, cor):
    """Processa o conteúdo markdown (parágrafos, listas, negrito, etc)"""
    html_parts = []

    # Divide em blocos (separados por linha dupla)
    blocos = conteudo.split('\n\n')

    for bloco in blocos:
        bloco = bloco.strip()
        if not bloco:
            continue

        # Detecta tipo de bloco
        if bloco.startswith('|') and '|' in bloco:
            # Tabela
            html_parts.append(processar_tabela(bloco, cor))
        elif bloco.startswith('```'):
            # Código
            html_parts.append(processar_codigo(bloco, cor))
        elif re.match(r'^[\*\-]\s+', bloco, re.MULTILINE):
            # Lista não ordenada - Detecta se é comparativa (Antes/Agora)
            if 'Antes' in bloco[:100] or 'Agora' in bloco[:100] or '❌' in bloco or '✅' in bloco:
                html_parts.append(processar_lista_comparativa(bloco, cor))
            else:
                html_parts.append(processar_lista_nao_ordenada(bloco, cor))
        elif re.match(r'^\d+\.\s+', bloco, re.MULTILINE):
            # Lista ordenada
            html_parts.append(processar_lista_ordenada(bloco, cor))
        elif bloco.startswith('**') and ':**' in bloco[:50]:
            # Definição destacada (ex: **O que é:** ...)
            html_parts.append(processar_definicao(bloco, cor))
        else:
            # Parágrafo normal
            html_parts.append(processar_paragrafo(bloco, cor))

    return '\n'.join(html_parts)

def processar_lista_comparativa(lista_md, cor):
    """Processa lista comparativa (Antes vs Agora) com visual rico"""
    linhas = [l.strip() for l in lista_md.split('\n') if l.strip()]

    # Detecta se tem cabeçalho "Antes:" ou "Agora:"
    tem_antes = any('Antes' in l for l in linhas[:3])
    tem_agora = any('Agora' in l or 'Hoje' in l or '2025' in l for l in linhas[:3])

    if tem_antes and tem_agora:
        # Layout de comparação lado a lado em grid
        html = '''
          <div class="grid md:grid-cols-2 gap-6 mb-8">
            <!-- Antes -->
            <div class="bg-neutral-50 dark:bg-neutral-900 p-6 rounded-xl border-2 border-neutral-200 dark:border-neutral-700">
              <h4 class="font-bold text-lg mb-4 text-neutral-600 dark:text-neutral-400">❌ Antes:</h4>
              <ul class="space-y-3">
'''

        # Processa itens "Antes"
        in_antes = False
        for linha in linhas:
            if 'Antes' in linha:
                in_antes = True
                continue
            if 'Agora' in linha or 'Hoje' in linha or '2025' in linha:
                break
            if in_antes and linha.startswith(('-', '*', '+')):
                texto = re.sub(r'^[\*\-\+]\s+', '', linha)
                texto_formatado = aplicar_formatacao_inline(texto)
                html += f'                <li class="flex items-start gap-3"><span class="text-red-500 text-xl flex-shrink-0">❌</span><span class="text-neutral-700 dark:text-neutral-300">{texto_formatado}</span></li>\n'

        html += '''              </ul>
            </div>
            <!-- Agora -->
            <div class="bg-''' + cor + '''/10 dark:bg-''' + cor + '''/20 p-6 rounded-xl border-2 border-''' + cor + '''/30">
              <h4 class="font-bold text-lg mb-4 text-''' + cor + '''">✅ Agora (2025):</h4>
              <ul class="space-y-3">
'''

        # Processa itens "Agora"
        in_agora = False
        for linha in linhas:
            if 'Agora' in linha or 'Hoje' in linha or '2025' in linha:
                in_agora = True
                continue
            if in_agora and linha.startswith(('-', '*', '+')):
                texto = re.sub(r'^[\*\-\+]\s+', '', linha)
                texto_formatado = aplicar_formatacao_inline(texto)
                html += f'                <li class="flex items-start gap-3"><span class="text-green-500 text-xl flex-shrink-0">✅</span><span class="text-neutral-700 dark:text-neutral-300">{texto_formatado}</span></li>\n'

        html += '''              </ul>
            </div>
          </div>
'''
        return html
    else:
        # Lista normal
        return processar_lista_nao_ordenada(lista_md, cor)

def processar_tabela(tabela_md, cor):
    """Converte tabela Markdown para HTML com estilo premium"""
    linhas = [l.strip() for l in tabela_md.split('\n') if l.strip()]

    # Ignora linha de separação (|---|---|)
    linhas = [l for l in linhas if not re.match(r'^\|[\s\-:]+\|$', l)]

    if len(linhas) < 2:
        return ''

    # Cabeçalho
    header = linhas[0]
    colunas_header = [c.strip() for c in header.split('|') if c.strip()]

    # Linhas de dados
    linhas_dados = linhas[1:]

    html = f'''
          <div class="overflow-x-auto mb-8 shadow-lg rounded-lg">
            <table class="w-full border-collapse">
              <thead>
                <tr class="bg-gradient-to-r from-{cor} to-{cor}/80 text-white">
'''

    for col in colunas_header:
        col_formatado = aplicar_formatacao_inline(col)
        html += f'                  <th class="px-6 py-4 text-left font-bold">{col_formatado}</th>\n'

    html += '''                </tr>
              </thead>
              <tbody class="bg-white dark:bg-neutral-800">
'''

    for i, linha in enumerate(linhas_dados):
        colunas = [c.strip() for c in linha.split('|') if c.strip()]
        bg_class = 'bg-white dark:bg-neutral-800' if i % 2 == 0 else 'bg-neutral-50 dark:bg-neutral-900'
        html += f'                <tr class="{bg_class} hover:bg-{cor}/5 transition-colors">\n'
        for col in colunas:
            col_formatado = aplicar_formatacao_inline(col)
            html += f'                  <td class="px-6 py-4 border-b border-neutral-200 dark:border-neutral-700">{col_formatado}</td>\n'
        html += '                </tr>\n'

    html += '''              </tbody>
            </table>
          </div>
'''

    return html

def processar_codigo(codigo_md, cor):
    """Processa bloco de código com visual terminal"""
    # Remove ```
    codigo = re.sub(r'^```\w*\n?', '', codigo_md)
    codigo = re.sub(r'\n?```$', '', codigo)

    # Escapa HTML
    codigo = codigo.replace('<', '&lt;').replace('>', '&gt;')

    return f'''
          <div class="bg-neutral-900 dark:bg-black p-6 rounded-lg overflow-x-auto mb-6 shadow-xl border border-{cor}/30">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-3 h-3 rounded-full bg-red-500"></div>
              <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
              <div class="w-3 h-3 rounded-full bg-green-500"></div>
            </div>
            <pre class="text-sm text-green-400 font-mono"><code>{codigo}</code></pre>
          </div>
'''

def processar_lista_nao_ordenada(lista_md, cor):
    """Converte lista não ordenada para HTML com ícones"""
    linhas = [l.strip() for l in lista_md.split('\n') if l.strip()]

    html = '          <ul class="space-y-3 mb-6">\n'

    for linha in linhas:
        # Remove marcador (-, *, +)
        texto = re.sub(r'^[\*\-\+]\s+', '', linha)

        # Detecta ícone/emoji no início
        icone_match = re.match(r'^([✅❌🔴🟢🟡⭐💡📊🎯🚀📈💰🎓💼📝🔧⚡🌟]+)\s+(.+)$', texto)
        if icone_match:
            icone = icone_match.group(1)
            texto_resto = icone_match.group(2)
            texto_formatado = aplicar_formatacao_inline(texto_resto)
            html += f'            <li class="flex items-start gap-3"><span class="text-2xl flex-shrink-0">{icone}</span><span class="flex-1 pt-1 text-neutral-700 dark:text-neutral-300">{texto_formatado}</span></li>\n'
        else:
            texto_formatado = aplicar_formatacao_inline(texto)
            html += f'            <li class="flex items-start gap-3"><span class="w-2 h-2 rounded-full bg-{cor} flex-shrink-0 mt-2"></span><span class="flex-1 text-neutral-700 dark:text-neutral-300">{texto_formatado}</span></li>\n'

    html += '          </ul>\n'

    return html

def processar_lista_ordenada(lista_md, cor):
    """Converte lista ordenada para HTML"""
    linhas = [l.strip() for l in lista_md.split('\n') if l.strip()]

    html = f'          <ol class="space-y-3 mb-6 list-decimal list-inside marker:text-{cor} marker:font-bold">\n'

    for linha in linhas:
        # Remove número
        texto = re.sub(r'^\d+\.\s+', '', linha)
        texto_formatado = aplicar_formatacao_inline(texto)
        html += f'            <li class="text-lg text-neutral-700 dark:text-neutral-300 pl-2">{texto_formatado}</li>\n'

    html += '          </ol>\n'

    return html

def processar_definicao(def_md, cor):
    """Processa definição destacada (ex: **O que é:** ...)"""
    # Separa label e conteúdo
    match = re.match(r'\*\*(.+?):\*\*\s+(.+)', def_md, re.DOTALL)
    if match:
        label = match.group(1)
        conteudo = match.group(2)
        conteudo_formatado = aplicar_formatacao_inline(conteudo)

        return f'''
          <div class="bg-{cor}/5 dark:bg-{cor}/10 p-4 rounded-lg mb-4 border-l-4 border-{cor}">
            <p class="text-lg"><span class="font-bold text-{cor} text-xl">{label}:</span> <span class="text-neutral-700 dark:text-neutral-300">{conteudo_formatado}</span></p>
          </div>
'''
    else:
        return processar_paragrafo(def_md, cor)

def processar_paragrafo(para_md, cor):
    """Processa parágrafo normal"""
    texto_formatado = aplicar_formatacao_inline(para_md)
    return f'          <p class="text-lg text-neutral-700 dark:text-neutral-300 mb-6 leading-relaxed">{texto_formatado}</p>\n'

def aplicar_formatacao_inline(texto):
    """Aplica formatação inline (negrito, itálico, links, etc)"""
    # Negrito
    texto = re.sub(r'\*\*(.+?)\*\*', r'<strong class="font-bold">\1</strong>', texto)

    # Itálico
    texto = re.sub(r'\*(.+?)\*', r'<em class="italic">\1</em>', texto)

    # Código inline
    texto = re.sub(r'`(.+?)`', r'<code class="px-2 py-1 bg-neutral-200 dark:bg-neutral-700 rounded text-sm font-mono">\1</code>', texto)

    # Links
    texto = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" class="text-blue-600 dark:text-blue-400 hover:underline font-medium">\1</a>', texto)

    return texto

def gerar_html_completo(trilha, modulo_num, titulo, duracao, objetivo, corpo_html):
    """Gera o HTML completo do módulo com layout premium"""
    cor_info = CORES_TRILHAS[trilha]
    cor = cor_info['cor']
    hex_cor = cor_info['hex']
    nome_trilha = NOMES_TRILHAS[trilha]

    # Define cor secundária para gradiente
    cores_gradiente = {
        'operacional': 'blue-600',
        'comunicador': 'emerald-600',
        'talento': 'amber-600',
        'tecnico': 'orange-600',
    }
    cor_grad = cores_gradiente.get(trilha, cor)

    html = f'''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo} | Trilha {nome_trilha} | FETD</title>
  <meta name="description" content="{objetivo}">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.jsdelivr.net/npm/tailwindcss-cdn@3.4.1/tailwindcss.js"></script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind Config -->
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            '{cor}': '{hex_cor}',
          }},
          fontFamily: {{
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
          }},
        }}
      }}
    }}
  </script>

  <style>
    * {{
      transition: background-color 200ms ease-in-out, border-color 200ms ease-in-out, color 200ms ease-in-out;
    }}
    .preload * {{
      transition: none !important;
    }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
  </style>
</head>

<body class="preload bg-neutral-50 dark:bg-neutral-900 text-neutral-900 dark:text-neutral-100">

  <!-- Navbar -->
  <nav class="sticky top-0 z-50 bg-white/95 dark:bg-neutral-800/95 backdrop-blur-md border-b border-neutral-200 dark:border-neutral-700 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center">
          <a href="../../index.html" class="text-2xl font-bold bg-gradient-to-r from-{cor} to-{cor_grad} bg-clip-text text-transparent hover:opacity-80 transition-opacity">
            🎓 FETD
          </a>
        </div>
        <div class="hidden md:flex items-center space-x-8">
          <a href="../../index.html" class="text-neutral-700 dark:text-neutral-300 hover:text-{cor} transition-colors font-medium">Início</a>
          <a href="../../trilhas/{trilha}.html" class="text-neutral-700 dark:text-neutral-300 hover:text-{cor} transition-colors font-medium">Trilha {nome_trilha}</a>
          <button id="theme-toggle" class="p-2 rounded-lg bg-neutral-100 dark:bg-neutral-700 hover:bg-{cor}/10 transition-colors">
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

  <!-- Breadcrumb -->
  <div class="bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <nav class="flex text-sm font-medium" aria-label="Breadcrumb">
        <a href="../../index.html" class="text-{cor} hover:opacity-80 transition-opacity">Início</a>
        <span class="mx-2 text-neutral-400">/</span>
        <a href="../../trilhas/{trilha}.html" class="text-{cor} hover:opacity-80 transition-opacity">Trilha {nome_trilha}</a>
        <span class="mx-2 text-neutral-400">/</span>
        <span class="text-neutral-600 dark:text-neutral-400">Módulo {modulo_num}</span>
      </nav>
    </div>
  </div>

  <!-- Hero Módulo -->
  <section class="bg-gradient-to-br from-{cor} via-{cor} to-{cor_grad} py-20 relative overflow-hidden">
    <div class="absolute inset-0 bg-grid-white/5 bg-[size:20px_20px]"></div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white relative z-10">

      <div class="flex flex-wrap items-center gap-3 mb-6">
        <span class="px-4 py-2 bg-white/20 backdrop-blur-sm rounded-full text-sm font-bold shadow-lg">Módulo {modulo_num} de 10</span>
        <span class="px-4 py-2 bg-white/20 backdrop-blur-sm rounded-full text-sm font-bold shadow-lg flex items-center gap-2">
          <span>⏱️</span>
          <span>{duracao}</span>
        </span>
      </div>

      <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight">
        {titulo}
      </h1>

      <p class="text-xl md:text-2xl text-white/95 mb-8 max-w-3xl font-medium leading-relaxed">
        {objetivo}
      </p>

      <div class="flex flex-wrap items-center gap-4 text-white/90">
        <span class="flex items-center gap-2 font-medium"><span class="text-xl">📚</span> Teoria</span>
        <span class="text-white/60">•</span>
        <span class="flex items-center gap-2 font-medium"><span class="text-xl">💭</span> Reflexão</span>
        <span class="text-white/60">•</span>
        <span class="flex items-center gap-2 font-medium"><span class="text-xl">🛠️</span> Prática</span>
      </div>
    </div>
  </section>

  <!-- Conteúdo Principal -->
  <section class="py-16 bg-white dark:bg-neutral-800">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

      <!-- Download Button -->
      <div class="flex justify-end mb-8">
        <a href="../../downloads/{trilha}/modulo-{modulo_num:02d}.md" download class="px-6 py-3 bg-gradient-to-r from-{cor} to-{cor_grad} text-white rounded-lg font-bold hover:opacity-90 inline-flex items-center gap-2 shadow-lg hover:shadow-xl transition-all">
          <span class="text-xl">📥</span>
          <span>Download MD</span>
        </a>
      </div>

{corpo_html}

    </div>
  </section>

  <!-- Footer / Navegação -->
  <section class="py-12 bg-gradient-to-br from-neutral-100 to-neutral-50 dark:from-neutral-900 dark:to-neutral-800 border-t border-neutral-200 dark:border-neutral-700">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center">
        <a href="../../trilhas/{trilha}.html" class="px-6 py-3 bg-gradient-to-r from-{cor} to-{cor_grad} text-white rounded-lg font-bold hover:opacity-90 shadow-lg hover:shadow-xl transition-all inline-flex items-center gap-2">
          <span>←</span>
          <span>Voltar para Trilha</span>
        </a>
        {f'<a href="modulo-{modulo_num+1:02d}.html" class="px-6 py-3 bg-gradient-to-r from-{cor} to-{cor_grad} text-white rounded-lg font-bold hover:opacity-90 shadow-lg hover:shadow-xl transition-all inline-flex items-center gap-2"><span>Próximo Módulo</span><span>→</span></a>' if modulo_num < 10 else ''}
      </div>
    </div>
  </section>

  <!-- Dark Mode Toggle Script -->
  <script>
    // Remove preload class
    window.addEventListener('load', () => {{
      document.body.classList.remove('preload');
    }});

    // Dark mode toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    // Check localStorage
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
      themeToggleLightIcon.classList.remove('hidden');
      document.documentElement.classList.add('dark');
    }} else {{
      themeToggleDarkIcon.classList.remove('hidden');
    }}

    themeToggleBtn.addEventListener('click', () => {{
      themeToggleDarkIcon.classList.toggle('hidden');
      themeToggleLightIcon.classList.toggle('hidden');

      if (localStorage.getItem('color-theme')) {{
        if (localStorage.getItem('color-theme') === 'light') {{
          document.documentElement.classList.add('dark');
          localStorage.setItem('color-theme', 'dark');
        }} else {{
          document.documentElement.classList.remove('dark');
          localStorage.setItem('color-theme', 'light');
        }}
      }} else {{
        if (document.documentElement.classList.contains('dark')) {{
          document.documentElement.classList.remove('dark');
          localStorage.setItem('color-theme', 'light');
        }} else {{
          document.documentElement.classList.add('dark');
          localStorage.setItem('color-theme', 'dark');
        }}
      }}
    }});
  </script>

</body>
</html>
'''

    return html

def converter_modulo(trilha, modulo_num):
    """Converte um módulo específico de MD para HTML ultra rico"""
    # Caminhos
    md_path = f'downloads/{trilha}/modulo-{modulo_num:02d}.md'
    html_path = f'modulos/{trilha}/modulo-{modulo_num:02d}.html'

    if not os.path.exists(md_path):
        print(f"❌ Arquivo não encontrado: {md_path}")
        return False

    # Lê Markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        conteudo_md = f.read()

    # Extrai metadados
    titulo, duracao, objetivo = extrair_metadados_md(conteudo_md)

    # Converte corpo (passa objetivo para adicionar box no topo)
    corpo_html = converter_markdown_para_html_corpo(conteudo_md, trilha, objetivo)

    # Gera HTML completo
    html_completo = gerar_html_completo(trilha, modulo_num, titulo, duracao, objetivo, corpo_html)

    # Cria diretório se não existe
    os.makedirs(os.path.dirname(html_path), exist_ok=True)

    # Salva HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_completo)

    print(f"✅ Convertido: {html_path}")
    return True

def converter_trilha_completa(trilha):
    """Converte todos os 10 módulos de uma trilha"""
    print(f"\n🔄 Convertendo trilha: {NOMES_TRILHAS[trilha]}")
    print(f"🎨 Layout ULTRA RICO v2.0 ativado!\n")
    sucesso = 0
    for i in range(1, 11):
        if converter_modulo(trilha, i):
            sucesso += 1
    print(f"\n✅ {sucesso}/10 módulos convertidos com layout premium!\n")

def main():
    """Função principal"""
    import sys

    if len(sys.argv) < 2:
        print("=" * 60)
        print("🎨 CONVERSOR MD → HTML ULTRA RICO v2.0")
        print("=" * 60)
        print("\nUso: python converter_md_para_html_rico_v2.py <trilha> [modulo_num]")
        print("\nExemplos:")
        print("  python converter_md_para_html_rico_v2.py talento        # Todos os 10 módulos")
        print("  python converter_md_para_html_rico_v2.py talento 1      # Apenas módulo 1")
        print("\nTrilhas disponíveis: operacional, comunicador, talento, tecnico")
        print("\nNovidades v2.0:")
        print("  ✨ Box de objetivo destacado no topo")
        print("  🎨 Cards comparativos Antes/Agora em grid")
        print("  📊 Tabelas com gradientes e hover effects")
        print("  💻 Blocos de código estilo terminal")
        print("  🎯 Ícones e emojis destacados")
        print("  🌈 Gradientes e sombras modernas")
        print("  📱 Layout totalmente responsivo")
        print("=" * 60)
        return

    trilha = sys.argv[1]

    if trilha not in CORES_TRILHAS:
        print(f"❌ Trilha inválida: {trilha}")
        print(f"Trilhas disponíveis: {', '.join(CORES_TRILHAS.keys())}")
        return

    if len(sys.argv) >= 3:
        # Converte módulo específico
        modulo_num = int(sys.argv[2])
        converter_modulo(trilha, modulo_num)
    else:
        # Converte trilha completa
        converter_trilha_completa(trilha)

if __name__ == '__main__':
    main()
