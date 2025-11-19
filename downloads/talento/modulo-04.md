# Módulo 4: Automação No-Code com Make

**Trilha:** Talento Emergente
**Duração:** 60-75 minutos
**Objetivo:** Criar sua primeira automação profissional sem escrever código

---

## Introdução: A Revolução No-Code

Imagine economizar 15-20 horas por semana eliminando tarefas repetitivas.

Não é futuro. É o que profissionais fazem HOJE com ferramentas no-code.

**Dados reais (2024-2025):**
- Profissionais que usam automação no-code: +62% produtividade
- Empresas economizam média: R$ 3.000-8.000/mês em trabalho manual
- Make tem 1.400+ apps integrados
- Mercado de automação no-code: crescimento 41% ao ano
- Automação Specialist: R$ 5.000-12.000/mês no Brasil

**Make** (antigo Integromat) é a ferramenta mais poderosa para automação visual. Empresas como Netflix, Tesla e Spotify usam ferramentas similares para automatizar processos internos.

Neste módulo você vai:
1. Entender como Make funciona (conceitos fundamentais)
2. Criar sua primeira automação (passo-a-passo completo)
3. Aprender integrações essenciais (Gmail, Sheets, Slack, Drive, etc)
4. Ver casos de uso que geram valor imediato
5. Técnicas avançadas (routers, iterators, error handling)
6. Como monetizar essa habilidade (R$ 500-10.000 por projeto)

## 1. O Que é Make e Por Que Usar

### 1.1 Conceitos Básicos: Como Funciona a Mágica

**Make conecta aplicativos diferentes para automatizar processos.**

Pense assim: você já faz muitas tarefas manualmente conectando apps. Exemplo:

**Manual (você faz):**
1. Recebe email com anexo
2. Abre anexo
3. Salva no Drive
4. Copia informações
5. Cola no Google Sheets
6. Notifica colega no Slack
7. Cria tarefa no Notion

**Tempo:** 5-10 minutos por email
**Com 20 emails/dia:** 100-200 min = 2-3 horas gastas

**Automação Make (robô faz):**
```
QUANDO novo email com anexo chega
  → ENTÃO salvar anexo no Google Drive (pasta específica)
  → E extrair informações do email (regex ou IA)
  → E adicionar linha no Google Sheets (com dados estruturados)
  → E criar task no Notion (com deadline automático)
  → E notificar time no Slack (mencionando responsável)
  → E enviar auto-reply confirmando recebimento
```

**Tempo:** 0 minutos (roda sozinho 24/7)
**Economia:** 2-3 horas/dia = 10-15 horas/semana

**Isso é automação no-code: conectar apps que você JÁ usa, sem programar.**

### 1.2 Anatomia de uma Automação Make

**Componentes principais:**

1. **Trigger (Gatilho):** O que inicia a automação
   - Exemplos: novo email, novo formulário, hora específica, webhook
   - "QUANDO [evento acontece]"

2. **Actions (Ações):** O que acontece depois
   - Exemplos: salvar arquivo, enviar email, criar tarefa
   - "ENTÃO [faça isso]"

3. **Filters (Filtros):** Condições para continuar
   - Exemplos: só emails importantes, só valores >R$ 100
   - "SE [condição] É VERDADEIRA"

4. **Routers (Roteadores):** Diferentes caminhos
   - Exemplos: se cliente VIP → ação A, senão → ação B
   - "ESCOLHA [caminho baseado em critério]"

5. **Iterators (Iteradores):** Repete para cada item
   - Exemplos: para cada anexo, para cada linha da planilha
   - "PARA CADA [item na lista]"

**Metáfora útil:**
- Trigger = Alarme do despertador
- Filter = "Só toca se for dia de semana"
- Action = Você levanta, escova dentes, toma café
- Router = "Se segunda, vai pra academia; se não, vai trabalhar direto"

### 1.3 Make vs Outras Ferramentas

**Make vs Zapier:**

**Make (Integromat):**
- ✅ Mais poderoso e flexível (lógica complexa)
- ✅ Interface visual superior (drag-and-drop intuitivo)
- ✅ Plano grátis mais generoso (1.000 ops/mês)
- ✅ Melhor para automações complexas (routers, iterators)
- ✅ Debugging mais fácil (vê cada passo visualmente)
- ✅ Preço melhor (custo/benefício)
- ❌ Curva de aprendizado um pouco maior
- ❌ Menos integrações que Zapier (mas 1.400+ é muito)

**Zapier:**
- ✅ Mais fácil para iniciantes absolutos
- ✅ Mais integrações (6.000+)
- ✅ Melhor documentação (mais tutoriais)
- ✅ Interface mais simples
- ❌ Plano grátis limitado (100 tarefas/mês)
- ❌ Menos flexível (dificulta lógicas complexas)
- ❌ Mais caro (planos pagos custam mais)
- ❌ Debugging mais difícil

**Make vs n8n:**

**n8n:**
- ✅ Open source (pode hospedar você mesmo)
- ✅ Grátis se self-hosted
- ✅ Flexibilidade máxima
- ❌ Requer conhecimento técnico (servidor, etc)
- ❌ Você mantém infraestrutura
- ❌ Não recomendado para iniciantes

**Recomendação:** 
- Aprenda **Make primeiro** (melhor custo-benefício, poderoso, fácil)
- Quando dominar Make, **Zapier** será trivial
- Se virar expert e precisar self-hosted, explore **n8n**

### 1.4 Quanto Custa (Realidade Brasileira 2025)

**Plano Gratuito (Free):**
- 1.000 operações/mês
- Integrações básicas
- Suficiente para: 10-15 automações simples rodando
- Cenários ilimitados
- Ótimo para: aprender, testar, uso pessoal

**Exemplo uso:** 
- 5 automações rodando 1x/hora = 3.600 ops/mês (não cabe)
- 10 automações rodando 3x/dia = 900 ops/mês (cabe!)

**Plano Core ($10,59/mês = ~R$ 55):**
- 10.000 operações/mês
- Todas integrações
- Webhooks ilimitados
- Apps premium (AI, databases avançados)
- Suficiente para: 50-100 automações rodando

**Plano Pro ($18,82/mês = ~R$ 98):**
- 40.000 operações/mês
- Usuários em equipe
- Prioridade de execução
- Para: freelancers profissionais, pequenas empresas

**Para você começando:**
- Mês 1-2: Use **grátis** (aprende + testa)
- Mês 3+: Se monetizando, upgrade para **Core** (~R$ 55)
- Cliente paga esse custo indiretamente no projeto

**ROI absurdo:** R$ 55/mês economiza 15h/semana = 60h/mês
- Se sua hora vale R$ 50: economiza R$ 3.000
- Se vale R$ 100: economiza R$ 6.000
- ROI: 5.400% a 10.800%

## 2. Primeira Automação: Tutorial Completo Passo-a-Passo

Vamos criar juntos: **"Email com anexo → Salvar no Drive + Extrair dados + Notificar Slack"**

Essa automação sozinha economiza ~1h/dia para quem recebe muitos emails com documentos.

### 2.1 Setup Inicial (10 minutos)

**Passo 1: Criar conta Make**

1. Acesse: https://make.com
2. Clique "Get started free"
3. Use email + senha OU login social (Google)
4. Confirme email
5. Faça tutorial rápido (5min - recomendo fazer)

**Passo 2: Familiarize-se com interface**

- **Dashboard:** lista seus cenários (automações)
- **Create scenario:** começa nova automação
- **Templates:** automações prontas para customizar
- **Connections:** apps conectados (Gmail, Drive, etc)
- **Organizations:** se trabalhar em equipe

**Passo 3: Criar novo cenário**

1. Clique "Create a new scenario"
2. Você verá tela em branco com um "+"
3. Essa é sua tela de trabalho (canvas)

**Interface explicada:**

- **Canvas:** área branca onde monta automação
- **Módulos:** blocos que executam ações (círculos)
- **Conexões:** linhas entre módulos = fluxo de dados
- **Toolbar superior:** salvar, testar, agendar, configurações
- **Sidebar direita:** configurações do módulo selecionado

### 2.2 Construindo Módulo por Módulo

**MÓDULO 1: Trigger - Gmail "Watch Emails"**

O que faz: Monitora caixa de entrada Gmail procurando novos emails

**Passos:**

1. Clique no "+" no canvas
2. Busque "Gmail" na caixa de busca
3. Clique no app Gmail
4. Escolha trigger: **"Watch Emails"**
5. Clique "Create a connection"
   - Selecione sua conta Google
   - Autorize Make a acessar Gmail (leitura apenas)
   - Conexão criada aparece verde ✓
6. Configure parâmetros:
   - **Folder:** INBOX (caixa de entrada)
   - **Criteria:** 
     * All emails: No
     * Enter criteria: Yes
     * Has attachment: Yes ← IMPORTANTE (só emails com anexo)
   - **Maximum number of results:** 10 (processa até 10 emails por rodada)
   - **From date:** (deixe vazio = processa desde a última execução)
7. Clique "OK"

**Testando módulo:**

1. Clique "Run once" (botão no canto inferior esquerdo)
2. Envie email para você mesmo COM ANEXO (qualquer arquivo)
3. Aguarde 10-20 segundos
4. Clique no módulo Gmail
5. Você verá output: dados do email capturado (remetente, assunto, anexos, etc)
6. Se funcionou: ✓ Módulo 1 completo

**Troubleshooting comum:**
- Não capturou? → Verifique se email tem anexo E está no INBOX
- Erro de conexão? → Reautorize conta Google
- "No data"? → Envie outro email e rode novamente

**MÓDULO 2: Action - Google Drive "Upload a File"**

O que faz: Pega anexo do email e salva no Google Drive

**Passos:**

1. Clique no "+" que aparece APÓS módulo Gmail (à direita)
2. Busque "Google Drive"
3. Escolha action: **"Upload a File"**
4. Clique "Create a connection" (autorize Google Drive)
5. Configure:
   - **Select destination:**
     * My Drive: Yes
     * Selecione pasta (crie uma chamada "Anexos Make" se quiser)
     * Ou clique "New folder" pra criar
   
   - **File name:** Aqui vem a mágica - usar dados do módulo anterior
     * Clique no campo
     * Aparece sidebar com outputs do módulo 1
     * Navegue: 1. Gmail > Attachments > 1. Name
     * Ou digite: `{{1.attachments[].name}}`
     * Isso pega nome original do arquivo
   
   - **File data:** O conteúdo binário do arquivo
     * Clique no campo
     * Selecione: 1. Gmail > Attachments > 1. Data
     * Ou digite: `{{1.attachments[].data}}`
   
   - **Convert:** No (queremos arquivo original)

6. Clique "OK"

**Entendendo mapeamento de dados:**

Quando você vê `{{1.attachments[].name}}`:
- `1` = módulo número 1 (Gmail)
- `attachments[]` = array de anexos (pode ter vários)
- `name` = propriedade "nome do arquivo"
- `[]` = Make itera automaticamente por cada anexo

**Testando:**

1. Clique "Run once" novamente
2. Make executa Módulo 1 (pega email) → Módulo 2 (salva Drive)
3. Abra seu Google Drive
4. Verifique se arquivo apareceu na pasta escolhida
5. ✓ Se sim, Módulo 2 completo!

**MÓDULO 3: Action - Slack "Create a Message"**

O que faz: Notifica equipe no Slack que arquivo foi salvo

**Passos:**

1. Clique "+" após módulo Google Drive
2. Busque "Slack"
3. Escolha: **"Create a Message"**
4. Conecte workspace Slack:
   - Se não tem Slack: pule esse módulo OU crie conta grátis (5min)
   - Autorize Make a postar mensagens
5. Configure:
   - **Channel:** 
     * Select from list: escolha canal (ex: #geral, #notificacoes)
     * Ou crie canal #automacoes-make pra testes
   
   - **Text:** Mensagem que aparece no Slack
     ```
     📎 Novo anexo salvo no Drive!
     
     Arquivo: {{2.name}}
     De: {{1.from.address}}
     Assunto: {{1.subject}}
     Link: {{2.webViewLink}}
     ```
     
     Breakdown:
     - `{{2.name}}` = nome arquivo (módulo 2 = Drive)
     - `{{1.from.address}}` = email remetente (módulo 1)
     - `{{1.subject}}` = assunto email
     - `{{2.webViewLink}}` = link direto pro arquivo no Drive
   
   - **Advanced settings:**
     * Username: Make Bot (ou nome que quiser)
     * Icon emoji: :robot_face: (opcional)

6. Clique "OK"

**Testando tudo junto:**

1. Clique "Run once" (executa 3 módulos em sequência)
2. Envie novo email com anexo
3. Aguarde 30 segundos
4. Verifique:
   - ✓ Email capturado
   - ✓ Arquivo no Drive
   - ✓ Mensagem no Slack

**Se tudo funcionou: parabéns! Primeira automação completa! 🎉**

### 2.3 Ativando Automação (Scheduling)

Até agora, automação só roda quando você clica "Run once". Vamos fazê-la rodar automaticamente.

**Passo 1: Configurar agendamento**

1. Clique no relógio (⏰ ícone scheduling) no módulo Gmail
2. Escolha intervalo:
   - **Every 15 minutes** (recomendado para começar)
   - Every hour (se email não é urgente)
   - Every 5 minutes (plano pago, consome mais ops)
3. Escolha horário de início (agora)
4. Clique "OK"

**Passo 2: Ativar cenário**

1. Toggle "ON" no canto superior esquerdo
2. Cenário fica azul = ativo ✓
3. Dê nome ao cenário: "Email anexos → Drive + Slack"
4. Salve (Ctrl+S ou botão Save)

**Pronto! Automação rodando 24/7 automaticamente.**

**Monitorando:**

- Dashboard mostra: quantas vezes rodou, sucessos, erros
- Clique no cenário > History pra ver execuções detalhadas
- Se erro aparecer: clique pra ver qual módulo falhou e por quê

### 2.4 Refinamentos e Melhorias

**Melhoria 1: Adicionar Filtro (só emails importantes)**

Entre módulo Gmail e Drive:

1. Clique na linha entre Gmail e Drive
2. Aparece opção "Set up a filter"
3. Clique
4. Configure condição:
   ```
   Label: Equals: IMPORTANT
   OU
   From: Contains: @cliente.com
   ```
5. Agora só processa emails que passam no filtro

**Melhoria 2: Organizar por remetente**

No módulo Drive, em vez de salvar tudo numa pasta:

**File name:** 
```
{{1.from.name}} - {{formatDate(1.date; "YYYY-MM-DD")}} - {{1.attachments[].name}}
```

Resultado: "João Silva - 2025-02-15 - contrato.pdf"

**Melhoria 3: Auto-reply agradecendo**

Adicione módulo 4:

1. Gmail > Send an Email
2. To: `{{1.from.address}}`
3. Subject: `Re: {{1.subject}}`
4. Content:
   ```
   Olá {{1.from.name}}!
   
   Recebi seu email e anexo foi salvo automaticamente.
   
   Em breve retorno.
   
   Obrigado!
   ```

**Sua automação agora:**
- Processa emails a cada 15 min
- Filtra só importantes
- Salva com nome organizado
- Notifica Slack
- Envia confirmação automática

**Isso economiza facilmente 1-2h/dia.**

## 3. Integrações Essenciais (Top 10)

### 3.1 Gmail + Google Sheets (Organização de Emails)

**Problema:** Emails importantes se perdem na caixa de entrada

**Solução:** Emails viram linhas estruturadas em planilha

**Automação:**
```
TRIGGER: Gmail - Watch Emails
  Filter: Label = IMPORTANT OU From contains "@empresa.com"

ACTION: Google Sheets - Add a Row
  Spreadsheet: "Controle Emails Importantes"
  Sheet: "2025"
  
  Valores mapeados:
  - Coluna A: {{1.date}}
  - Coluna B: {{1.from.name}}
  - Coluna C: {{1.from.address}}
  - Coluna D: {{1.subject}}
  - Coluna E: {{substring(1.text; 0; 200)}} (primeiros 200 chars)
  - Coluna F: {{1.webLink}} (link direto pro email)
  - Coluna G: Status (padrão: "Pendente")
```

**Valor:** 
- Dashboard de emails importantes
- Nunca perde email crítico
- Pode adicionar status, responsável, prazo
- Compartilha com equipe

**Tempo setup:** 15min
**Economia:** 30min/dia procurando emails

### 3.2 Google Forms + CRM + Email (Captura de Leads)

**Problema:** Lead preenche formulário, você copia manualmente pro CRM e manda email

**Solução:** Tudo automático em segundos

**Automação:**
```
TRIGGER: Google Forms - Watch Responses
  Form: "Interesse Produto X"

ACTION 1: Google Sheets - Add Row (backup)
  Todos dados do formulário

ACTION 2: HubSpot/Pipedrive/Notion - Create Contact
  Name: {{1.nome}}
  Email: {{1.email}}
  Phone: {{1.telefone}}
  Company: {{1.empresa}}
  Interest: {{1.produto_interesse}}
  Source: Google Forms
  Status: New Lead

ACTION 3: Gmail - Send Email (boas-vindas personalizado)
  To: {{1.email}}
  Subject: "Obrigado pelo interesse, {{1.nome}}!"
  Body: [Template personalizado com nome, interesse, próximos passos]

ACTION 4: Slack - Send Message
  Channel: #vendas
  Text: "🎯 Novo lead: {{1.nome}} ({{1.empresa}}) interessado em {{1.produto_interesse}}"
        "@vendedor, fazer follow-up!"
```

**Valor:**
- Lead cai no CRM automaticamente
- Email de boas-vindas instantâneo (aumenta conversão)
- Time de vendas notificado em tempo real
- Zero trabalho manual

**Conversão:** Empresas reportam +30-50% conversão com follow-up instantâneo

**Tempo setup:** 30min
**Economia:** 10min por lead × 50 leads/mês = 8h/mês

### 3.3 E-commerce (Shopify/Hotmart) + Logística + Email

**Problema:** Vendeu, agora tem que processar pedido manualmente

**Solução:** Da venda ao envio, tudo automático

**Automação:**
```
TRIGGER: Shopify - Watch Orders
  Filter: Financial Status = Paid

ACTION 1: Google Sheets - Add Row (controle financeiro)
  - Pedido #
  - Cliente
  - Produto
  - Valor
  - Data
  - Status

ACTION 2: Calculate Shipping (API Correios ou Melhor Envio)
  Origin: [seu CEP]
  Destination: {{1.shipping_address.zip}}
  Weight: {{1.total_weight}}
  Dimensions: [produto]

ACTION 3: Gmail - Send Email (confirmação com tracking)
  To: {{1.customer.email}}
  Subject: "Pedido #{{1.order_number}} confirmado!"
  Body: 
    "Oi {{1.customer.first_name}}!
    
    Seu pedido foi confirmado e está sendo preparado.
    
    Detalhes:
    - Produto: {{1.line_items[].title}}
    - Valor: R$ {{formatNumber(1.total_price; 2; ","; ".")}}
    - Previsão envio: 1-2 dias úteis
    - Frete: R$ {{2.price}} ({{2.delivery_time}} dias)
    
    Em breve você recebe código de rastreio!
    
    Obrigado pela compra! 🎉"

ACTION 4: Trello/Notion - Create Card
  Board: Pedidos
  List: Separar
  Title: "Pedido #{{1.order_number}} - {{1.customer.name}}"
  Description: Produtos, endereço, observações
  Due date: +1 dia
```

**Valor:**
- Zero trabalho manual pós-venda
- Cliente recebe confirmação instantânea (melhora experiência)
- Equipe logística sabe o que separar
- Controle financeiro automático

**Economia:** 15min por pedido × 100 pedidos/mês = 25 horas/mês

### 3.4 Curadoria de Conteúdo (RSS + Notion + Slack)

**Problema:** Acompanhar 20+ blogs para ficar atualizado no setor

**Solução:** Robô lê tudo, resume, organiza pra você

**Automação:**
```
TRIGGER: RSS - Watch RSS Feed Items
  URL: [feeds dos blogs que segue]
  Intervalo: 1x por dia

ACTION 1: OpenAI - Create Completion (resumir com IA)
  Prompt: "Resuma este artigo em 3 bullets:
           
           Título: {{1.title}}
           Conteúdo: {{1.content}}
           
           Formato:
           - Tema principal
           - Insights-chave (2-3)
           - Relevância para [seu setor]"

ACTION 2: Notion - Create Page
  Database: Content Curation
  Properties:
    - Title: {{1.title}}
    - URL: {{1.url}}
    - Published: {{1.pubDate}}
    - Source: {{1.feed.title}}
    - Summary: {{2.result}}
    - Tags: [auto-detect com IA ou manual]
    - Status: To Read

ACTION 3: Filter + Slack (só muito relevante)
  Condition: Se summary contém "keyword importante" OU source = "blog VIP"
  Then: Post no Slack #conteudo-must-read
```

**Valor:**
- Acompanha 20+ fontes sem ler tudo
- IA resume pra você (economiza 90% tempo leitura)
- Tudo organizado no Notion
- Time recebe só o mais relevante

**Tempo setup:** 45min
**Economia:** 5-10h/semana de curadoria manual

### 3.5 Onboarding Automático de Clientes/Funcionários

**Automação:**
```
TRIGGER: Google Forms - New Response (form onboarding)

ACTION 1: Gmail - Create account (G Suite API)
ACTION 2: Google Drive - Create folder structure
  /[Nome]/Documentos
  /[Nome]/Projetos
  /[Nome]/Recursos
ACTION 3: Notion - Add to Employee Database
ACTION 4: Slack - Add to workspace + Send welcome DM
ACTION 5: Trello - Create onboarding checklist
  - Dia 1: [tarefas]
  - Semana 1: [tarefas]
  - Mês 1: [tarefas]
ACTION 6: Google Calendar - Schedule 1:1 meetings
ACTION 7: Gmail - Send welcome email com credenciais e próximos passos
```

**Economia:** Onboarding manual (8h) → automático (15min)

## 4. Técnicas Avançadas

### 4.1 Routers (Múltiplos Caminhos Condicionais)

**Cenário:** Lead preenche formulário. Ação depende do orçamento.

**Sem router (ruim):** Mesmo processo pra todo mundo

**Com router (inteligente):**
```
TRIGGER: Google Forms - New Lead

ROUTER (divide em 3 caminhos):

  PATH 1 - VIP (Budget > R$ 50k):
    Filter: {{1.orcamento}} > 50000
    → Slack: Notifica CEO diretamente
    → Calendar: Agenda reunião com fundador (automático)
    → Gmail: Email personalizado de C-level
    → CRM: Tag "Enterprise"
    
  PATH 2 - Médio (R$ 10k - R$ 50k):
    Filter: {{1.orcamento}} >= 10000 AND <= 50000
    → Slack: Notifica gerente vendas
    → Gmail: Email template vendas consultivas
    → CRM: Tag "Mid-market"
    → Calendar: Convite webinar exclusivo
    
  PATH 3 - Self-service (< R$ 10k):
    Filter: {{1.orcamento}} < 10000
    → Gmail: Email automação com trial gratuito
    → CRM: Tag "SMB"
    → Autopilot: Sequência emails educacionais
```

**Por que é poderoso:**
- Tratamento personalizado baseado em valor
- Eficiência: C-level não perde tempo com pequeno
- Conversão: cada segmento recebe flow ideal

**Como configurar:**
1. Adicione módulo "Router" após trigger
2. Clique "+" em cada braço do router
3. Configure filter em cada caminho
4. Adicione ações específicas

### 4.2 Iterators (Loop em Arrays)

**Problema:** Email com 5 anexos. Quer salvar cada um em pasta diferente baseado no tipo.

**Solução:** Iterator processa cada anexo individualmente

**Automação:**
```
TRIGGER: Gmail - Watch Emails (com anexos)

ITERATOR: Para cada anexo
  Input: {{1.attachments[]}}
  
  ROUTER (dentro do iterator):
    
    PATH 1 - PDFs:
      Filter: {{1.attachments[].name}} ends with ".pdf"
      → Drive: Upload to /Contratos
      → Notion: Log em database Contratos
    
    PATH 2 - Imagens:
      Filter: {{1.attachments[].name}} matches ".jpg|.png|.jpeg"
      → Drive: Upload to /Imagens
      → Compress image (módulo image processing)
    
    PATH 3 - Planilhas:
      Filter: {{1.attachments[].name}} ends with ".xlsx"
      → Drive: Upload to /Planilhas
      → Sheets: Import data (se formato conhecido)
    
    PATH 4 - Outros:
      Default (sem filter)
      → Drive: Upload to /Outros
      → Slack: Notifica "arquivo desconhecido"
```

**Resultado:** 1 email com 5 anexos → 5 arquivos organizados automaticamente

**Como configurar:**
1. Adicione módulo "Iterator" após fonte de dados
2. Selecione array para iterar (ex: attachments[])
3. Módulos depois do iterator processam 1 item por vez
4. Make roda loop automaticamente

### 4.3 Error Handling (Tratamento de Erros)

**Problema:** Automação falha às vezes (API fora, conexão ruim, etc)

**Sem error handling:** Automação para, dados se perdem

**Com error handling:** Automação tenta resolver ou notifica

**Exemplo:**
```
TRIGGER: Novo pedido e-commerce

TRY:
  ACTION 1: Upload invoice to Drive
  
CATCH (se ACTION 1 falha):
  → Retry 3x (intervalo 1min entre tentativas)
  → Se ainda falha:
    → Save invoice locally (fallback storage)
    → Slack: Notifica tech team com erro específico
    → Google Sheets: Log erro (timestamp, order_id, error_message)
    → Continue processando resto (não trava tudo)
  
TRY:
  ACTION 2: Send email to customer

CATCH:
  → Wait 5min
  → Retry 2x
  → If still fails: Add to "retry queue" (outro cenário processa depois)
```

**Como configurar:**
1. Clique direito no módulo
2. "Add error handler"
3. Escolha tipo:
   - Ignore (continua como se nada)
   - Retry (tenta X vezes)
   - Commit (aceita erro e continua)
   - Resume (executa ações alternativas)
   - Rollback (desfaz mudanças)

**Best practices:**
- Always add error handling em módulos críticos
- Log erros pra análise posterior
- Notifique equipe em erros graves
- Tenha fallback (plano B)

### 4.4 Webhooks (Integrações Custom)

**O que é:** URL única que recebe dados de qualquer lugar

**Quando usar:**
- App não tem integração nativa no Make
- Quer triggerar automação de outro sistema
- API custom da empresa

**Exemplo:**
```
CENÁRIO MAKE:

TRIGGER: Webhook - Custom Webhook
  URL gerada: https://hook.make.com/abc123xyz

ACTIONS: [processar dados recebidos]

---

EM OUTRO SISTEMA (seu site, app, etc):

Quando evento acontece:
  POST para https://hook.make.com/abc123xyz
  Body: {
    "user_id": 123,
    "action": "purchase",
    "value": 299.90
  }

Make recebe → processa → executa ações
```

**Caso real:** Formulário custom no seu site → envia dados pro webhook → Make processa

**Como configurar:**
1. Adicione módulo "Webhooks - Custom webhook"
2. Make gera URL única
3. Configure seu sistema pra enviar dados pra essa URL
4. Dados chegam no Make → automação roda

**Poder:** Integra QUALQUER coisa, até sistemas proprietários

## 5. Casos de Uso que Geram Valor (Templates Prontos)

### 5.1 Para Freelancers

**Automação 1: Invoice Automático**

```
TRIGGER: Trello - Card moved to "Concluído"

ACTION 1: Google Docs - Generate from template
  Template: Invoice padrão
  Replace:
    {{cliente}}: {{1.card.name}}
    {{valor}}: {{1.custom_field.valor}}
    {{data}}: {{formatDate(now; "DD/MM/YYYY")}}
    {{descricao}}: {{1.card.desc}}
  
  Generate PDF

ACTION 2: Gmail - Send Email
  To: {{1.custom_field.email_cliente}}
  Subject: "Invoice #{{1.card.idShort}} - {{formatDate(now; "MM/YYYY")}}"
  Attachments: {{2.pdf}}
  Body: [Template profissional]

ACTION 3: Google Sheets - Add row (financeiro)
  - Data emissão
  - Cliente
  - Valor
  - Status: Enviado
  - Vencimento: +15 dias

ACTION 4: Google Calendar - Create reminder
  Date: +14 dias (1 dia antes vencimento)
  Title: "Checar pagamento {{1.card.name}}"
```

**Economia:** 30min por projeto × 10 projetos/mês = 5h/mês

**Automação 2: Time Tracking Automático**

```
TRIGGER: Toggl - Timer Stopped

ACTION: Google Sheets - Add Row
  Sheet: "Horas 2025"
  Values:
    - Data: {{1.end}}
    - Cliente: {{1.project.name}}
    - Tarefa: {{1.description}}
    - Horas: {{formatNumber(1.duration/3600; 2)}}
    - Valor hora: R$ 80 (ou busca de tabela preços)
    - Valor total: =Horas * Valor hora
```

**Valor:** Relatório automático pra cobrar clientes. Precisão 100%.

### 5.2 Para Pequenas Empresas

**Automação: Onboarding Funcionário Completo**

```
TRIGGER: Google Forms - Novo Funcionário

[Executa tudo em paralelo para speed]

ACTION 1: Google Workspace - Create User
  Email: {{lowercase(1.nome)}}.{{lowercase(1.sobrenome)}}@empresa.com
  Password: [auto-generated]
  Send welcome email: Yes

ACTION 2: Google Drive - Create Folder Structure
  /Funcionarios/{{1.nome}}/
    - Documentos
    - Projetos
    - 1:1s
  Permissions: Share com manager

ACTION 3: Notion - Add to Database
  Database: Team
  Properties:
    - Nome: {{1.nome}}
    - Cargo: {{1.cargo}}
    - Department: {{1.departamento}}
    - Start Date: {{1.data_inicio}}
    - Manager: {{1.gestor}}
    - Status: Active

ACTION 4: Slack - Multi-step
  - Add to workspace
  - Add to channels baseado em dept
  - Send DM:
    "Bem-vindo {{1.nome}}! 🎉
    
    Seu email: [email criado]
    Senha temporária: [gerada]
    
    Próximos passos:
    1. Acesse email e mude senha
    2. Preencha perfil Slack
    3. Confira Notion (tarefas onboarding)
    4. Reunião 1:1 com {{1.gestor}} agendada para [data]"

ACTION 5: Trello - Create Board
  Name: "Onboarding - {{1.nome}}"
  Lists: Dia 1 | Semana 1 | Mês 1 | Concluído
  Cards: [Checklist de onboarding predefinido]
  Assign: {{1.gestor}}

ACTION 6: Google Calendar - Schedule Meetings
  - 1:1 com gestor (Dia 1, 10h)
  - Tour escritório (Dia 1, 14h)
  - Apresentação equipe (Dia 2, 11h)
  - Check-in semanal (toda sexta, 15h)

ACTION 7: Gmail - Send Manual Recursos Humanos
  Attachments: 
    - Manual funcionário (PDF)
    - Política home office
    - Benefícios
    - Contato TI
```

**Impacto:**
- Manual: 8 horas (RH + TI + Manager)
- Automação: 10 minutos (só preencher form)
- Economia: ~R$ 800 em horas-homem por contratação
- Experiência: Funcionário impressionado desde dia 1

### 5.3 Para Uso Pessoal (Exemplos Práticos)

**Automação 1: Controle Financeiro Automático**

```
TRIGGER: Gmail - Watch Emails
  Filter: From contains "extrato" OR "fatura" OR "cobranca"

ACTION 1: OpenAI - Extract Data (IA extrai valores)
  Prompt: "Deste email de banco/fatura, extraia:
           - Data: [formato DD/MM/YYYY]
           - Valor: [só número]
           - Categoria: [alimentacao|transporte|moradia|lazer|etc]
           - Descrição: [breve]
           
           Email: {{1.text}}"

ACTION 2: Google Sheets - Add Row
  Sheet: "Financas 2025"
  Values:
    - Data: {{2.data}}
    - Categoria: {{2.categoria}}
    - Descrição: {{2.descricao}}
    - Valor: {{2.valor}}
    - Tipo: Despesa

ACTION 3: Calculate Monthly Total
  Formula: =SUMIF(categoria, {{2.categoria}}, valor)

ACTION 4: IF total > orçamento categoria:
  → Gmail: Send alert to yourself
    "⚠️ Alerta: você gastou R$ {{3.total}} em {{2.categoria}} este mês.
    Orçamento: R$ {{limite}}
    Excedeu: R$ {{3.total - limite}}"
```

**Valor:** Controle financeiro sem abrir app, sem planilha manual

**Automação 2: Digest Diário Personalizado**

```
SCHEDULE: Every day 7am

ACTION 1: Weather API - Get forecast
  Location: Sua cidade
  
ACTION 2: Google Calendar - Get today events

ACTION 3: Notion - Query tasks
  Filter: Due date = today OR overdue

ACTION 4: RSS - Get top news (fontes escolhidas)

ACTION 5: Aggregate tudo

ACTION 6: Gmail - Send Email
  To: você
  Subject: "🌅 Seu dia {{formatDate(now; "DD/MM")}}"
  Body:
    "Bom dia!
    
    ☁️ CLIMA:
    {{1.condition}} - {{1.temp_min}}°C a {{1.temp_max}}°C
    
    📅 AGENDA ({{2.count}} eventos):
    {{#each 2.items}}
    - {{this.time}}: {{this.summary}}
    {{/each}}
    
    ✅ TAREFAS ({{3.count}} pendentes):
    {{#each 3.items}}
    - {{this.title}} {{if this.overdue}}⚠️ ATRASADO{{/if}}
    {{/each}}
    
    📰 NOTÍCIAS:
    {{#each 4.items limit=5}}
    - {{this.title}} [{{this.source}}]
    {{/each}}
    
    Bom dia produtivo! 💪"
```

**Impacto:** Começa dia informado, organizado, em 2 minutos de leitura

## 6. Como Monetizar Automação (R$ 500 - R$ 10.000 por Projeto)

### 6.1 Modelos de Precificação

**Modelo 1: Por Hora (Iniciante)**
- Júnior (0-6 meses exp): R$ 50-80/h
- Pleno (6-18 meses exp): R$ 80-150/h
- Sênior (18+ meses exp): R$ 150-250/h

**Quando usar:** Projetos imprevisíveis, escopo não claro

**Modelo 2: Por Projeto (Recomendado)**

Baseado em complexidade + valor entregue:

| Tipo | Módulos | Tempo | Preço |
|------|---------|-------|-------|
| Simples | 2-3 | 2-4h | R$ 500-1.500 |
| Médio | 5-10 | 6-12h | R$ 1.500-4.000 |
| Complexo | 10-20 | 15-30h | R$ 4.000-10.000 |
| Enterprise | 20+ | 40+h | R$ 10.000+ |

**Exemplo:**
- Automação "Form → CRM → Email": Simples = R$ 800
- Automação "E-commerce completo": Complexo = R$ 6.000

**Modelo 3: Valor (Avançado - Melhor ROI)**

Precifique baseado no valor que cliente economiza:

Cliente economiza 20h/semana = 80h/mês
Valor hora funcionário: R$ 50
Economia: R$ 4.000/mês

**Seu preço:**
- Setup: R$ 3.000 (paga em 3 semanas de economia)
- Manutenção: R$ 500/mês (12,5% da economia)
- ROI cliente: 1.200%+ no primeiro ano

**Cliente fica feliz (economiza muito) + você ganha bem**

**Modelo 4: Retainer Mensal (Melhor para você)**

Pacotes:

| Plano | Automações | Suporte | Preço |
|-------|-----------|---------|-------|
| Starter | até 5 | Email | R$ 500/mês |
| Business | até 15 | Slack + 2h/mês ajustes | R$ 1.200/mês |
| Enterprise | ilimitado | Prioridade + 8h/mês | R$ 3.000/mês |

**Vantagem:** Receita recorrente previsível

### 6.2 Proposta que Vende (Template)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROPOSTA: Automação [Nome Processo]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PARA: [Cliente]
DE: [Seu Nome] - Automation Specialist
DATA: [Data]

━━━ SITUAÇÃO ATUAL ━━━

Processo: [Nome]
Frequência: [X vezes/dia, semana, mês]
Tempo por execução: [Xh]
Pessoas envolvidas: [quantas]

CUSTO ATUAL:
- Tempo total: [Xh/mês]
- Custo hora: R$ [Y]
- Custo mensal: R$ [X × Y] = R$ [TOTAL]
- Custo anual: R$ [TOTAL × 12]

PROBLEMAS IDENTIFICADOS:
- [Problema 1: ex: erro humano frequente]
- [Problema 2: ex: demora excessiva]
- [Problema 3: ex: falta rastreabilidade]

━━━ SOLUÇÃO PROPOSTA ━━━

Automação com Make conectando:
- [App 1]
- [App 2]
- [App 3]

FUNCIONAMENTO:
1. [Trigger]: Quando [evento]
2. [Action 1]: Sistema automaticamente [faz X]
3. [Action 2]: E então [faz Y]
4. [Action 3]: Por fim [faz Z]
5. [Notificação]: Equipe recebe confirmação

BENEFÍCIOS:
✅ Reduz tempo: [Xh] → [Ymin] (redução de [%])
✅ Elimina erros manuais
✅ Rastreabilidade completa (logs)
✅ Escalável (processa 10 ou 1.000, mesmo esforço)
✅ Funciona 24/7 sem intervenção

━━━ INVESTIMENTO ━━━

SETUP (one-time):
- Mapeamento processo: R$ [X]
- Desenvolvimento automação: R$ [Y]
- Testes + ajustes: R$ [Z]
- Treinamento equipe: R$ [W]
TOTAL SETUP: R$ [X+Y+Z+W]

MENSAL (recorrente):
- Monitoramento: R$ [X]/mês
- Ajustes/melhorias (2h/mês): R$ [Y]/mês
- Suporte: R$ [Z]/mês
TOTAL MENSAL: R$ [X+Y+Z]/mês

FERRAMENTAS (cliente paga):
- Make: R$ 55/mês (plano Core)
- [Outras se necessário]

━━━ ROI ━━━

Economia mensal: R$ [economia - custo mensal]
Payback: [setup ÷ economia mensal] meses
ROI primeiro ano: [((economia×12 - setup - mensal×12) ÷ (setup + mensal×12)) × 100]%

Exemplo:
- Economia: R$ 4.000/mês
- Setup: R$ 3.000
- Mensal: R$ 500
- Payback: 0,75 mês (~3 semanas)
- ROI ano 1: 1.050%

━━━ CRONOGRAMA ━━━

Semana 1:
- Reunião alinhamento (1h)
- Mapeamento detalhado processo (2h)
- Aprovação escopo

Semana 2:
- Desenvolvimento automação
- Testes internos

Semana 3:
- Testes com equipe cliente
- Ajustes baseado em feedback

Semana 4:
- Go-live
- Treinamento equipe (2h)
- Documentação entregue

TIMELINE TOTAL: 4 semanas

━━━ GARANTIAS ━━━

✅ Automação funcionando 100% ou reembolso
✅ 30 dias de suporte pós-go-live inclusos
✅ Documentação completa entregue
✅ Treinamento gravado para consulta

━━━ PRÓXIMOS PASSOS ━━━

1. Aprovação desta proposta
2. Assinatura contrato
3. Pagamento 50% setup (início trabalho)
4. Kickoff meeting agendado
5. Pagamento 50% restante (go-live)

VALIDADE PROPOSTA: 15 dias

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Seu Nome]
Automation Specialist
[Email] | [Telefone] | [LinkedIn]
```

**Taxa de conversão:** Propostas assim convertem 40-60% (vs 10-20% propostas genéricas)

### 6.3 Onde Encontrar Clientes

**Online:**
1. Workana, 99Freelas (Brasil)
2. Upwork, Fiverr (internacional)
3. LinkedIn (poste projetos, DM em empresas)
4. Comunidades: grupos Slack/Discord de no-code

**Networking:**
1. Eventos tech/startups locais
2. Meetups de automação
3. Ofereça grátis pra 2-3 primeiros (portfolio)

**Prospecção ativa:**
1. Identifica empresas usando apps integráveis
2. Envia proposta: "Vi que usam X e Y, posso conectá-los automaticamente"
3. Taxa resposta: 5-10% (mas qualificados)

## 7. Exercício Prático (2 Horas)

**Objetivo:** Sair deste módulo com 3 automações funcionando que você pode mostrar em portfolio

**PARTE 1: Automação Pessoal (45min)**

Escolha 1:
- A) Finanças: Emails de banco → Sheets (categoriza gastos)
- B) Produtividade: Todo list Notion → Reminder Slack/Email
- C) Aprendizado: RSS blogs → Notion (com resumo IA)

**Entrega:** Automação funcionando + screenshot

**PARTE 2: Automação Profissional (45min)**

Escolha 1:
- A) Lead capture: Form → Sheets + Email + CRM
- B) Atendimento: Email suporte → Trello card + Auto-reply
- C) Relatório: Dados (qualquer fonte) → Sheet + Email digest diário

**Entrega:** Automação funcionando + documentação (o que faz, por quê, ROI)

**PARTE 3: Automação Portfolio (30min)**

Crie algo impressionante para mostrar:
- Complexo (5+ módulos)
- Útil (resolve problema real)
- Visual (gráficos, dashboards)

Ideias:
- E-commerce mini: Produto vendido → tudo automático
- Dashboard executivo: Várias fontes → 1 email/sheet
- Onboarding completo: Form → 8 ações simultâneas

**Entrega:**
1. Vídeo 2min mostrando funcionando (Loom)
2. Descrição completa
3. "Antes vs Depois" (tempo economizado)

**BÔNUS: Publique no LinkedIn**

Post modelo:
```
Acabei de criar minha [número]ª automação no-code! 🤖

Problema: [descrever]
Solução: [descrever]
Resultado: [tempo economizado, erro eliminado, etc]

Ferramentas: Make + [apps]

[Imagem/vídeo da automação]

#nocode #automacao #produtividade #make
```

**Isso atrai recrutadores e clientes.**

---

## Próximos Passos

**Módulo 5: Notion para Produtividade**
- Notion como segundo cérebro
- Gestão de projetos e tarefas
- Databases e relations
- Base de conhecimento
- Integrações Make + Notion (power combo!)

**Prepare-se para:** Organização nivel expert que impressiona em entrevistas

Nos vemos lá! 🚀

---

**© 2025 FETD - Formação em Engenharia de Intenção**
