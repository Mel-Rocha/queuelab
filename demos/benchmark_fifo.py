from instrumentation.logging_config import configure_logging
from instrumentation.benchmark import QueueBenchmark
from fifo.naive import FIFOQueueNaive
from fifo.optimized import FIFOQueueOptimized


def main():
    configure_logging()

    bench_naive = QueueBenchmark(FIFOQueueNaive, n_operations=50_000)
    bench_naive.run()

    bench_opt = QueueBenchmark(FIFOQueueOptimized, n_operations=50_000)
    bench_opt.run()


if __name__ == "__main__":
    main()
