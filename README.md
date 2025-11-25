# 🎯 Objetivo do Projeto

Repositório de estudos, destinado a entender e comparar diferentes **estruturas de filas em Python**.

A ideia é criar um espaço organizado onde cada estrutura — FIFO, filas circulares, de prioridade, deques — possa ser explorada de forma clara, prática e com foco tanto no aprendizado quanto na observação de desempenho.

Para cada estrutura implementada, o projeto oferece:

- **Implementação ingênua (naive)**
    
    Uma versão simples, ideal para enxergar o funcionamento interno sem camadas de abstração.
    
- **Implementação otimizada**
    
    Uma variante eficiente, aproveitando estruturas internas do Python quando fizer sentido.
    
- **Explicação detalhada**
    
    Como funciona, quando usar, limitações e visualizações que ajudam a entender o fluxo da estrutura.
    
- **Análise Big-O**
    
    Complexidade das operações explicada e documentada.
    
- **Comparação de performance**
    
    Benchmarks que mostram, de forma prática, como cada implementação se comporta.
    
- **Testes unitários completos**
    
    Garantem que a estrutura funciona corretamente e lida bem com cenários extremos.
    
- **Demonstrações executáveis (demos)**
    
    Pequenos exemplos para ver a fila operando com logs claros.
    

O projeto serve como base sólida para dominar filas, experimentar melhorias e construir conhecimento que será útil quando a transição para sistemas de filas distribuídas (como Redis, Celery ou RabbitMQ) acontecer naturalmente.

---
# Requisitos
Python 3.10

---

# Variáveis de Ambiente

## Variáveis

| Variável             | Tipo | Valores aceitos                                   | Padrão | Descrição |
| ---                  | ---  | ---                                               | ---    | --- |
| `QUEUELAB_LOG_LEVEL` | str  | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`   | `INFO` | Controla o nível de detalhamento dos logs durante demos e benchmarks. |



## Comandos utéis

Caso pretenda configurar o comportamento do projeto por variáveis de ambiente, utilize o arquivo `env.example` como ponto de partida. Ele contém todas as variáveis reconhecidas pelo sistema e seus valores padrão (quando aplicável).

```bash
cp env.example .env
```

---

# FIFO (First-In, First-Out) — explicação detalhada

Esta seção explica, visualmente e de forma organizada, a implementação de **FIFO** presente no repositório (versão *naive* e *optimized*), quando usar cada uma, a complexidade (Big-O) das operações e como validar comportamento via testes e benchmarks.

---

## O que é uma FIFO?

Uma **fila FIFO** (First-In, First-Out) é uma estrutura onde o primeiro elemento a entrar é o primeiro a sair — como uma fila num banco. Operações básicas que usamos aqui:

- `enqueue(item)` — insere um item no final da fila.
- `dequeue()` — remove e retorna o item da frente (head).
- `peek()` — retorna o item da frente sem removê-lo.
- `size()` — retorna o tamanho atual da fila.
- `is_empty()` — indica se a fila está vazia.

---

## Visualização (como pensar mentalmente)

Fila com 3 elementos — `A` chegou primeiro, depois `B`, depois `C`:

```
head                         tail
  v                            v
[ A,  B,  C ]
```

- `peek()` → `A`
- `dequeue()` → remove `A`, fila vira `[ B, C ]`
- `enqueue('D')` → fila vira `[ B, C, D ]`

---

## Implementações no repositório

### 1) `FIFOQueueNaive` (fifo/naive.py)

- Implementação usando **lista Python** internamente (`list`).
- `enqueue`: usa `list.append(item)` — **amortizado O(1)**.
- `dequeue`: usa `list.pop(0)` — **O(n)** por causa do deslocamento dos elementos.
- Boa para: aprendizado, casos com filas muito pequenas, simplicidade e clareza.

### 2) `FIFOQueueOptimized` (fifo/optimized.py)

- Implementação encapsulando `collections.deque`.
- `enqueue`: `deque.append(item)` — **O(1)**.
- `dequeue`: `deque.popleft()` — **O(1)**.
- Boa para: produção, filas com muitos elementos, quando `dequeue` é operação frequente.

---

## Big-O (resumo)

| Operação | FIFO naive (list) | FIFO optimized (deque) |
| --- | --- | --- |
| enqueue | O(1) amortizado | O(1) |
| dequeue | O(n) | O(1) |
| peek | O(1) | O(1) |
| size | O(1) | O(1) |
| is_empty | O(1) | O(1) |

> Nota: list.append é amortizado O(1) — ocasionalmente pode realocar, mas custo médio é constante. Essas complexidades refletem a implementação no CPython (listas e deque otimizados em C).
> 

---

## Quando usar qual implementação?

- **Use `FIFOQueueNaive`** se:
    - o objetivo é estudo didático;
    - filas mantidas forem muito pequenas;
    - simplicidade e transparência forem mais importantes que performance.
- **Use `FIFOQueueOptimized`** se:
    - a fila pode crescer (milhares/milhões de itens);
    - `dequeue` é chamado com frequência;
    - você busca eficiência real em produção.

---

## Exemplos de uso (Python)

```
from fifo.naive import FIFOQueueNaive
from fifo.optimized import FIFOQueueOptimized

# Naive
qn = FIFOQueueNaive()
qn.enqueue(1)
qn.enqueue(2)
print(qn.peek())   # 1
print(qn.dequeue())# 1

# Optimized
qo = FIFOQueueOptimized()
qo.enqueue("a")
qo.enqueue("b")
print(qo.size())   # 2
```

---

## Como validar comportamento

### 1) Testes unitários

Os testes estão em `fifo/tests/` e cobrem:

- enqueue / dequeue em ordem correta (FIFO);
- `peek` não altera estado;
- exceções (`QueueEmptyError`) ao chamar `dequeue`/`peek` em fila vazia;
- representação (`__repr__`).

Execute:

```
python -m unittest discover -v
```

ou, para rodar só os testes da fifo:

```
python -m unittest discover -v fifo/tests
```

### 2) Benchmarks

Para comparar *na prática* as duas implementações, use o runner:

```
python -m demos.benchmark
```

O benchmark (em `instrumentation.QueueBenchmark`) mede o tempo total de N `enqueue` e N `dequeue` usando `time.perf_counter` e registra via `logging`. Recomenda-se variar `n_operations` para observar escalabilidade.
