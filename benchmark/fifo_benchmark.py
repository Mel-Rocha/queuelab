"""
Script de demonstração para execução de benchmarks de filas.

Este módulo configura o sistema de logging e executa benchmarks para
as implementações específicas de filas, permitindo a
comparação direta de performance entre elas.
"""

from instrumentation.logging_config import configure_logging
from instrumentation.benchmark import QueueBenchmark
from fifo.naive import FIFOQueueNaive
from fifo.optimized import FIFOQueueOptimized


def main():
    """
    Executa os benchmarks para as implementações de fila.

    A função inicializa o sistema de logging, cria instâncias de
    QueueBenchmark para cada implementação e executa os testes.

    :return: None
    """
    configure_logging()

    bench_naive = QueueBenchmark(FIFOQueueNaive, n_operations=50_000)
    bench_naive.run()

    bench_opt = QueueBenchmark(FIFOQueueOptimized, n_operations=50_000)
    bench_opt.run()


if __name__ == "__main__":
    main()
