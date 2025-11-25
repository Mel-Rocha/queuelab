"""
Definições de protocolos para estruturas de filas.

Este módulo expõe `QueueProtocol`, um contrato estrutural usado
para tipagem estática. As implementações concretas de fila devem
fornecer os métodos básicos definidos.
"""

from typing import Protocol, Any

class QueueProtocol(Protocol):
    def enqueue(self, item: Any) -> None: ...
    def dequeue(self) -> Any: ...
    def peek(self) -> Any: ...
    def size(self) -> int: ...
