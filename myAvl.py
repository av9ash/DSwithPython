class Node(object):
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.rightChild = None
        self.leftChild = None

class avlTree(object):

    def __init__(self):
        self.root = None

    def getHeight(self,node):

        if not node:
            return -1
        return node.height

    def addNode(self,data):
        self.root = self.__addNewNode__(self.root, data)

    def traverseInOrder(self):
        if self.root:
            self.__traverseInOrder__(self.root)

    #  >1 left heavy situation, if <-1 right heavy situation
    def __getBalance__(self,node):

        if not node:
            return 0

        return self.getHeight(node.leftChild) - self.getHeight(node.rightChild)

    def __addNewNode__(self,node,data):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.__addNewNode__(node.leftChild,data)
        else:
            node.rightChild = self.__addNewNode__(node.rightChild,data)

        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        return self.__settleInViolations__(node,data)

    def __settleInViolations__(self,node,data):
        balance = self.__getBalance__(node)
        # /
        if balance >1 and self.__getBalance__(node.leftChild)>=0:
            return self.__rotateRight__(node)
        # <
        if balance >1 and self.__getBalance__(node.leftChild)<0:
            node.leftChild = self.__rotateLeft__(node.leftChild)
            return self.__rotateRight__(node)
        # \
        if balance < -1 and self.__getBalance__(node.rightChild) <= 0:
            return self.__rotateLeft__(node)
        # >
        if balance < -1 and self.__getBalance__(node.rightChild) > 0:
            node.rightChild = self.__rotateRight__(node.rightChild)
            return self.__rotateLeft__(node)

        return node

    # resolve right heavy
    def __rotateLeft__(self, node):
        newRoot = node.rightChild
        tmpLchild = newRoot.leftChild

        newRoot.leftChild = node
        node.rightChild = tmpLchild

        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        newRoot.height = max(self.getHeight(newRoot.leftChild), self.getHeight(newRoot.rightChild)) + 1

        return newRoot

    # resolve left heavy
    def __rotateRight__(self,node):
        newRoot = node.leftChild
        tmpRight = newRoot.rightChild

        newRoot.rightChild = node
        node.leftChild = tmpRight

        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        newRoot.height = max(self.getHeight(newRoot.leftChild), self.getHeight(newRoot.rightChild)) + 1

        return newRoot

    def __traverseInOrder__(self,root):

        if root.leftChild:
            self.__traverseInOrder__(root.leftChild)

        print(root.data)

        if root.rightChild:
            self.__traverseInOrder__(root.rightChild)

def main():
    atree = avlTree()

    for i in range(0,10):
        atree.addNode(i)

    atree.addNode(27)
    atree.addNode(25)
    atree.addNode(30)
    atree.addNode(26)
    atree.addNode(28)
    atree.addNode(29)

    atree.traverseInOrder()


if __name__ == "__main__":
    main()
