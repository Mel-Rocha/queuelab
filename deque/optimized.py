from domain.exceptions import QueueEmptyError
from deque.base import BaseDeque


class OptimizedDeque(BaseDeque):
    """
    Implementação otimizada de um Deque usando buffer circular.

    Características:
    - Todas as operações são O(1)
    - Nenhum deslocamento de elementos
    - Uso explícito de ponteiros (head e tail)
    """

    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")

        self._capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    # =========================
    # Métodos internos genéricos
    # =========================

    def _push(self, item, *, left: bool):
        if self._size == self._capacity:
            raise OverflowError("Deque is full")

        if left:
            self._head = (self._head - 1) % self._capacity
            self._buffer[self._head] = item
        else:
            self._buffer[self._tail] = item
            self._tail = (self._tail + 1) % self._capacity

        self._size += 1

    def _pop(self, *, left: bool):
        if self._size == 0:
            raise QueueEmptyError("Deque is empty")

        if left:
            value = self._buffer[self._head]
            self._buffer[self._head] = None
            self._head = (self._head + 1) % self._capacity
        else:
            self._tail = (self._tail - 1) % self._capacity
            value = self._buffer[self._tail]
            self._buffer[self._tail] = None

        self._size -= 1
        return value

    def _peek(self, *, left: bool):
        if self._size == 0:
            raise QueueEmptyError("Deque is empty")

        if left:
            return self._buffer[self._head]
        else:
            index = (self._tail - 1) % self._capacity
            return self._buffer[index]

    # =========================
    # Interface pública (contrato)
    # =========================

    def push_left(self, item):
        self._push(item, left=True)

    def push_right(self, item):
        self._push(item, left=False)

    def pop_left(self):
        return self._pop(left=True)

    def pop_right(self):
        return self._pop(left=False)

    def peek_left(self):
        return self._peek(left=True)

    def peek_right(self):
        return self._peek(left=False)

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size