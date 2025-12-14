from itertools import count


class StableCounter:
    """
    Contador incremental usado para garantir desempate estável
    em filas de prioridade.

    Cada instância representa uma fila independente.

    Complexidade: O(1) por incremento.
    """

    def __init__(self, start: int = 0):
        self._counter = count(start)

    def next(self) -> int:
        return next(self._counter)
