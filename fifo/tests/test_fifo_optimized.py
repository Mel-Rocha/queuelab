import unittest

from fifo.optimized import FIFOQueueOptimized
from fifo.exceptions import QueueEmptyError


class TestFIFOQueueOptimized(unittest.TestCase):

    def test_enqueue_and_size(self):
        q = FIFOQueueOptimized()
        q.enqueue("A")
        q.enqueue("B")
        self.assertEqual(q.size(), 2)

    def test_dequeue_returns_in_fifo_order(self):
        q = FIFOQueueOptimized()
        q.enqueue("A")
        q.enqueue("B")
        self.assertEqual(q.dequeue(), "A")
        self.assertEqual(q.dequeue(), "B")

    def test_dequeue_empty_raises(self):
        q = FIFOQueueOptimized()
        with self.assertRaises(QueueEmptyError):
            q.dequeue()

    def test_peek(self):
        q = FIFOQueueOptimized()
        q.enqueue("X")
        self.assertEqual(q.peek(), "X")
        self.assertEqual(q.size(), 1)

    def test_str_representation(self):
        q = FIFOQueueOptimized()
        q.enqueue("A")
        q.enqueue("B")
        self.assertIn("A", str(q))
        self.assertIn("B", str(q))
