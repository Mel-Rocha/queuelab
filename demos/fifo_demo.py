from demos.base_demos import run_queue_demo
from fifo.naive import FIFOQueueNaive
from fifo.optimized import FIFOQueueOptimized

def fifo_enqueue(queue):
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")


if __name__ == "__main__":
    run_queue_demo(FIFOQueueNaive(), fifo_enqueue)
    run_queue_demo(FIFOQueueOptimized(), fifo_enqueue)
