stackarr=[1,4,7,8,9]
class Stack:
    @staticmethod
    def Emptystack():
        return stackarr == []

    @staticmethod
    def push(stack_item):
        stackarr.append(stack_item)

    @staticmethod
    def pop():
        last = len(stackarr)
        stackarr.pop(last-1)

    @staticmethod
    def peek():
        return stackarr[0]

array=Stack()
array.Emptystack()
array.push(7)
array.pop()
array.peek()



