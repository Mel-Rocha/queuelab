# Priority Queue (Fila de Prioridade)

Esta seção explica, de forma visual e organizada, a implementação de **Priority Queue** presente no repositório, sua política de ordenação, casos de uso, complexidade (Big-O) das operações e exemplos práticos, com foco didático.

---

## O que é uma Priority Queue?

Em uma Priority Queue, cada item entra na fila com um valor que representa
o quanto ele é importante naquele contexto.

Esse valor pode representar:
- urgência;
- criticidade;
- peso;
- nível de serviço;
- preferência.

A estrutura existe exatamente para responder à pergunta:

"Qual é o item mais importante agora?"

---

### Exemplo do mundo real

Imagine uma fila em um banco ou supermercado:

- pessoas **preferenciais** (idosos, gestantes, PCDs);
- pessoas **não preferênciais**.

Mesmo que uma pessoa não preferêncial chegue antes,
uma pessoa preferencial **será atendida primeiro**.

Nesse cenário:

- o atendimento não segue ordem de chegada;
- segue um **critério de prioridade social**;
- a fila existe para garantir justiça segundo regras de importância,
  não segundo o tempo.

---

### Operações básicas usadas aqui:

- `enqueue(item, priority)` — insere um item com uma prioridade associada.
- `dequeue()` — remove e retorna o item de maior prioridade.
- `peek()` — retorna o próximo item a sair, sem removê-lo.
- `size()` — retorna o tamanho atual da fila.
- `is_empty()` — indica se a fila está vazia.

Diferente da FIFO, **quem sai primeiro não é quem chegou primeiro**, mas quem possui **maior prioridade** segundo a política definida.

---

## Política de Entrada (enqueue)

Na Priority Queue, cada elemento entra **acompanhado de um valor de prioridade**.

Nesta implementação, seguimos a política:

> **Quanto menor o valor da prioridade, maior a prioridade do elemento.**

Isso ocorre porque utilizamos internamente um **min-heap**, fornecido pelo módulo `heapq` do Python.

Ao enfileirar, o que realmente é inserido no heap é uma estrutura do tipo:

(priority, item)

yaml
Copiar código

Ou seja, o heap organiza os elementos **com base na prioridade**, não no valor do item em si.

Características dessa política:

- a ordenação acontece automaticamente no momento do `enqueue`;
- não existe conceito de “final da fila”;
- o heap garante apenas a ordem mínima necessária (raiz correta), não uma lista totalmente ordenada.

---

## Política de Saída (dequeue e peek)

A operação `dequeue` remove e retorna **o elemento com maior prioridade**, ou seja:

- o elemento cujo `priority` é o **menor valor numérico**.

A operação `peek` apenas observa esse elemento, sem removê-lo.

Regra fundamental:

> O próximo a sair é sempre o elemento com a **menor prioridade numérica** no heap.

Se dois elementos tiverem a mesma prioridade, o comportamento depende da ordem interna do heap e da comparação dos valores armazenados — **não há garantia FIFO nesses casos**.

---

## Por que Priority Queue é importante?

Filas de prioridade são essenciais quando **nem todas as tarefas têm o mesmo peso ou urgência**.

Casos comuns de uso:

- escalonadores de tarefas (jobs mais urgentes primeiro);
- algoritmos clássicos (Dijkstra, A*, Prim);
- sistemas de eventos e simulações;
- filas de processamento com SLA;
- sistemas operacionais e motores de jogos.

Ela representa um salto conceitual em relação à FIFO:

> não é mais “quem chegou primeiro”, e sim “quem é mais importante agora”.

---

## Visualização (como pensar mentalmente)

Imagine a seguinte fila de prioridade, onde o número representa a prioridade:

(priority, item)

arduino
Copiar código
    (1, "B")
   /         \
(3, "C") (5, "A")

yaml
Copiar código

- `"B"` tem prioridade 1 → sai primeiro  
- `"C"` tem prioridade 3  
- `"A"` tem prioridade 5 → sai por último  

Mesmo que `"A"` tenha chegado antes, `"B"` será removido primeiro.

---

## Implementação no repositório

### `PriorityQueue` (`priority/optimized.py`)

- Implementação baseada em **heap binário mínimo (min-heap)**.
- Utiliza o módulo padrão `heapq` do Python.
- Estrutura interna: lista que representa um heap.

### Complexidade das operações

- `enqueue`: `heapq.heappush` — **O(log n)**
- `dequeue`: `heapq.heappop` — **O(log n)**
- `peek`: acesso ao índice `0` — **O(1)**
- `size`: **O(1)**
- `is_empty`: **O(1)**

A complexidade maior em relação à FIFO é o custo necessário para manter a propriedade do heap.

---

## Big-O (resumo)

| Operação  | Priority Queue (heapq) |
|----------|------------------------|
| enqueue  | O(log n)               |
| dequeue  | O(log n)               |
| peek     | O(1)                   |
| size     | O(1)                   |
| is_empty | O(1)                   |

> Nota: o heap **não mantém os elementos totalmente ordenados**, apenas garante que o menor elemento esteja sempre na raiz. Isso é o que permite eficiência em inserções e remoções.

---

## Quando usar Priority Queue?

**Use Priority Queue** quando:

- a ordem de processamento importa mais que a ordem de chegada;
- tarefas possuem pesos, urgências ou níveis;
- você precisa sempre do “melhor candidato” disponível.

**Não use** se:

- a ordem cronológica deve ser preservada;
- todas as tarefas têm o mesmo peso;
- simplicidade extrema é prioridade (FIFO é suficiente).

---

## Exemplos de uso (Python)

```python
from priority.optimized import OptimizedPriorityQueue

pq = OptimizedPriorityQueue()

pq.enqueue("A", priority=5)
pq.enqueue("B", priority=1)
pq.enqueue("C", priority=3)

print(pq.peek())     # "B"
print(pq.dequeue())  # "B"
print(pq.dequeue())  # "C"
```

Mesmo que "A" tenha sido inserido primeiro, ele sai por último devido à prioridade.