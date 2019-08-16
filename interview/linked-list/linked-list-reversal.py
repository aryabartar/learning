class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse_linedlist(head):
    node = head
    prev_node = None

    while node is not None:
        next_node = node.nextnode
        node.nextnode = prev_node

        prev_node = node
        node = next_node



# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

# print(d.nextnode.value)


print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse_linedlist(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
print(a.nextnode)