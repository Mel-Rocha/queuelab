from collections import deque

from domain.base_queue import BaseQueue
from domain.exceptions import QueueEmptyError


class FIFOQueueOptimized(BaseQueue):
    """
    Implementação otimizada de uma fila FIFO usando collections.deque.

    A deque oferece O(1) em append e popleft, tornando esta fila
    muito mais eficiente do que uma implementação baseada em list.

    Métodos:
        enqueue(item): adiciona ao final.
        dequeue(): remove e retorna o primeiro elemento.
        peek(): retorna o primeiro sem remover.
        size(): quantidade de itens.
        is_empty(): True se vazia.
    """

    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if not self._queue:
            raise QueueEmptyError("Cannot dequeue from an empty queue.")
        return self._queue.popleft()

    def peek(self):
        if not self._queue:
            raise QueueEmptyError("Cannot peek from an empty queue.")
        return self._queue[0]

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0

    def __repr__(self):
        return f"FIFOQueueOptimized({list(self._queue)})"
