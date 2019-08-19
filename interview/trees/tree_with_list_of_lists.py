class Tree(object):
    def __init__(self, value):
        self.array = [value, None, None]

    def __str__(self):
        return str(self.array[0])

    def insert_left(self, node):
        array = self.array
        array[1] = node

    def insert_right(self, node):
        array = self.array
        array[2] = node

    def get_left_node(self):
        return self.array[1]

    def get_right_node(self):
        return self.array[2]


root = Tree('1')
left = Tree('2')
right = Tree('3')

root.insert_left(left)
left.insert_right(right)

print(root.get_left_node().get_left_node())
