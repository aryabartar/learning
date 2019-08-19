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


r = Tree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
