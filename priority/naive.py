from bisect import bisect_left

from domain.exceptions import QueueEmptyError
from priority.base import BasePriorityQueue


class NaivePriorityQueue(BasePriorityQueue):
    """
    Implementação ingênua de uma fila de prioridade usando
    uma lista sempre ordenada.

    Estratégia:
    - A lista interna permanece ordenada por (priority, counter)
    - Menor número de prioridade representa maior urgência
    - Empates são resolvidos de forma estável pelo contador

    Complexidade:
    - enqueue: O(n)
    - peek: O(1)
    - dequeue: O(1) lógico / O(n) físico
    """

    def __init__(self):
        super().__init__()
        self._items = []

    def enqueue(self, priority, value):
        item = self._build_item(priority, value)
        index = bisect_left(self._items, item)
        self._items.insert(index, item)

    def dequeue(self):
        if not self._items:
            raise QueueEmptyError("Priority queue is empty")
        _, _, value = self._items.pop(0)
        return value

    def peek(self):
        if not self._items:
            raise QueueEmptyError("Priority queue is empty")
        return self._items[0][2]

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self.size() == 0
