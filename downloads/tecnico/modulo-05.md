# Módulo 5: Blog Técnico com IA - Conteúdo em Escala

**Duração:** 60 minutos
**Nível:** Intermediário
**Objetivo:** Criar sistema de produção de conteúdo técnico que roda quase sozinho com IA

---

## 🎯 O Que Você Vai Aprender

✅ Criar blog técnico em 15 minutos (zero infraestrutura)
✅ Sistema de ideias infinitas com IA
✅ Escrever posts técnicos em 30 minutos com IA
✅ Distribuição automática (Dev.to, LinkedIn, Medium)
✅ SEO técnico para aparecer no Google

**Resultado:** Blog funcionando + sistema semanal de 1h que gera 4 posts/mês

---

## 🔥 Por Que Blog Técnico Importa

**Dados reais:**
- Devs que bloguem ganham **30-50% a mais**
- 73% dos recrutadores buscam no Google antes de contratar
- Seu blog aparece em buscas por anos (conteúdo evergreen)
- Network técnico de qualidade
- Autoridade na sua área

**O problema:** "Não tenho tempo"

**Solução:** IA escreve 80%, você adiciona os 20% de expertise real

---

## 📝 Setup do Blog (15 minutos)

### Opção 1: Hashnode (Recomendado)

**Por quê:**
- ✅ Grátis para sempre
- ✅ Domínio custom gratuito
- ✅ SEO otimizado
- ✅ Comunidade embutida
- ✅ Backup automático
- ✅ Newsletter integrada
- ✅ Analytics incluído

**Setup:**

1. Acesse [hashnode.com](https://hashnode.com)
2. Crie conta (GitHub login)
3. Create Blog → escolha nome (`seu-nome.hashnode.dev`)
4. Customize (logo, cores, bio)
5. Write first post!

**Custom domain (opcional):**
```
Comprar: blog.seunome.dev ($12/ano)
Adicionar em Settings → Domain
DNS: CNAME apontando para hashnode.network
```

### Opção 2: Dev.to (Zero Setup)

**Pros:**
- ✅ Audiência pronta (milhões de devs)
- ✅ Zero setup
- ✅ Boa distribuição

**Cons:**
- ❌ Não é "seu" (vive na plataforma)
- ❌ Menos controle
- ❌ Sem custom domain

**Quando usar:** Começar rápido, testar ideias

### Opção 3: GitHub Pages + Jekyll

**Para quem:** Quer controle total, sabe Git

```bash
# Setup rápido
gem install jekyll bundler
jekyll new meu-blog
cd meu-blog
bundle exec jekyll serve

# Publicar no GitHub Pages
# Criar repo: username.github.io
git push origin main
# Live em: username.github.io
```

---

## 💡 Sistema de Ideias Infinitas

### Problema: "Sobre o que escrever?"

**Solução:** Capturar aprendizados do dia a dia

**Regra de ouro:** Se você gastou 1h+ debugando algo, vire post!

### Template de Captura (Notion/Obsidian)

```markdown
# Banco de Ideias

## TIL (Today I Learned) - Viram posts rápidos
- [ ] Docker layer caching economiza 5min de build
- [ ] GitHub Actions matrix para testar múltiplas versões
- [ ] Python dataclasses > dicts para configs

## Problemas Resolvidos - Viram tutoriais
- [ ] Deploy falhando com erro 502 (resolvido mudando timeout)
- [ ] Database migration travando em produção
- [ ] CI/CD ficando lento (otimizamos de 20min → 5min)

## Comparações - Público adora
- [ ] Docker vs Podman em produção
- [ ] Terraform vs Pulumi (6 meses de uso real)
- [ ] Pytest vs Unittest (por que mudamos)

## Opiniões - Geram engajamento
- [ ] Por que paramos de usar microservices
- [ ] Testes e2e são overrated
- [ ] Docs > código bonito
```

### Usando IA para Gerar Ideias

**Prompt para ChatGPT:**

```
Sou desenvolvedor [Backend/DevOps/Frontend] trabalhando com [suas techs].

Gere 20 ideias de posts técnicos sobre:
- Problemas comuns em [área]
- Tutoriais práticos
- Comparações de ferramentas
- Otimizações

Formato:
- Título chamativo
- Gancho (por que ler)
- Promessa (o que vai aprender)
```

**Output esperado:**
```
1. "Como reduzir build do Docker de 10min para 2min"
   Gancho: Build lento é o #1 problema de produtividade
   Promessa: 3 técnicas simples que funcionam

2. "Debugando 502 em produção sem downtime"
   Gancho: 502 = pânico 3h da manhã
   Promessa: Checklist passo a passo
```

---

## ✍️ Escrevendo com IA (30 minutos)

### Framework: IA Draft → Você Refina → Publica

**Passo 1: Outline com IA (5 min)**

**Prompt:**

```
Crie outline detalhado para post técnico:

Título: "Como otimizamos CI/CD de 20min para 5min"

Audiência: Devs que sofrem com CI lento

Estrutura:
1. Intro (hook do problema)
2. Contexto (nosso cenário)
3. Problema (por que 20min é ruim)
4. Solução (3 otimizações específicas)
5. Resultados (métricas antes/depois)
6. Conclusão (take-aways)

Incluir:
- Dados reais (inventar placeholders)
- Code snippets
- Screenshots (placeholders)
```

**Passo 2: IA Escreve Draft (10 min)**

```
Usando o outline anterior, escreva o post completo.

Tom: Conversacional mas técnico
Estilo: Tutorial prático, não teoria
Tamanho: 1200-1500 palavras

Use:
- Emojis sutis (✅❌⚡)
- Code blocks com syntax highlighting
- Listas e bullets
- Negrito para destacar

NÃO:
- Jargão desnecessário
- Parágrafos longos
- Introdução genérica
```

**Passo 3: Você Adiciona Expertise (10 min)**

Aqui entra o diferencial:

✅ **Adicione:**
- Métricas REAIS do seu contexto
- Code snippets do SEU código
- Screenshots reais
- Erros que você cometeu
- Aprendizados específicos

❌ **Remova:**
- Frases genéricas da IA
- Explicações óbvias
- Disclaimers desnecessários

**Passo 4: Revisão Final (5 min)**

Checklist rápido:
- [ ] Título claro e searchable
- [ ] Intro responde "por que ler?"
- [ ] Code snippets testados
- [ ] Conclusão com ação clara
- [ ] Tags relevantes (max 5)
- [ ] Cover image atraente

---

## 🎨 Criando Cover Images com IA

**Opção 1: Canva (mais fácil)**

1. Template "Blog Banner"
2. Título do post
3. Screenshot de código (Carbon.now.sh)
4. Export PNG

**Opção 2: Unsplash + Texto**

```python
# Script rápido
from PIL import Image, ImageDraw, ImageFont
import requests

# Download de imagem tech
img_url = "https://unsplash.com/photos/tech-background"
img = Image.open(requests.get(img_url, stream=True).raw)

# Adicionar título
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Arial.ttf", 60)
draw.text((50, 50), "Título do Post", fill="white", font=font)

img.save("cover.png")
```

---

## 📤 Distribuição Automática

### Cross-posting Inteligente

**Estratégia:**
1. Publica no seu blog (canonical URL)
2. Cross-post em Dev.to (com canonical link)
3. Post resumo no LinkedIn (com link)
4. Tweet thread com highlights

**Ferramentas:**

**1. Hashnode → Dev.to (automático)**

Hashnode tem integração nativa:
- Settings → Integrations → Dev.to
- Conectar conta
- Posts publicam automaticamente em ambos

**2. RSS → LinkedIn (Zapier/IFTTT)**

```
Trigger: New RSS item (seu blog)
Action: Create LinkedIn post

Template:
"Novo post: {{title}}

{{summary}}

Leia completo: {{link}}

#DevOps #Automation"
```

**3. Buffer/Hootsuite para agendar**

- Escreve 4 posts no domingo
- Agenda 1/semana
- Buffer distribui automaticamente

---

## 🔍 SEO Técnico para Devs

### Keywords que Funcionam

**Fórmula:** `[Tecnologia] + [Ação] + [Contexto]`

✅ **Bom:**
- "Docker multi-stage build tutorial"
- "GitHub Actions cache dependencies"
- "Kubernetes troubleshooting CrashLoopBackOff"

❌ **Ruim:**
- "How to code" (muito genérico)
- "My thoughts on Python" (não searchable)

### Template de Post SEO-Friendly

```markdown
# [Tecnologia]: Como [Ação] [Resultado]

> [Sumário de 1 linha com keyword principal]

## O Problema

[Descrever problema comum com keywords naturais]

## Solução Passo a Passo

### 1. [Passo com keyword]

[Explicação + code]

### 2. [Outro passo com keyword]

[Explicação + code]

## Conclusão

[Resumo com call-to-action]

**Tags:** #docker #devops #tutorial #automation
```

### Checklist SEO

- [ ] Título com keyword principal (50-60 caracteres)
- [ ] URL limpa (`/docker-multi-stage-build`)
- [ ] Meta description (150-160 caracteres)
- [ ] H2/H3 com variações da keyword
- [ ] Links internos (outros posts seus)
- [ ] Links externos (docs oficiais)
- [ ] Alt text em imagens
- [ ] Code snippets com linguagem especificada

---

## 📊 Métricas que Importam

**Não foque em:**
- Total de views (vaidade)
- Likes/reactions

**Foque em:**
- 🎯 **Comentários técnicos** (prova que leram)
- 💼 **Mensagens de recrutadores** mencionando posts
- 🔗 **Backlinks** (outros blogs linkando)
- 🔍 **Tráfego orgânico** (Google Search Console)
- 📈 **Email subscribers** (se tiver newsletter)

**Meta 6 meses:**
- 10-15 posts publicados
- 1.000-2.000 views/mês orgânico
- 3-5 comentários/post em média
- 50-100 email subscribers
- Aparecendo no Google para 5-10 keywords

---

## 🗓️ Calendário Editorial Automatizado

### Sistema Semanal (1h total)

**Domingo 30min:**
- Revisar semana (commits, tickets, aprendizados)
- IA gera 3 ideias baseadas no trabalho da semana
- Escolher 1 para escrever

**Terça 30min:**
- IA escreve draft completo
- Você revisa e adiciona expertise
- Agendar publicação para quinta

**Resultado:** 4 posts/mês, 1h/semana

### Notion Template

```
| Status | Ideia | Outline | Draft | Publicado | Link |
|--------|-------|---------|-------|-----------|------|
| ✅ Done | Post X | ✅ | ✅ | 2025-01-20 | [link] |
| 🟡 Writing | Post Y | ✅ | 🔄 | - | - |
| 📋 Planned | Post Z | ✅ | - | - | - |
| 💡 Idea | Post W | - | - | - | - |
```

---

## 🎓 Exercício Prático

### Desafio: Primeiro Post em 60 Minutos

**Minuto 0-15: Setup**
- Criar conta Hashnode/Dev.to
- Configurar perfil
- Escolher tema

**Minuto 15-25: Ideia e Outline**
- Pegar 1 problema que você resolveu essa semana
- IA gera outline

**Minuto 25-45: Escrever**
- IA draft
- Você adiciona expertise real
- Code snippets testados

**Minuto 45-55: Polir**
- Cover image
- Tags
- SEO check

**Minuto 55-60: Publicar!**
- Publish
- Compartilhar no LinkedIn
- Tweet

**Meta:** Post publicado + 5 reações no LinkedIn

---

## 💡 Dicas de Ouro

### 1. Quantidade > Perfeição (no início)

- Posts mediocres publicados > posts perfeitos não publicados
- Primeiros 10 posts são aprendizado
- Melhora conforme pratica

### 2. Reutilize Conteúdo

**1 problema resolvido = 5 formatos:**
1. Post de blog (long-form)
2. TIL no GitHub (short)
3. Thread no Twitter (social)
4. Post LinkedIn (resumo + link)
5. YouTube short (screencast)

### 3. Responda Perguntas Reais

- Stack Overflow que você respondeu → vira post
- Slack/Discord answer → vira post
- Code review comment longo → vira post

### 4. "Tutorial Hell" Reverso

Não faça: "Tutorial de X para iniciantes"

Faça: "Como resolvi Y usando X em produção"

### 5. Série > Posts Isolados

**Exemplo:**
- "Otimizando CI/CD - Parte 1: Caching"
- "Otimizando CI/CD - Parte 2: Paralelização"
- "Otimizando CI/CD - Parte 3: Monitoramento"

Vantagens:
- Mais fácil escrever (tópico dividido)
- Pessoas voltam para próxima parte
- Vira guia completo

---

## 🚀 Próximos Passos

**Semana 1:** Setup + Primeiro post
**Semana 2-4:** 1 post/semana
**Mês 2:** Achar cadência confortável
**Mês 3:** Otimizar sistema com IA
**Mês 6:** Blog estabelecido, tráfego orgânico

**Próximo passo no Módulo 6:**
Vamos criar **apresentações e vídeos técnicos** usando NotebookLM, HeyGen e outras ferramentas de IA!

---

## 📚 Recursos

**Plataformas:**
- [Hashnode](https://hashnode.com)
- [Dev.to](https://dev.to)
- [Medium](https://medium.com)

**IA Writing:**
- ChatGPT / Claude
- [Grammarly](https://grammarly.com)
- [Hemingway Editor](http://hemingwayapp.com)

**Cover Images:**
- [Canva](https://canva.com)
- [Carbon](https://carbon.now.sh) (code screenshots)
- [Unsplash](https://unsplash.com)

**Distribuição:**
- [Buffer](https://buffer.com)
- [Zapier](https://zapier.com)

---

**Tempo:** 3-4h (setup + primeiros 2 posts)
**Manutenção:** 1h/semana

**Próximo módulo:** Módulo 6 - Apresentações e Vídeos com IA (NotebookLM, HeyGen, Podscap)
