"""
Módulo responsável por executar benchmarks em implementações de filas.

Este módulo fornece a classe `QueueBenchmark`, que permite medir o tempo
de operações de enqueue e dequeue em qualquer implementação que siga o
`QueueProtocol`. A ideia é oferecer um instrumento simples de comparação
de performance entre diferentes estruturas de fila.
"""

import logging

from domain.interfaces import QueueProtocol
from instrumentation.monitor import PerformanceMonitor

logger = logging.getLogger(__name__)


class QueueBenchmark:
    """
    Executa medições de performance para implementações de filas.

    A classe recebe a classe da fila a ser instanciada e testa o tempo de
    execução de `enqueue` e `dequeue` para um número configurável de
    operações.
    """
    def __init__(self, queue_class: type[QueueProtocol], n_operations: int = 100_000):
        """
       Inicializa o benchmark.

       :param queue_class: Classe da fila a ser testada. Deve implementar QueueProtocol.
       :param n_operations: Número de operações de enqueue/dequeue a serem medidas.
       """
        self.queue_class = queue_class
        self.n_operations = n_operations
        self.monitor = PerformanceMonitor()

    def run(self):
        queue = self.queue_class()
        logger.info("Iniciando benchmark para %s", self.queue_class.__name__)

        enqueue_result = self.monitor.measure(
            lambda: [queue.enqueue(i) for i in range(self.n_operations)]
        )
        logger.info(
            "Tempo de enqueue (%s ops): %.6f segundos",
            self.n_operations,
            enqueue_result["time"],
        )

        dequeue_result = self.monitor.measure(
            lambda: [queue.dequeue() for _ in range(self.n_operations)]
        )
        logger.info(
            "Tempo de dequeue (%s ops): %.6f segundos",
            self.n_operations,
            dequeue_result["time"],
        )

        return {
            "enqueue_time": enqueue_result["time"],
            "dequeue_time": dequeue_result["time"],
        }
