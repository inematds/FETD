# 📘 Formato da Trilha Operacional (Formato Manual Rico)

**Data:** 2025-01-19
**Trilha:** Operacional Produtivo
**Status:** Formato aprovado e em uso

---

## 🎯 Visão Geral

A Trilha 1 (Operacional) usa um formato HTML manual cuidadosamente criado que serve como **referência de qualidade visual** para as outras trilhas.

### Características Principais

- ✅ **Hero simples** com gradiente duplo (`from-operacional to-blue-600`)
- ✅ **Box de objetivo destacado** com ícone 🎯
- ✅ **Grid comparativo Antes/Agora** em boxes separados
- ✅ **Cards de mitos** (vermelho) com exemplos internos
- ✅ **Card de verdade** (verde) ao final
- ✅ **Layout limpo** com espaçamento generoso
- ✅ **Dark mode** completo

---

## 🎨 Elementos Visuais

### 1. Hero Section

**Características:**
- Gradiente duplo simples: `bg-gradient-to-r from-operacional to-blue-600`
- Padding padrão: `py-16`
- Badges com fundo semi-transparente: `bg-white/20`
- Título até `text-5xl` (não 6xl)

**Código:**
```html
<section class="bg-gradient-to-r from-operacional to-blue-600 py-16">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white">
    <div class="flex items-center gap-3 mb-4">
      <span class="px-3 py-1 bg-white/20 rounded-full text-sm font-semibold">Módulo 1 de 10</span>
      <span class="px-3 py-1 bg-white/20 rounded-full text-sm font-semibold">⏱️ 30 minutos</span>
    </div>

    <h1 class="text-4xl lg:text-5xl font-extrabold mb-4">
      A Virada - Por Que Agora é Diferente
    </h1>

    <p class="text-xl text-white/90 mb-6 max-w-3xl">
      Descrição do módulo
    </p>

    <div class="flex items-center gap-4">
      <span class="text-white/80">📚 Teoria</span>
      <span class="text-white/80">•</span>
      <span class="text-white/80">💭 Reflexão</span>
      <span class="text-white/80">•</span>
      <span class="text-white/80">🛠️ Prática</span>
    </div>
  </div>
</section>
```

### 2. Box de Objetivo

**Diferenças do v2.0:**
- SEM ícone dentro do título (ícone vem antes do texto)
- Título sem flex: `<h3>🎯 Objetivo deste Módulo</h3>`
- Não tem sombra (`shadow-lg` ausente)

**Código:**
```html
<div class="bg-operacional/10 dark:bg-operacional/20 border-l-4 border-operacional p-6 rounded-lg mb-12">
  <h3 class="text-xl font-bold text-operacional mb-2">🎯 Objetivo deste Módulo</h3>
  <p class="text-neutral-700 dark:text-neutral-300">
    Texto do objetivo aqui
  </p>
</div>
```

### 3. Grid Comparativo "Antes / Agora"

**Características:**
- 2 boxes separados (não grid em 2 colunas)
- Empilhados verticalmente
- Fundo neutro para "Antes"
- Fundo colorido da trilha para "Agora"
- Sem borders duplos

**Código:**
```html
<!-- Antes -->
<div class="bg-neutral-50 dark:bg-neutral-900 p-6 rounded-xl mb-6">
  <h4 class="font-bold text-lg mb-4">Antes de 2023:</h4>
  <ul class="space-y-3 text-neutral-700 dark:text-neutral-300">
    <li class="flex items-start gap-3">
      <span class="text-red-500 text-xl">❌</span>
      <span>Item negativo</span>
    </li>
    <!-- ... mais itens -->
  </ul>
</div>

<!-- Agora -->
<div class="bg-operacional/10 dark:bg-operacional/20 p-6 rounded-xl mb-6">
  <h4 class="font-bold text-lg mb-4">Agora (2025):</h4>
  <ul class="space-y-3 text-neutral-700 dark:text-neutral-300">
    <li class="flex items-start gap-3">
      <span class="text-green-500 text-xl">✅</span>
      <span>Item positivo</span>
    </li>
    <!-- ... mais itens -->
  </ul>
</div>
```

### 4. Cards de Mitos

**Características:**
- Fundo vermelho: `bg-red-50 dark:bg-red-900/20`
- Border à esquerda: `border-l-4 border-red-500`
- Título vermelho: `text-red-700 dark:text-red-400`
- **Box interno branco** com exemplo (diferencial!)
- SEM sombra hover

**Código:**
```html
<div class="bg-red-50 dark:bg-red-900/20 border-l-4 border-red-500 p-6 rounded-lg mb-6">
  <h3 class="text-xl font-bold text-red-700 dark:text-red-400 mb-3">
    ❌ MITO 1: "Título do mito"
  </h3>
  <p class="text-neutral-700 dark:text-neutral-300 mb-3">
    <strong>FALSO.</strong> Explicação do porquê é falso.
  </p>

  <!-- Box de exemplo interno (DIFERENCIAL!) -->
  <div class="bg-white dark:bg-neutral-800 p-4 rounded">
    <p class="text-sm italic">
      <strong>Exemplo real:</strong> História de uma pessoa...
    </p>
  </div>
</div>
```

### 5. Card de Verdade

**Características:**
- Fundo verde: `bg-green-50 dark:bg-green-900/20`
- Border à esquerda: `border-l-4 border-green-500`
- Título verde: `text-green-700 dark:text-green-400`
- Sem box interno

**Código:**
```html
<div class="bg-green-50 dark:bg-green-900/20 border-l-4 border-green-500 p-6 rounded-lg">
  <p class="text-lg font-bold text-green-700 dark:text-green-400 mb-2">
    ✅ A VERDADE:
  </p>
  <p class="text-neutral-700 dark:text-neutral-300">
    Você só precisa de: <strong>vontade + tempo + computador</strong>.
  </p>
</div>
```

---

## 📊 Comparação: Trilha Operacional vs Conversor v2.0

| Elemento | Trilha Operacional (Manual) | Conversor v2.0 (Automático) |
|----------|----------------------------|----------------------------|
| **Hero** | Gradiente duplo simples | Gradiente triplo + grid pattern |
| **Hero Size** | py-16, text-5xl | py-20, text-6xl |
| **Hero Badges** | bg-white/20 (opaco) | bg-white/20 backdrop-blur-sm |
| **Box Objetivo** | Sem sombra | Com shadow-lg |
| **Antes/Agora** | 2 boxes empilhados | Grid 2 colunas (md:grid-cols-2) |
| **Cards Mitos** | Com box exemplo interno | Sem box interno |
| **Cards Mitos Sombra** | Sem hover | shadow-md hover:shadow-lg |
| **Tabelas** | Não presente no M1 | Header gradiente + hover |
| **Código** | Não presente no M1 | Terminal com 3 bolinhas |
| **Download Button** | Botão simples | Gradiente + shadow hover |
| **Font Weights** | 400-800 | 400-900 |
| **Navbar Blur** | backdrop-blur-sm | backdrop-blur-md |

---

## 🎯 Qual Usar?

### Use Trilha Operacional (Manual) quando:

- ✅ Você quer controle total sobre cada elemento
- ✅ Precisa de layout único e personalizado
- ✅ Quer adicionar elementos especiais (ex: box de exemplo interno)
- ✅ Está criando um módulo de referência
- ✅ Prefere simplicidade e clareza

### Use Conversor v2.0 (Automático) quando:

- ✅ Tem muito conteúdo Markdown para converter
- ✅ Quer velocidade e consistência
- ✅ Prefere layout mais "premium" e visual
- ✅ Precisa converter múltiplos módulos rapidamente
- ✅ Quer aproveitar detecção automática de cards especiais

---

## 💡 Recomendação

**Para o FETD:**

1. **Trilha Operacional** (Trilha 1) → Mantenha formato manual original
   - É a trilha de referência
   - Layout limpo e direto
   - Já está bem estruturado

2. **Trilhas 2, 3, 4** → Use Conversor v2.0
   - Acelera criação de conteúdo
   - Consistência visual entre trilhas
   - Facilita manutenção futura

3. **Módulos especiais** → Adapte manualmente
   - Se precisar de elementos únicos
   - Inspirar-se nos dois formatos

---

## 🔧 Elementos Únicos da Trilha Operacional

### Box de Exemplo Interno (nos Cards de Mitos)

Este é um elemento ÚNICO da Trilha Operacional que não está no Conversor v2.0:

```html
<!-- Dentro do card de mito -->
<div class="bg-white dark:bg-neutral-800 p-4 rounded">
  <p class="text-sm italic">
    <strong>Exemplo real:</strong> Maria, analista administrativa, criou sozinha...
  </p>
</div>
```

**Vantagem:**
- Destaca exemplos práticos visualmente
- Quebra visual dentro do card
- Mais fácil de ler (texto menor, itálico)

**Para adicionar ao Conversor v2.0:**
Seria necessário detectar padrões como:
```markdown
### ❌ Mito 1: Título

Explicação do mito.

**Exemplo real:** João fez X...
```

E gerar HTML com box interno automaticamente.

---

## 📝 Checklist de Elementos

### ✅ Presentes em Ambos

- [x] Navbar sticky com dark mode toggle
- [x] Breadcrumb
- [x] Hero com gradiente
- [x] Box de objetivo destacado
- [x] Cards de mitos (vermelho)
- [x] Listas com ícones
- [x] Dark mode completo
- [x] Responsivo
- [x] Footer com navegação

### ⚠️ Apenas na Trilha Operacional

- [x] Box de exemplo interno nos mitos
- [x] Grid "Antes/Agora" vertical (empilhado)
- [x] Layout mais limpo e direto

### ⚠️ Apenas no Conversor v2.0

- [x] Hero com gradient triplo
- [x] Hero com grid pattern
- [x] Grid "Antes/Agora" horizontal (2 colunas)
- [x] Tabelas com gradiente
- [x] Código estilo terminal
- [x] Cards com hover effects
- [x] Box de objetivo com sombra
- [x] Download button com gradiente
- [x] Cards de dados (azul)
- [x] Cards importantes (amarelo)
- [x] Títulos de seção com gradient background

---

## 🚀 Como Aplicar Formato Trilha Operacional

Se você quiser replicar o formato da Trilha Operacional em outras trilhas:

### 1. Copiar estrutura base

```bash
cp modulos/operacional/modulo-01.html modulos/comunicador/modulo-01-base.html
```

### 2. Trocar cores

```bash
# Substituir 'operacional' pela nova trilha
sed -i 's/operacional/comunicador/g' modulos/comunicador/modulo-01-base.html

# Substituir hex color
sed -i 's/#3B82F6/#10B981/g' modulos/comunicador/modulo-01-base.html
```

### 3. Substituir conteúdo

Editar manualmente:
- Título do módulo
- Descrição
- Seções e subseções
- Cards de mitos
- Exemplos

---

## 📚 Referências de Código

### Navbar da Trilha Operacional

```html
<nav class="sticky top-0 z-50 bg-white/90 dark:bg-neutral-800/90 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-700">
  <!-- Sem shadow-sm -->
</nav>
```

### Download Button da Trilha Operacional

```html
<a href="../../downloads/operacional/modulo-01.md" download class="px-6 py-3 bg-operacional text-white rounded-lg font-semibold hover:opacity-90 inline-flex items-center gap-2">
  <!-- Botão simples, sem gradiente, sem sombra -->
</a>
```

### Títulos de Seção da Trilha Operacional

```html
<h2 class="text-3xl font-bold mb-6">1. Título da Seção</h2>
<!-- Sem gradient background, sem border-b, mais simples -->
```

---

## ✨ Conclusão

**Trilha Operacional** = Formato manual limpo e direto
**Conversor v2.0** = Formato automático premium e visual

Ambos são válidos e têm seus casos de uso. A Trilha Operacional serve como referência de clareza, enquanto o Conversor v2.0 adiciona camadas extras de polish visual.

**Escolha baseada em:**
- Tempo disponível (manual = mais tempo)
- Controle necessário (manual = total)
- Quantidade de conteúdo (automático = melhor para volume)
- Estilo preferido (limpo vs premium)

---

**Última atualização:** 2025-01-19
**Versão:** 1.0
