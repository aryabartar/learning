class Tree(object):

    def __init__(self, value):
        self.value = value
        self.right_node = None
        self.left_node = None

    def insertLeft(self, value):
        current_left_node = self.left_node
        self.left_node = Tree(value)

        if current_left_node is not None:
            self.left_node.left_node = current_left_node

    def insertRight(self, value):
        current_right_node = self.right_node
        self.right_node = Tree(value)

        if current_right_node is not None:
            self.right_node.right_node = current_right_node

    def getRightChild(self):
        return self.right_node

    def getLeftChild(self):
        return self.left_node

    def setRootVal(self, obj):
        self.value = obj

    def getRootVal(self):
        return self.value


root = Tree(1)
root.insertLeft(2)
root.getLeftChild().insertLeft(4)
root.getLeftChild().insertRight(5)
root.insertRight(3)


def preorder_traversal(node):
    print(node.getRootVal())
    if node.getLeftChild() is not None:
        preorder_traversal(node.getLeftChild())
    if node.getRightChild() is not None:
        preorder_traversal(node.getRightChild())


preorder_traversal(root)
