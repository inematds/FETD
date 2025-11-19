# Módulo 7: Slack e Comunicação Assíncrona

**Trilha:** Talento Emergente
**Duração:** 45 minutos
**Objetivo:** Dominar ferramentas de comunicação profissional remota

---

## Introdução: A Nova Era do Trabalho Remoto

Trabalho remoto exige comunicação eficaz. **Slack** é padrão em 80%+ das startups e scale-ups brasileiras.

**Dados 2024-2025:**
- 70% empresas tech usam Slack
- Profissionais gastam 2-4h/dia no Slack
- Má comunicação assíncrona: -20% produtividade
- Boa comunicação assíncrona: +35% produtividade
- Dominar Slack = diferencial em 90% das vagas remotas

**O que você vai aprender:**
- Slack profissional (etiqueta que impressiona)
- Canais e organização
- Comunicação assíncrona eficaz
- Bots e automações
- Integrações (Slack + Make + Notion + IA)

## 1. Slack Profissional: Fundamentos

### 1.1 Anatomia do Slack

**Elementos principais:**

**Workspace:** Empresa/comunidade inteira
- Exemplo: empresa-tech.slack.com

**Channels:** Conversas organizadas por tópico
- Públicos: Qualquer um no workspace vê
- Privados: Só membros convidados
- Prefixos comuns:
  * `#geral` - Announcements gerais
  * `#random` - Casual/off-topic
  * `#proj-nome` - Por projeto
  * `#team-nome` - Por equipe
  * `#help-tema` - Suporte/dúvidas
  * `#notif-sistema` - Notificações automáticas

**Direct Messages (DMs):** Conversas 1:1 ou pequenos grupos

**Threads:** Respostas organizadas (NÃO polui canal)

**Mentions:**
- `@pessoa` - Notifica pessoa específica
- `@channel` - Notifica todos no canal (use com parcimônia!)
- `@here` - Notifica só quem está online agora

**Reações:** Emojis pra responder rápido (✅ ❌ 👀 🎉)

### 1.2 Etiqueta Slack que Impressiona

**DO (Faça):**

✅ **Use threads religiosamente**
```
Mensagem original:
"Precisamos decidir sobre X"

❌ Resposta solta no canal:
"Concordo, e também acho que..."

✅ Resposta em thread:
[Click "Reply in thread"]
"Concordo, e também acho que..."
```

Por quê: Mantém canal limpo. Facilita acompanhar discussões.

✅ **Mensagens completas e claras**
```
❌ Ruim:
"Oi, tudo bem? Podemos conversar?"

✅ Bom:
"Oi Maria! Sobre projeto X: 

Contexto: Precisamos definir timeline
Pergunta: Você consegue entregar módulo Y até sexta?
Urgência: Não urgente, responde quando puder

Obrigado!"
```

✅ **Status claro**
```
🟢 Disponível (padrão)
🟡 Ausente (afk, almoço)
🔴 Não perturbe (deep work)
🟣 Férias
🔵 Reunião
```

Settings → Set a status

✅ **Reaja antes de responder**
```
Alguém posta: "Revisem doc X até amanhã"

Você:
1. Reage com 👀 (vi)
2. Quando revisa, reage com ✅ (feito)
3. Se tiver comentário, responde em thread
```

Evita 20 mensagens de "ok", "vi", "feito".

✅ **Code blocks para código/logs**
```
❌ Ruim:
Olha esse erro: TypeError: undefined is not a function

✅ Bom:
```
TypeError: undefined is not a function
  at Object.<anonymous> (/src/app.js:42:5)
  at Module._compile (module.js:652:30)
```
```

Use ` para inline code, ``` para blocos.

**DON'T (Não faça):**

❌ **@channel sem necessidade**
```
❌ "@channel alguém sabe onde fica arquivo X?"
✅ "Alguém sabe onde fica arquivo X?" (sem @)
```

@channel só se:
- Emergência (site fora, bug crítico)
- Anúncio importante que TODO MUNDO precisa ver AGORA

❌ **DM quando deveria ser canal**
```
❌ DM: "Como faço X?"
✅ Canal #help-tech: "Como faço X?"
```

Por quê: Outros aprendem também. Conhecimento fica documentado.

❌ **Mensagens quebradas**
```
❌ Ruim:
[13:04] "Oi"
[13:04] "Tudo bem?"
[13:05] "Preciso"
[13:05] "de ajuda"
[13:06] "com algo"

✅ Bom:
[13:04] "Oi! Tudo bem? Preciso de ajuda com X. [detalhes completos]"
```

❌ **Sem contexto em threads antigas**
```
❌ "Resolveu?"
(Ninguém lembra do que era)

✅ "Resolveu aquele bug do login que você mencionou ontem?"
```

❌ **TUDO EM CAPS LOCK**
```
❌ "URGENTE PRECISO AJUDA AGORA"
✅ "🚨 Urgente: Site fora do ar, precisamos investigar"
```

### 1.3 Atalhos de Teclado (Slack Ninja)

**Navegação:**
- `Ctrl/Cmd + K` - Jump to channel/DM (mais usado!)
- `Alt + ↑/↓` - Canal anterior/próximo
- `Ctrl/Cmd + [/]` - Navegação histórico
- `Ctrl/Cmd + .` - Toggle right sidebar

**Mensagens:**
- `Ctrl/Cmd + Enter` - Envia mensagem
- `↑` - Edita última mensagem sua
- `R` - Responder em thread (message selecionada)
- `E` - Adicionar emoji reaction
- `M` - Mencionar pessoa

**Marcação:**
- `Shift + Esc` - Marca tudo como lido
- `Esc` - Limpa mensagens não lidas do canal atual

**Formatação:**
- `Ctrl/Cmd + B` - **Bold**
- `Ctrl/Cmd + I` - *Italic*
- `Ctrl/Cmd + Shift + X` - ~~Strikethrough~~
- `Ctrl/Cmd + Shift + C` - `Code`

**Busca:**
- `Ctrl/Cmd + G` - Busca avançada
- `Ctrl/Cmd + F` - Busca no canal atual

**Desafio:** 1 dia inteiro sem usar mouse no Slack.

### 1.4 Configurações de Produtividade

**Notificações (Settings → Notifications):**

**Recomendado:**
```
Desktop notifications:
- Direct messages, mentions, keywords: ✓
- All new messages: ✗ (NUNCA ative isso)

Do Not Disturb:
- Schedule: 20:00 - 08:00 (ou seu horário)
- Duration: Quando ativar manual, 1h padrão

Keywords: 
- Seu nome
- Palavras relacionadas ao seu trabalho
- "urgente", "crítico" (se relevante)

Sound:
- Direct messages, mentions: ✓
- All messages: ✗
```

**Focus time:**
1. `/dnd 2 hours` - Ativa DND por 2h
2. Status: 🔴 Deep Work - Disponível às 16h
3. Notificações: Off
4. Trabalha focado

**Starred Channels:**
- Canais que você acessa 5x/dia
- Aparecem no topo da sidebar
- Click na estrela ao lado do nome do canal

**Sections (sidebar organizada):**

Organize canais em seções:
```
⭐ Starred
📁 Projetos
  #proj-a
  #proj-b
👥 Times
  #team-tech
  #team-product
📢 Updates
  #anuncios
  #general
```

Settings → Sidebar → Create new section

## 2. Comunicação Assíncrona Eficaz

### 2.1 O que é Comunicação Assíncrona

**Síncrona:** Resposta imediata esperada (call, reunião, chat ao vivo)

**Assíncrona:** Resposta quando conveniente (email, Slack, Notion comments)

**Por que assíncrona é melhor para trabalho profundo:**
- Sem interrupções constantes
- Responde quando tem contexto
- Pensamento mais elaborado
- Documentado automaticamente

**Mas requer disciplina e clareza.**

### 2.2 Framework de Mensagem Assíncrona Perfeita

**CRISP for Slack:**

**C - Context (Contexto)**
```
"Sobre projeto X:"
"Referente ao bug reportado ontem:"
"No PR #123:"
```

**R - Request (Pedido específico)**
```
"Preciso que você revise o doc Y"
"Pode aprovar o PR?"
"Confirma se esse approach faz sentido?"
```

**I - Information (Informações necessárias)**
```
"Link: [url]"
"Prazo ideal: sexta"
"Contexto adicional: [detalhes]"
```

**S - Support (Como ajudar)**
```
"Se tiver dúvidas, me chama"
"Posso explicar melhor em call se preferir"
"Não urgente, responde quando conseguir"
```

**P - Priority (Urgência)**
```
🔴 Urgente: Preciso até EOD (end of day)
🟡 Importante: Até esta semana
🟢 Normal: Quando conseguir, próximos dias
⚪ FYI: Só informando, sem ação necessária
```

**Exemplo completo:**
```
📊 Sobre projeto X (Dashboard vendas)

Preciso que você revise o Figma antes da reunião de amanhã.

Link: [figma.com/...]
Foco: UX do filtro de datas (slide 3-5)
Contexto: Cliente pediu simplificar

Se tiver dúvidas, marca call comigo.

🟡 Importante: Até amanhã 10h (reunião às 11h)
```

**vs mensagem ruim:**
```
"Oi, vê isso aqui quando puder [link] valeu"
```

### 2.3 Quando Usar Qual Canal

**Slack DM:**
- Questão rápida pra 1 pessoa
- Feedback pessoal (não público)
- Conversa casual 1:1
- Coordenar algo que não interessa ao time

**Slack Channel:**
- Discussão que beneficia time
- Decisões que precisam documentação
- Updates de projeto
- Ajuda técnica (outros aprendem)

**Thread:**
- Resposta a mensagem específica
- Discussão profunda sobre tópico
- Não quer poluir canal principal

**Reunião síncrona (Call):**
- Discussão complexa com muitas idas e voltas
- Brainstorming criativo
- Decisão crítica e urgente
- Alinhar quando assíncrono falhando

**Email:**
- Formal/oficial
- Externo (fora da empresa)
- Documento/contrato
- Registro legal

**Regra de ouro:** Default = assíncrono. Só vai pra síncrono se necessário.

## 3. Slack Bots e Automações

### 3.1 Bots Essenciais

**1. Polly (Polls/Votações)**

```
/polly "Qual horário melhor pra reunião?" "10h" "14h" "16h"
```

Cria poll interativa. Time vota com cliques.

**2. Simple Poll**

```
/poll "Aprovam proposta X?" "Sim" "Não" "Preciso mais info"
```

**3. Standup Bot (Daily standup assíncrono)**

Config:
- Pergunta diariamente (9h):
  * O que fez ontem?
  * O que vai fazer hoje?
  * Algum bloqueio?
- Respostas compiladas e postadas no canal

**Substitui reunião diária de 30min por 5min assíncronos.**

**4. Donut (Team bonding)**

Pareia aleatoriamente pessoas do time pra coffee chat.

**5. Geekbot (Async standups + retrospectives)**

Templates prontos:
- Daily standup
- Weekly check-in
- Sprint retrospective
- 1:1 prep

**6. Workflow Builder (Slack nativo - sem code)**

Cria workflows:

**Exemplo: Onboarding automatizado**
```
Trigger: Pessoa entra no workspace
→ Envia DM:
  "Bem-vindo! 👋
   
   Próximos passos:
   1. Preenche perfil
   2. Lê #handbook
   3. Apresenta-se no #geral
   
   Dúvidas? Chama @HR"
→ Add aos canais: #geral, #random, #anuncios
→ Notifica RH: "Novo membro: [nome]"
```

**Exemplo: Request de férias**
```
Trigger: Comando /ferias
→ Form aparece:
  - Datas
  - Motivo
  - Observações
→ Post no #rh-requests
→ Notifica gestor
→ Add ao Google Calendar
```

Slack → Tools → Workflow Builder → Create

**Não precisa código!**

### 3.2 Slack + Make (Automações Custom)

**Automação 1: Novo lead → Slack notification**
```
Google Forms - New response (Lead form)
→ Slack - Send Message
  Channel: #vendas
  Message:
    "🎯 Novo lead!
    
    Nome: {{1.nome}}
    Empresa: {{1.empresa}}
    Interesse: {{1.produto}}
    Budget: {{1.orcamento}}
    
    @vendedor, fazer follow-up!"
```

**Automação 2: Deploy falhou → Alert Slack**
```
GitHub - Workflow Run Failed
→ Slack - Send Message
  Channel: #tech-alerts
  Message:
    "🚨 Deploy FALHOU
    
    Repo: {{1.repository}}
    Branch: {{1.branch}}
    Commit: {{1.commit_message}}
    Author: @{{1.author}}
    
    Logs: {{1.logs_url}}"
```

**Automação 3: Task Notion completada → Celebrar no Slack**
```
Notion - Watch Database Items (Tasks)
  Filter: Status = Done AND Priority = P1
→ Slack - Send Message
  Channel: #wins
  Message:
    "🎉 @{{1.owner}} completou task P1!
    
    Task: {{1.name}}
    Projeto: {{1.project}}
    
    Great job! 🚀"
```

**Automação 4: Slack → Notion (Capture ideas)**
```
Slack - New Message
  Channel: #ideias
  Filter: Contains emoji :bulb:
→ Notion - Create Page
  Database: Ideias
  Properties:
    - Ideia: {{1.text}}
    - Autor: {{1.user}}
    - Data: {{1.timestamp}}
    - Link Slack: {{1.permalink}}
```

Workflow: Teve ideia → posta no #ideias com 💡 → vai pro Notion automaticamente

### 3.3 Slash Commands Custom

Crie comandos próprios:

**API → Slack webhook:**

**Exemplo: `/deploy production`**

Quando você digita isso no Slack:
1. Slack envia webhook pra seu servidor
2. Servidor executa deploy
3. Responde no Slack: "Deploy iniciado... ✓ Completo!"

**Como configurar:**
1. Slack API → Create app
2. Slash Commands → Create command
   - Command: `/deploy`
   - Request URL: `https://seu-servidor.com/slack/deploy`
3. Permissions: Adicione ao workspace
4. Código no servidor processa e responde

**Outros exemplos:**
- `/standup` - Posta standup
- `/analytics` - Mostra métricas
- `/support` - Abre ticket
- `/lunch` - Pede comida (integra com iFood API 😄)

## 4. Integrações Avançadas

### 4.1 Slack + Notion

**Via Make:**

**Sync bidirecional:**
```
Notion - New page em Database "Tasks"
→ Slack - Post em #tasks
  "Nova task: {{1.name}}
   Owner: @{{1.owner}}
   Due: {{1.due_date}}"

Slack - Reaction added (:white_check_mark:)
→ Notion - Update page
  Status: Done
```

**Meeting notes:**
```
Slack - Scheduled Message (antes reunião)
  "Reunião em 1h: [tópico]
   Notas: [link Notion]
   Agenda: [lista]"

Google Calendar - Event ended
→ Slack - Reminder
  "@participantes: Preencham notas reunião [link]"
```

### 4.2 Slack + IA (ChatGPT/Claude)

**Bot IA no Slack:**

**Via Make + OpenAI API:**
```
Slack - New Message
  Channel: #ai-assistant
→ OpenAI - Create Completion
  Prompt: {{1.text}}
  Model: gpt-4
→ Slack - Reply Thread
  Text: {{2.response}}
```

**Resultado:** Qualquer pergunta no #ai-assistant → IA responde

**Use cases:**
- "Resuma este doc: [link]"
- "Traduza para inglês: [texto]"
- "Crie email de follow-up para [contexto]"
- "Analise estes dados: [dados]"

**Atenção:** Custo de API. Configure limits.

### 4.3 Slack + Google Workspace

**Native integrations (Slack app):**

**Google Calendar:**
- Eventos aparecem como status Slack
- Reminder 10min antes
- Join meet direto do Slack

**Google Drive:**
- Post link Drive → preview automático
- Commenta no Drive → notifica Slack
- Share Drive file direto no Slack

**Gmail:**
- Email importante → forward pro Slack (email único por canal)

## 5. Slack Analytics e Produtividade

### 5.1 Search (Busca Profissional)

**Operadores:**

**Por pessoa:**
```
from:@joao
```

**Por canal:**
```
in:#tech
```

**Por data:**
```
after:2025-01-01
before:2025-02-01
during:january
```

**Por tipo:**
```
has:link
has:file
has:emoji
```

**Combinados:**
```
from:@maria in:#projeto-x has:link after:2025-01-15

= Mensagens da Maria no #projeto-x com links após 15/01
```

**Saved searches:**
- Busca complexa frequente
- Click "Save this search"
- Acesso rápido depois

### 5.2 Produtividade no Slack

**Tips:**

**1. Inbox Zero diário**
- Todas mentions/DMs respondidos ou marcados pra depois
- "Mark as unread" se precisa voltar depois
- Ou salva com estrela

**2. Snooze messages**
- Mensagem que precisa responder depois
- Click ⋮ → Remind me about this
- Choose: 20min, 1h, tomorrow, custom

**3. Scheduled messages**
```
/remind @pessoa "fazer X" at 9am tomorrow
/remind #canal "reunião em 10min" in 10 minutes
```

Ou:
- Escreve mensagem
- Click ⌄ ao lado do Send
- Schedule for later

**Caso de uso:** Trabalha de noite, mas não quer notificar time → agenda pra 9am

**4. Saved items**
- Mensagem importante
- Click estrela ⭐
- Acessa depois: Saved items (sidebar)

**5. Custom status**
```
🏖️ Férias até 20/02
🤒 Doente hoje
🏃 Academia - volto 14h
🎧 Focus time - respondo às 16h
```

Settings → Set a status

## 6. Exercício Prático (45min)

**PARTE 1: Setup Profissional (15min)**

1. Configure notificações otimizadas
2. Crie 3 sections na sidebar
3. Configure status com emoji + texto
4. Starre 3 canais mais usados
5. Salve 2 searches úteis

**PARTE 2: Comunicação (15min)**

1. Escreva 3 mensagens usando framework CRISP:
   - Request de revisão
   - Update de projeto
   - Dúvida técnica
2. Pratique threads (não polua canal!)
3. Use reações adequadamente

**PARTE 3: Automação (15min)**

Escolha 1:
- A) Configure Workflow Builder (onboarding ou request)
- B) Make: Slack notification de algo (Form, Notion, etc)
- C) Configure bot (Polly, Standup, etc)

**ENTREGA:**
- Screenshots de cada parte
- 3 mensagens escritas (exemplos reais ou simulados)
- 1 automação funcionando

**BÔNUS:** Compartilha no LinkedIn dica de Slack que aprendeu. Tag #slack #comunicacaoassincrona

---

## Próximos Passos

**Módulo 8: Canva e Design Básico**
- Criar visuais profissionais sem ser designer
- Posts LinkedIn que convertem
- Apresentações impactantes
- Brand kit pessoal

**Prepare-se para:** Comunicação visual que destaca

Nos vemos lá! 🚀

---

**© 2025 FETD - Formação em Engenharia de Intenção**
