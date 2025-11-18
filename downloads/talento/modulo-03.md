# Módulo 3: Primeiras Ferramentas de IA

**Trilha:** Talento Emergente
**Duração:** 60 minutos
**Objetivo:** Dominar ChatGPT, Claude e Gemini para trabalho profissional

---

## Introdução: A Era da IA Generativa

Há 3 anos, usar IA no trabalho era privilégio de grandes empresas com orçamentos milionários. 

Hoje, você tem acesso gratuito às mesmas IAs que empresas pagam milhares de dólares por mês para usar.

O problema? 95% das pessoas usam IA de forma superficial:
- "Escreva um email"
- "Resuma este texto"
- "Crie uma lista"

Isso é como usar Ferrari para ir à padaria. Funciona, mas você está desperdiçando 90% do potencial.

Neste módulo você vai aprender:
1. ChatGPT vs Claude vs Gemini: quando usar cada um
2. Prompt engineering: estrutura que funciona
3. IA para análise de dados (sem código)
4. Automação de tarefas repetitivas

## 1. Os 3 Pilares da IA: ChatGPT, Claude, Gemini

### 1.1 ChatGPT (OpenAI)

**Melhor para:**
- ✅ Criação de conteúdo rápido
- ✅ Brainstorming e ideação
- ✅ Tarefas gerais do dia-a-dia
- ✅ Plugins e integrações
- ✅ Análise de imagens (GPT-4)

**Pontos fortes:**
- Interface mais conhecida
- Plugins expandem funcionalidades
- Code Interpreter para análise de dados
- DALL-E integrado (geração de imagens)

**Limitações:**
- Às vezes "inventa" fatos
- Contexto menor que Claude
- Pode ser verboso demais

**Quando usar:**
```
✅ Preciso de resposta rápida
✅ Vou fazer várias perguntas seguidas
✅ Quero usar plugins (web browsing, code interpreter)
✅ Preciso analisar imagens
```

**Planos:**
- Grátis: GPT-3.5 (bom, mas limitado)
- Pago ($20/mês): GPT-4 (muito melhor)

**Dica profissional:**
Use GPT-4 para tarefas importantes. Vale cada centavo.

### 1.2 Claude (Anthropic)

**Melhor para:**
- ✅ Análises profundas e detalhadas
- ✅ Trabalho com textos longos
- ✅ Precisão factual
- ✅ Raciocínio complexo
- ✅ Tarefas que exigem nuance

**Pontos fortes:**
- Contexto ENORME (200k tokens)
- Mais preciso e menos "inventivo"
- Melhor em seguir instruções complexas
- Excelente para análise de documentos

**Limitações:**
- Não tem plugins
- Menos conhecido
- Às vezes mais "conservador" nas respostas

**Quando usar:**
```
✅ Analisando documento longo (contratos, relatórios)
✅ Preciso de precisão máxima
✅ Trabalho complexo que exige raciocínio
✅ Análise de dados detalhada
```

**Planos:**
- Grátis: acesso limitado (bom para testar)
- Pago ($20/mês): Claude Pro (contexto maior, prioridade)

**Dica profissional:**
Para análise de planilhas grandes, Claude > ChatGPT.

### 1.3 Gemini (Google)

**Melhor para:**
- ✅ Integração com Google Workspace
- ✅ Busca em tempo real
- ✅ Análise de dados do Google
- ✅ Tarefas que exigem informação atualizada

**Pontos fortes:**
- Acesso direto à busca Google
- Integra com Gmail, Drive, Docs
- Informações sempre atualizadas
- Grátis (por enquanto)

**Limitações:**
- Menos poderoso que GPT-4 e Claude
- Menos controle sobre comportamento
- Ainda em evolução

**Quando usar:**
```
✅ Preciso de informação atual/recente
✅ Trabalho dentro do ecossistema Google
✅ Quero buscar e resumir informações da web
```

**Dica profissional:**
Combine Gemini (pesquisa) + Claude (análise) + ChatGPT (execução).

### 1.4 Comparação Prática

**Cenário 1: Análise de planilha de vendas (5.000 linhas)**
- 🥇 Claude: Melhor análise profunda
- 🥈 ChatGPT: Bom com Code Interpreter
- 🥉 Gemini: Limitado para datasets grandes

**Cenário 2: Criar email de vendas**
- 🥇 ChatGPT: Rápido e criativo
- 🥈 Claude: Bom mas mais formal
- 🥉 Gemini: Funciona mas genérico

**Cenário 3: Analisar contrato de 50 páginas**
- 🥇 Claude: Contexto enorme, precisão
- 🥈 ChatGPT: OK mas pode perder detalhes
- 🥉 Gemini: Não recomendado

**Cenário 4: Pesquisar tendências de mercado 2025**
- 🥇 Gemini: Acesso web em tempo real
- 🥈 ChatGPT: Com plugin de browsing
- 🥉 Claude: Dados até 2024 apenas

**Minha recomendação:**
Tenha conta nas 3. Use cada uma pro que faz melhor.

## 2. Prompt Engineering: A Habilidade de R$ 8.000/mês

### 2.1 Por Que Prompt Engineering Vale Tanto

Duas pessoas usando a mesma IA:

**Pessoa A (iniciante):**
```
Prompt: "Analise estas vendas"
Resultado: Análise genérica, superficial, pouco útil
```

**Pessoa B (prompt engineer):**
```
Prompt: "Você é analista de vendas sênior com 15 anos de experiência em e-commerce.

Analise a planilha anexa focando em:
1. Produtos com maior queda YoY
2. Regiões com melhor performance
3. Padrões de sazonalidade
4. Segmentos de clientes mais lucrativos

Para cada insight:
- Quantifique o impacto ($)
- Identifique causa raiz provável
- Sugira 2-3 ações específicas

Formato: Tabela + 3 insights principais + recomendações priorizadas por ROI."

Resultado: Análise profunda, acionável, com valor imediato
```

Mesma IA. Resultado **10x melhor** só mudando o prompt.

### 2.2 Estrutura de Prompt Profissional

**Template CRISP:**

**C - Contexto**
```
"Você é [papel/expertise específica]"
```

**R - Requisitos**
```
"Preciso que você [tarefa específica] focando em [aspectos importantes]"
```

**I - Instruções**
```
"Siga este processo:
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]"
```

**S - Saída (Output)**
```
"Formato: [estrutura desejada]
Tom: [formal/casual/técnico]
Tamanho: [máximo X palavras/parágrafos]"
```

**P - Prova/Validação**
```
"Antes de responder, valide se:
- [Critério 1]
- [Critério 2]"
```

### 2.3 Exemplos Práticos

**Exemplo 1: Análise de dados**

```
CONTEXTO:
Você é cientista de dados especializado em e-commerce com foco em análise de churn.

REQUISITOS:
Analise esta base de clientes (CSV anexo) e identifique:
1. Principais indicadores de churn
2. Segmentos de maior risco
3. Timing médio entre sinais e saída

INSTRUÇÕES:
1. Primeiro, explore os dados e identifique padrões
2. Depois, segmente clientes por comportamento
3. Por fim, crie modelo preditivo simples

SAÍDA:
- Tabela: Top 5 indicadores de churn com correlação
- Gráfico: Distribuição de churn por segmento
- Lista: 10 clientes em maior risco agora
- Recomendações: 3 ações para reduzir churn em 30 dias

VALIDAÇÃO:
Antes de responder, confirme se:
- Dados fazem sentido estatisticamente
- Recomendações são acionáveis
- Números batem com totais
```

**Exemplo 2: Criação de conteúdo**

```
CONTEXTO:
Você é copywriter especializado em LinkedIn B2B tech.

REQUISITOS:
Crie post sobre [tema X] que:
- Prenda atenção nos primeiros 3 segundos
- Eduque sobre problema real
- Posicione produto como solução
- Gere engajamento (comentários)

INSTRUÇÕES:
1. Gancho: dado/estatística surpreendente
2. Problema: dor específica do público
3. Agitação: consequências de não resolver
4. Solução: como produto ajuda
5. CTA: pergunta que gera discussão

SAÍDA:
- Máximo 150 palavras
- 3-5 parágrafos curtos
- 2-3 emojis no máximo
- 1 pergunta final engajadora

VALIDAÇÃO:
- Evitar jargões técnicos excessivos
- Tom: consultivo, não vendedor
- Foco: problema, não produto
```

### 2.4 Técnicas Avançadas

**1. Few-Shot Learning (Exemplos)**
```
Crie emails de follow-up seguindo estes exemplos:

Exemplo 1:
[cola exemplo bom]

Exemplo 2:
[cola outro exemplo bom]

Agora crie para este contexto:
[seu caso específico]
```

**2. Chain of Thought (Raciocínio Passo-a-Passo)**
```
Analise este problema:
[problema complexo]

Pense passo-a-passo:
1. Qual é o problema real?
2. Quais são as causas possíveis?
3. Como validar cada causa?
4. Qual solução para cada causa validada?
5. Como priorizar soluções por impacto vs esforço?

Mostre seu raciocínio antes da resposta final.
```

**3. Role Playing (Assumir Personagem)**
```
Você é CFO experiente analisando este investimento.

Você é cético, orientado a dados, avesso a risco.

Analise esta proposta procurando:
- Riscos não mencionados
- Suposições otimistas demais
- Furos no modelo financeiro

Seja duro na análise. Empresa conta com isso.
```

**4. Formato Específico**
```
Resuma reunião seguindo EXATAMENTE este formato:

## Decisões Tomadas
- [lista]

## Próximos Passos
| Tarefa | Responsável | Prazo |
|--------|-------------|-------|
| ...    | ...         | ...   |

## Bloqueios
- [lista]

NÃO adicione seções extras.
NÃO mude formato da tabela.
```

## 3. IA para Análise de Dados (Sem Código)

### 3.1 O Poder do Code Interpreter (ChatGPT)

ChatGPT Plus tem Code Interpreter que executa Python por você.

**O que você consegue fazer:**
- ✅ Analisar planilhas (CSV, Excel)
- ✅ Criar gráficos profissionais
- ✅ Limpar e processar dados
- ✅ Encontrar padrões e correlações
- ✅ Fazer previsões simples

**Sem escrever uma linha de código.**

**Exemplo prático:**

```
Upload: vendas_2024.csv

Prompt:
"Analise estas vendas e:
1. Mostre evolução mensal com gráfico
2. Identifique top 10 produtos por receita
3. Calcule ticket médio por mês
4. Encontre correlação entre preço e volume
5. Preveja vendas próximos 3 meses (tendência linear)

Crie visualizações profissionais."

Resultado: Análise completa + 5 gráficos em 2 minutos.
```

### 3.2 Claude para Análise Profunda

Claude não executa código, mas é EXCELENTE para análise de dados textuais.

**Upload planilha e pergunte:**
```
"Analise estes dados de churn de clientes.

Para cada cliente que saiu:
- Identifique padrão de uso antes da saída
- Tempo médio como cliente
- Valor total gasto
- Última interação

Depois:
- Agrupe por similaridade
- Identifique 3-5 perfis de churn distintos
- Para cada perfil, sugira estratégia de retenção

Seja específico e quantitativo."
```

Claude vai ler 5.000 linhas e dar análise detalhada.

### 3.3 Workflows Práticos

**Workflow 1: Análise Semanal de Vendas**
```
1. Exporta dados do CRM/Shopify (CSV)
2. Upload no ChatGPT Code Interpreter
3. Prompt: "Crie dashboard semanal: vendas, conversão, ticket médio, top produtos"
4. Salva gráficos
5. Copia insights
6. Cola no relatório/apresentação
```

Tempo: 5 minutos (vs 2 horas manual)

**Workflow 2: Segmentação de Clientes**
```
1. Exporta base de clientes
2. Upload no Claude
3. Prompt: "Segmente por: frequência de compra, valor gasto, produtos preferidos, região"
4. Recebe segmentação + características
5. Usa para campanhas direcionadas
```

**Workflow 3: Análise de Sentimento**
```
1. Exporta reviews/feedback de clientes
2. Upload no ChatGPT
3. Prompt: "Analise sentimento: positivo/neutro/negativo. Identifique temas recorrentes. Quantifique."
4. Recebe análise completa
5. Prioriza melhorias baseado em frequência
```

## 4. Automação de Tarefas com IA

### 4.1 Tarefas que IA Faz Melhor que Humanos

**1. Resumir conteúdo**
```
Upload: contrato de 50 páginas

Prompt:
"Resuma em 3 seções:
1. Pontos principais (bullet points)
2. Riscos/cláusulas importantes
3. Ações necessárias nossa parte

Máximo 1 página."
```

**2. Extrair informações estruturadas**
```
Upload: 100 emails de clientes

Prompt:
"Crie planilha com:
- Nome cliente
- Produto de interesse
- Orçamento mencionado
- Prazo de decisão
- Objeções principais

Formato CSV."
```

**3. Gerar variações em massa**
```
"Tenho este template de email:
[template]

Crie 20 variações mudando:
- Linha de assunto
- Primeiro parágrafo
- CTA

Mantenha tom e estrutura."
```

**4. Traduzir e adaptar**
```
"Traduza este conteúdo do inglês para português BR.

Mas NÃO traduza literalmente.

Adapte:
- Expressões idiomáticas
- Referências culturais
- Exemplos (use brasileiros)
- Tom (mais casual em BR)

Mantenha: estrutura, mensagem, CTA."
```

### 4.2 Biblioteca de Prompts Profissionais

**Análise competitiva:**
```
"Você é analista de mercado especializado em [setor].

Analise estes 3 concorrentes:
[lista sites/produtos]

Para cada um, identifique:
1. Proposta de valor única
2. Público-alvo principal
3. Estratégia de preço
4. Pontos fortes vs fracos
5. Diferenciação

Depois, crie matriz comparativa e recomende como nos posicionar."
```

**Criação de persona:**
```
"Baseado nestes dados de clientes:
[upload planilha]

Crie 3 personas detalhadas:

Para cada persona inclua:
- Nome e background
- Objetivos profissionais
- Desafios diários
- Como toma decisões de compra
- Objeções típicas
- Canais que usa
- Mensagem que ressoa

Seja específico e realista."
```

**Planejamento de conteúdo:**
```
"Sou [seu cargo] em [seu nicho].

Objetivo: crescer LinkedIn de 500 para 5.000 seguidores em 90 dias.

Crie calendário de conteúdo com:
- 3 posts por semana
- Mix: 40% educacional, 30% cases, 20% pessoal, 10% vendas
- Variação de formato: texto, carrossel, vídeo
- Horários otimizados

Para cada post:
- Título/gancho
- Estrutura (bullets)
- CTA
- Hashtags relevantes

90 dias = ~40 posts. Liste todos."
```

## Exercício Prático

**Duração:** 90 minutos

**Objetivo:** Dominar as 3 IAs na prática

**Parte 1: Comparação (30min)**
1. Pegue 1 tarefa real sua (análise, email, relatório)
2. Execute a mesma tarefa nos 3 (ChatGPT, Claude, Gemini)
3. Compare resultados
4. Documente qual foi melhor e por quê

**Parte 2: Prompt Engineering (30min)**
1. Escolha 1 tarefa que você faz semanalmente
2. Crie prompt usando estrutura CRISP
3. Teste e refine até resultado satisfatório
4. Salve prompt na sua biblioteca pessoal

**Parte 3: Análise de Dados (30min)**
1. Pegue 1 planilha sua (vendas, leads, qualquer)
2. Upload no ChatGPT Code Interpreter
3. Peça análise completa + gráficos
4. Extraia pelo menos 3 insights acionáveis

**Entrega:**
- Documento comparando as 3 IAs
- 5 prompts salvos (sua biblioteca)
- 1 análise de dados completa

**Isso vai te colocar acima de 90% dos usuários de IA.**

---

## Próximos Passos

**Módulo 4: Automação No-Code com Make**
- Interface do Make
- Primeira automação (passo-a-passo)
- Integrações poderosas
- Casos de uso práticos

**Ferramentas que vamos usar:**
Make, Zapier, integrações com IA

Nos vemos lá! 🚀

---

**© 2025 FETD - Formação em Engenharia de Intenção**
