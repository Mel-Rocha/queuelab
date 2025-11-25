from demos.base_demos import run_queue_demo
from fifo.naive import FIFOQueueNaive
from fifo.optimized import FIFOQueueOptimized

if __name__ == "__main__":
    run_queue_demo(FIFOQueueNaive())
    run_queue_demo(FIFOQueueOptimized())
