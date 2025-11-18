#!/usr/bin/env python3
"""
Script para adicionar seção de progresso em todos os módulos
"""

import re

# Seção de progresso HTML template
SECAO_PROGRESSO = '''      <!-- Seção de Progresso -->
      <div class="mb-8 bg-white dark:bg-neutral-800 rounded-2xl p-8 border-2 border-operacional/30">
        <div class="text-center mb-6">
          <h3 class="text-2xl font-bold mb-2">Você completou este módulo?</h3>
          <p class="text-neutral-600 dark:text-neutral-400">
            Marque como concluído para acompanhar seu progresso na trilha
          </p>
        </div>

        <div class="flex flex-col items-center gap-4">
          <button
            id="btn-concluir-modulo"
            data-trilha="operacional"
            data-modulo="{modulo}"
            class="px-10 py-4 bg-operacional text-white rounded-lg font-bold text-lg hover:bg-blue-700 transition-all shadow-lg hover:shadow-xl">
            ✓ Marcar como Concluído
          </button>

          <div id="progresso-info" class="text-center">
            <!-- Será preenchido pelo JavaScript -->
          </div>
        </div>

        <div class="mt-6 pt-6 border-t border-neutral-200 dark:border-neutral-700">
          <div class="flex items-center justify-center gap-2 text-sm text-neutral-600 dark:text-neutral-400">
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path>
            </svg>
            <span>Seu progresso é salvo no navegador e persiste entre sessões</span>
          </div>
        </div>
      </div>

'''

for modulo in range(2, 11):
    arquivo = f'/home/nmaldaner/projetos/FETD/modulos/operacional/modulo-{str(modulo).zfill(2)}.html'

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Procurar por navegação e adicionar seção de progresso antes
        if '<!-- Seção de Progresso -->' not in conteudo:
            secao = SECAO_PROGRESSO.format(modulo=modulo)

            # Tentar encontrar a div de navegação
            padrao_nav = r'(\n\s*<div class="bg-gradient-to-r from-operacional to-blue-600 text-white rounded-2xl p-8">)'
            if re.search(padrao_nav, conteudo):
                conteudo = re.sub(padrao_nav, secao + r'\1', conteudo, count=1)

            # Atualizar botão "Em breve" para link funcional (se existir)
            if modulo < 10:
                proximo = modulo + 1
                # Padrão: botão desabilitado
                padrao_desabilitado = r'<button[^>]*disabled[^>]*>[\s\S]*?Módulo ' + str(proximo) + r'[^<]*<\/button>'
                link_habilitado = f'<a href="modulo-{str(proximo).zfill(2)}.html" class="px-6 py-3 bg-white text-operacional rounded-lg font-semibold hover:bg-yellow-300 hover:text-neutral-900 transition-all">\n            Módulo {proximo} →\n          </a>'
                conteudo = re.sub(padrao_desabilitado, link_habilitado, conteudo)

            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)

            print(f'✅ Atualizado: modulo-{str(modulo).zfill(2)}.html')
        else:
            print(f'⚠️  Já tem progresso ou sem navegação: modulo-{str(modulo).zfill(2)}.html')

    except FileNotFoundError:
        print(f'❌ Arquivo não encontrado: modulo-{str(modulo).zfill(2)}.html')
    except Exception as e:
        print(f'❌ Erro em modulo-{str(modulo).zfill(2)}.html: {e}')

print('\n🎉 Concluído!')
