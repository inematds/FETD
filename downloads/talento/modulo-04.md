# Módulo 4: Automação No-Code com Make

**Trilha:** Talento Emergente
**Duração:** 60-75 minutos
**Objetivo:** Criar sua primeira automação profissional sem escrever código

---

## Introdução

Imagine economizar 15-20 horas por semana eliminando tarefas repetitivas.

Não é futuro. É o que profissionais fazem HOJE com ferramentas no-code.

**Make** (antigo Integromat) é a ferramenta mais poderosa para automação visual.

Neste módulo você vai:
1. Entender como Make funciona
2. Criar sua primeira automação (passo-a-passo)
3. Aprender integrações essenciais
4. Ver casos de uso que geram valor imediato

## 1. O Que é Make e Por Que Usar

### 1.1 Conceitos Básicos

**Make conecta aplicativos diferentes para automatizar processos.**

Exemplo simples:
```
QUANDO novo lead preenche formulário no site
→ ENTÃO salvar dados no Google Sheets
→ E enviar email de boas-vindas
→ E criar tarefa no Notion para vendedor
→ E notificar time no Slack
```

Tudo isso acontece **automaticamente, 24/7, sem intervenção humana**.

### 1.2 Make vs Zapier

**Make:**
- ✅ Mais poderoso e flexível
- ✅ Interface visual superior
- ✅ Plano grátis mais generoso (1.000 operações)
- ✅ Melhor para automações complexas
- ❌ Curva de aprendizado maior

**Zapier:**
- ✅ Mais fácil para iniciantes
- ✅ Mais integrações
- ✅ Melhor documentação
- ❌ Plano grátis limitado (100 tarefas)
- ❌ Menos flexível

**Recomendação:** Aprenda Make. Quando dominar, Zapier será fácil.

### 1.3 Quanto Custa

**Plano Gratuito:**
- 1.000 operações/mês
- Suficiente para 10-15 automações básicas
- Ótimo para aprender e testar

**Plano Core ($9/mês):**
- 10.000 operações/mês
- Webhooks ilimitados
- Apps premium
- Suficiente para 50-100 automações

**Para freelancer iniciante:** Grátis é suficiente.

## 2. Primeira Automação: Passo-a-Passo

Vamos criar juntos: **"Novo email com anexo → Salvar no Drive + Notificar Slack"**

### 2.1 Setup Inicial

**Passo 1: Criar conta**
- Acesse make.com
- Cadastre com email
- Confirme conta

**Passo 2: Criar novo cenário**
- Click "Create new scenario"
- Você verá tela em branco

**Passo 3: Entender a interface**
- **Módulos:** blocos que executam ações
- **Conexões:** linhas entre módulos (fluxo)
- **Roteadores:** dividem fluxo em caminhos
- **Filtros:** condições (se/então)

### 2.2 Construindo a Automação

**Módulo 1: Trigger (Gmail - Watch Emails)**

1. Click no "+" na tela
2. Busque "Gmail"
3. Escolha "Watch Emails"
4. Configure:
   - Folder: INBOX
   - Criteria: Has attachment = Yes
   - Maximum results: 10
5. Conecte sua conta Gmail
6. Salve

**Testando:**
- Click "Run once"
- Envie email para você com anexo
- Verifique se Make capturou

**Módulo 2: Action (Google Drive - Upload)**

1. Click no "+" após Gmail
2. Busque "Google Drive"
3. Escolha "Upload a File"
4. Configure:
   - Folder: [escolha ou crie]
   - File name: {{1.attachments[].name}}
   - File data: {{1.attachments[].data}}
5. Conecte Google Drive
6. Salve

**Módulo 3: Action (Slack - Send Message)**

1. Click no "+" após Drive
2. Busque "Slack"
3. Escolha "Create a Message"
4. Configure:
   - Channel: [escolha]
   - Text: "Novo anexo salvo: {{2.name}} no Drive"
5. Conecte Slack
6. Salve

**Passo final: Ativar**
- Click "Scheduling"
- Escolha frequência (ex: every 15 minutes)
- Ative o cenário

**Pronto! Sua primeira automação está funcionando.**

### 2.3 Testando e Refinando

**Envie email com anexo e observe:**
1. Make detecta email
2. Salva anexo no Drive
3. Notifica no Slack

**Se não funcionou:**
- Verifique conexões
- Veja logs de erro
- Teste módulo por módulo

## 3. Integrações Essenciais

### 3.1 Gmail + Sheets (Organizar Emails)

**Caso de uso:** Emails importantes viram linhas em planilha

```
TRIGGER: Gmail - Watch Emails
FILTER: Apenas emails de clientes (contains "@empresa.com")
ACTION: Google Sheets - Add Row
   - Email do remetente
   - Assunto
   - Data/hora
   - Link para email
```

**Valor:** Nunca mais perde email importante.

### 3.2 Formulário + CRM (Captura de Leads)

```
TRIGGER: Google Forms - Watch Responses
ACTION 1: Google Sheets - Add Row (backup)
ACTION 2: HubSpot/Pipedrive - Create Contact
ACTION 3: Gmail - Send Email (boas-vindas personalizado)
ACTION 4: Slack - Notify vendedor
```

**Valor:** Lead cai direto no CRM com follow-up automático.

### 3.3 Shopify + Logística (E-commerce)

```
TRIGGER: Shopify - Watch Orders
FILTER: Status = Paid
ACTION 1: Google Sheets - Add Row (controle)
ACTION 2: Correios API - Calculate Shipping
ACTION 3: Gmail - Send tracking email
ACTION 4: Trello - Create Card (separação)
```

**Valor:** Elimina 90% do trabalho manual pós-venda.

### 3.4 Redes Sociais + Notion (Gestão de Conteúdo)

```
TRIGGER: RSS Feed - Watch new posts (blogs favoritos)
ACTION 1: Notion - Create Page
   - Título do artigo
   - Link
   - Resumo (com ChatGPT API)
   - Tags automáticas
ACTION 2: Slack - Share interessantes
```

**Valor:** Curadoria de conteúdo automatizada.

## 4. Casos de Uso que Geram Valor

### 4.1 Para Freelancers

**Automação 1: Invoice automático**
```
TRIGGER: Trello - Card moved to "Concluído"
ACTION 1: Google Docs - Generate from template
   - Nome cliente (da card)
   - Valor (custom field)
   - Data
ACTION 2: Gmail - Send invoice
ACTION 3: Google Sheets - Add to financeiro
```

**Economia:** 30min por projeto.

**Automação 2: Time tracking**
```
TRIGGER: Toggl - Timer stopped
ACTION: Google Sheets - Add row
   - Cliente
   - Projeto
   - Horas
   - Descrição
```

**Valor:** Relatórios automáticos para cobrar clientes.

### 4.2 Para Pequenas Empresas

**Automação: Onboarding de funcionários**
```
TRIGGER: Google Forms - Novo funcionário
ACTION 1: Gmail - Create account
ACTION 2: Google Drive - Create folder structure
ACTION 3: Notion - Add to database
ACTION 4: Slack - Send welcome message
ACTION 5: Trello - Create onboarding tasks
ACTION 6: Calendar - Schedule meetings
```

**Economia:** 8 horas → 15 minutos.

### 4.3 Para Você Pessoal

**Automação: Finanças pessoais**
```
TRIGGER: Gmail - Recebeu extrato bancário
ACTION 1: Extract data (regex ou IA)
ACTION 2: Google Sheets - Categorize expenses
ACTION 3: Calculate monthly total
ACTION 4: If > orçamento → Send alert
```

**Valor:** Controle financeiro sem esforço.

## 5. Técnicas Avançadas

### 5.1 Routers (Múltiplos Caminhos)

```
TRIGGER: Novo lead
ROUTER:
  Path 1 (se orçamento > R$10k):
    → Notifica CEO
    → Agenda reunião
  Path 2 (se orçamento < R$10k):
    → Vendedor padrão
    → Email template
```

### 5.2 Iterators (Loop em Listas)

```
TRIGGER: Email com múltiplos anexos
ITERATOR: Para cada anexo
  ACTION: Save to specific folder based on type
    - .pdf → Contratos
    - .jpg → Imagens
    - .xlsx → Planilhas
```

### 5.3 Error Handling

```
TRY:
  Upload to Drive
CATCH (se erro):
  1. Send error to Slack
  2. Retry 3x
  3. If still fails → Salva local
```

### 5.4 Webhooks (Integrações Custom)

```
TRIGGER: Webhook - Custom URL
  (pode ser chamado de qualquer lugar)
ACTION: Process data + Execute actions
```

**Uso:** Integrar ferramentas que Make não tem conector nativo.

## 6. Biblioteca de Automações Prontas

### Automação 1: Email Daily Digest
```
SCHEDULE: Every day 8am
ACTION 1: Gmail - Get unread important
ACTION 2: Aggregate into single email
ACTION 3: Send summary
```

### Automação 2: Backup Automático
```
SCHEDULE: Every night 2am
ACTION 1: Google Drive - List files
ACTION 2: Zip all
ACTION 3: Upload to Dropbox/OneDrive
```

### Automação 3: Social Media Repost
```
TRIGGER: Instagram - New post
ACTION 1: Download image
ACTION 2: Resize for each platform
ACTION 3: Post to:
   - LinkedIn
   - Twitter
   - Facebook
```

### Automação 4: Meeting Notes
```
TRIGGER: Google Calendar - Meeting ended
ACTION 1: Notion - Create page
   - Attendees
   - Agenda
   - Template for notes
ACTION 2: Slack - Remind to fill notes
```

## 7. Como Cobrar por Automações

### 7.1 Precificação

**Modelo 1: Por hora**
- Júnior: R$ 50-80/hora
- Pleno: R$ 80-150/hora

**Modelo 2: Por projeto**
- Automação simples (2-3 módulos): R$ 500-1.500
- Automação média (5-10 módulos): R$ 1.500-4.000
- Automação complexa (15+ módulos): R$ 4.000-10.000

**Modelo 3: Recorrente (melhor!)**
- Mensalidade por manutenção: R$ 300-1.000/mês
- Inclui: monitoramento, ajustes, suporte

### 7.2 Proposta que Vende

```
## Proposta: Automação de [Processo X]

**Situação Atual:**
- Tempo gasto: Xh/semana
- Erros: Y/mês
- Custo estimado: R$ Z

**Solução Proposta:**
[Descrever automação]

**Ferramentas:** Make + Apps cliente já usa

**Tempo de Implementação:** 1-2 semanas

**Investimento:**
- Setup: R$ X.XXX (one-time)
- Manutenção: R$ XXX/mês

**ROI Esperado:**
- Economia: Xh/semana = R$ Y/mês
- Payback: 2-3 meses
- ROI anual: 300%+

**Próximos Passos:**
1. Reunião técnica (30min)
2. Mapeamento processos (1h)
3. Desenvolvimento (1 semana)
4. Testes + ajustes (1 semana)
5. Treinamento team (2h)
```

## Exercício Prático

**Duração:** 2 horas

**Objetivo:** Criar 3 automações funcionais

**Automação 1: Pessoal (45min)**
Automatize algo da sua vida:
- Finanças
- Emails
- Tarefas
- Estudos

**Automação 2: Profissional (45min)**
Automatize processo do trabalho:
- Relatórios
- Follow-ups
- Data entry
- Notificações

**Automação 3: Portfólio (30min)**
Crie automação para mostrar em entrevistas:
- Útil e impressionante
- Documente com prints
- Grave vídeo mostrando funcionando

**Entrega:**
- 3 automações ativas
- Documentação de cada uma
- 1 vídeo (Automação 3)

**Isso é experiência real que vale em entrevistas.**

---

## Próximos Passos

**Módulo 5: Notion para Produtividade**
- Notion como segundo cérebro
- Gestão de projetos e tarefas
- Base de conhecimento
- Integrações com Make

Nos vemos lá! 🚀

---

**© 2025 FETD - Formação em Engenharia de Intenção**
