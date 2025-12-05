# FIFO (First-In, First-Out) 

Esta seção explica, visualmente e de forma organizada, a implementação de **FIFO** presente no repositório (versão *naive* e *optimized*), quando usar cada uma, a complexidade (Big-O) das operações, para fins didáticos.

---

## O que é uma FIFO?

Uma **fila FIFO** (First-In, First-Out) é uma estrutura onde o primeiro elemento a entrar é o primeiro a sair — como uma fila num banco. Operações básicas que usamos aqui:

- `enqueue(item)` — insere um item no final da fila.
- `dequeue()` — remove e retorna o item da frente (head).
- `peek()` — retorna o item da frente sem removê-lo.
- `size()` — retorna o tamanho atual da fila.
- `is_empty()` — indica se a fila está vazia.

---

## Política de Entrada (enqueue)

A operação enqueue segue uma regra simples e estável:

Todo novo item é adicionado ao final da fila.

A FIFO não tenta reorganizar elementos, não cria prioridades e não faz nenhum tipo de análise do valor.
Ela apenas registra a ordem cronológica de chegada.

Isso significa que a entrada é sempre:

- linear;
- previsível;
- sem nenhum critério além da ordem em que os itens chegam;

Do ponto de vista conceitual: o tempo de chegada define a posição do elemento na fila.

## Política de Saída (dequeue e peek)

A operação dequeue remove e devolve o elemento que está há mais tempo na fila.
A operação peek apenas observa esse mesmo elemento, sem removê-lo.

A regra é:

O próximo a sair é sempre o elemento mais antigo da fila.

Essa política garante que:

nenhum item “fura a fila”

a ordem absoluta de chegada é mantida

a estrutura se comporta como uma fila real de atendimento

## Por que FIFO é importante?

A FIFO é a base conceitual para diversos sistemas:

- buffers de I/O;
- pipelines de processamento;
- controle de tarefas em sistemas concorrentes;
- estruturas internas de frameworks de mensageria.

Mesmo sendo simples, ela define o padrão mental sobre o qual outras filas mais complexas (como Priority Queue) se diferenciam.

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