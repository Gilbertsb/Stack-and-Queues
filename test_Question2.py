import unittest
import Question2

class Queue(unittest.TestCase):
    def test_Emptyqueue(self):
        arr=Question2.Queue.Emptyqueue()
        self.assertEqual(arr,False)
    def test_Enqueue(self):
        Question2.Queue.enqueue(6)
        last=len(Question2.queuearr)
        queue=Question2.queuearr[last-1]
        self.assertEqual(queue,6)
    def test_dequeue(self):
        before=len(Question2.queuearr)
        Question2.Queue.dequeue()
        after=len(Question2.queuearr)
        self.assertEqual(after,before-1)

    def test_peek(self):
        self.assertEqual((Question2.Queue.peek()),(Question2.queuearr[0]))


if __name__ == '__main__':
    unittest.main()
