import unittest

from priority.optimized import OptimizedPriorityQueue
from domain.exceptions import QueueEmptyError


class TestOptimizedPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = OptimizedPriorityQueue()

    def test_queue_starts_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_enqueue_adds_item(self):
        self.queue.enqueue(1, "task A")
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_respects_priority(self):
        self.queue.enqueue(2, "task B")
        self.queue.enqueue(1, "task A")
        self.queue.enqueue(3, "task C")

        self.assertEqual(self.queue.dequeue(), "task A")
        self.assertEqual(self.queue.dequeue(), "task B")
        self.assertEqual(self.queue.dequeue(), "task C")

    def test_stable_order_with_same_priority(self):
        self.queue.enqueue(1, "task A")
        self.queue.enqueue(1, "task B")
        self.queue.enqueue(1, "task C")

        self.assertEqual(self.queue.dequeue(), "task A")
        self.assertEqual(self.queue.dequeue(), "task B")
        self.assertEqual(self.queue.dequeue(), "task C")

    def test_peek_does_not_remove_item(self):
        self.queue.enqueue(1, "task A")

        value = self.queue.peek()

        self.assertEqual(value, "task A")
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_removes_item(self):
        self.queue.enqueue(1, "task A")
        self.queue.dequeue()

        self.assertTrue(self.queue.is_empty())

    def test_peek_empty_queue_raises_error(self):
        with self.assertRaises(QueueEmptyError):
            self.queue.peek()

    def test_dequeue_empty_queue_raises_error(self):
        with self.assertRaises(QueueEmptyError):
            self.queue.dequeue()
