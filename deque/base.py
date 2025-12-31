from abc import ABC, abstractmethod


class BaseDeque(ABC):
    """
    Contrato base para uma Double-Ended Queue (Deque).

    Um deque permite inserções, remoções e inspeções
    em ambas as extremidades: esquerda e direita.

    Esta classe define apenas o comportamento esperado.
    Detalhes de implementação e complexidade pertencem
    às classes concretas.
    """

    @abstractmethod
    def push_left(self, item):
        """Insere um elemento na extremidade esquerda."""
        pass

    @abstractmethod
    def push_right(self, item):
        """Insere um elemento na extremidade direita."""
        pass

    @abstractmethod
    def pop_left(self):
        """Remove e retorna o elemento da extremidade esquerda."""
        pass

    @abstractmethod
    def pop_right(self):
        """Remove e retorna o elemento da extremidade direita."""
        pass

    @abstractmethod
    def peek_left(self):
        """Retorna o elemento da extremidade esquerda sem removê-lo."""
        pass

    @abstractmethod
    def peek_right(self):
        """Retorna o elemento da extremidade direita sem removê-lo."""
        pass

    @abstractmethod
    def is_empty(self):
        """Retorna True se o deque estiver vazio."""
        pass

    @abstractmethod
    def size(self):
        """Retorna a quantidade de elementos no deque."""
        pass
