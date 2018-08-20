class mQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        x = self.queue[0]
        del self.queue[0]
        return x

    def isEmpty(self):
        return self.queue ==[]

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]

    def length(self):
        return len(self.queue)

    def printQ(self):
        print(list(self.queue))

def main():

    q = mQueue()

    for i in range(0, 10):
        q.enqueue(i)

    q.printQ()

    print(q.isEmpty())
    print(q.length())
    print(q.peek())
    print(q.dequeue())
    print(q.peek())

if __name__=='__main__':
    main()
