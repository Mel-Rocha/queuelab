from fifo.exceptions import QueueEmptyError


class FIFOQueueNaive:
    """
    Fila simples implementada com lista.

    Enqueue: O(1)
    Dequeue: O(n) due to list shifting
    """

    def __init__(self):
        # _data: lista interna que armazena os elementos da fila.
        # usamos '_' para sinalizar que é atributo "privado" (convenção).
        self._data = []

    def enqueue(self, item):
        """Adicionar item ao final da fila."""
        # append é amortizado O(1) — eficiente para inserir no fim.
        self._data.append(item)

    def dequeue(self):
        """
        Remover e retornar o elemento que chegou primeiro.
        Lança QueueEmptyError se a fila estiver vazia.
        """
        if self.is_empty():
            # levantamos uma exceção específica para deixar a API clara
            raise QueueEmptyError("Cannot dequeue from an empty queue.")
        # pop(0) remove o primeiro elemento da lista; custo O(n) porque
        # todos os elementos restantes são deslocados para a esquerda.
        return self._data.pop(0)

    def peek(self):
        """Retornar o próximo elemento sem removê-lo (olhar a cabeça da fila)."""
        if self.is_empty():
            raise QueueEmptyError("Cannot peek an empty queue.")
        return self._data[0]

    def is_empty(self):
        """Retorna True se a fila estiver vazia."""
        return len(self._data) == 0

    def size(self):
        """Retorna o número de elementos na fila."""
        return len(self._data)

    def __repr__(self):
        """Representação útil para debugging (não expõe implementação interna)."""
        return f"{self.__class__.__name__}({self._data})"
