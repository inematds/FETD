# Módulo 3: Seu Primeiro Assistente - IA na Prática

**Trilha:** Operacional Produtivo
**Duração:** 1 hora
**Objetivo:** Dominar IAs generativas para tarefas operacionais usando o Framework LRP

---

## 🎯 Objetivo deste Módulo

Você vai aprender a usar IAs generativas de forma profissional. Não é "conversar com robô", é ter assistentes que multiplicam sua produtividade em tarefas operacionais reais.

---

## 1. ChatGPT, Claude, Gemini: Quando Usar Cada Um

Existem dezenas de IAs disponíveis, mas **3 dominam o mercado profissional**. Cada uma tem pontos fortes específicos.

### 💬 ChatGPT (OpenAI)

**Melhor para:** Criação de conteúdo, brainstorming, conversação natural

**Pontos Fortes:**
- ✓ Escreve muito bem
- ✓ Tom natural e criativo
- ✓ Versatiidade geral
- ✓ Plugins e extensões

**Use quando:** Precisa escrever emails, criar textos, gerar ideias, respostas rápidas e criativas

### 🧠 Claude (Anthropic)

**Melhor para:** Análise profunda, tarefas complexas, raciocínio detalhado

**Pontos Fortes:**
- ✓ Raciocínio lógico superior
- ✓ Análise de documentos longos
- ✓ Seguir instruções complexas
- ✓ Contexto extenso (200k tokens)

**Use quando:** Precisa analisar relatórios, resumir documentos grandes, tarefas que exigem lógica e precisão

### 🔍 Gemini (Google)

**Melhor para:** Pesquisa, dados atualizados, integração Google Workspace

**Pontos Fortes:**
- ✓ Acesso à web em tempo real
- ✓ Integrado ao Google (Docs, Sheets)
- ✓ Bom com dados e números
- ✓ Multimodal (texto, imagem, vídeo)

**Use quando:** Precisa de informações atuais, trabalha no Google Workspace, quer pesquisar dados recentes

### 💡 Dica Profissional:

Não precisa escolher apenas um. Use **cada ferramenta para o que ela faz de melhor**. Profissionais de alta performance usam as 3.

---

## 2. Framework LRP: Listen / Repeat / Poke

Este é o **método mais eficiente** para extrair resultados de qualquer IA. Não é mágica, é metodologia.

### 📢 L = LISTEN (Escutar)

**Primeiro, dê contexto completo à IA**. Ela não sabe quem você é, o que faz, qual seu objetivo.

**❌ Errado (prompt vago):**
"Me ajuda a organizar emails"

**✅ Certo (prompt completo):**
"Sou analista financeiro e recebo 200+ emails/dia. A maioria são relatórios automáticos, solicitações internas e newsletters. Preciso de um sistema de filtros para categorizar automaticamente por: [Urgente], [Relatórios], [Leitura Posterior], [Newsletters]. Sugira regras de filtros para Gmail."

**Checklist LISTEN:**
- Quem você é (cargo/função)
- Contexto da situação
- Objetivo específico
- Restrições ou requisitos

### 🔁 R = REPEAT (Repetir)

**Peça para a IA repetir com as palavras dela**. Isso garante que ela entendeu corretamente.

**Exemplo de REPEAT:**
"Antes de sugerir a solução, me diga com suas palavras: qual é o problema que estou tentando resolver?"

**Por que funciona:**
A IA vai reprocessar o contexto e, se entendeu errado, você corrige antes de perder tempo com solução errada.

**Economia de tempo:** 5 segundos pedindo REPEAT economiza 30 minutos refazendo trabalho baseado em resposta errada.

### 👆 P = POKE (Cutucar)

**Refine iterativamente**. A primeira resposta raramente é perfeita. Melhore aos poucos.

**Exemplos de POKE:**
- "✓ Bom, mas pode ser mais conciso?"
- "✓ Pode dar 3 exemplos práticos disso?"
- "✓ Essa parte ficou confusa, pode reformular?"
- "✓ Pode adicionar uma tabela comparativa?"
- "✓ Transforme isso num checklist passo a passo"

**Regra de Ouro:** Nunca aceite a primeira resposta. Faça pelo menos 2-3 POKEs para chegar no resultado ideal.

### 🎯 Framework LRP Completo em Ação:

**1️⃣ LISTEN:**
"Sou coordenador de projetos. Gasto 2h/dia atualizando status reports manualmente. Tenho dados em Google Sheets. Preciso de um template de relatório automático semanal."

**2️⃣ REPEAT:**
"Antes de criar o template, confirme: você quer um relatório que puxa dados automáticos do Google Sheets e formata num padrão semanal. Correto?"

**3️⃣ POKE (iterações):**
→ "Ótimo! Agora pode adicionar uma seção de riscos?"
→ "Pode formatar isso como tabela HTML?"
→ "Perfeito! Pode criar a fórmula do Sheets que alimenta isso?"

---

## 3. Como Dar Instruções Claras

A qualidade da resposta da IA é **diretamente proporcional à qualidade da sua instrução**. Lixo entra, lixo sai.

### 📋 Anatomia de uma Instrução Perfeita:

1. **PAPEL** (quem é a IA nesse contexto)
   *"Você é um especialista em automação de processos administrativos..."*

2. **CONTEXTO** (situação atual)
   *"Trabalho numa empresa de consultoria, recebo 50 planilhas por semana de diferentes clientes..."*

3. **TAREFA** (o que você quer)
   *"Preciso de um sistema que consolide automaticamente todos os dados numa planilha mestra..."*

4. **FORMATO** (como quer a resposta)
   *"Responda com: passo a passo numerado + exemplo de fórmula + prints se possível..."*

5. **RESTRIÇÕES** (limitações importantes)
   *"Não posso usar ferramentas pagas. Só Google Workspace gratuito..."*

### ❌ Instruções Ruins vs ✅ Instruções Boas

**Vago:**
❌ "Faz um email profissional"
✅ "Escreva email agradecendo proposta comercial, mas pedindo 10% desconto. Tom educado e profissional."

**Sem contexto:**
❌ "Cria uma planilha de vendas"
✅ "Crie planilha rastreando vendas mensais com: produto, valor, vendedor, status. Incluir fórmulas de total e média."

**Sem formato:**
❌ "Explica como funciona Zapier"
✅ "Explique Zapier em 5 bullet points para alguém não-técnico, com 1 exemplo prático."

### 🎯 Template Reutilizável:

```
PAPEL: Você é [especialista em X]
CONTEXTO: Estou em [situação Y]
TAREFA: Preciso que você [faça Z]
FORMATO: Responda com [formato específico]
RESTRIÇÕES: Não pode [limitações]
```

---

## 4. Templates de Prompts Operacionais

Aqui estão **5 prompts prontos** que você pode copiar e adaptar para suas tarefas do dia a dia.

### PROMPT 1: Organizar Dados

```
Você é especialista em organização de dados. Tenho uma lista desorganizada com [descreva os dados]. Preciso que você: 1) Identifique padrões, 2) Sugira estrutura de categorização, 3) Forneça template de planilha com colunas ideais. Formato: passo a passo + exemplo de categorização.
```

**Use quando:** Tem dados bagunçados e precisa de estrutura lógica

### PROMPT 2: Escrever Email Profissional

```
Escreva email profissional para [destinatário]. Objetivo: [o que você quer]. Tom: [formal/amigável/direto]. Contexto importante: [situação]. Máximo 150 palavras. Inclua assunto do email.
```

**Use quando:** Precisa escrever email rápido mas bem formatado

### PROMPT 3: Resumir Documento Longo

```
Você receberá um documento de [X páginas]. Preciso de: 1) Resumo executivo (5 linhas), 2) Principais pontos (bullets), 3) Ações recomendadas (se houver). Foco em [aspecto específico]. [Cole o texto aqui]
```

**Use quando:** Recebe relatórios/documentos longos e precisa extrair essência

### PROMPT 4: Gerar Relatório

```
Crie relatório [semanal/mensal] sobre [tema]. Dados disponíveis: [liste métricas]. Estrutura desejada: 1) Overview, 2) Métricas principais (tabela), 3) Análise de tendências, 4) Recomendações. Formato: HTML ou Markdown para copiar direto.
```

**Use quando:** Precisa transformar dados brutos em relatório apresentável

### PROMPT 5: Formatar Conteúdo

```
Tenho este conteúdo desformatado: [cole texto]. Reformate para: [checklist / tabela / bullets / numeração]. Mantenha todas as informações, apenas organize visualmente. Se faltar informação, sinalize [COMPLETAR AQUI].
```

**Use quando:** Tem informação boa mas apresentação ruim

---

## 5. Erros Comuns e Como Evitar

Aprenda com os erros que **90% dos iniciantes cometem** ao usar IA.

### ❌ ERRO 1: Aceitar a Primeira Resposta

**O problema:** IAs dão respostas "ok" na primeira vez. Respostas ÓTIMAS vêm depois de iterações.

**✅ Como evitar:** Sempre faça pelo menos 2-3 refinamentos (POKEs). "Pode melhorar X?", "Adicione Y", "Simplifique Z".

### ❌ ERRO 2: Não Dar Contexto Suficiente

**O problema:** IA não é telepata. Sem contexto, ela chuta respostas genéricas.

**✅ Como evitar:** Use o framework LRP. Sempre comece com LISTEN (contexto completo antes da tarefa).

### ❌ ERRO 3: Copiar Sem Revisar

**O problema:** IAs inventam coisas (alucinações), erram detalhes, não conhecem sua empresa.

**✅ Como evitar:** Sempre revise e adapte. IA te dá 80% do caminho, você adiciona os 20% de personalização.

### ❌ ERRO 4: Usar IA para Tudo

**O problema:** Nem tudo precisa de IA. Às vezes uma fórmula simples resolve.

**✅ Como evitar:** Lembre do Golden Ratio: 60% automação pura (sem IA), 30% IA assistida, 10% humano. Use cada ferramenta certa.

### ❌ ERRO 5: Não Salvar Prompts Que Funcionam

**O problema:** Você cria um prompt perfeito... e perde. Precisa recriar toda vez.

**✅ Como evitar:** Crie sua "Biblioteca de Prompts" (você vai fazer isso no exercício prático deste módulo!).

---

## 💭 Exercícios de Reflexão

### Pergunta 1:

Qual das 3 IAs (ChatGPT, Claude, Gemini) faz mais sentido para **suas tarefas específicas**? Por quê?

*Pense nas tarefas que você listou no Módulo 1: são mais criativas, analíticas ou baseadas em dados?*

**Resposta:**

_______________________________________________

### Pergunta 2:

Quando você pediu ajuda de IA antes (se já usou), **qual erro da lista acima você cometeu?**

*Seja honesto: aceitou primeira resposta? Não deu contexto? Copiou sem revisar?*

**Resposta:**

_______________________________________________

### Pergunta 3:

Das 5 categorias de prompts (Organizar, Email, Resumir, Relatório, Formatar), **quais 2 você mais usaria no dia a dia?**

*Pense nas tarefas que mais consome seu tempo atualmente.*

**Resposta:**

_______________________________________________

---

## 🛠️ Exercício Prático

### 📋 Tarefa 1: Criar 5 Prompts Customizados

Para cada uma das 5 categorias, crie um prompt adaptado para SUA realidade:

**1. Organizar Dados (sua versão):**
- Que tipo de dados você organiza? (emails? planilhas? documentos?)
- Qual estrutura faz sentido para você?
- Escreva o prompt completo e teste numa IA

**Seu prompt:**

_______________________________________________

---

**2. Email Profissional (sua versão):**
- Qual tipo de email você mais escreve?
- Follow-up de reunião? Solicitação? Agradecimento?
- Qual tom você normalmente usa?

**Seu prompt:**

_______________________________________________

---

**3. Resumir (sua versão):**
- Que tipo de documento você precisa resumir?
- Relatórios técnicos? Atas de reunião? Artigos?
- Que informações são mais importantes extrair?

**Seu prompt:**

_______________________________________________

---

**4. Relatório (sua versão):**
- Que tipo de relatório você cria regularmente?
- Vendas? Performance? Status? KPIs?
- Que métricas você rastreia?

**Seu prompt:**

_______________________________________________

---

**5. Formatar (sua versão):**
- Que tipo de conteúdo você precisa formatar?
- Notas de reunião? Listas? Procedimentos?
- Que formato final você prefere? (tabela, checklist, bullets)

**Seu prompt:**

_______________________________________________

---

### 🧪 Tarefa 2: Testar com Framework LRP

Escolha **1 dos 5 prompts** e aplique o framework LRP completo:

**LISTEN (contexto completo):**

_______________________________________________

**REPEAT (confirmar entendimento):**

_______________________________________________

**POKE (refinar 3 vezes):**

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### 💾 Tarefa 3: Salvar sua Biblioteca

Crie um documento (Notion, Google Docs, Evernote) com seus 5 prompts finais:

**Template de documentação:**
- **Nome do Prompt:** [ex: "Organizar emails por projeto"]
- **Quando usar:** [situação específica]
- **IA recomendada:** [ChatGPT/Claude/Gemini]
- **Prompt completo:** [texto do prompt]
- **Exemplo de uso:** [caso real que testou]

---

## ✅ Entregável do Módulo 3

**"Biblioteca de Prompts Pessoal"** com:

- [ ] 5 prompts customizados para suas tarefas específicas
- [ ] 1 prompt testado com Framework LRP completo
- [ ] Documento organizado para reutilização futura

---

## 🎉 Conclusão

### O que você conquistou neste módulo:

- ✓ Dominou as diferenças entre ChatGPT, Claude e Gemini
- ✓ Aprendeu o Framework LRP (Listen/Repeat/Poke)
- ✓ Entendeu como dar instruções claras e eficientes
- ✓ Criou 5 prompts operacionais customizados
- ✓ Testou na prática e criou sua biblioteca reutilizável

### ➡️ Próximo Módulo:

**Ferramentas No-Code - Zapier e Make**

Você vai aprender a conectar sistemas diferentes sem escrever uma linha de código. Suas primeiras 3 automações práticas!

---

**© 2025 FETD - Formação em Engenharia de Intenção**
