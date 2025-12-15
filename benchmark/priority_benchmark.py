from benchmark.base_benchmarks import QueueBenchmark
from instrumentation.logging_config import configure_logging
from priority.naive import NaivePriorityQueue
from priority.optimized import OptimizedPriorityQueue


def priority_enqueue(queue, i):
    # Variação intencional de prioridade para evitar entradas quase ordenadas
    # e garantir medições de desempenho mais representativas do heap.
    queue.enqueue(i % 10, f"task-{i}")


def main():
    """
    Executa os benchmarks para as implementações de fila.

    A função inicializa o sistema de logging, cria instâncias de
    QueueBenchmark para cada implementação e executa os testes.

    :return: None
    """
    configure_logging()

    bench_naive = QueueBenchmark(NaivePriorityQueue, priority_enqueue, n_operations=50_000)
    bench_naive.run()

    bench_opt = QueueBenchmark(OptimizedPriorityQueue, priority_enqueue, n_operations=50_000)
    bench_opt.run()


if __name__ == "__main__":
    main()
