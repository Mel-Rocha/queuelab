from abc import ABC

from domain.base_queue import BaseQueue
from priority.utils import StableCounter


class BasePriorityQueue(BaseQueue, ABC):
    """
    Classe base para filas de prioridade.

    Define o contrato específico:
    - enqueue exige prioridade
    - desempate é estável
    - regras de prioridade são centralizadas
    """

    def __init__(self):
        super().__init__()
        self._counter = StableCounter()

    def _build_item(self, priority, value):
        order = self._counter.next()
        return priority, order, value