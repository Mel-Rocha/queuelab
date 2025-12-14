import heapq
from typing import Any

from domain.exceptions import QueueEmptyError
from priority.base import BasePriorityQueue


class OptimizedPriorityQueue(BasePriorityQueue):
    """
        Implementação otimizada de uma fila de prioridade usando heap binário
        (min-heap) da biblioteca padrão do Python.

        Estratégia:
        - Os elementos são armazenados em um heap como tuplas no formato:
          (priority, order, value)
        - Menor valor de prioridade representa maior urgência
        - O campo 'order' é um contador monotônico usado para garantir
          desempate estável entre elementos com a mesma prioridade

        Comportamento:
        - O elemento mais prioritário está sempre no topo do heap
        - Operações de inserção e remoção reorganizam o heap automaticamente
        - Apenas o valor armazenado é exposto ao usuário da fila

        Complexidade:
        - enqueue: O(log n)
        - dequeue: O(log n)
        - peek: O(1)
        - size: O(1)
        - espaço: O(n)

        Observações:
        - Esta implementação é indicada para filas grandes ou com alta
          taxa de inserções e remoções
        - A regra de prioridade é garantida pela ordenação natural das tuplas,
          sem necessidade de comparações explícitas via regras de domínio
    """

    def __init__(self):
        super().__init__()
        self._heap: list[tuple[int, int, Any]] = []

    def enqueue(self, priority: int, value: Any) -> None:
        item = self._build_item(priority, value)
        heapq.heappush(self._heap, item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise QueueEmptyError("Priority queue is empty")
        _, _, value = heapq.heappop(self._heap)
        return value

    def peek(self) -> Any:
        if self.is_empty():
            raise QueueEmptyError("Priority queue is empty")
        return self._heap[0][2]

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return self.size() == 0
