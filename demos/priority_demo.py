from demos.base_demos import run_queue_demo
from priority.naive import NaivePriorityQueue
from priority.optimized import OptimizedPriorityQueue


def priority_enqueue(queue):
    queue.enqueue(2, "task B")
    queue.enqueue(1, "task A")
    queue.enqueue(1, "task C")


if __name__ == "__main__":
    run_queue_demo(NaivePriorityQueue(), priority_enqueue)
    run_queue_demo(OptimizedPriorityQueue(), priority_enqueue)
