# MÓDULO 7: Documentação e Arquivos Automáticos

**Objetivo:** Gerar documentos, relatórios e apresentações automaticamente

---

## 1. O Problema da Documentação Manual (E Como Ele Está Matando Sua Produtividade)

### A Verdade Dolorosa

Quantas horas você perdeu ESTA SEMANA:
- Criando relatórios semanais/mensais com os mesmos formatos?
- Copiando dados de uma planilha para um documento Word?
- Ajustando formatação de apresentações?
- Procurando aquele arquivo "versão_final_final_AGORA_VAI.docx"?

**Estatística chocante:** Profissionais gastam em média **4-6 horas por semana** apenas criando documentação repetitiva.

São **200-300 horas por ano**. Quase **2 MESES de trabalho** fazendo coisas que poderiam ser automatizadas.

### Os 3 Pecados Capitais da Documentação Manual

**1. Erro Humano**
- Copiar dado errado da planilha
- Esquecer de atualizar um número
- Trocar nome de cliente/projeto
- Resultado: Apresentação com dados de outubro quando era para ser novembro

**2. Falta de Padronização**
- Cada pessoa formata de um jeito
- Logos em lugares diferentes
- Fontes e tamanhos aleatórios
- Resultado: Empresa parece amadora

**3. Desperdício de Tempo**
- Fazer a mesma coisa toda semana/mês
- "Ah, só vou copiar o documento do mês passado e alterar os números"
- 40 minutos depois você ainda está ajustando formatação
- Resultado: Tempo que poderia estar fazendo trabalho estratégico

### O Que Vamos Resolver HOJE

Neste módulo você vai aprender:

1. **Templates inteligentes** que se preenchem sozinhos
2. **IA para gerar documentos complexos** em 30 segundos
3. **Automação de relatórios** 100% automáticos
4. **Organização automática** de arquivos no Drive
5. **Versionamento** que funciona (nunca mais "final_v8.docx")

**Meta realista:** Reduzir de 4-6h/semana para 30min-1h/semana em documentação.

São **3-5 horas economizadas por semana = Meio dia de trabalho!**

---

## 2. Templates Inteligentes (Copy, Paste, Repeat... NUNCA MAIS!)

### A Regra de Ouro dos Templates

**Se você criou o mesmo tipo de documento 3+ vezes, você PRECISA de um template.**

Exemplos comuns:
- Relatório semanal/mensal
- Ata de reunião
- Proposta comercial
- Contrato padrão
- Procedimento operacional
- Apresentação de resultados

### Google Docs com Variáveis (Tutorial Completo)

**Conceito:** Criar documento modelo com "placeholders" que são substituídos automaticamente.

**Exemplo:**

```
Relatório Semanal - {{SEMANA}}

Cliente: {{NOME_CLIENTE}}
Período: {{DATA_INICIO}} a {{DATA_FIM}}

Resumo Executivo:
- Vendas: R$ {{VALOR_VENDAS}}
- Meta: R$ {{VALOR_META}} ({{PERCENTUAL_META}}%)
- Status: {{STATUS}}

Observações:
{{OBSERVACOES}}
```

**Como funciona:**

**Opção 1: Manual (rápido)**
1. Crie template com {{VARIÁVEIS}}
2. Ctrl+H (Localizar e Substituir)
3. Substitua {{VARIÁVEL}} pelo valor real
4. Salve como novo documento

**Opção 2: Apps Script (automático - melhor)**

```javascript
function gerarRelatorio() {
  // 1. Abrir template
  var templateId = "ID_DO_SEU_TEMPLATE"; // Copie da URL do template
  var template = DriveApp.getFileById(templateId);
  var copia = template.makeCopy("Relatório " + new Date().toLocaleDateString());

  // 2. Abrir documento copiado
  var doc = DocumentApp.openById(copia.getId());
  var corpo = doc.getBody();

  // 3. Buscar dados (pode ser de Sheets, por exemplo)
  var planilha = SpreadsheetApp.openById("ID_DA_SUA_PLANILHA");
  var dados = planilha.getSheetByName("Dados").getRange("A2:E2").getValues()[0];

  // 4. Substituir variáveis
  corpo.replaceText("{{NOME_CLIENTE}}", dados[0]);
  corpo.replaceText("{{VALOR_VENDAS}}", "R$ " + dados[1].toFixed(2));
  corpo.replaceText("{{VALOR_META}}", "R$ " + dados[2].toFixed(2));
  corpo.replaceText("{{PERCENTUAL_META}}", ((dados[1]/dados[2])*100).toFixed(0) + "%");
  corpo.replaceText("{{STATUS}}", dados[3]);
  corpo.replaceText("{{OBSERVACOES}}", dados[4]);
  corpo.replaceText("{{SEMANA}}", "Semana " + new Date().getWeek());

  // 5. Salvar e fechar
  doc.saveAndClose();

  // 6. Retornar link
  Logger.log("Relatório gerado: " + copia.getUrl());
}
```

**Resultado:** Aperta botão → Relatório pronto em 5 segundos.

### 10 Templates Operacionais Prontos para Usar

#### 1. Relatório Semanal

```
RELATÓRIO SEMANAL - SEMANA {{NUMERO_SEMANA}}/{{ANO}}

Cliente/Projeto: {{NOME_PROJETO}}
Responsável: {{NOME_RESPONSAVEL}}
Período: {{DATA_INICIO}} a {{DATA_FIM}}

📊 NÚMEROS DA SEMANA

Entregas Realizadas: {{QTD_ENTREGAS}}
Tarefas Concluídas: {{QTD_TAREFAS_CONCLUIDAS}}
Tarefas Pendentes: {{QTD_TAREFAS_PENDENTES}}
% de Conclusão: {{PERCENTUAL_CONCLUSAO}}%

✅ PRINCIPAIS REALIZAÇÕES

1. {{REALIZACAO_1}}
2. {{REALIZACAO_2}}
3. {{REALIZACAO_3}}

⚠️ BLOQUEIOS E DESAFIOS

{{BLOQUEIOS}}

📅 PRÓXIMOS PASSOS

{{PROXIMOS_PASSOS}}

---
Gerado automaticamente em {{DATA_GERACAO}}
```

#### 2. Ata de Reunião

```
ATA DE REUNIÃO

Data: {{DATA_REUNIAO}}
Horário: {{HORA_INICIO}} às {{HORA_FIM}}
Local: {{LOCAL}}

Participantes:
{{LISTA_PARTICIPANTES}}

Pauta:
{{PAUTA}}

Decisões Tomadas:
✅ {{DECISAO_1}}
✅ {{DECISAO_2}}
✅ {{DECISAO_3}}

Ações e Responsáveis:
⏳ {{ACAO_1}} - Responsável: {{RESPONSAVEL_1}} - Prazo: {{PRAZO_1}}
⏳ {{ACAO_2}} - Responsável: {{RESPONSAVEL_2}} - Prazo: {{PRAZO_2}}
⏳ {{ACAO_3}} - Responsável: {{RESPONSAVEL_3}} - Prazo: {{PRAZO_3}}

Próxima Reunião:
📅 {{DATA_PROXIMA_REUNIAO}}

---
Ata gerada por: {{AUTOR}}
```

#### 3. Proposta Comercial

```
PROPOSTA COMERCIAL

Para: {{NOME_CLIENTE}}
CNPJ: {{CNPJ_CLIENTE}}
Contato: {{CONTATO_CLIENTE}}

Válida até: {{DATA_VALIDADE}}

Sobre Nós:
{{TEXTO_INSTITUCIONAL}}

Escopo do Projeto:
{{DESCRICAO_ESCOPO}}

Entregas:
✓ {{ENTREGA_1}}
✓ {{ENTREGA_2}}
✓ {{ENTREGA_3}}

Prazo Total: {{PRAZO_TOTAL}}

Investimento:
{{DESCRICAO_INVESTIMENTO}}
Valor Total: R$ {{VALOR_TOTAL}}
Condições de Pagamento: {{CONDICOES_PAGAMENTO}}

Próximos Passos:
{{PROXIMOS_PASSOS}}

Atenciosamente,

{{NOME_VENDEDOR}}
{{CARGO_VENDEDOR}}
{{CONTATO_VENDEDOR}}
```

#### 4. Contrato Padrão (Estrutura Base)

```
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

CONTRATANTE:
Nome/Razão Social: {{NOME_CONTRATANTE}}
CNPJ/CPF: {{DOC_CONTRATANTE}}
Endereço: {{ENDERECO_CONTRATANTE}}

CONTRATADA:
Nome/Razão Social: {{NOME_CONTRATADA}}
CNPJ/CPF: {{DOC_CONTRATADA}}
Endereço: {{ENDERECO_CONTRATADA}}

DO OBJETO:
{{DESCRICAO_OBJETO}}

DO PRAZO:
Início: {{DATA_INICIO}}
Término: {{DATA_TERMINO}}

DO VALOR E PAGAMENTO:
Valor Total: R$ {{VALOR_TOTAL}}
Forma de Pagamento: {{FORMA_PAGAMENTO}}

DAS OBRIGAÇÕES:
{{OBRIGACOES}}

DAS PENALIDADES:
{{PENALIDADES}}

Local e Data: {{CIDADE}}, {{DATA_ASSINATURA}}

________________________
{{NOME_CONTRATANTE}}

________________________
{{NOME_CONTRATADA}}
```

#### 5. Checklist de Processo

```
CHECKLIST - {{NOME_PROCESSO}}

Responsável: {{RESPONSAVEL}}
Data: {{DATA}}

ETAPA 1: {{NOME_ETAPA_1}}
☐ {{ITEM_1_1}}
☐ {{ITEM_1_2}}
☐ {{ITEM_1_3}}

ETAPA 2: {{NOME_ETAPA_2}}
☐ {{ITEM_2_1}}
☐ {{ITEM_2_2}}
☐ {{ITEM_2_3}}

ETAPA 3: {{NOME_ETAPA_3}}
☐ {{ITEM_3_1}}
☐ {{ITEM_3_2}}
☐ {{ITEM_3_3}}

OBSERVAÇÕES:
{{OBSERVACOES}}

APROVAÇÃO:
☐ Processo concluído
Data de conclusão: ___/___/___
Responsável: _______________
```

#### 6. Procedimento Operacional Padrão (POP)

```
PROCEDIMENTO OPERACIONAL PADRÃO

Código: {{CODIGO_POP}}
Versão: {{VERSAO}}
Data de criação: {{DATA_CRIACAO}}
Última revisão: {{DATA_REVISAO}}

Título: {{TITULO_POP}}

1. OBJETIVO
{{OBJETIVO}}

2. APLICAÇÃO
{{APLICACAO}}

3. RESPONSABILIDADES
{{RESPONSABILIDADES}}

4. PROCEDIMENTO

4.1. {{PASSO_1_TITULO}}
{{PASSO_1_DESCRICAO}}

4.2. {{PASSO_2_TITULO}}
{{PASSO_2_DESCRICAO}}

4.3. {{PASSO_3_TITULO}}
{{PASSO_3_DESCRICAO}}

5. DOCUMENTOS DE REFERÊNCIA
{{DOCUMENTOS_REFERENCIA}}

6. REGISTROS
{{REGISTROS}}

Elaborado por: {{ELABORADOR}}
Aprovado por: {{APROVADOR}}
```

#### 7. Apresentação de Resultados

```
APRESENTAÇÃO DE RESULTADOS - {{PERIODO}}

{{LOGO_EMPRESA}}

Indicadores Principais:

📈 Receita: R$ {{RECEITA}} ({{VAR_RECEITA}}% vs. mês anterior)
🎯 Meta: R$ {{META}} ({{PERC_META}}% atingido)
👥 Novos Clientes: {{NOVOS_CLIENTES}}
💰 Ticket Médio: R$ {{TICKET_MEDIO}}

Destaques do Período:

✅ {{DESTAQUE_1}}
✅ {{DESTAQUE_2}}
✅ {{DESTAQUE_3}}

Desafios:

⚠️ {{DESAFIO_1}}
⚠️ {{DESAFIO_2}}

Plano de Ação:

→ {{ACAO_1}}
→ {{ACAO_2}}
→ {{ACAO_3}}

Projeção para {{PROXIMO_PERIODO}}:
{{PROJECAO}}
```

#### 8. Email Formal de Envio

```
Assunto: {{ASSUNTO}}

Prezado(a) {{NOME_DESTINATARIO}},

{{SAUDACAO_PERSONALIZADA}}

{{CONTEXTO}}

Segue em anexo:
- {{DOCUMENTO_1}}
- {{DOCUMENTO_2}}
- {{DOCUMENTO_3}}

{{CALL_TO_ACTION}}

Prazo: {{PRAZO}}

Qualquer dúvida, estou à disposição.

Atenciosamente,

{{NOME_REMETENTE}}
{{CARGO_REMETENTE}}
{{TELEFONE_REMETENTE}}
{{EMAIL_REMETENTE}}
```

#### 9. Relatório de Incidente

```
RELATÓRIO DE INCIDENTE

ID: {{ID_INCIDENTE}}
Data/Hora: {{DATA_HORA_INCIDENTE}}
Reportado por: {{REPORTADOR}}

DESCRIÇÃO DO INCIDENTE:
{{DESCRICAO}}

IMPACTO:
Severidade: {{SEVERIDADE}} (Crítico/Alto/Médio/Baixo)
Sistemas Afetados: {{SISTEMAS_AFETADOS}}
Usuários Impactados: {{USUARIOS_IMPACTADOS}}

CAUSA RAIZ:
{{CAUSA_RAIZ}}

AÇÕES IMEDIATAS:
{{ACOES_IMEDIATAS}}

RESOLUÇÃO:
{{RESOLUCAO}}
Data/Hora de Resolução: {{DATA_HORA_RESOLUCAO}}

AÇÕES PREVENTIVAS:
{{ACOES_PREVENTIVAS}}

Responsável pela Análise: {{RESPONSAVEL_ANALISE}}
```

#### 10. Feedback de Desempenho

```
FEEDBACK DE DESEMPENHO

Colaborador: {{NOME_COLABORADOR}}
Cargo: {{CARGO}}
Período Avaliado: {{PERIODO}}
Avaliador: {{NOME_AVALIADOR}}
Data: {{DATA_AVALIACAO}}

PONTOS FORTES:

✅ {{PONTO_FORTE_1}}
✅ {{PONTO_FORTE_2}}
✅ {{PONTO_FORTE_3}}

ÁREAS DE MELHORIA:

📍 {{AREA_MELHORIA_1}}
   Sugestão: {{SUGESTAO_1}}

📍 {{AREA_MELHORIA_2}}
   Sugestão: {{SUGESTAO_2}}

METAS PARA PRÓXIMO PERÍODO:

🎯 {{META_1}}
🎯 {{META_2}}
🎯 {{META_3}}

PLANO DE DESENVOLVIMENTO:
{{PLANO_DESENVOLVIMENTO}}

Próximo Feedback: {{DATA_PROXIMO_FEEDBACK}}

________________________
Assinatura do Avaliador

________________________
Assinatura do Colaborador
```

### Como Criar Seus Próprios Templates

**Passo 1: Identifique documentos repetitivos** (1 semana observando)
- Quais documentos você cria mais de 1x por mês?
- Anote modelo e frequência

**Passo 2: Extraia estrutura comum** (30min por template)
- Abra 3-5 versões antigas do mesmo tipo de documento
- Destaque o que SEMPRE repete
- Destaque o que VARIA (serão suas variáveis)

**Passo 3: Crie template genérico** (20min)
- Google Docs novo
- Cole estrutura comum
- Substitua partes variáveis por {{NOME_VARIAVEL}}
- Use nomes descritivos: {{VALOR_TOTAL}} não {{X}}

**Passo 4: Teste** (10min)
- Faça uma cópia
- Preencha variáveis manualmente (Ctrl+H)
- Veja se ficou bom
- Ajuste formatação

**Passo 5: Automatize (opcional mas recomendado)** (1-2h - uma vez só)
- Use Apps Script (código acima)
- Conecte com Google Sheets (dados ficam lá)
- Crie botão "Gerar Documento"

---

## 3. IA para Gerar Documentos (Seu Escritor Profissional 24/7)

### O Poder da IA para Documentação

**Cenário real:** Você precisa criar manual de procedimento de 10 páginas para novo processo.

**Antigamente:**
- 4-6 horas escrevendo
- Mais 2 horas formatando
- Mais 1 hora revisando
- Total: **7-9 horas**

**Com IA:**
- 5 minutos descrevendo processo para IA
- 30 segundos gerando documento
- 20 minutos revisando e ajustando
- Total: **25-30 minutos**

**Economia: 6-8 horas** (quase 1 dia de trabalho!).

### Estrutura de Prompt para Documentos

```
Tipo de documento: [Relatório/Manual/Procedimento/Apresentação/etc]
Público-alvo: [Quem vai ler? Técnico? Executivo? Cliente?]
Objetivo: [Informar/Convencer/Instruir/Documentar]
Tom: [Formal/Técnico/Acessível/Persuasivo]
Tamanho: [Número de páginas ou palavras]
Estrutura desejada: [Tópicos principais]
Informações-chave: [Dados específicos a incluir]
Formato de saída: [Markdown/Google Docs/Lista/Prosa]
```

### 10 Prompts para Diferentes Tipos de Documentos

#### 1. Relatório Executivo

```
Tipo: Relatório Executivo
Público: Diretoria
Objetivo: Apresentar resultados do trimestre e solicitar aprovação de budget
Tom: Formal, objetivo, baseado em dados
Tamanho: 2-3 páginas
Estrutura:
1. Resumo Executivo (5 linhas)
2. Principais Métricas (bullet points com números)
3. Destaques Positivos
4. Desafios Enfrentados
5. Solicitação de Budget (R$ 50.000 para expansão)
6. Próximos Passos

Informações:
- Receita trimestre: R$ 1.2M (+15% vs trim anterior)
- Novos clientes: 23
- Churn: 3%
- NPS: 78
- Budget solicitado para: contratar 2 vendedores + campanha marketing

Gere o relatório completo em português, pronto para apresentar.
```

#### 2. Manual de Processo

```
Tipo: Manual de Procedimento Operacional
Público: Equipe operacional (nível técnico médio)
Objetivo: Instruir passo a passo como realizar processo de onboarding de cliente
Tom: Claro, didático, objetivo
Tamanho: 4-5 páginas
Estrutura:
1. Objetivo do Procedimento
2. Pré-requisitos
3. Materiais Necessários
4. Passo a Passo Detalhado (mínimo 10 passos)
5. Pontos de Atenção / Cuidados
6. O Que Fazer em Caso de Erro
7. Checklist de Validação

Contexto:
Onboarding inclui: criação de conta, envio de documentos, configuração de acesso, treinamento inicial.

Gere manual completo, detalhado e prático.
```

#### 3. Procedimento Operacional Padrão (POP)

```
Tipo: Procedimento Operacional Padrão (POP)
Público: Operadores de produção
Objetivo: Padronizar processo de controle de qualidade
Tom: Técnico, normativo, preciso
Tamanho: 3 páginas
Estrutura (formato POP oficial):
1. Objetivo
2. Aplicação
3. Documentos de Referência
4. Definições
5. Responsabilidades
6. Procedimento (descritivo + fluxograma em texto)
7. Registros
8. Anexos

Processo: Inspeção visual de peças metálicas (3 pontos de verificação: dimensão, acabamento, marcação)

Gere POP profissional seguindo normas ISO se possível.
```

#### 4. Análise de Dados

```
Tipo: Análise de Dados
Público: Gerência
Objetivo: Analisar queda de 12% nas vendas de outubro e propor ações
Tom: Analítico, propositivo
Tamanho: 2 páginas
Estrutura:
1. Contexto e Problema
2. Dados Analisados (apresentar números)
3. Principais Hipóteses (mínimo 4)
4. Análise Detalhada de Cada Hipótese
5. Conclusões
6. Recomendações de Ação (pelo menos 5 ações concretas)

Dados:
- Vendas set: R$ 450k
- Vendas out: R$ 396k (-12%)
- Tráfego site: -5%
- Taxa conversão: -8%
- Ticket médio: +2%
- Principais produtos afetados: Categoria Premium (-25%)
- Categoria Econômica cresceu +5%

Gere análise profissional com insights acionáveis.
```

#### 5. Apresentação de Resultados

```
Tipo: Apresentação em Slides (roteiro)
Público: Time comercial
Objetivo: Motivar equipe mostrando resultados + lançar desafio do próximo mês
Tom: Inspirador, energético, celebratório
Tamanho: 10-12 slides
Estrutura:
Slide 1: Título + Frase de Impacto
Slides 2-3: Números do Mês (grandes, visuais)
Slide 4: Ranking de Vendedores (Top 3)
Slide 5: Cases de Sucesso
Slide 6: Lições Aprendidas
Slide 7: Desafios do Próximo Mês
Slides 8-9: Plano de Ação
Slide 10: Meta do Mês (grande, ousada)
Slide 11-12: Mensagem Motivacional + Agradecimento

Dados:
- Vendas totais: R$ 580k (superamos meta de R$ 500k!)
- Top vendedor: João - R$ 95k
- Maior contrato fechado: R$ 120k (Cliente XPTO)
- Meta próximo mês: R$ 650k

Gere roteiro completo com texto sugerido para cada slide.
```

#### 6. Resumo Executivo

```
Tipo: Resumo Executivo
Público: CEO
Objetivo: Resumir documento técnico de 40 páginas em 1 página
Tom: Muito objetivo, estratégico
Tamanho: Máximo 1 página (300 palavras)
Estrutura:
- Contexto (2 linhas)
- Principal Conclusão (destaque)
- 3-4 Pontos Críticos
- Recomendação Final (clara e direta)

Documento original:
[Cole aqui trecho ou principais pontos do documento longo]

Gere resumo executivo que CEO possa ler em 2 minutos e tomar decisão.
```

#### 7. Ata de Reunião

```
Tipo: Ata de Reunião
Público: Participantes + gestores
Objetivo: Documentar decisões e ações da reunião
Tom: Objetivo, factual
Tamanho: 1-2 páginas
Estrutura:
- Cabeçalho (data, hora, local, participantes)
- Pauta discutida
- Resumo das discussões (bullet points)
- Decisões tomadas (destacar)
- Ações definidas (responsável + prazo para cada)
- Data da próxima reunião

Notas da reunião (podem ser bagunçadas):
[Cole aqui suas anotações/transcrição da reunião]

Gere ata formal e organizada.
```

#### 8. Proposta de Projeto

```
Tipo: Proposta de Projeto
Público: Cliente potencial (Diretor de TI)
Objetivo: Convencer a contratar nosso serviço de consultoria
Tom: Profissional, consultivo, baseado em valor
Tamanho: 5-7 páginas
Estrutura:
1. Sobre Nós (credibilidade)
2. Entendimento do Desafio do Cliente
3. Nossa Proposta de Solução
4. Metodologia de Trabalho
5. Entregas Detalhadas
6. Timeline
7. Investimento (valor + ROI esperado)
8. Diferenciais
9. Cases de Sucesso Similares
10. Próximos Passos

Cliente:
- Empresa: Indústria de médio porte, 200 funcionários
- Problema: Sistema legado travando crescimento
- Budget estimado: R$ 80-120k

Gere proposta persuasiva e profissional.
```

#### 9. Comunicado Interno

```
Tipo: Comunicado Interno
Público: Todos colaboradores
Objetivo: Anunciar mudança de horário de funcionamento
Tom: Institucional mas acessível, transparente
Tamanho: 1 página
Estrutura:
1. Título chamativo
2. O que vai mudar
3. Por que estamos mudando (razões claras)
4. Quando entra em vigor
5. Como funciona na prática
6. Exceções / Casos especiais
7. A quem recorrer em caso de dúvida
8. Agradecimento

Mudança:
- Horário atual: 8h-17h
- Novo horário: 9h-18h
- Motivo: Pesquisa interna mostrou que 75% prefere + alinhamento com horário de clientes
- Início: 01/12

Gere comunicado claro que minimize resistências.
```

#### 10. Documento Técnico

```
Tipo: Documentação Técnica
Público: Desenvolvedores
Objetivo: Documentar API REST
Tom: Técnico, preciso, completo
Tamanho: 3-4 páginas
Estrutura:
1. Visão Geral da API
2. Autenticação
3. Endpoints (para cada: método, URL, parâmetros, exemplo request, exemplo response)
4. Códigos de Erro
5. Rate Limiting
6. Exemplos de Uso (código)
7. FAQs

API:
- RESTful
- Autenticação via Bearer Token
- 5 endpoints principais: listar usuários, criar usuário, atualizar, deletar, buscar por ID
- Retorna JSON

Gere documentação completa estilo Swagger/OpenAPI.
```

### Como Refinar Documentos Gerados por IA

**Checklist pós-geração:**

1. **Leia criticamente**
   - IA inventou dados? (remova ou substitua)
   - Tom está adequado?
   - Linguagem natural ou robótica?

2. **Personalize**
   - Adicione exemplos específicos da sua empresa
   - Ajuste nomes, valores, datas
   - Inclua jargões/termos internos

3. **Formate**
   - Aplique template visual da empresa
   - Adicione logo, cores corporativas
   - Ajuste fontes e tamanhos

4. **Valide tecnicamente**
   - Peça para colega revisar
   - Confira números e datas
   - Teste instruções (em caso de manuais)

5. **Aprimore prompt**
   - Anote o que ficou faltando
   - Melhore prompt para próxima vez
   - Crie biblioteca de prompts testados

---

## 4. Automação de Relatórios (100% no Piloto Automático)

### O Santo Graal: Relatório Que Se Faz Sozinho

**Cenário ideal:**
- Segunda-feira, 8h da manhã
- Você abre email
- Tem relatório semanal completo, formatado, com todos os dados atualizados
- Você NÃO FEZ NADA

**Não é sonho. É totalmente possível com:**
- Google Sheets (dados)
- Google Docs (template)
- Apps Script (automação)
- Zapier (orquestração - opcional)

### Arquitetura de Relatório Automático

**Componentes:**

1. **Fonte de Dados** (Google Sheets)
   - Dados atualizados automaticamente (via IMPORTRANGE, API, Zapier, etc.)

2. **Template de Documento** (Google Docs)
   - Estrutura pronta com {{VARIÁVEIS}}

3. **Script de Geração** (Apps Script)
   - Busca dados do Sheets
   - Preenche template
   - Gera documento final

4. **Agendamento** (Trigger do Apps Script)
   - Roda automaticamente (ex: toda segunda, 7h)

5. **Distribuição** (Apps Script + Gmail)
   - Envia por email automaticamente

### Tutorial Completo: Relatório Semanal 100% Automático

#### Passo 1: Preparar Planilha de Dados

**Estrutura sugerida (aba "Dados"):**

| Semana | Vendas | Meta | % Meta | Novos Clientes | Observações |
|--------|--------|------|--------|----------------|-------------|
| 47     | 45000  | 50000| 90%    | 5              | Boa semana  |

**Dados podem vir de:**
- IMPORTRANGE de outras planilhas
- Zapier (de CRM, e-commerce, etc.)
- Apps Script (de API externa)

#### Passo 2: Criar Template no Docs

```
RELATÓRIO SEMANAL - SEMANA {{SEMANA}}

📊 NÚMEROS DA SEMANA

Vendas: R$ {{VENDAS}}
Meta: R$ {{META}}
Atingimento: {{PERCENTUAL}}%

Novos Clientes: {{NOVOS_CLIENTES}}

💬 OBSERVAÇÕES

{{OBSERVACOES}}

---
Relatório gerado automaticamente em {{DATA_GERACAO}}
```

Salve e copie o ID da URL.

#### Passo 3: Script de Geração

No Google Sheets, vá em **Extensões → Apps Script** e cole:

```javascript
function gerarRelatorioSemanal() {
  // IDs (substitua pelos seus)
  var TEMPLATE_ID = "SEU_TEMPLATE_ID_AQUI";
  var PASTA_DESTINO_ID = "ID_DA_PASTA_ONDE_SALVAR";

  // 1. Buscar dados da última semana
  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var aba = planilha.getSheetByName("Dados");
  var ultimaLinha = aba.getLastRow();
  var dados = aba.getRange(ultimaLinha, 1, 1, 6).getValues()[0];

  // 2. Fazer cópia do template
  var template = DriveApp.getFileById(TEMPLATE_ID);
  var semana = dados[0];
  var nomeArquivo = "Relatório Semanal - Semana " + semana;
  var pastaDestino = DriveApp.getFolderById(PASTA_DESTINO_ID);
  var novoDoc = template.makeCopy(nomeArquivo, pastaDestino);

  // 3. Abrir documento e substituir variáveis
  var doc = DocumentApp.openById(novoDoc.getId());
  var corpo = doc.getBody();

  corpo.replaceText("{{SEMANA}}", semana);
  corpo.replaceText("{{VENDAS}}", "R$ " + dados[1].toLocaleString('pt-BR'));
  corpo.replaceText("{{META}}", "R$ " + dados[2].toLocaleString('pt-BR'));
  corpo.replaceText("{{PERCENTUAL}}", dados[3]);
  corpo.replaceText("{{NOVOS_CLIENTES}}", dados[4]);
  corpo.replaceText("{{OBSERVACOES}}", dados[5]);
  corpo.replaceText("{{DATA_GERACAO}}", new Date().toLocaleDateString('pt-BR'));

  // 4. Salvar
  doc.saveAndClose();

  // 5. Enviar por email
  enviarPorEmail(novoDoc.getUrl(), semana);

  Logger.log("Relatório gerado: " + novoDoc.getUrl());
}

function enviarPorEmail(linkRelatorio, semana) {
  var destinatarios = "chefe@empresa.com, equipe@empresa.com"; // Ajuste

  var assunto = "📊 Relatório Semanal - Semana " + semana;

  var corpo = "Olá,<br><br>" +
              "Segue relatório semanal atualizado:<br><br>" +
              "<a href='" + linkRelatorio + "'>📄 Clique aqui para visualizar</a><br><br>" +
              "Qualquer dúvida, estou à disposição.<br><br>" +
              "Atenciosamente,<br>" +
              "Sistema Automático";

  MailApp.sendEmail({
    to: destinatarios,
    subject: assunto,
    htmlBody: corpo
  });
}
```

#### Passo 4: Agendar Execução Automática

1. No Apps Script, clique no ícone do **Relógio** (Acionadores)
2. "Adicionar acionador"
3. Configurar:
   - Função: `gerarRelatorioSemanal`
   - Origem do evento: **Acionado por tempo**
   - Tipo: **Acionador de timer semanal**
   - Dia da semana: **Segunda-feira**
   - Hora do dia: **7h às 8h**
4. Salvar

**Pronto!** Agora toda segunda-feira, entre 7h-8h:
1. Script busca dados da semana
2. Gera relatório preenchido
3. Salva no Drive
4. Envia por email para equipe

**Você não faz NADA. Automático pra sempre.**

### Mais Exemplos de Relatórios Automáticos

**1. Relatório de Vendas Diário**
- Trigger: Todo dia, 18h
- Dados: Vendas do dia (de CRM ou e-commerce)
- Envia: Para gerente comercial

**2. Resumo Mensal Executivo**
- Trigger: Dia 1 de cada mês, 8h
- Dados: Consolidado do mês anterior
- Envia: Para diretoria

**3. Status de Projetos (Semanal)**
- Trigger: Sexta-feira, 16h
- Dados: Tarefas concluídas/pendentes (de Trello/Asana via Zapier)
- Envia: Para gerente de projetos

---

## 5. Organização e Versionamento (Nunca Mais "final_v9_AGORA_VAI_MESMO.docx")

### O Caos dos Arquivos

**Cenário real que você já viveu:**

```
Pasta "Propostas Cliente XPTO":
- Proposta_XPTO.docx
- Proposta_XPTO_v2.docx
- Proposta_XPTO_final.docx
- Proposta_XPTO_final_revisado.docx
- Proposta_XPTO_final_APROVADA.docx
- Proposta_XPTO_final_APROVADA_ajustes.docx
- Proposta_XPTO_ESSA_É_A_BOA.docx
```

**E você não lembra qual é a versão certa.**

### Regras de Ouro de Nomenclatura

**Formato padrão:**
```
TIPO_Cliente-Projeto_YYYY-MM-DD_Versao.extensao
```

**Exemplos:**
```
Proposta_ACME-SitNovo_2024-11-15_v1.docx
Contrato_XYZ-Consultoria_2024-11-20_Final.pdf
Relatorio_VendasNovembro_2024-12-01_v3.docx
```

**Componentes:**
1. **TIPO:** Proposta, Contrato, Relatório, Apresentação, etc.
2. **Cliente/Projeto:** Nome curto e claro
3. **Data:** Formato YYYY-MM-DD (ordena cronologicamente automaticamente)
4. **Versão:** v1, v2, v3 ou Final, Revisao, Aprovado
5. **Extensão:** .docx, .pdf, .pptx

**Vantagens:**
- Ordem cronológica automática
- Fácil identificar tipo e cliente
- Versão clara

### Google Drive: Organização Automática

#### Estrutura de Pastas Recomendada

```
📁 Drive da Empresa
├── 📁 01_Clientes
│   ├── 📁 Cliente_ACME
│   │   ├── 📁 Propostas
│   │   ├── 📁 Contratos
│   │   ├── 📁 Projetos
│   │   └── 📁 Comunicação
│   └── 📁 Cliente_XYZ
├── 📁 02_Projetos
│   ├── 📁 Projeto_Alpha
│   └── 📁 Projeto_Beta
├── 📁 03_Operacional
│   ├── 📁 Relatórios
│   ├── 📁 Procedimentos
│   └── 📁 Templates
├── 📁 04_Administrativo
└── 📁 05_Arquivados
```

**Dicas:**
- Prefixos numéricos mantêm ordem
- Máximo 3 níveis de profundidade
- Nomes curtos e claros
- Pasta "Arquivados" para projetos finalizados

#### Automatizar Organização com Apps Script

**Exemplo: Mover arquivos automaticamente**

```javascript
function organizarArquivosPorTipo() {
  var pastaOrigem = DriveApp.getFolderById("ID_PASTA_BAGUNÇADA");
  var pastaPropostas = DriveApp.getFolderById("ID_PASTA_PROPOSTAS");
  var pastaRelatorios = DriveApp.getFolderById("ID_PASTA_RELATORIOS");

  var arquivos = pastaOrigem.getFiles();

  while (arquivos.hasNext()) {
    var arquivo = arquivos.next();
    var nome = arquivo.getName();

    // Mover propostas
    if (nome.indexOf("Proposta") > -1) {
      arquivo.moveTo(pastaPropostas);
    }

    // Mover relatórios
    if (nome.indexOf("Relatorio") > -1 || nome.indexOf("Relatório") > -1) {
      arquivo.moveTo(pastaRelatorios);
    }
  }
}
```

**Configure para rodar 1x por dia e mantém Drive sempre organizado.**

### Versionamento Nativo do Google Docs

**Vantagem:** Google Docs/Sheets salva TODAS as versões automaticamente.

**Como acessar:**
1. Arquivo → Histórico de versões → Ver histórico de versões
2. Veja todas alterações com data/hora/autor
3. Restaure versão antiga com 1 clique

**Nunca mais precisa de "v2", "v3", "final"** → Sempre edita o mesmo arquivo, Google guarda histórico.

**Nomear versões importantes:**
1. Arquivo → Histórico de versões
2. Clique nos 3 pontinhos ao lado de versão
3. "Nomear esta versão": Ex: "Aprovado pelo Cliente"

### Backup Automático

**Google Drive JÁ FAZ backup**, mas para segurança extra:

**Opção 1: Google Takeout (Backup manual periódico)**
1. takeout.google.com
2. Selecione "Drive"
3. Baixe ZIP com tudo

**Opção 2: Apps Script (Backup seletivo)**

```javascript
function backupPastaImportante() {
  var pastaOrigem = DriveApp.getFolderById("ID_PASTA_IMPORTANTE");
  var pastaBackup = DriveApp.getFolderById("ID_PASTA_BACKUP");

  var arquivos = pastaOrigem.getFiles();
  var dataBackup = new Date().toLocaleDateString('pt-BR').replace(/\//g, '-');

  while (arquivos.hasNext()) {
    var arquivo = arquivos.next();
    var nomeCopia = "[BACKUP_" + dataBackup + "] " + arquivo.getName();
    arquivo.makeCopy(nomeCopia, pastaBackup);
  }
}
```

**Configure para rodar semanalmente.**

### Compartilhamento Inteligente

**Níveis de permissão:**
- **Visualizador:** Só vê (clientes externos)
- **Comentador:** Vê + comenta (revisores)
- **Editor:** Edita (equipe interna)

**Compartilhar com link:**
- Botão "Compartilhar" → "Obter link"
- Escolha permissão
- Copie link

**Automatizar compartilhamento via Script:**

```javascript
function compartilharComCliente(arquivoId, emailCliente) {
  var arquivo = DriveApp.getFileById(arquivoId);
  arquivo.addViewer(emailCliente);

  // Enviar email notificando
  var link = arquivo.getUrl();
  MailApp.sendEmail({
    to: emailCliente,
    subject: "Documento Compartilhado",
    body: "Olá, segue documento: " + link
  });
}
```

---

## 6. Apresentações Automatizadas (Slides que Se Fazem Sozinhos)

### Google Slides + Dados Dinâmicos

**Conceito:** Apresentação conectada a planilha → Números se atualizam automaticamente.

**Como fazer (manualmente):**
1. Crie apresentação
2. Insira → Gráfico → "De Planilhas"
3. Selecione Google Sheets
4. Escolha intervalo
5. Insere gráfico vinculado

**Quando dados mudarem na planilha:**
- Abra apresentação
- Clique no gráfico
- "Atualizar" → Pronto!

**Automatizar atualização via Apps Script:**

```javascript
function atualizarGraficosSlides() {
  var apresentacaoId = "ID_DA_SUA_APRESENTACAO";
  var apresentacao = SlidesApp.openById(apresentacaoId);
  var slides = apresentacao.getSlides();

  slides.forEach(function(slide) {
    var graficos = slide.getSheetsCharts();
    graficos.forEach(function(grafico) {
      grafico.refresh(); // Atualiza gráfico
    });
  });
}
```

**Configure para rodar antes de apresentações importantes.**

### Templates Reutilizáveis

**Crie biblioteca de slides padrão:**

- Slide de Capa
- Slide de Agenda
- Slide de Números (2 métricas)
- Slide de Números (4 métricas)
- Slide de Gráfico Grande
- Slide de Tabela
- Slide de Citação
- Slide de Agradecimento

**Mantenha em apresentação "Master Template" e copie quando precisar.**

### Gerar Slides com IA (Apps Script + OpenAI API)

**Script avançado (exemplo conceitual):**

```javascript
function gerarApresentacaoComIA(tema, slides) {
  // 1. Gerar roteiro com ChatGPT
  var prompt = "Crie roteiro de apresentação sobre: " + tema + ". " + slides + " slides.";
  var roteiro = chamarChatGPT(prompt); // Função que chama API OpenAI

  // 2. Criar apresentação em branco
  var apresentacao = SlidesApp.create("Apresentação - " + tema);

  // 3. Para cada slide do roteiro, criar slide real
  // (parsear resposta da IA e criar slides)

  // 4. Retornar link
  return apresentacao.getUrl();
}

function chamarChatGPT(prompt) {
  var apiKey = "SUA_API_KEY_OPENAI";
  var url = "https://api.openai.com/v1/chat/completions";

  var payload = {
    model: "gpt-4",
    messages: [{role: "user", content: prompt}]
  };

  var options = {
    method: "post",
    headers: {"Authorization": "Bearer " + apiKey},
    contentType: "application/json",
    payload: JSON.stringify(payload)
  };

  var response = UrlFetchApp.fetch(url, options);
  var json = JSON.parse(response.getContentText());
  return json.choices[0].message.content;
}
```

---

## 7. Exercícios Práticos (Implemente HOJE!)

### Exercício 1: Criar 3 Templates (60 minutos)

**Tarefa:** Identifique 3 documentos que você cria repetidamente e crie templates.

**Sugestões:**
1. Relatório semanal/mensal
2. Ata de reunião
3. Email padrão de envio

**Passo a passo:**
1. Escolha os 3 tipos
2. Para cada um:
   - Abra 2-3 versões antigas
   - Identifique estrutura comum
   - Crie Google Doc com {{VARIÁVEIS}}
   - Salve na pasta "Templates"
   - Nomeie: "TEMPLATE - [tipo]"

**Checklist:**
- [ ] 3 templates criados
- [ ] Salvos em pasta organizada
- [ ] Testou usar 1 deles

### Exercício 2: Automatizar 1 Relatório (90 minutos)

**Tarefa:** Escolha 1 relatório que você faz toda semana/mês e automatize.

**Passo a passo:**
1. Crie planilha com dados necessários
2. Crie template do relatório em Docs
3. Copie script de geração (adapte do exemplo acima)
4. Teste rodar manualmente
5. (Opcional) Configure trigger para rodar automaticamente

**Checklist:**
- [ ] Planilha de dados criada
- [ ] Template pronto
- [ ] Script funcionando
- [ ] Testado geração de 1 relatório

### Exercício 3: Gerar 1 Documento com IA (30 minutos)

**Tarefa:** Use ChatGPT para gerar um documento completo.

**Opções:**
- Manual de procedimento
- Análise de dados
- Proposta
- Apresentação (roteiro)

**Passo a passo:**
1. Escolha tipo de documento
2. Escreva prompt detalhado (use templates acima)
3. Gere no ChatGPT
4. Copie para Google Docs
5. Revise e ajuste
6. Formate

**Checklist:**
- [ ] Documento gerado
- [ ] Revisado e personalizado
- [ ] Formatado profissionalmente
- [ ] Comparado tempo gasto vs. fazer manual

---

## 8. Dicas Avançadas de Produtividade em Documentação

### Atalhos Essenciais do Google Docs (Economize Horas)

**Navegação:**
- `Ctrl + Alt + N/P` - Próximo/Anterior comentário
- `Ctrl + Alt + M` - Inserir comentário
- `Ctrl + Alt + Shift + H` - Ver histórico de revisões
- `Ctrl + F` - Buscar texto
- `Ctrl + H` - Buscar e substituir

**Formatação rápida:**
- `Ctrl + Alt + 1/2/3` - Título 1, 2, 3
- `Ctrl + Alt + 0` - Texto normal
- `Ctrl + B/I/U` - Negrito/Itálico/Sublinhado
- `Ctrl + K` - Inserir link
- `Ctrl + Shift + V` - Colar sem formatação

**Produtividade:**
- `Ctrl + /` - Buscar nos menus (super útil!)
- `Ctrl + Alt + C` - Contar palavras
- `Ctrl + Enter` - Quebra de página
- `@` - Mencionar pessoa ou inserir item especial

**Truque ninja: Comandos de voz (Chrome)**
1. Ferramentas → Digitação por voz
2. Fale em português
3. Comandos: "Novo parágrafo", "Ponto", "Vírgula", "Selecionar tudo"

**Resultado:** Ditar documento 3x mais rápido que digitar.

### Uso de Variáveis e Macros no Google Docs

Embora Google Docs não tenha macros VBA como Excel, você pode criar "pseudo-variáveis" com Building Blocks (blocos de construção).

**Método 1: Blocos Reutilizáveis**

1. Escreva trecho que usa muito (assinatura, rodapé, seção padrão)
2. Selecione o texto
3. Ferramentas → Blocos de construção → Salvar como bloco
4. Dê um nome (ex: "assinatura_padrao")

**Para usar:**
1. Digite `@` no documento
2. Comece a digitar o nome do bloco
3. Selecione e insere automaticamente

**Exemplo de uso:**
- Assinatura de email
- Rodapé com disclaimer legal
- Seções padrão de relatórios

### Colaboração Inteligente: Comentários e Sugestões

**Tipos de edição:**

1. **Modo Edição (padrão):** Altera direto
2. **Modo Sugestão:** Mudanças ficam como propostas
3. **Modo Visualização:** Só lê

**Para trocar:** Botão no canto superior direito (lápis/caneta)

**Melhores práticas de colaboração:**

**Para revisor:**
- Use modo Sugestão para mudanças estruturais
- Use Comentários para dúvidas/discussões
- Mencione pessoa (@nome) para notificar

**Para autor:**
- Aceite/Rejeite sugestões (não deixe acumular)
- Responda comentários
- Resolva discussões quando concluídas

**Atalho para aceitar todas sugestões:**
1. Ferramentas → Revisar sugestões
2. Use setas ou `J/K` para navegar
3. `A` aceita, `R` rejeita

**Histórico de versões:**
- Arquivo → Histórico de versões → Ver histórico
- Restaure versões antigas com 1 clique
- Nomeie versões importantes: "Aprovado pelo cliente"

### Automatização com Add-ons Úteis

**1. Autocomplete (autocorretor inteligente)**
- Corrige erros comuns automaticamente
- Aprende com seu estilo de escrita

**2. Remove Line Breaks**
- Remove quebras de linha extras ao colar texto
- Útil quando copia de PDF

**3. Doc Tools**
- Encontrar e substituir avançado (suporta regex)
- Capitalizar textos
- Remover espaços extras

**4. Table Formatter**
- Formata tabelas automaticamente
- Aplica estilos consistentes

**Como instalar:**
1. Extensões → Complementos → Obter complementos
2. Busque pelo nome
3. Instale
4. Use pelo menu Extensões

### Geração de Sumário Automático

**Para documentos longos (> 5 páginas):**

**Passo 1: Use estilos de título corretamente**
- Título 1 para capítulos principais
- Título 2 para seções
- Título 3 para subseções

**Passo 2: Inserir sumário**
1. Clique onde quer o sumário
2. Inserir → Sumário
3. Escolha estilo (com links ou com números de página)

**Vantagem:** Sumário atualiza automaticamente quando você:
- Adiciona/remove seções
- Renomeia títulos
- Reorganiza documento

**Para atualizar:** Clique no sumário → Atualizar

### Campos Dinâmicos (Datas, Número de Páginas, etc.)

**Inserir data que atualiza automaticamente:**
1. Inserir → Data e hora
2. Escolha se quer que atualize sempre ou fique fixa

**Inserir número de páginas:**
1. Inserir → Número de páginas → Contagem de páginas
2. Ou: `Inserir → Cabeçalhos e rodapés → Número da página`

**Campos úteis:**
- Contagem de palavras (atualiza automaticamente)
- Número de página atual / total de páginas
- Título do documento (se mudar título, atualiza em todos lugares)

**Exemplo de rodapé profissional:**
```
[Nome Empresa] | Confidencial | Página [X] de [Y] | Atualizado em [DD/MM/AAAA]
```

Insira os campos automaticamente:
- Nome Empresa: digite manualmente
- "Página X de Y": Inserir → Número de páginas
- Data: Inserir → Data

### Conversão e Exportação Inteligente

**Exportar para PDF com opções:**

**Método 1: Básico**
- Arquivo → Download → PDF

**Método 2: Avançado (Apps Script para múltiplos documentos)**

```javascript
function exportarParaPDF() {
  var doc = DocumentApp.getActiveDocument();
  var docId = doc.getId();
  var nome = doc.getName();

  var pdf = DriveApp.getFileById(docId).getAs('application/pdf');
  pdf.setName(nome + "_" + new Date().toLocaleDateString('pt-BR') + ".pdf");

  // Salvar em pasta específica
  var pasta = DriveApp.getFolderById("ID_DA_PASTA_PDF");
  pasta.createFile(pdf);
}
```

**Exportar para Word (.docx):**
- Arquivo → Download → Microsoft Word

**Dica:** Para manter formatação, exporte via Google Docs. Para editar no Word, exporte .docx.

### Modelos de Documentos por Tipo de Projeto

**Modelo 1: Relatório Técnico (Projetos de TI/Engenharia)**

```
Capa:
- Logo
- Título do Projeto
- Versão
- Data
- Autor

Sumário (automático)

1. Resumo Executivo
2. Introdução
   2.1 Contexto
   2.2 Objetivos
3. Metodologia
4. Resultados
   4.1 Análise
   4.2 Descobertas
5. Conclusões
6. Recomendações
7. Anexos
```

**Modelo 2: Manual de Usuário**

```
Capa + Sumário

1. Visão Geral
   - O que é o sistema
   - Para quem é
2. Primeiros Passos
   - Como acessar
   - Login
3. Funcionalidades Principais
   (1 seção por funcionalidade)
   - O que faz
   - Como usar (passo a passo)
   - Capturas de tela
   - Dicas
4. Solução de Problemas (FAQ)
5. Contato para Suporte
```

**Modelo 3: Documentação de API**

```
1. Introdução
2. Autenticação
3. Endpoints
   Para cada endpoint:
   - Nome e descrição
   - Método HTTP (GET/POST/etc)
   - URL
   - Parâmetros
   - Exemplo de Request
   - Exemplo de Response
   - Códigos de erro possíveis
4. Rate Limiting
5. Changelog (histórico de versões)
```

### Checklist de Qualidade para Documentos

**Antes de enviar qualquer documento importante, verifique:**

**Conteúdo:**
- [ ] Todas informações estão corretas e atualizadas?
- [ ] Números/datas conferidos?
- [ ] Nomes de pessoas/empresas corretos?
- [ ] Links funcionando?
- [ ] Anexos incluídos (se mencionados)?

**Formatação:**
- [ ] Fonte consistente (recomendado: Arial 11 ou Calibri 11)
- [ ] Margens adequadas (2.5cm sugerido)
- [ ] Espaçamento entre linhas (1.15 ou 1.5)
- [ ] Títulos formatados como Título 1/2/3 (não só negrito)
- [ ] Alinhamento correto (justificado para textos longos)

**Elementos visuais:**
- [ ] Logo da empresa (se documento externo)
- [ ] Cabeçalho/Rodapé (com data, nº página)
- [ ] Sumário (se > 5 páginas)
- [ ] Tabelas formatadas consistentemente
- [ ] Imagens com qualidade adequada

**Revisão:**
- [ ] Corretor ortográfico rodado
- [ ] Lido em voz alta (pega erros que leitura silenciosa não pega)
- [ ] Segunda pessoa revisou (se documento importante)
- [ ] Versão final salva com nomenclatura correta

**Distribuição:**
- [ ] Formato certo (PDF para externos, Google Docs para internos colaborativos)
- [ ] Permissões de acesso configuradas
- [ ] Email de envio revisado
- [ ] Destinatários confirmados

### Integração com Outras Ferramentas

**Google Docs + Slack:**

Apps Script para notificar Slack quando documento é atualizado:

```javascript
function notificarSlack() {
  var doc = DocumentApp.getActiveDocument();
  var url = doc.getUrl();
  var nome = doc.getName();

  var webhookUrl = "SUA_WEBHOOK_URL_DO_SLACK";

  var payload = {
    "text": "📄 Documento atualizado: " + nome + "\n" + url
  };

  UrlFetchApp.fetch(webhookUrl, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload)
  });
}
```

**Google Docs + Trello:**

Criar card no Trello quando documento é criado:

Via Zapier:
- Trigger: Google Docs - "New Document in Folder"
- Action: Trello - "Create Card"

**Google Docs + Notion:**

Copiar documento do Docs para Notion (via Zapier ou Make):
- Útil para centralizar documentação

**Google Docs + Google Calendar:**

Incluir link de documento em eventos do Calendar (para atas de reunião):

```javascript
function criarEventoComDoc() {
  var doc = DocumentApp.getActiveDocument();
  var docUrl = doc.getUrl();

  var evento = CalendarApp.getDefaultCalendar().createEvent(
    'Reunião Semanal',
    new Date('December 15, 2024 10:00:00'),
    new Date('December 15, 2024 11:00:00'),
    {description: 'Ata: ' + docUrl}
  );
}
```

---

## RESUMO DO MÓDULO: O Que Você Aprendeu

✅ **O problema da documentação manual:** 4-6h/semana desperdiçadas
✅ **Templates inteligentes:** 10 modelos prontos + como criar seus
✅ **IA para documentos:** 10 prompts para diferentes tipos
✅ **Automação de relatórios:** Sistema 100% automático
✅ **Organização de arquivos:** Nomenclatura + estrutura + versionamento
✅ **Apresentações automatizadas:** Slides conectados a dados
✅ **Exercícios práticos:** 3 implementações reais

---

## RESULTADO ESPERADO

**Antes:**
- ⏱ 4-6 horas/semana em documentação
- 😫 Copiar/colar dados manualmente
- 📝 Erros e inconsistências
- 🗂 Drive bagunçado

**Depois:**
- ⏱ 30min-1h/semana (só revisão)
- 🤖 Relatórios automáticos
- ✅ Documentos padronizados e precisos
- 📁 Tudo organizado e encontrável

**Economia:** **3-5 horas por semana = Meio dia de trabalho!**

---

## PRÓXIMO PASSO

**Parabéns!** Você completou os 3 módulos centrais da **Trilha Operacional Produtivo**:

✅ Módulo 5: Emails automatizados (7-8h economizadas/semana)
✅ Módulo 6: Planilhas inteligentes (3-5h economizadas/semana)
✅ Módulo 7: Documentação automática (3-5h economizadas/semana)

**Total potencial: 13-18 horas economizadas por semana!**

Isso é **quase meio mês de trabalho por ano** recuperado.

Continue implementando, automatizando e otimizando. Seu futuro eu agradece!

---

**© 2025 FETD - Formação em Engenharia de Intenção**
