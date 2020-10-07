queuearr= [4, 5, 4, 5]
class Queue:
    @staticmethod
    def Emptyqueue():
        return queuearr == []

    @staticmethod
    def enqueue(q_item):
        queuearr.append(q_item)

    @staticmethod
    def dequeue():
        last=len(queuearr)
        queuearr.pop(last-1)

    @staticmethod
    def peek():
        return queuearr[0]


DF=Queue()
DF.Emptyqueue()
DF.enqueue(78)
DF.dequeue()
DF.peek()



