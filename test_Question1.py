import unittest
import Question1

class Stack(unittest.TestCase):
    def test_Emptystack(self):
        arr=Question1.Stack.Emptystack()
        self.assertEqual(arr,False)
    def test_Push(self):
        Question1.Stack.push(6)
        last=len(Question1.stackarr)
        arr=Question1.stackarr[last-1]
        self.assertEqual(arr,6)
    def test_pop(self):
        before=len(Question1.stackarr)
        Question1.Stack.pop()
        after=len(Question1.stackarr)
        self.assertEqual(after,before-1)

    def test_peek(self):
        self.assertEqual((Question1.Stack.peek()),(Question1.stackarr[0]))



if __name__ == '__main__':
    unittest.main()
