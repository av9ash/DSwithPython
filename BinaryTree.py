class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def addNode(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.addnewnode(self.root, data)

    def printTreeAscending(self):
        if not self.root:
            print("Empty Tree")
            return
        self.traverseTree(self.root)

    def getMin(self):
        root = self.root
        while root.leftChild!=None:
            root = root.leftChild
        return root.data

    def getMax(self):
        root = self.root
        while root.rightChild!=None:
            root = root.rightChild
        return root.data

    def removeNode(self,data):
        if not self.root:
            return
        self.deleteNode(self.root,data)

    def getPredecessor(self,node):
        while node.rightChild :
            node = node.rightChild
        return node

    #RECURSIONS
    def traverseTree(self,root):
        if not root:
            return
        self.traverseTree(root.leftChild)
        print(root.data)
        self.traverseTree(root.rightChild)

    def addnewnode(self,root,data):
        if data < root.data:
            if root.leftChild == None:
                root.leftChild = Node(data)
            else:
                self.addnewnode(root.leftChild, data)
        elif data > root.data:
            if root.rightChild == None:
                root.rightChild = Node(data)
            else:
                self.addnewnode(root.rightChild, data)

    def deleteNode(self,node,data):

        if data < node.data:
            node.leftChild = self.deleteNode(node.leftChild,data)
        elif data > node.data:
            node.rightChild = self.deleteNode(node.rightChild,data)
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
                tmp = self.getPredecessor(node.leftChild)
                node.data = tmp.data
                node.leftChild = self.deleteNode(node.leftChild,tmp.data)

        return node

def main():
    btree = BinaryTree()

    Nodes = [32,10,55,1,19,16,23,17,18,79]
    for node in Nodes:
        btree.addNode(node)

    btree.removeNode(32)
    print("---tree---")
    btree.printTreeAscending()

    # print(btree.getMax())
    # print(btree.getMin())

if __name__ == '__main__':
    main()
