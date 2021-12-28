
# top is root
# root's(link of root) of tree contain sub-trees
# parent's parent are grandparent
# root is parent
# node from parent are child of same level and same parent are siblings
# node with same grandparents are cousins
#  node with no child are called leaf
# in BST left side is smaller than root or node and right side is bigger than root or node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None  # head of the node

    def Insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def Contain(self,value):
        if self.root is None:
            return None
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_node = BinarySearchTree()

print(my_node.Contain(7))

my_node.Insert(5)
my_node.Insert(2)
my_node.Insert(7)

print(my_node.root.value)
print(my_node.root.right.value)
print(my_node.root.left.value)

print(my_node.Contain(7))
print(my_node.Contain(17))


