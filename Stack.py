class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        x = self.stack[-1]
        del self.stack[-1]
        return x

    def length(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def printStack(self):
        print(list(self.stack))

    def isEmpty(self):
        return self.stack ==[]

def main():
    stack = Stack()

    for i in range(0,10):
        stack.push(i)

    print(stack.isEmpty())
    print(stack.length())
    print(stack.pop())

    stack.printStack()

if __name__=="__main__":
    main()