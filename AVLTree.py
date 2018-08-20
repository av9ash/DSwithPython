class Node(object):
    def __init__(self,data):
        self.rightChild = None
        self.leftChild = None
        self.data = data
        self.height = 0

class AVL(object):

    def __init__(self):
        self.root = None;

    def getHeight(self,node):
        if not node:
            return -1
        return node.height

    def insert(self,data):
        self.root = self.__insertNode__(data,self.root)

    def traverse(self):
        if self.root:
            self.__traverseInOrder__(self.root)

    def removeNode(self, data):
        if not self.root:
            return
        self.__deleteNode__(self.root, data)

    def __getPredecessor__(self,node):
        while node.rightChild :
            node = node.rightChild
        return node

    # If this returns > 1 left heavy tree or if <-1 right heavy tree
    def __getBalance__(self,node):
        if not node:
            return 0
        return self.getHeight(node.leftChild) - self.getHeight(node.rightChild)

    def __rotateRight__(self,node):

        print("Performing right rotation.")
        tmpL = node.leftChild
        tmpRchild = tmpL.rightChild

        tmpL.rightChild = node
        node.leftChild = tmpRchild

        node.height = max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1
        tmpL.height = max(self.getHeight(tmpL.leftChild),self.getHeight(tmpL.rightChild))+1

        return tmpL;

    def __rotateLeft__(self,node):
        print("Performing left rotation.")
        tmpR = node.rightChild
        tmpLchild = tmpR.leftChild

        tmpR.leftChild = node
        node.rightChild = tmpLchild

        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        tmpR.height = max(self.getHeight(tmpR.leftChild),self.getHeight(tmpR.rightChild))+1

        return tmpR

    def __settleInViolation__(self,data,node):
        balance = self.__getBalance__(node)

        # /
        if balance > 1 and data < node.leftChild.data:
            return self.__rotateRight__(node)
        # <
        if balance > 1 and data > node.leftChild.data:
            node.leftChild = self.__rotateLeft__(node.leftChild)
            return self.__rotateRight__(node)
        # \
        if balance < -1 and data > node.rightChild.data:
            return self.__rotateLeft__(node)
        # >
        if balance < -1 and data < node.rightChild.data:
            node.rightChild = self.__rotateRight__(node.rightChild)
            return self.__rotateLeft__(node)

        return node;

    def __settleOutViolation__(self, node):
        balance = self.__getBalance__(node)

        # /
        if balance > 1 and self.__getBalance__(node.leftChild)>=0:
            return self.__rotateRight__(node)
        # <
        if balance > 1 and self.__getBalance__(node.leftChild)<0:
            node.leftChild = self.__rotateLeft__(node.leftChild)
            return self.__rotateRight__(node)
        # \
        if balance < -1 and self.__getBalance__(node.rightChild)<=0:
            return self.__rotateLeft__(node)
        # >
        if balance < -1 and self.__getBalance__(node.rightChild) > 0:
            node.rightChild = self.__rotateRight__(node.rightChild)
            return self.__rotateLeft__(node)

        return node;

    # Recursion
    def __traverseInOrder__(self,node):
        if node.leftChild:
            self.__traverseInOrder__(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.__traverseInOrder__(node.rightChild)

    def __insertNode__(self,data,node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.__insertNode__(data,node.leftChild)
        else:
            node.rightChild = self.__insertNode__(data,node.rightChild)

        node.height = max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1
        return self.__settleInViolation__(data,node)

    def __deleteNode__(self,node,data):

        if data < node.data:
            node.leftChild = self.__deleteNode__(node.leftChild,data)
        elif data > node.data:
            node.rightChild = self.__deleteNode__(node.rightChild,data)
        else:
            if not node.rightChild and not node.leftChild:
                del node
                return None

            elif not node.leftChild:
                tmp = node.rightChild
                del node
                return tmp
            elif not node.rightChild:
                tmp = node.leftChild
                del node
                return tmp

            elif node.rightChild and node.leftChild:
                tmp = self.__getPredecessor__(node.leftChild)
                node.data = tmp.data
                node.leftChild = self.__deleteNode__(node.leftChild,tmp.data)

        if not node:
            return node

        node.height = max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))+1

        return self.__settleOutViolation__(node)

def main():
    avl = AVL()
    avl.insert(60)
    avl.insert(50)
    avl.insert(55)
    avl.insert(52)
    avl.traverse()
    avl.removeNode(55)
    avl.traverse()

if __name__=="__main__":
    main()