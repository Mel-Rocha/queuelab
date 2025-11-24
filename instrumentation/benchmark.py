import logging

from instrumentation.monitor import PerformanceMonitor
from instrumentation.interfaces import QueueProtocol

logger = logging.getLogger(__name__)


class QueueBenchmark:
    def __init__(self, queue_class: type[QueueProtocol], n_operations: int = 100_000):
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
