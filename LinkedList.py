class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def addNode(self,data):
        self.size +=1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def getSize(self):
        return self.size

    def printList(self):
        currNode = self.head
        print()
        while currNode:
            print(currNode.data,'->',end='')
            currNode = currNode.next

    def popNode(self):
        if self.head:
            self.head = self.head.next

    def insertAtEnd(self,data):
        currNode = self.head

        while currNode.next:
            currNode = currNode.next

        currNode.next = Node(data)

def main():
    l_list = LinkedList()

    for i in range(1,10):
        l_list.addNode(i)

    print('Size:',l_list.getSize())
    l_list.printList()

    l_list.insertAtEnd(0)
    l_list.printList()

if __name__=="__main__":
    main()
