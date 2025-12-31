from deque.base import BaseDeque
from domain.exceptions import QueueEmptyError


class NaiveDeque(BaseDeque):
    """
    Implementação naive de um Deque usando lista Python.

    Estratégia:
    - Extremidade esquerda -> índice 0
    - Extremidade direita  -> último índice da lista

    Complexidade:
    - push_right: O(1) amortizado
    - pop_right:  O(1)
    - push_left:  O(n)
    - pop_left:   O(n)
    - peek_*:     O(1)
    """

    def __init__(self):
        self._data = []

    # -------------------------
    # Métodos internos
    # -------------------------

    def _push(self, item, left: bool):
        if left:
            self._data.insert(0, item)  # O(n)
        else:
            self._data.append(item)     # O(1) amortizado

    def _pop(self, left: bool):
        if self.is_empty():
            raise QueueEmptyError("Deque is empty")

        if left:
            return self._data.pop(0)    # O(n)
        return self._data.pop()          # O(1)

    def _peek(self, left: bool):
        if self.is_empty():
            raise QueueEmptyError("Deque is empty")

        if left:
            return self._data[0]
        return self._data[-1]

    # -------------------------
    # Interface pública
    # -------------------------

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
        return len(self._data) == 0

    def size(self):
        return len(self._data)
