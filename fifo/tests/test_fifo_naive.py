import unittest

from fifo.naive import FIFOQueueNaive
from fifo.exceptions import QueueEmptyError


class TestFIFOQueueNaive(unittest.TestCase):

    def test_enqueue_and_size(self):
        q = FIFOQueueNaive()
        q.enqueue("A")
        q.enqueue("B")
        self.assertEqual(q.size(), 2)

    def test_dequeue_returns_in_fifo_order(self):
        q = FIFOQueueNaive()
        q.enqueue("A")
        q.enqueue("B")
        self.assertEqual(q.dequeue(), "A")
        self.assertEqual(q.dequeue(), "B")

    def test_dequeue_empty_raises(self):
        q = FIFOQueueNaive()
        with self.assertRaises(QueueEmptyError):
            q.dequeue()

    def test_peek(self):
        q = FIFOQueueNaive()
        q.enqueue("X")
        self.assertEqual(q.peek(), "X")
        self.assertEqual(q.size(), 1)  # garante que não remove

    def test_str_representation(self):
        q = FIFOQueueNaive()
        q.enqueue("A")
        q.enqueue("B")
        self.assertIn("A", str(q))
        self.assertIn("B", str(q))
