# Módulo 6: Google Workspace Avançado

**Trilha:** Talento Emergente
**Duração:** 60 minutos
**Objetivo:** Dominar Google Workspace como profissional

---

## Introdução

Google Workspace (Gmail, Drive, Sheets, Docs, Calendar) é usado por 90%+ das empresas.

Dominar vai além de "saber usar". É usar PROFISSIONALMENTE com automações, organização e produtividade máxima.

**Dados:** Profissionais avançados em Google Workspace economizam 8-12h/semana vs usuários básicos.

## 1. Gmail Profissional

### 1.1 Labels e Filtros Automatizados

**Problema:** Inbox com 500+ emails. Caos total.

**Solução:** Sistema de labels + filtros automáticos.

**Estrutura de Labels:**
```
📥 0-INBOX (tudo processado)
├── @Action (preciso fazer algo)
├── @Waiting (aguardando resposta)
├── @Read (ler depois)
└── @Archive (referência)

📁 1-PROJETOS
├── Projeto A
├── Projeto B
└── Projeto C

📁 2-CLIENTES
├── Cliente X
├── Cliente Y
└── Cliente Z

📁 3-CATEGORIAS
├── Financeiro
├── Contratos
├── Marketing
└── Tech
```

**Filtros Automáticos:**

**Filtro 1: Emails de clientes VIP**
```
From: (cliente1@empresa.com OR cliente2@empresa.com)
→ Apply label: Clientes/VIP
→ Star it
→ Never send to spam
→ Mark as important
```

**Filtro 2: Newsletters para ler depois**
```
From: (newsletter@* OR noreply@*)
Has words: unsubscribe
→ Skip inbox
→ Apply label: @Read
→ Mark as read
```

**Filtro 3: Receipts/Financeiro**
```
Subject: (invoice OR receipt OR payment OR fatura)
→ Apply label: Financeiro/Receipts
→ Skip inbox
→ Star it
```

**Criar filtro:**
1. Pesquise exemplo do email
2. Click ⋮ (3 pontos)
3. "Filter messages like this"
4. Refine critérios
5. "Create filter"

**Meta: Inbox Zero diariamente.**

### 1.2 Templates e Respostas Prontas

**Canned Responses (Respostas Prontas):**

Ative: Settings → Advanced → Templates → Enable

**Template 1: Follow-up Educado**
```
Assunto: Re: [assunto]

Oi [Nome],

Espero que esteja bem!

Estou acompanhando nossa conversa sobre [tópico].

Você conseguiu [o que estava esperando]?

Qualquer dúvida, estou à disposição.

Abraço,
[Seu Nome]
```

**Template 2: Agendar Reunião**
```
Assunto: Reunião: [tópico]

Oi [Nome],

Ótimo! Vamos agendar.

Estes horários funcionam pra você?
- [Data 1] às [hora]
- [Data 2] às [hora]
- [Data 3] às [hora]

Duração estimada: [X] minutos

Me confirma qual melhor!

Abs,
[Seu Nome]
```

**Como usar:**
1. Compose
2. Click ⋮ → Templates → Insert template
3. Personaliza [campos]
4. Envia

**Economia:** 5-10min por email × 20 emails/semana = 2h/semana

### 1.3 Atalhos de Teclado (Gmail Ninja)

Ative: Settings → General → Keyboard shortcuts → ON

**Essenciais:**
- `c` - Compose (novo email)
- `r` - Reply
- `a` - Reply all
- `f` - Forward
- `e` - Archive
- `#` - Delete
- `s` - Star
- `gi` - Go to Inbox
- `gl` - Go to label
- `j/k` - Email anterior/próximo
- `o` - Abrir email
- `u` - Volta pra lista

**Avançados:**
- `l` - Apply label (abre menu)
- `v` - Move to (folder)
- `Shift+i` - Mark as read
- `Shift+u` - Mark as unread
- `Shift+3` - Delete
- `Tab+Enter` - Envia email

**Desafio:** Processe 50 emails sem usar mouse.

### 1.4 Múltiplas Caixas de Entrada

Settings → Inbox → Inbox type → Multiple Inboxes

**Config:**
- **Caixa 1:** is:starred (favoritos)
- **Caixa 2:** label:@Action (preciso agir)
- **Caixa 3:** label:@Waiting (aguardando)
- **Caixa 4:** is:unread (não lidos)

**Resultado:** Vê tudo importante num golpe de vista.

## 2. Google Sheets Avançado

### 2.1 Fórmulas Profissionais

**1. QUERY (SQL-like em Sheets)**

Mais poderosa que FILTER, SORT, etc combinados.

```
=QUERY(A1:F100, "SELECT A, B, SUM(F) WHERE C = 'Vendas' GROUP BY A, B ORDER BY SUM(F) DESC")
```

Tradução: Seleciona colunas A e B, soma coluna F, filtra onde C = 'Vendas', agrupa por A e B, ordena por soma decrescente.

**Exemplos práticos:**

**Dashboard de vendas:**
```
=QUERY(Vendas!A:F, 
  "SELECT A, SUM(F) 
   WHERE B >= date '2025-01-01' 
   GROUP BY A 
   LABEL A 'Produto', SUM(F) 'Total Vendido'")
```

**Top 10 clientes:**
```
=QUERY(Clientes!A:D,
  "SELECT A, SUM(D)
   GROUP BY A
   ORDER BY SUM(D) DESC
   LIMIT 10")
```

**2. ARRAYFORMULA (Aplica fórmula em toda coluna)**

Em vez de arrastar fórmula:

```
=ARRAYFORMULA(IF(A2:A="", "", B2:B * C2:C))
```

Multiplica coluna B por C automaticamente. Se adicionar linha nova, já calcula.

**3. IMPORTRANGE (Importa de outra planilha)**

```
=IMPORTRANGE("URL_da_planilha", "Sheet1!A1:F100")
```

**Caso de uso:** Consolida dados de múltiplas planilhas num dashboard central.

**4. SPARKLINE (Gráficos mini)**

```
=SPARKLINE(B2:F2, {"charttype", "line"; "color", "blue"})
```

Gráfico na célula! Ótimo para dashboards compactos.

**5. Combos poderosos:**

**Calcular idade:**
```
=DATEDIF(A2, TODAY(), "Y") & " anos"
```

**Extrair domínio de email:**
```
=REGEXEXTRACT(A2, "@(.+)")
```

**Remover espaços extras:**
```
=TRIM(A2)
```

**Primeira letra maiúscula:**
```
=PROPER(A2)
```

### 2.2 Formatação Condicional Avançada

**Caso 1: Semáforo de status**

Seleciona coluna Status:
- Format → Conditional formatting
- Format cells if: Text is exactly "Atrasado" → Background red
- Add another rule: Text is exactly "Em dia" → Background green
- Add another rule: Text is exactly "Alerta" → Background yellow

**Caso 2: Heatmap de valores**

Seleciona range numérico:
- Conditional formatting
- Format cells if: Color scale
- Min: Red, Midpoint: Yellow, Max: Green

**Caso 3: Destacar duplicatas**

Seleciona coluna:
- Custom formula: `=COUNTIF($A$2:$A, A2)>1`
- Background: Yellow

**Caso 4: Linhas alternadas (zebra)**

Seleciona range:
- Custom formula: `=MOD(ROW(), 2)=0`
- Background: Light gray

### 2.3 Dashboards Profissionais

**Estrutura:**

**Sheet 1: RAW DATA (dados brutos)**
- Importa de fonte (Form, API, manual)
- Nunca edita aqui (só adiciona linhas)

**Sheet 2: PROCESSED (dados processados)**
- Fórmulas limpam/transformam dados
- QUERY, ARRAYFORMULA, etc

**Sheet 3: DASHBOARD (visualização)**
- Charts
- Cards com métricas principais
- Sparklines
- Conditional formatting

**Exemplo Dashboard Vendas:**

```
┌────────────────────────────────────────┐
│ 📊 VENDAS - JANEIRO 2025               │
├────────────────────────────────────────┤
│                                         │
│ R$ 125.430 │ 423 pedidos │ R$ 296,50  │
│ Total      │ Quantidade  │ Ticket Médio│
│            │             │             │
│ ▓▓▓▓▓▓░░░░ 65% da meta                │
│                                         │
│ [Gráfico Evolução Diária - Line]      │
│                                         │
│ TOP 5 PRODUTOS      │ TOP 5 CLIENTES  │
│ 1. Produto A  R$ X  │ 1. Cliente A    │
│ 2. Produto B  R$ Y  │ 2. Cliente B    │
│ 3. ...              │ ...             │
│                                         │
│ [Gráfico Pizza: Vendas por Categoria] │
│                                         │
└────────────────────────────────────────┘
```

**Fórmulas usadas:**

**Total vendido:**
```
=SUM(Processed!F:F)
```

**Quantidade pedidos:**
```
=COUNTA(Processed!A:A)-1
```

**Ticket médio:**
```
=Total/Quantidade
```

**Progress bar meta:**
```
=REPT("▓", ROUND(Total/Meta*10, 0)) & REPT("░", 10-ROUND(Total/Meta*10, 0)) & " " & TEXT(Total/Meta, "0%")
```

**Top 5 produtos:**
```
=QUERY(Processed!A:F, "SELECT A, SUM(F) GROUP BY A ORDER BY SUM(F) DESC LIMIT 5")
```

### 2.4 Apps Script (Automações Custom)

**O que é:** JavaScript que roda no Google Sheets. Automatiza qualquer coisa.

**Exemplos:**

**1. Enviar email quando célula muda:**

Extensions → Apps Script:

```javascript
function onEdit(e) {
  var sheet = e.source.getActiveSheet();
  var range = e.range;
  
  if (sheet.getName() == "Vendas" && range.getColumn() == 5) {
    if (range.getValue() == "Aprovado") {
      MailApp.sendEmail({
        to: "gestor@empresa.com",
        subject: "Venda aprovada",
        body: "Venda na linha " + range.getRow() + " foi aprovada."
      });
    }
  }
}
```

**2. Limpar dados automaticamente:**

```javascript
function cleanData() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var range = sheet.getDataRange();
  var values = range.getValues();
  
  for (var i = 0; i < values.length; i++) {
    values[i][1] = values[i][1].trim(); // Remove espaços
    values[i][2] = values[i][2].toLowerCase(); // Lowercase
  }
  
  range.setValues(values);
}
```

Agendar: Triggers → Add trigger → Time-driven → Every day at 2am

**3. Integração API externa:**

```javascript
function fetchDataFromAPI() {
  var response = UrlFetchApp.fetch("https://api.exemplo.com/data");
  var data = JSON.parse(response.getContentText());
  
  var sheet = SpreadsheetApp.getActiveSheet();
  sheet.getRange(2, 1, data.length, data[0].length).setValues(data);
}
```

**Poder:** Sheets vira mini-aplicação web.

## 3. Google Drive Organizado

### 3.1 Estrutura de Pastas Profissional

**Método PARA:**

```
📁 My Drive
│
├── 📁 0-INBOX (tudo começa aqui)
│
├── 📁 1-PROJETOS (ativos)
│   ├── Projeto A
│   │   ├── Docs
│   │   ├── Assets
│   │   └── Archive
│   └── Projeto B
│
├── 📁 2-ÁREAS (responsabilidades contínuas)
│   ├── Marketing
│   ├── Vendas
│   ├── Produto
│   └── Administrativo
│
├── 📁 3-RECURSOS (referência)
│   ├── Templates
│   ├── Brand Assets
│   ├── Documentação
│   └── Contratos
│
└── 📁 4-ARQUIVO (concluído/inativo)
    ├── 2024
    ├── 2023
    └── Older
```

**Convenções de nomenclatura:**

**Arquivos:**
```
YYYY-MM-DD_TipoDocumento_Descrição_vXX

Exemplos:
2025-02-15_Proposta_ClienteX_v03.pdf
2025-02-10_Contrato_FornecedorY_FINAL.pdf
2025-02-01_Relatorio_Vendas_Janeiro.xlsx
```

**Pastas:**
```
NúmeroOrdem_NomePasta

Exemplos:
01_Projetos_Ativos
02_Clientes
03_Templates
```

Força ordem alfabética consistente.

### 3.2 Compartilhamento e Permissões

**Níveis:**
- **Viewer:** Só vê
- **Commenter:** Vê + comenta
- **Editor:** Vê + edita
- **Owner:** Controle total

**Best practices:**

**1. Nunca "Anyone with link can edit"**
- Risco: Qualquer um pode deletar/estragar
- Use: Specific people

**2. Pastas compartilhadas para projetos**
- Cria pasta projeto
- Compartilha pasta (não arquivo individual)
- Todo arquivo novo dentro já está compartilhado

**3. Grupos para times**
- Cria Google Group: time-marketing@empresa.com
- Compartilha pastas com grupo
- Adicionar pessoa ao time = acesso automático a tudo

**4. Link expiration para externos**
- Compartilha com prazo (ex: 7 dias)
- Drive revoga acesso automaticamente

**5. Notificações de acesso**
- Drive → Settings → Notifications
- "Notify me when someone edits/comments"

### 3.3 Busca Avançada

**Operadores:**

**Por tipo:**
```
type:spreadsheet
type:document
type:presentation
type:pdf
type:image
type:folder
```

**Por dono:**
```
owner:joao@empresa.com
```

**Por compartilhamento:**
```
to:maria@empresa.com (compartilhado com)
from:maria@empresa.com (compartilhado por)
```

**Por data:**
```
before:2025-01-01
after:2025-01-01
```

**Combinados:**
```
type:spreadsheet owner:me after:2025-01-01

= Planilhas minhas criadas depois de 01/01/2025
```

**Starred/Trash:**
```
is:starred
is:trashed
```

**Atalho:** `/` (barra) vai direto pra busca

## 4. Google Calendar Produtivo

### 4.1 Time Blocking

**Método:** Agenda não é só reuniões. É TODO seu tempo.

**Estrutura ideal:**

```
Segunda-Feira
─────────────────────
08:00-09:00 ⚡ Morning routine + planning
09:00-12:00 🎯 Deep Work - Projeto A
12:00-13:00 🍽️ Almoço
13:00-14:00 📧 Email + admin
14:00-16:00 🎯 Deep Work - Projeto B
16:00-17:00 🤝 Reuniões/Calls
17:00-18:00 📝 Planning amanhã + wrap up
```

**Cores (code visual):**
- 🔴 Deep Work (foco total, sem interrupções)
- 🔵 Reuniões
- 🟢 Admin/Email
- 🟡 Breaks
- 🟣 Pessoal

**Criar evento recorrente:**
1. Novo evento
2. "Does not repeat" → Custom
3. Config recorrência
4. Salva

**Evento "Focus Time":**
- Bloqueia agenda
- Others see: Busy
- Notificações: Off
- Description: "Trabalho focado - não agende reuniões"

### 4.2 Múltiplos Calendários

**Setup:**

**Calendar 1: Trabalho (principal)**
- Reuniões
- Deadlines
- Time blocks

**Calendar 2: Pessoal**
- Compromissos família
- Academia
- Lazer

**Calendar 3: Metas/Hábitos**
- Exercício diário
- Leitura
- Study time

**Calendar 4: Feriados BR**
- Adiciona: Browse calendars → Holidays in Brazil

**Vantagem:** Liga/desliga por contexto. Compartilha só o relevante.

### 4.3 Integrações Calendar

**Calendar + Gmail:**

Email com data/hora → Gmail sugere adicionar ao calendar automaticamente

**Calendar + Meet:**

Evento com convidados → Adiciona Google Meet automaticamente
Settings → Event settings → Add Google Meet automatically

**Calendar + Tasks:**

Tasks com prazo aparecem no calendar

**Calendar + Notion (via Make):**
```
Google Calendar - Event starts
→ Notion - Create page (meeting notes)
  Title: {{event.summary}}
  Date: {{event.start}}
  Attendees: {{event.attendees}}
  Template: Meeting notes
```

## 5. Google Workspace Integrações

### 5.1 Gmail + Sheets (Lead tracking)

**Make automation:**
```
Gmail - New email
  Label: Leads
→ Google Sheets - Add row
  Sheet: "Leads 2025"
  Values:
    - Date: {{receivedDate}}
    - From: {{from.name}}
    - Email: {{from.address}}
    - Subject: {{subject}}
    - Body preview: {{substring(text; 0; 200)}}
    - Link: {{webLink}}
```

**Resultado:** Todo lead email vira linha em planilha rastreável.

### 5.2 Forms + Sheets + Email (Automação completa)

**Fluxo:**

1. Google Forms: Cliente preenche
2. Resposta cai no Sheets automaticamente
3. Apps Script detecta nova linha
4. Envia email personalizado
5. Cria evento no Calendar
6. Notifica Slack

**Apps Script:**
```javascript
function onFormSubmit(e) {
  var nome = e.values[1];
  var email = e.values[2];
  var servico = e.values[3];
  
  // Envia email
  MailApp.sendEmail({
    to: email,
    subject: "Recebemos seu pedido!",
    body: "Oi " + nome + ",\n\nObrigado pelo interesse em " + servico + ".\n\nRetornamos em 24h.\n\nAbraço!"
  });
  
  // Cria evento calendar
  CalendarApp.getDefaultCalendar().createEvent(
    "Follow-up: " + nome,
    new Date(Date.now() + 86400000), // +1 dia
    new Date(Date.now() + 90000000),
    {description: "Contatar sobre " + servico}
  );
}
```

Trigger: Forms → On form submit

### 5.3 Drive + Docs (Templates automáticos)

**Gerar contrato personalizado:**

**Template (Google Docs):**
```
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

CONTRATANTE: {{nome_cliente}}
CNPJ: {{cnpj}}
ENDEREÇO: {{endereco}}

SERVIÇO: {{descricao_servico}}
VALOR: R$ {{valor}}
PRAZO: {{prazo}} dias

DATA: {{data_contrato}}

____________________        ____________________
  {{nome_cliente}}             {{nome_empresa}}
   Contratante                  Contratada
```

**Apps Script (em Sheets com dados):**
```javascript
function gerarContrato() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var templateId = "ID_DO_TEMPLATE";
  
  for (var i = 1; i < data.length; i++) {
    var cliente = data[i][0];
    var cnpj = data[i][1];
    // ...
    
    // Copia template
    var docCopy = DriveApp.getFileById(templateId).makeCopy("Contrato_" + cliente);
    var doc = DocumentApp.openById(docCopy.getId());
    var body = doc.getBody();
    
    // Substitui placeholders
    body.replaceText("{{nome_cliente}}", cliente);
    body.replaceText("{{cnpj}}", cnpj);
    // ... todos campos
    
    doc.saveAndClose();
  }
}
```

**Resultado:** 1 clique → 100 contratos personalizados gerados.

## 6. Exercício Prático (60min)

**PARTE 1: Gmail Setup (20min)**

1. Crie estrutura de labels (mínimo 5)
2. Configure 3 filtros automáticos
3. Crie 2 templates de email
4. Ative atalhos de teclado
5. Processe inbox até zero

**PARTE 2: Sheets Dashboard (20min)**

1. Cria planilha com dados fictícios (vendas, leads, etc)
2. Sheet 1: Raw data
3. Sheet 2: Dashboard com:
   - 3 métricas principais (cards)
   - 2 gráficos
   - 1 tabela com QUERY
   - Formatação condicional

**PARTE 3: Automação (20min)**

Escolha 1:
- A) Apps Script: Email automático quando célula muda
- B) Make: Form → Sheets → Email
- C) Drive: Estrutura de pastas profissional + compartilhamento

**ENTREGA:**
- Screenshots de cada parte
- Link compartilhado (view only)
- Descrição: o que automatizou e por quê

**BÔNUS:** Compartilha no LinkedIn seu dashboard ou automação. Tag #googleworkspace

---

## Próximos Passos

**Módulo 7: Slack e Comunicação Assíncrona**
- Slack profissional (etiqueta, produtividade)
- Canais e workflows
- Bots e automações
- Integração Slack + Make + Notion

**Prepare-se para:** Comunicação remota expert level

Nos vemos lá! 🚀

---

**© 2025 FETD - Formação em Engenharia de Intenção**
