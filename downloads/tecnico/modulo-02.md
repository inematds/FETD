# Módulo 2: Automações que Resolvem Problemas de Verdade

**Duração:** 75-90 minutos
**Objetivo:** Criar automações práticas que as pessoas realmente usam (não scripts que só você entende)

---

## Introdução: A Diferença Entre Script e Automação

Você já criou um script bash que funciona perfeitamente... mas só você usa?

**O problema:** Técnicos criam ferramentas para si mesmos.
**A solução:** Criar automações que QUALQUER PESSOA usa.

**Diferença fundamental:**

| Script Pessoal | Automação Real |
|----------------|----------------|
| Terminal, CLI complexo | Interface clara (botão, form, chat) |
| Você precisa explicar | Auto-explicativo |
| Requer conhecimento técnico | Qualquer um usa |
| Documentação = zero | Tutorial embutido |
| Só resolve SEU problema | Resolve problema de TODOS |

**Exemplo real:**

**Script que só você usa:**
```bash
./deploy.sh prod db-migration skip-tests
```
(Ninguém além de você sabe o que isso faz)

**Automação que todos usam:**
```
Portal Web:
┌─────────────────────────────┐
│  🚀 Deploy Automático       │
├─────────────────────────────┤
│  Ambiente: [Produção ▼]     │
│  Incluir migration? [✓]     │
│  Rodar testes? [✓]          │
│  [  Iniciar Deploy  ]       │
└─────────────────────────────┘
```

**Qual você acha que o time vai usar?**

---

## Os 3 Tipos de Automações Solucionadoras

### Tipo 1: Automações de Resposta (Chatbots/FAQs)

**Problema que resolve:**
Você responde mesmas perguntas 100x

**Exemplos de perguntas repetidas:**
- "Como fazer deploy?"
- "Como acessar logs de produção?"
- "Como configurar ambiente local?"
- "Por que o build falhou?"
- "Como reverter deploy?"

**Solução: Chatbot que Responde Automaticamente**

**Stack recomendada:**

**Opção 1: Botpress (No-Code, Mais Rápido)**
- Interface visual
- RAG nativo (treina com suas docs)
- Deploy em 30 min
- Integra: Slack, Discord, Web
- **Gratuito** até 2000 msgs/mês

**Passo a passo:**
1. Criar conta em Botpress Cloud
2. Upload de documentação (markdown, PDFs)
3. Treinar bot com perguntas/respostas
4. Testar no playground
5. Integrar com Slack/Discord
6. Monitorar: que perguntas estão sendo feitas?

**Opção 2: n8n + ChatGPT API (Low-Code, Mais Flexível)**
- Workflow visual
- Conecta Slack → ChatGPT → Notion (knowledge base)
- Mais controle
- **Open-source, self-hosted grátis**

**Workflow:**
```
Trigger: Mensagem no Slack com palavra-chave
  ↓
Buscar resposta na base de conhecimento (Notion/Docs)
  ↓
Se encontrou: Responder automaticamente
Se não encontrou: Mandar ChatGPT gerar resposta genérica + tag você
  ↓
Adicionar thread no Slack com resposta
```

**Resultado esperado:**
- 60-80% das perguntas respondidas automaticamente
- Você só responde casos complexos
- Time tem resposta 24/7

**Case Real: Mariana, DevOps em Fintech**

**Antes:**
- 20 perguntas/dia no Slack
- 2h/dia respondendo
- Sempre interrompida

**Criou:**
- Botpress bot treinado em docs de infra
- Top 30 perguntas + respostas
- Integrou no Slack canal #devops-help

**Depois:**
- Bot responde 75% das perguntas
- 30 min/dia revisando casos complexos
- **Economizou: 1.5h/dia = 30h/mês**

**Promoção:** 3 meses depois → Senior DevOps
**Motivo:** "Escalou conhecimento do time"

---

### Tipo 2: Automações de Processo (Workflows)

**Problema que resolve:**
Tarefas manuais chatas que todos fazem

**Exemplos de processos chatos:**
- Onboarding de novo dev (15 passos manuais)
- Aprovação de PR (checklist repetitivo)
- Deploy (build → test → deploy → notify)
- Criação de ambiente (setup, permissões, configs)
- Backup e restore de databases

**Solução: Workflow Automatizado Visual**

**Stack recomendada:**

**Para Devs: GitHub Actions**

**Exemplo: Automação de PR Review**

```yaml
name: PR Auto-Checks
on: pull_request

jobs:
  auto-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Tests
        run: npm test

      - name: Check Code Style
        run: npm run lint

      - name: Security Scan
        run: npm audit

      - name: Comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '✅ Testes passaram!\n✅ Lint ok\n✅ Sem vulnerabilidades'
            })
```

**Resultado:**
- PR automaticamente testado
- Feedback imediato
- Reviewer não perde tempo com basics

**Para Operações: n8n (Visual Workflow)**

**Exemplo: Automação de Onboarding**

```
Workflow Visual:
1. Trigger: Novo dev adicionado no Notion
2. Criar conta GitHub (API)
3. Adicionar em 5 repos principais (GitHub API)
4. Criar email corporativo (Google Workspace API)
5. Adicionar em Slack channels (Slack API)
6. Enviar email de boas-vindas (Gmail)
7. Criar card no Jira de tarefas onboarding
8. Notificar manager no Slack
```

**Antes:** 2h de trabalho manual
**Depois:** 5 min (você só preenche nome e email)

**Para Não-Devs: Zapier (Super Simples)**

**Exemplo: Notificar time de deploys**

```
Trigger: Commit na branch main (GitHub)
  ↓
Aciona build (GitHub Actions)
  ↓
Se sucesso:
  - Manda mensagem no Slack
  - Atualiza Notion com deploy log
  - Email para stakeholders
Se falhou:
  - Alerta no PagerDuty
  - Thread no Slack com logs
```

**Case Real: Rafael, Tech Lead**

**Problema:**
Deploy manual com 20 passos.
Erros frequentes. 2h de trabalho.

**Criou:**
GitHub Action completa:
```
- Build
- Tests
- Security scan
- Deploy staging
- Smoke tests staging
- Deploy production
- Smoke tests production
- Rollback automático se falhar
- Notificações em cada step
```

**Resultado:**
- Deploy: 2h → 15 min (automatizado)
- Erros: 30% → 2%
- Time pode fazer deploy 5x/dia vs 1x/semana
- Rafael virou Staff Engineer

---

### Tipo 3: Automações Self-Service (Portais/Dashboards)

**Problema que resolve:**
Time depende de você para coisas simples

**Exemplos de dependências:**
- "Me dá acesso ao servidor"
- "Como tá o status do sistema?"
- "Qual versão está em produção?"
- "Preciso ver os logs de ontem"
- "Cria um ambiente de teste pra mim"

**Solução: Portal Onde Pessoas Fazem Sozinhas**

**Stack recomendada:**

**Opção 1: Retool (Rápido, Poderoso)**

**O que é:**
- Ferramenta de internal tools
- Conecta com qualquer API/database
- Interface drag-and-drop
- **Grátis** para 5 users

**Casos de uso:**

**1. Portal de Logs:**
```
Interface:
┌────────────────────────────┐
│  Buscar Logs               │
├────────────────────────────┤
│  Serviço: [API ▼]          │
│  Período: [Últimas 24h ▼]  │
│  Level: [Error ▼]          │
│  Keyword: [________]       │
│  [  Buscar  ]              │
├────────────────────────────┤
│  Resultados:               │
│  2025-01-19 10:23 - Error  │
│  Connection timeout...     │
│  [Ver Stack Trace]         │
└────────────────────────────┘
```

**Backend:**
Conecta direto no Elasticsearch/CloudWatch

**2. Portal de Permissões:**
```
Interface:
┌────────────────────────────┐
│  Solicitar Acesso          │
├────────────────────────────┤
│  Recurso: [Prod DB ▼]      │
│  Duração: [2 horas ▼]      │
│  Motivo: [Debug issue #123]│
│  [  Solicitar  ]           │
└────────────────────────────┘
```

**Backend:**
- Validação automática
- Aprova se for dev senior
- Notifica security se for produção
- Revoga acesso automaticamente após tempo

**Opção 2: Streamlit (Para Python Devs)**

**O que é:**
- Python puro vira dashboard web
- Zero frontend necessário
- Deploy grátis no Streamlit Cloud

**Exemplo: Dashboard de Deploy:**

```python
import streamlit as st
import subprocess

st.title("🚀 Deploy Portal")

ambiente = st.selectbox("Ambiente", ["staging", "production"])
run_tests = st.checkbox("Rodar testes?", value=True)
migration = st.checkbox("Incluir migration?", value=False)

if st.button("Deploy"):
    with st.spinner(f"Deploying para {ambiente}..."):
        cmd = f"./deploy.sh {ambiente}"
        if not run_tests:
            cmd += " --skip-tests"
        if migration:
            cmd += " --migration"

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            st.success("✅ Deploy completo!")
            st.code(result.stdout)
        else:
            st.error("❌ Deploy falhou")
            st.code(result.stderr)
```

**Deploy:**
```bash
streamlit run app.py
# Acessa via http://localhost:8501
```

**Opção 3: Notion + Automação (Zero Code)**

**Para times não-técnicos:**

Criar database no Notion:
```
Solicitações de Acesso
├─ Nome do solicitante
├─ Recurso solicitado
├─ Motivo
├─ Status [Pendente/Aprovado/Negado]
└─ Data de expiração
```

Automação (Zapier/n8n):
```
Trigger: Nova linha no Notion
  ↓
Se recurso = "Produção":
  - Notificar security no Slack
  - Esperar aprovação
Se recurso = "Staging":
  - Aprovar automaticamente
  - Executar script de acesso
  - Atualizar Notion com credenciais
  - Agendar revogação
```

**Case Real: Carla, SRE**

**Problema:**
10 pedidos/dia de acesso temporário a servidores.
30 min cada = 5h/dia só nisso.

**Criou:**
Portal Retool:
- Self-service request
- Aprovação automática (regras pre-definidas)
- Acesso temporário (auto-revoga)
- Audit log completo

**Resultado:**
- 90% dos pedidos resolvidos sem ela
- 30 min/dia só revisando audit
- **Economizou: 4.5h/dia**
- Time security adorou (melhor controle)
- Promovida a Platform Lead

---

## Princípios de Automações que Funcionam

### Princípio 1: Interface > Terminal

**Ruim:**
```bash
$ create-env --name test --type staging --db postgres --cache redis
```
Ninguém lembra dos flags.

**Bom:**
```
┌─────────────────────────┐
│  Criar Ambiente         │
├─────────────────────────┤
│  Nome: [_____]          │
│  Tipo: [Staging ▼]     │
│  Database: [Postgres ▼] │
│  Cache: [Redis ▼]       │
│  [  Criar  ]            │
└─────────────────────────┘
```
Impossível errar.

---

### Princípio 2: Feedback Imediato

**Ruim:**
Script roda em silêncio. Você não sabe se travou ou está funcionando.

**Bom:**
```
🔄 Iniciando deploy...
✅ Build completo (23s)
✅ Testes passaram (45s)
🔄 Enviando para produção...
✅ Deploy completo!
📊 Tempo total: 1m32s
🌐 Acesse: https://app.com
```

Pessoa sabe exatamente o que está acontecendo.

---

### Princípio 3: Error Messages Humanos

**Ruim:**
```
Error: NullPointerException at line 234
Stack trace: [50 linhas de java stacktrace]
```

**Bom:**
```
❌ Ops! Algo deu errado no deploy.

Problema: Variável DATABASE_URL não configurada

Como resolver:
1. Adicione DATABASE_URL nas secrets do GitHub
2. Ou rode: export DATABASE_URL=postgres://...

Precisa de ajuda? Veja: https://docs.com/env-vars
Ou chame @devops no Slack
```

Pessoa consegue resolver sozinha.

---

### Princípio 4: Idempotência

Automação rodada 2x deve ter mesmo resultado que 1x.

**Ruim:**
```bash
# Cria user
createuser admin
# Falha se rodar 2x: "user already exists"
```

**Bom:**
```bash
# Cria user (se não existir)
if ! user_exists admin; then
  createuser admin
else
  echo "User admin já existe, pulando..."
fi
```

Pessoa pode rodar quantas vezes quiser.

---

### Princípio 5: Rollback Fácil

Se der errado, desfazer deve ser trivial.

**Exemplo: Deploy com rollback:**
```
[Deploy v2.0]
  ↓
Smoke tests
  ↓
Sucesso? → Continua
Falha? → Rollback automático para v1.9
  ↓
Notifica time no Slack
```

---

## Projeto Prático: Crie Sua Primeira Automação

### Passo 1: Identifique o Problema (10 min)

Responda:
1. Que tarefa você faz 5+ vezes por semana?
2. Que pergunta você responde 5+ vezes por semana?
3. Que processo depende só de você?

**Exemplos:**
- Deploy manual
- Gerar relatório semanal
- Dar acesso temporário
- Responder "como configurar X"
- Criar ambiente de teste

Escolha **1** problema.

---

### Passo 2: Escolha a Ferramenta Certa (10 min)

| Se o problema é... | Use... |
|--------------------|--------|
| Responder perguntas repetidas | Botpress (chatbot) |
| Workflow com vários steps | n8n (visual) ou GitHub Actions |
| Portal self-service | Retool ou Streamlit |
| Notificações/integrações simples | Zapier |

---

### Passo 3: Desenhe o Fluxo (15 min)

No papel ou Excalidraw, desenhe:

**Antes (manual):**
```
Pessoa pede → Você faz step 1 → step 2 → step 3 → Responde
```

**Depois (automatizado):**
```
Pessoa clica botão → Automação faz steps → Feedback automático
```

**Exemplo real:**

**Antes:**
```
Dev pergunta no Slack: "Pode criar ambiente de teste?"
  ↓
Você: ssh no servidor
  ↓
Você: clona projeto
  ↓
Você: configura env vars
  ↓
Você: inicia serviços
  ↓
Você: pega URL e manda no Slack
Tempo: 20 min
```

**Depois:**
```
Dev: Clica botão no portal "Criar Ambiente"
  ↓
Script automático faz tudo
  ↓
Portal mostra: "✅ Ambiente criado! URL: https://test-123.com"
Tempo: 2 min
```

---

### Passo 4: Implemente (MVP em 2h)

**Dica:** Faça versão SIMPLES primeiro.

**MVP = Minimum Viable Product**

Não precisa de:
- ❌ Autenticação complexa
- ❌ UI perfeita
- ❌ Tratamento de 100 edge cases

Precisa de:
- ✅ Resolver caso de uso principal
- ✅ Interface clara
- ✅ Feedback de sucesso/erro

**Exemplo: Chatbot MVP**

Versão MVP:
- 5 perguntas mais comuns
- Respostas fixas (não precisa de IA ainda)
- Slack integration
- Tempo: 1-2h

Depois você:
- Adiciona mais perguntas
- Treina com RAG
- Melhora respostas

---

### Passo 5: Teste com 1 Pessoa (30 min)

Antes de mostrar para todo mundo:
- Peça 1 colega testar
- Veja ele usar (não explique nada!)
- Anote: onde ele travou? O que não ficou claro?
- Ajuste

---

### Passo 6: Documente Rapidamente (15 min)

README mínimo:
```markdown
# Nome da Automação

## O que faz
Resolve [problema X] automaticamente

## Como usar
1. Acesse [URL ou comando]
2. Preencha [campos]
3. Clique [botão]

## Deu erro?
- Erro A → Solução A
- Erro B → Solução B

## Precisa de ajuda?
Chama @seu-nome no Slack
```

---

### Passo 7: Lance e Monitore (contínuo)

**Lançamento:**
- Post no Slack:
```
🎉 Lançamento: [Nome da Automação]!

Agora vocês podem [fazer X] sozinhos.

Como usar: [link docs]
Link: [url]

Qualquer dúvida, me chamem!
```

**Monitore primeira semana:**
- Quantas pessoas usaram?
- Que erros aconteceram?
- Que perguntas surgiram?

**Itere:**
- Corrige bugs
- Adiciona casos de uso
- Melhora docs

---

## Exemplos de Automações por Área

### DevOps / SRE

1. **Portal de Logs**
   - Buscar logs sem SSH
   - Ferramenta: Retool + Elasticsearch

2. **Auto-scaling de ambientes**
   - Criar/destruir ambientes sob demanda
   - Ferramenta: Terraform + Portal web

3. **Incident Response Bot**
   - Checklist automático quando alert dispara
   - Ferramenta: PagerDuty + Slack bot

---

### Backend Dev

1. **API Testing Dashboard**
   - Testa endpoints com 1 clique
   - Ferramenta: Streamlit + requests

2. **Database Migration Portal**
   - Roda migrations de forma segura
   - Ferramenta: Retool + scripts

3. **Performance Profiler**
   - Profile de queries lentas
   - Ferramenta: Grafana + alertas

---

### Frontend Dev

1. **Screenshot Comparison**
   - Compara UI antes/depois automaticamente
   - Ferramenta: GitHub Action + Percy

2. **Bundle Size Monitor**
   - Alerta se bundle crescer muito
   - Ferramenta: bundlesize + CI

3. **A11y Checker**
   - Testa acessibilidade em cada PR
   - Ferramenta: Lighthouse CI

---

## Métricas de Sucesso

Como saber se sua automação está funcionando?

### Métricas Quantitativas:

**1. Tempo economizado**
```
Antes: 20 min/tarefa × 10 tarefas/semana = 200 min/semana
Depois: 2 min/tarefa × 10 tarefas/semana = 20 min/semana
Economia: 180 min/semana = 3h/semana
```

**2. Adoção**
```
Semana 1: 5 pessoas usaram
Semana 2: 12 pessoas usaram
Semana 3: 20 pessoas usaram
→ Crescimento consistente = sucesso
```

**3. Redução de perguntas**
```
Antes: 15 perguntas/semana sobre deploy
Depois: 3 perguntas/semana
→ 80% redução = automação funcionando
```

### Métricas Qualitativas:

**Feedback positivo:**
- "Isso mudou minha vida!"
- "Economizei horas com isso"
- "Time todo tá usando"

**Sinais indiretos:**
- Outros times pedindo pra usar
- Gestor mencionando em reunião
- Pessoas sugerindo melhorias (= estão usando!)

---

## Checklist: Sua Automação Está Pronta?

Antes de lançar, verifique:

**Interface:**
- [ ] Pessoa consegue usar sem explicação?
- [ ] Botões/campos têm labels claros?
- [ ] Tem feedback de progresso?

**Funcionamento:**
- [ ] Funciona 100% do tempo no caso comum?
- [ ] Error messages são claros?
- [ ] Tem rollback se der erro?

**Documentação:**
- [ ] README existe?
- [ ] Tem screenshots/GIF mostrando uso?
- [ ] Lista troubleshooting comum?

**Acesso:**
- [ ] Fácil de achar (link pinado no Slack)?
- [ ] Permissões corretas?
- [ ] Funciona para todos do time?

---

## Próximos Passos

**Nos próximos 7 dias:**

**Dia 1-2:** Escolha problema + ferramenta
**Dia 3-4:** Implemente MVP
**Dia 5:** Teste com 1 pessoa
**Dia 6:** Documente + lance
**Dia 7:** Monitore uso

**No Módulo 3:**
Vamos criar chatbot com RAG que responde perguntas técnicas 24/7.

**Lembre-se:**
Automação perfeita não existe.
Automação que resolve 80% dos casos + 20% você = excelente.

🚀 **Comece pequeno. Itere rápido. Escale depois.**
