# Módulo 3: ChatGPT Personalizado com RAG - Seu Assistente Técnico que Sabe Tudo do Seu Domínio

**Duração:** 90 minutos
**Nível:** Intermediário
**Objetivo:** Criar chatbots personalizados que conhecem profundamente sua área técnica usando RAG (Retrieval-Augmented Generation)

---

## 🎯 O Que Você Vai Aprender

Ao final deste módulo, você será capaz de:

✅ Entender como RAG funciona e por que é revolucionário
✅ Criar chatbots personalizados com conhecimento específico do seu domínio
✅ Implementar sistemas de perguntas e respostas sobre documentação técnica
✅ Construir assistentes que ajudam pessoas com problemas reais da sua área
✅ Integrar conhecimento técnico (docs, código, tickets) em IA conversacional

**Resultado prático:** Chatbot funcionando que responde perguntas sobre SUA área técnica com precisão.

---

## 🔥 Por Que RAG Muda o Jogo

### O Problema com ChatGPT Normal

**Cenário real:** Alguém pergunta no Slack:

> "Como faço deploy da nossa API em staging?"

**Opções tradicionais:**
- ❌ Você responde manualmente (15 min)
- ❌ Procura na wiki desatualizada (20 min de frustração)
- ❌ Pede pra alguém mais velho explicar (interrompe 2 pessoas)
- ❌ Usa ChatGPT genérico que inventa comandos errados

**Com RAG:**
- ✅ Chatbot responde em 10 segundos
- ✅ Baseado na SUA documentação real
- ✅ Com comandos corretos do SEU ambiente
- ✅ Links para docs relevantes
- ✅ Você economizou 15 minutos + ajudou permanentemente

### O Que é RAG (sem enrolação)

**RAG = Retrieval-Augmented Generation**

Tradução prática:
1. **Retrieval:** Busca informação relevante nos SEUS documentos
2. **Augmented:** Injeta essa informação no prompt
3. **Generation:** ChatGPT responde baseado no SEU conteúdo

**Analogia:**
- **ChatGPT normal:** Estudante respondendo de memória (às vezes inventa)
- **ChatGPT com RAG:** Estudante com seus livros abertos fazendo consulta ao vivo

### Por Que Funciona Melhor

| Aspecto | ChatGPT Normal | ChatGPT com RAG |
|---------|----------------|-----------------|
| **Conhecimento** | Genérico até 2023 | SEU domínio, atualizado |
| **Precisão** | Inventa quando não sabe | Cita fontes reais |
| **Contexto** | Limitado (8k-32k tokens) | Acessa toda sua base |
| **Atualização** | Fixo no tempo | Atualiza com novos docs |
| **Confiabilidade** | 70-80% | 90-95% (se docs bons) |

---

## 🛠️ Como RAG Funciona (Arquitetura Simples)

### Fluxo Passo a Passo

```
┌─────────────────────────────────────────────────────────┐
│ 1. PREPARAÇÃO (fazer 1x)                                │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Seus Documentos (docs, wikis, READMEs)                 │
│           ↓                                              │
│  Chunking (quebra em pedaços)                           │
│           ↓                                              │
│  Embeddings (transforma em vetores)                     │
│           ↓                                              │
│  Vector Database (Pinecone, Chroma, FAISS)              │
│                                                           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ 2. QUANDO ALGUÉM PERGUNTA (tempo real)                  │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Pergunta do usuário                                     │
│           ↓                                              │
│  Embedding da pergunta                                   │
│           ↓                                              │
│  Busca vetorial (acha docs relevantes)                  │
│           ↓                                              │
│  Top 3-5 trechos mais relevantes                        │
│           ↓                                              │
│  Monta prompt: contexto + pergunta                      │
│           ↓                                              │
│  ChatGPT responde baseado no contexto                   │
│           ↓                                              │
│  Resposta + fontes citadas                              │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Conceitos-Chave

**1. Embeddings (Vetores Semânticos)**

Transforma texto em números que capturam significado:

```python
# Texto original
"Como fazer deploy em staging?"

# Vira vetor (exemplo simplificado)
[0.23, -0.45, 0.78, ..., 0.12]  # 1536 dimensões

# Textos similares têm vetores próximos
"Deploy para ambiente de testes" → vetor parecido ✅
"Como fazer café?" → vetor distante ❌
```

**2. Vector Database**

Banco de dados especializado em buscar vetores similares:

```python
# Busca semântica (não precisa palavras exatas)
pergunta = "subir API pra homologação"

# Acha documentos sobre:
# - "deploy em staging"  ✅
# - "publicar em ambiente de teste"  ✅
# - "CI/CD pipeline"  ✅
#
# Mesmo sem usar palavras exatas!
```

**3. Chunking (Quebrar Documentos)**

Divide docs grandes em pedaços úteis:

```markdown
# Doc original: 10 páginas sobre deploy

# Chunks (pedaços de 500-1000 caracteres)
Chunk 1: "Para fazer deploy em staging..."
Chunk 2: "Configuração do ambiente..."
Chunk 3: "Comandos necessários..."
...

# Por que?
# ChatGPT só vê 3-5 chunks mais relevantes
# Não precisa ler 10 páginas inteiras
```

---

## 🚀 Projeto Prático: Chatbot de Documentação Técnica

Vamos criar um chatbot que responde perguntas sobre SUA documentação técnica.

### Opção 1: LangChain + OpenAI (Mais Completo)

**Stack:**
- LangChain (framework RAG)
- OpenAI API (embeddings + chat)
- Chroma (vector database local)
- Streamlit (interface)

**Passo 1: Setup**

```bash
# Instalar dependências
pip install langchain openai chromadb tiktoken streamlit

# Criar estrutura
mkdir meu-chatbot-rag
cd meu-chatbot-rag
mkdir docs  # Coloque seus documentos aqui
```

**Passo 2: Indexar Documentos** (`indexar.py`)

```python
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os

# Configurar API key
os.environ["OPENAI_API_KEY"] = "sua-api-key-aqui"

# 1. Carregar documentos
print("📂 Carregando documentos...")
loader = DirectoryLoader('docs/', glob="**/*.md", loader_cls=TextLoader)
documents = loader.load()
print(f"✅ {len(documents)} documentos carregados")

# 2. Quebrar em chunks
print("✂️ Quebrando em chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Tamanho do pedaço
    chunk_overlap=200,  # Sobreposição (contexto)
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(documents)
print(f"✅ {len(chunks)} chunks criados")

# 3. Criar embeddings e salvar
print("🧠 Criando embeddings...")
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"  # Salva localmente
)
vectorstore.persist()
print("✅ Base de conhecimento criada!")
```

**Passo 3: Interface Streamlit** (`app.py`)

```python
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# Configuração
os.environ["OPENAI_API_KEY"] = "sua-api-key-aqui"

st.title("🤖 Assistente de Documentação Técnica")
st.caption("Pergunte qualquer coisa sobre nossa stack!")

# Carregar base de conhecimento
@st.cache_resource
def load_qa_chain():
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    llm = ChatOpenAI(
        model_name="gpt-4",
        temperature=0  # Respostas mais precisas
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # Tipo de chain
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}  # Top 3 chunks
        ),
        return_source_documents=True  # Retorna fontes
    )

    return qa_chain

qa_chain = load_qa_chain()

# Interface de chat
pergunta = st.text_input("Faça sua pergunta:")

if pergunta:
    with st.spinner("🔍 Buscando na documentação..."):
        result = qa_chain({"query": pergunta})

        # Mostrar resposta
        st.markdown("### 💡 Resposta")
        st.write(result["result"])

        # Mostrar fontes
        st.markdown("### 📚 Fontes")
        for i, doc in enumerate(result["source_documents"], 1):
            with st.expander(f"Fonte {i}: {doc.metadata.get('source', 'Documento')}"):
                st.text(doc.page_content)

# Sidebar com exemplos
st.sidebar.title("Exemplos de perguntas")
st.sidebar.markdown("""
- Como fazer deploy em staging?
- Qual é o processo de code review?
- Como rodar os testes localmente?
- Onde fica a documentação da API?
- Como configurar ambiente de dev?
""")
```

**Passo 4: Rodar**

```bash
# 1. Colocar seus docs .md na pasta docs/
# 2. Indexar (fazer 1x ou quando docs mudarem)
python indexar.py

# 3. Rodar chatbot
streamlit run app.py
```

### Opção 2: OpenAI Assistants API (Mais Fácil)

OpenAI agora tem RAG embutido! Não precisa gerenciar vector database.

**Código completo:**

```python
import openai
import streamlit as st

client = openai.OpenAI(api_key="sua-api-key")

# 1. Criar assistente (fazer 1x)
def criar_assistente():
    # Upload arquivos
    file1 = client.files.create(
        file=open("docs/deploy.md", "rb"),
        purpose="assistants"
    )
    file2 = client.files.create(
        file=open("docs/api-docs.md", "rb"),
        purpose="assistants"
    )

    # Criar assistente com file search (RAG)
    assistant = client.beta.assistants.create(
        name="Assistente Técnico",
        instructions="""Você é um assistente técnico especializado.
        Responda baseado nos documentos fornecidos.
        Sempre cite as fontes.""",
        model="gpt-4-turbo",
        tools=[{"type": "file_search"}],
        tool_resources={
            "file_search": {
                "vector_stores": [{
                    "file_ids": [file1.id, file2.id]
                }]
            }
        }
    )

    return assistant.id

# 2. Interface Streamlit
st.title("🤖 Assistente com RAG (OpenAI)")

# Inicializar
if "assistant_id" not in st.session_state:
    st.session_state.assistant_id = "asst_xxxxx"  # Seu ID aqui
if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

# Chat
pergunta = st.text_input("Sua pergunta:")

if pergunta:
    # Enviar mensagem
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=pergunta
    )

    # Rodar assistente
    with st.spinner("Pensando..."):
        run = client.beta.threads.runs.create_and_poll(
            thread_id=st.session_state.thread_id,
            assistant_id=st.session_state.assistant_id
        )

    # Pegar resposta
    messages = client.beta.threads.messages.list(
        thread_id=st.session_state.thread_id
    )

    resposta = messages.data[0].content[0].text.value
    st.markdown(f"**Resposta:** {resposta}")
```

**Vantagens:**
- ✅ Não precisa gerenciar vector database
- ✅ OpenAI cuida de tudo (chunking, embeddings, busca)
- ✅ Código mais simples
- ✅ Escala automaticamente

**Desvantagens:**
- ❌ Mais caro (paga por storage de arquivos)
- ❌ Menos controle sobre chunking
- ❌ Depende 100% da OpenAI

---

## 🎯 Casos de Uso Reais

### Caso 1: Assistente de Onboarding

**Problema:** Novos devs fazem as mesmas perguntas

**Solução RAG:**

```python
# Documentos indexados:
# - README.md
# - CONTRIBUTING.md
# - ARCHITECTURE.md
# - Onboarding wiki
# - FAQs do Slack (exportados)

# Chatbot responde:
# "Como rodar o projeto local?"
# "Qual é o fluxo de PR?"
# "Onde fica a staging?"
# "Preciso de acesso a quê?"
```

**Resultado:**
- ⏱️ Dev júnior demora 3 dias → 1 dia pra ser produtivo
- 🕐 Você economiza 5h de onboarding manual
- 📈 Satisfação de novos devs sobe 40%

### Caso 2: Bot de Troubleshooting

**Problema:** Suporte pergunta "como resolver erro X" toda semana

**Solução RAG:**

```python
# Base de conhecimento:
# - Post-mortems de incidentes
# - Runbooks
# - Issues do GitHub resolvidos
# - Logs de troubleshooting

# Bot ajuda com:
# "API retornando 502, o que fazer?"
# "Build falhou com erro XYZ"
# "Como fazer rollback de deploy?"
```

**Resultado:**
- 🚀 70% dos problemas resolvidos sem escalar
- ⏱️ MTTR (Mean Time To Resolution) cai 50%
- 😊 Time de suporte feliz

### Caso 3: Chatbot de API Docs

**Problema:** Documentação de API complexa, difícil de navegar

**Solução RAG:**

```python
# Indexa:
# - OpenAPI/Swagger spec
# - Exemplos de código
# - Changelog
# - Guias de autenticação

# Desenvolvedor pergunta naturalmente:
# "Como autenticar na API?"
# "Exemplo de request pra criar usuário"
# "Rate limits da API de payments?"
# "O que mudou na v2?"
```

**Resultado:**
- 📉 Tickets de suporte sobre API: -60%
- ⚡ Time to first successful API call: -70%
- 💰 Adoção da API aumenta

---

## 🧰 Ferramentas e Alternativas

### Vector Databases

| Ferramenta | Quando usar | Custo |
|------------|-------------|-------|
| **Chroma** | Projetos pequenos, local | Grátis |
| **Pinecone** | Produção, escala | $70/mês |
| **Weaviate** | Self-hosted, controle total | Grátis (infra sua) |
| **FAISS** | Pesquisa rápida, offline | Grátis |
| **Qdrant** | Open source, produção | Grátis ou pago |

### Frameworks RAG

**LangChain:**
```python
# Mais completo, muitos integrações
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(...)
```

**LlamaIndex:**
```python
# Especializado em RAG, mais simples
from llama_index import VectorStoreIndex
index = VectorStoreIndex.from_documents(docs)
```

**Haystack:**
```python
# Focado em NLP pipelines
from haystack.nodes import DensePassageRetriever
retriever = DensePassageRetriever(...)
```

### Soluções No-Code

**1. ChatBase** (chatbase.co)
- Upload docs → chatbot pronto
- Embeddable widget
- $19/mês

**2. CustomGPT** (customgpt.ai)
- RAG sem código
- Integrações prontas
- $89/mês

**3. Dante AI** (dante-ai.com)
- Treinamento rápido
- Multi-plataforma
- $30/mês

**Quando usar no-code:**
- ✅ Validar ideia rápido
- ✅ Não tem time de dev
- ✅ Volume baixo de perguntas

**Quando fazer custom:**
- ✅ Integração com sistemas internos
- ✅ Controle total sobre dados
- ✅ Alto volume (mais barato)

---

## 📊 Otimizando Seu RAG

### 1. Melhorar Qualidade das Respostas

**Chunking inteligente:**

```python
# ❌ Ruim: quebra no meio de seção
RecursiveCharacterTextSplitter(chunk_size=500)

# ✅ Bom: respeita estrutura markdown
from langchain.text_splitter import MarkdownHeaderTextSplitter

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)
```

**Metadados úteis:**

```python
# Adicionar metadados aos chunks
for i, chunk in enumerate(chunks):
    chunk.metadata = {
        "source": "deploy.md",
        "section": "Staging",
        "last_updated": "2025-01-15",
        "author": "DevOps Team"
    }

# Usar em filtros
vectorstore.similarity_search(
    "como fazer deploy",
    filter={"section": "Staging"}  # Busca só em Staging
)
```

**Prompt engineering:**

```python
# Template de prompt otimizado
template = """Use os seguintes documentos para responder a pergunta.
Se não souber, diga "não encontrei essa informação".
NÃO invente informações.

Contexto:
{context}

Pergunta: {question}

Resposta (em português, cite fontes):"""
```

### 2. Reduzir Custos

**Embeddings mais baratos:**

```python
# OpenAI embeddings: $0.0001/1K tokens
embeddings = OpenAIEmbeddings()

# Alternativa grátis (roda local):
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

**Caching agressivo:**

```python
# Cachear respostas comuns
import hashlib
import json

cache = {}

def ask_with_cache(question):
    key = hashlib.md5(question.encode()).hexdigest()

    if key in cache:
        return cache[key]  # Hit!

    answer = qa_chain(question)
    cache[key] = answer
    return answer
```

**Modelo mais barato para retrieval:**

```python
# Use GPT-4 só quando necessário
from langchain.chat_models import ChatOpenAI

# Retrieval + ranqueamento: GPT-3.5 (mais barato)
cheap_llm = ChatOpenAI(model="gpt-3.5-turbo")

# Resposta final: GPT-4 (melhor qualidade)
good_llm = ChatOpenAI(model="gpt-4")
```

### 3. Melhorar Performance

**Hybrid search (keyword + semantic):**

```python
from langchain.retrievers import BM25Retriever, EnsembleRetriever

# Busca semântica
semantic_retriever = vectorstore.as_retriever()

# Busca por palavras-chave
bm25_retriever = BM25Retriever.from_documents(documents)

# Combina os dois!
ensemble_retriever = EnsembleRetriever(
    retrievers=[semantic_retriever, bm25_retriever],
    weights=[0.5, 0.5]  # 50% cada
)
```

**Reranking:**

```python
# Busca 10 docs, rerankeia com modelo melhor, usa top 3
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank

compressor = CohereRerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever(search_kwargs={"k": 10})
)
```

---

## ✅ Checklist de Implementação

### Fase 1: Setup Básico (1-2h)

- [ ] Escolher stack (LangChain vs OpenAI Assistants vs no-code)
- [ ] Configurar ambiente (instalar libs, API keys)
- [ ] Coletar documentos (READMEs, wikis, docs)
- [ ] Organizar docs em pasta estruturada

### Fase 2: Indexação (30min-1h)

- [ ] Implementar chunking (tamanho adequado)
- [ ] Adicionar metadados relevantes
- [ ] Criar embeddings e indexar
- [ ] Testar busca vetorial manualmente

### Fase 3: Chatbot (1-2h)

- [ ] Criar interface (Streamlit, web, Slack bot)
- [ ] Implementar chain de QA
- [ ] Adicionar prompt customizado
- [ ] Testar com perguntas reais

### Fase 4: Refinamento (1-2h)

- [ ] Coletar feedback de usuários
- [ ] Ajustar chunking se necessário
- [ ] Melhorar prompt com exemplos
- [ ] Adicionar cache para perguntas comuns
- [ ] Implementar analytics (quais perguntas, taxa de sucesso)

### Fase 5: Produção (variável)

- [ ] Deploy (Streamlit Cloud, Vercel, Docker)
- [ ] Configurar atualização automática de docs
- [ ] Monitoramento de custos
- [ ] Sistema de feedback dos usuários
- [ ] Documentar para o time usar

---

## 🎓 Exercício Prático

### Desafio: Chatbot da Sua Área

**Objetivo:** Criar chatbot que responde perguntas sobre SUA área técnica.

**Passo a passo:**

1. **Escolha o domínio** (30 min)
   - Sua stack atual (ex: "Deploy de aplicações Node.js")
   - Troubleshooting comum (ex: "Resolver erros de banco de dados")
   - Onboarding (ex: "Setup de ambiente de dev")

2. **Colete documentos** (30 min)
   - READMEs de projetos
   - Documentação interna
   - Runbooks
   - Post-mortems
   - FAQs do Slack
   - **Meta: 5-10 documentos** (não precisa ser perfeito)

3. **Implemente versão básica** (1-2h)
   - Use Opção 1 (LangChain) OU Opção 2 (OpenAI Assistants)
   - Indexe seus docs
   - Crie interface Streamlit simples
   - Teste com 5 perguntas reais

4. **Refine** (30 min-1h)
   - Ajuste prompts baseado nos resultados
   - Adicione metadados se necessário
   - Melhore chunking se respostas incompletas

5. **Compartilhe** (15 min)
   - Mande link do Streamlit para 3 colegas
   - Peça feedback honesto
   - Itere baseado no feedback

**Critérios de sucesso:**
- ✅ Responde 8/10 perguntas corretamente
- ✅ Cita fontes relevantes
- ✅ Tempo de resposta < 10 segundos
- ✅ Pelo menos 1 colega diz "isso é útil!"

---

## 📈 Métricas de Sucesso

Como saber se seu RAG está funcionando?

### Métricas Técnicas

**1. Precisão da Busca**
```python
# Porcentagem de perguntas que retornam docs relevantes
# Meta: > 85%

def avaliar_retrieval(perguntas_teste):
    acertos = 0
    for q in perguntas_teste:
        docs = vectorstore.similarity_search(q['pergunta'], k=3)
        if q['doc_esperado'] in [d.metadata['source'] for d in docs]:
            acertos += 1
    return acertos / len(perguntas_teste)
```

**2. Qualidade da Resposta**
- Usuário dá 👍/👎 após resposta
- Meta: > 80% de 👍

**3. Latência**
- Tempo de resposta end-to-end
- Meta: < 5 segundos

### Métricas de Negócio

**1. Redução de Perguntas Repetidas**
- Antes vs Depois de ter chatbot
- Meta: -50% em canais de suporte

**2. Time to Answer**
- Quanto tempo demora pra pessoa obter resposta
- Antes: 2h (espera humano) → Depois: 10s (chatbot)

**3. Satisfação (CSAT)**
- Survey rápido: "O chatbot ajudou?" (1-5)
- Meta: > 4.0

**4. Adoção**
- % do time que usa o chatbot
- Meta: > 60% após 1 mês

---

## 🚀 Próximos Passos

### Nível 1: Básico Funcionando ✅
- Chatbot responde perguntas da sua documentação
- Interface Streamlit simples
- Rodando localmente

### Nível 2: Produção
- Deploy em cloud (Streamlit Cloud, Vercel)
- Integração com Slack/Teams
- Analytics de uso
- Sistema de feedback

### Nível 3: Avançado
- Multi-modal (aceita imagens, PDFs)
- Multi-idioma
- Atualização automática (docs novos → reindexação)
- A/B testing de prompts

### Nível 4: Enterprise
- Multiple chatbots (um por domínio)
- Controle de acesso (chatbot só vê docs que user tem permissão)
- Audit log (quem perguntou o quê)
- Fine-tuning de modelo

---

## 💡 Dicas de Ouro

### 1. Comece Pequeno
- ❌ Não tente indexar toda a empresa no dia 1
- ✅ Comece com 1 domínio específico (ex: deploy)
- ✅ Prove valor → Expanda

### 2. Documentação Ruim = RAG Ruim
- Se seus docs são ruins, RAG vai responder ruim
- **Aproveite para melhorar docs** enquanto implementa RAG
- Chatbot expõe buracos na documentação

### 3. Prompt é 50% do Sucesso
```python
# ❌ Prompt genérico
"Responda a pergunta baseado nos documentos."

# ✅ Prompt específico
"""Você é especialista em DevOps na empresa X.
Responda baseado APENAS nos documentos fornecidos.
Se não souber, diga claramente.
Cite comandos exatos e links quando relevante.
Seja conciso mas completo."""
```

### 4. Feedback Loop é Crítico
```python
# Adicionar botões de feedback
col1, col2 = st.columns(2)
if col1.button("👍 Útil"):
    salvar_feedback(pergunta, resposta, positivo=True)
if col2.button("👎 Não ajudou"):
    salvar_feedback(pergunta, resposta, positivo=False)
```

### 5. Monitore Custos
```python
# Rastreie custos de API
import tiktoken

def estimar_custo(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = len(encoding.encode(text))
    custo_por_mil = 0.0001  # embeddings
    return (tokens / 1000) * custo_por_mil

print(f"Custo estimado: ${estimar_custo(all_docs):.4f}")
```

---

## 🎯 Resumo do Módulo

**O que você aprendeu:**

✅ **RAG = ChatGPT + Seus Documentos**
- Busca informação relevante nos seus docs
- Injeta no prompt
- ChatGPT responde baseado no SEU conteúdo

✅ **Arquitetura:**
- Embeddings → Vector Database → Retrieval → Generation

✅ **Implementação:**
- LangChain + Chroma (controle total)
- OpenAI Assistants (mais fácil)
- No-code (validação rápida)

✅ **Casos de uso:**
- Onboarding de devs
- Troubleshooting
- Documentação de API
- FAQs técnicos

**Próximo passo no Módulo 4:**
Vamos criar seu **portfólio técnico no GitHub** que mostra todos esses projetos incríveis que você está construindo!

---

## 📚 Recursos Adicionais

**Tutoriais:**
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [OpenAI Assistants Guide](https://platform.openai.com/docs/assistants/overview)
- [Pinecone RAG Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)

**Ferramentas:**
- [LangSmith](https://smith.langchain.com/) - Debug RAG chains
- [Ragas](https://github.com/explodinggradients/ragas) - Avaliar qualidade RAG
- [Chroma](https://www.trychroma.com/) - Vector database

**Comunidades:**
- r/LangChain (Reddit)
- LangChain Discord
- OpenAI Developer Forum

---

**Tempo estimado de conclusão:** 3-4 horas (incluindo exercício prático)

**Prerequisitos:** Conhecimento básico de Python, familiaridade com APIs

**Próximo módulo:** Módulo 4 - GitHub como Portfólio de Solucionador Técnico
