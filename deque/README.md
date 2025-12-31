# DEQUE (Double-Ended Queue)

Esta seção explica, visualmente e de forma organizada, a implementação de **Deque** presente no repositório (versão *naive* e *optimized*), quando usar cada uma, a complexidade (Big-O) das operações, para fins didáticos.

---

## O que é um Deque?

Um **Deque** (Double-Ended Queue) é uma estrutura de dados que permite **inserção e remoção de elementos em ambas as extremidades** da fila: início (*left*) e fim (*right*).

Diferente da FIFO tradicional, o Deque **não impõe uma única política de entrada ou saída**. Ele oferece flexibilidade total.

### Operações básicas usadas aqui

- `push_left(item)` — insere um item no início do deque  
- `push_right(item)` — insere um item no final do deque  
- `pop_left()` — remove e retorna o item do início  
- `pop_right()` — remove e retorna o item do final  
- `peek_left()` — retorna o item do início sem removê-lo  
- `peek_right()` — retorna o item do final sem removê-lo  
- `size()` — retorna o tamanho atual  
- `is_empty()` — indica se está vazio  

---

## Política de Entrada (push_left e push_right)

O Deque **não possui uma política única de entrada**.

Quem usa a estrutura decide, a cada operação, onde o elemento entra:

- `push_left(item)` → entrada pelo início  
- `push_right(item)` → entrada pelo final  

Isso significa que:

- a ordem não é apenas cronológica;
- a estrutura não impõe regras de prioridade;
- o controle está totalmente nas mãos do código que usa o deque.

Conceitualmente, o Deque é uma **fila bidirecional**, não uma fila com comportamento fixo.

---

## Política de Saída (pop_left e pop_right)

Da mesma forma, a remoção pode acontecer em qualquer extremidade:

- `pop_left()` → remove o elemento mais à esquerda  
- `pop_right()` → remove o elemento mais à direita  

Essa liberdade permite simular diferentes estruturas:

- FIFO → `push_right` + `pop_left`  
- LIFO (pilha) → `push_right` + `pop_right`  
- buffers deslizantes  
- janelas temporais  
- algoritmos de duas pontas  

Nada “fura fila” por regra interna — **quem define o comportamento é o padrão de uso**.

---

## Por que Deque é importante?

O Deque é uma das estruturas mais versáteis da computação prática. Ele aparece em:

- algoritmos de janela deslizante (*sliding window*);
- BFS (busca em largura) e variações;
- schedulers simples;
- buffers circulares;
- estruturas internas de caches;
- substituição eficiente de listas quando há remoção no início.

Ele é um ótimo exemplo de estrutura onde **o poder vem da neutralidade**: poucas regras, muitas possibilidades.

---

## Visualização (como pensar mentalmente)

Deque com três elementos:

```
left                       right
  v                           v
[ A,  B,  C ]
```


Operações possíveis:

- `push_left('X')` → `[ X, A, B, C ]`
- `push_right('Y')` → `[ A, B, C, Y ]`
- `pop_left()` → remove `A`
- `pop_right()` → remove `C`

O Deque não “escolhe lados”. Ele apenas oferece os dois.

---

## Implementações no repositório

### 1) `DequeNaive` (`deque/naive.py`)

Implementação usando **lista Python (`list`)**.

**Operações:**

- `push_right`: `list.append(item)` — **O(1) amortizado**
- `push_left`: `list.insert(0, item)` — **O(n)**
- `pop_right`: `list.pop()` — **O(1)**
- `pop_left`: `list.pop(0)` — **O(n)**

**Boa para:**

- fins didáticos;
- entender o custo real de deslocamento em listas;
- cenários pequenos e controlados.

---

### 2) `OptimizedDeque` (`deque/optimized.py`)

Implementação encapsulando **`collections.deque`**.

**Operações:**

- `append` / `appendleft` — **O(1)**
- `pop` / `popleft` — **O(1)**

**Boa para:**

- produção;
- grandes volumes de dados;
- algoritmos que exigem remoção frequente nas duas extremidades.

O `deque` da biblioteca padrão é implementado em C e otimizado exatamente para esse caso de uso.

---

## Big-O (resumo)

| Operação     | Deque naive (list) | Deque optimized (deque) |
|--------------|--------------------|--------------------------|
| push_left    | O(n)               | O(1)                     |
| push_right   | O(1) amortizado    | O(1)                     |
| pop_left     | O(n)               | O(1)                     |
| pop_right    | O(1)               | O(1)                     |
| peek_left    | O(1)               | O(1)                     |
| peek_right   | O(1)               | O(1)                     |
| size         | O(1)               | O(1)                     |
| is_empty     | O(1)               | O(1)                     |

> **Nota:** os custos refletem o comportamento real das estruturas no CPython.  
> O `deque` foi projetado exatamente para evitar o custo de deslocamento presente nas listas.

---

## Quando usar qual implementação?

**Use `DequeNaive` se:**

- o objetivo é aprendizado;
- você quer visualizar claramente o custo das operações;
- o tamanho da estrutura é pequeno.

**Use `OptimizedDeque` se:**

- remoções nos dois lados são frequentes;
- desempenho importa de verdade.
