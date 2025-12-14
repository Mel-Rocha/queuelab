from abc import ABC, abstractmethod


class BaseQueue(ABC):
    """Contrato base para estruturas de fila (FIFO, Circular, Priority)."""

    @abstractmethod
    def enqueue(self, *args, **kwargs):
        """Adiciona um elemento à coleção da fila."""
        # Não especificamos 'final'
        pass

    @abstractmethod
    def dequeue(self):
        """Remove e retorna o próximo elemento a ser processado, de acordo com a regra da fila."""
        # Não especificamos 'início'
        pass

    @abstractmethod
    def peek(self):
        """Retorna (sem remover) o próximo elemento a ser processado, de acordo com a regra da fila."""
        pass

    @abstractmethod
    def size(self):
        """Retorna o número de elementos na fila."""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a fila está vazia."""
        pass
