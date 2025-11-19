# Módulo 9: Consultoria Interna - Virando Referência na Empresa

**Duração:** 60 minutos
**Objetivo:** Aplicar tudo que aprendeu para virar "o consultor de todo mundo" dentro da sua empresa

---

## 🎯 O Que Você Vai Aprender

✅ Posicionar-se como consultor interno
✅ Oferecer ajuda escalável (não virar gargalo)
✅ Criar "office hours" técnicos
✅ Documentar conhecimento institucional
✅ Conseguir promoções/reconhecimento

**Resultado:** Ser a pessoa que todos procuram para resolver problemas técnicos

---

## 🔥 De Executor para Consultor

### O Problema do Técnico Invisível

**Cenário comum:**
```
Você: Resolve 10 problemas/semana sozinho
Gestor: "O que você fez essa semana?"
Você: "Uh... resolvi uns bugs..."
Resultado: Sem reconhecimento, sem promoção
```

**Cenário consultor:**
```
Você: Resolve 3 problemas + ensina 10 pessoas a resolverem
Gestor: "Equipe toda melhorou, o que mudou?"
Todos: "Fulano criou um sistema/bot/doc que ajudou muito"
Resultado: Promoção, raise, reconhecimento
```

### Mindset Shift

**De:** "Vou resolver esse problema"
**Para:** "Vou resolver esse problema E criar sistema para que outros resolvam sozinhos"

---

## 🎓 Office Hours Técnicos

### Conceito

1 hora/semana que você está disponível para ajudar qualquer um com problemas técnicos.

**Benefícios:**
- ✅ Previsível (não interrompe trabalho aleatoriamente)
- ✅ Escalável (várias pessoas ao mesmo tempo)
- ✅ Visível (todos sabem que você ajuda)

### Setup

**Formato 1: Slack/Teams (Async)**

```
Canal: #office-hours-backend
Horário: Terças 15-16h

Regras:
1. Poste pergunta com contexto
2. [Seu nome] responde durante o horário
3. Outros podem ajudar também
4. FAQ vai sendo construído

Template de pergunta:
🔴 Problema: [descrição]
🎯 Objetivo: [o que quer alcançar]
✅ Já tentei: [o que fez]
```

**Formato 2: Google Meet (Sync)**

```
Sextas 14-15h
Meet link fixo

Agenda compartilhada:
- Pessoas adicionam tópicos
- 10 min por tópico
- Gravado e compartilhado depois

Vira: Série de vídeos de troubleshooting
```

### Escalar Office Hours

**Problema:** Muito popular → Não escala

**Solução: Train the Trainers**

```
Mês 1-2: Você lidera sozinho
Mês 3: Convida 2 devs senior para co-hospedar
Mês 4: Eles revezam com você
Mês 6: Você apenas supervisiona, eles lideram

Resultado: Cultura de ajuda mútua, não depende de você
```

---

## 📚 Sistema de Documentação Institucional

### Problema

Conhecimento crítico na cabeça de 2-3 pessoas:
- Como fazer deploy de emergência
- Onde estão os segredos/keys
- Como debugar problema X
- Processos que "todo mundo sabe"

**Risco:** Essas pessoas saem → Empresa para

### Solução: Runbook Vivo

**Estrutura no Notion/Confluence:**

```
Runbooks/
├── Operações Críticas
│   ├── Deploy de Emergência
│   ├── Rollback em Produção
│   └── Restore de Backup
│
├── Troubleshooting
│   ├── API retornando 502
│   ├── Database slow queries
│   └── CI/CD failing
│
└── Processos
    ├── Onboarding novo dev
    ├── Code review checklist
    └── Release process
```

**Template de Runbook:**

```markdown
# [Nome do Processo]

## 🚨 Quando usar
[Cenário específico]

## ✅ Pré-requisitos
- [ ] Acesso X
- [ ] Tool Y instalado

## 📋 Passo a Passo

### 1. [Passo]
```bash
comando aqui
```
**Output esperado:** [...]
**Se der erro:** [troubleshooting]

### 2. [Próximo passo]
[continua...]

## ⚠️ Cuidados
- Nunca fazer X
- Sempre checar Y

## 📞 Escalação
Se não funcionar, chamar: [pessoa/time]

## 📊 Métricas de Sucesso
Como saber que funcionou: [...]

---
Última atualização: 2025-01-19
Responsável: [Seu nome]
```

### Auto-Updating Docs

**Bot que detecta docs desatualizados:**

```python
# Roda semanalmente
for doc in runbooks:
    if doc.last_updated > 90_days:
        notify_slack(
            f"⚠️ Runbook desatualizado: {doc.title}
            Responsável: {doc.owner}
            
            Por favor revisar!"
        )
```

---

## 🤝 Programas de Mentoria Interno

### Formal Mentorship (1-on-1)

**Setup:**
```
- 2 juniors/mid que você mentora
- 30 min/semana cada
- Objetivos trimestrais claros
```

**Estrutura da sessão:**

```
1. Check-in (5 min)
   - Como foi a semana?
   - Bloqueios?

2. Tópico técnico (15 min)
   - Ensinar algo novo
   - Code review de projeto pessoal
   - Pair programming

3. Próximos passos (10 min)
   - O que vai fazer até próxima
   - Recursos para estudar
```

**Benefícios:**
- Eles aprendem rápido
- Você solidifica conhecimento
- Reconhecimento de liderança

### Informal "Ask Me Anything"

**Slack bot:**

```
/ask-senior [pergunta técnica]

Bot:
- Categoriza pergunta
- Se AUTO → Responde da knowledge base
- Se MANUAL → Marca você + sugere horário office hours
- Se URGENTE → Notifica imediato

Você responde quando pode, tudo documentado
```

---

## 📊 Métricas de Impacto (Para Promoção)

### Rastreie Seu Impacto

**Notion/Google Sheets:**

```
| Semana | Pessoas Ajudadas | Horas Economizadas | Projetos Desbloqueados |
|--------|------------------|--------------------|-----------------------|
| 1      | 5                | 10h                | 2                     |
| 2      | 8                | 15h                | 3                     |
| ...    | ...              | ...                | ...                   |
| Total  | 120              | 300h               | 45                    |
```

**Apresentar ao gestor trimestralmente:**

```
Q1 2025 Impact Report

🎯 Consultoria Técnica:
- 120 pessoas ajudadas diretamente
- 300h economizadas do time (estimativa)
- 45 projetos desbloqueados

🤖 Automações Criadas:
- Deploy bot (84h/mês economizadas)
- FAQ chatbot (40h/mês economizadas)
- Onboarding automation (15h/novo dev)

📚 Documentação:
- 15 runbooks criados
- 25 posts técnicos publicados
- 3 office hours sessions/mês

💡 Resultado:
Time 30% mais produtivo em tarefas técnicas
```

### KPIs de Consultor Interno

**Leading indicators (curto prazo):**
- Mensagens/semana pedindo ajuda
- Participantes em office hours
- Views em documentação

**Lagging indicators (longo prazo):**
- Promoções no time
- Redução de tickets de suporte técnico
- Satisfação do time (survey)

---

## 💼 Conseguir Promoção/Reconhecimento

### Documentar Tudo

**Brag document (arquivo privado):**

```markdown
# Conquistas 2025

## Janeiro
- Criei bot que economiza 84h/mês
- Ajudei 25 pessoas em office hours
- Publiquei 4 posts técnicos (1K views total)

## Fevereiro
[continua...]

## Skills Desenvolvidas
- Liderança técnica
- Comunicação
- Automação
[...]
```

**Usar em:**
- 1-on-1 com gestor
- Self-review de performance
- Candidatura para promoção

### Proposta de Promoção

**Template:**

```
Assunto: Proposta: Senior → Tech Lead

Contexto:
Nos últimos 6 meses, expandi meu papel além de executar tasks
para liderar tecnicamente e multiplicar impacto do time.

Evidências:

1. Liderança Técnica
   - Criei 3 sistemas que economizam 200h/mês do time
   - Conduzo office hours semanais (avg 8 participantes)
   - Mentoria de 2 devs juniors

2. Impacto no Negócio
   - Reduzi deployment time 80% (45min → 9min)
   - Onboarding de novos devs: 3 dias → 1 dia
   - 70% menos tickets técnicos repetidos

3. Influência e Comunicação
   - 30 posts técnicos publicados
   - GitHub com 150 stars
   - Reconhecido como referência em DevOps internamente

Proposta:
Tech Lead focado em:
- Arquitetura e technical direction
- Mentoria e crescimento do time
- Developer productivity e tooling

Expectativa: +20% salário (benchmarks: [links])
```

---

## 🎯 Resumo do Módulo

**Consultoria Interna = Multiplicador de Impacto**

**Sistema completo:**

1. **Office Hours:** 1h/semana ajudando múltiplos
2. **Runbooks:** Documentar conhecimento crítico
3. **Mentoria:** 2-3 pessoas crescendo com você
4. **Automações:** Sistemas que escalam ajuda
5. **Métricas:** Provar impacto quantitativamente

**Resultado em 6 meses:**
- Conhecido como referência técnica
- Time 30-50% mais produtivo
- Caminho claro para tech lead/staff
- Raise de 20-40%

**Próximo Módulo 10 (Final):**
Integrar TUDO em um **sistema completo** que roda quase sozinho!

---

**Tempo:** 2-3h setup inicial
**Manutenção:** 2-3h/semana
**ROI:** Promoção + Reconhecimento + Impacto real

**Próximo módulo:** Módulo 10 - Sistema Completo Integrado
