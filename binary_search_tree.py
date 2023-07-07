class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BTS:
    def __init__(self) -> None:
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        
        t = self.root
        while t :
            if t.value > value:
                if t.left is None:
                    t.left = Node(value)
                    return True
                else:
                    t = t.left

            elif t.value < value:
                if t.right is None:
                    t.right = Node(value)
                    return True
                else:
                    t = t.right

            elif t.value == value:
                return False
            

    def contains(self, value):
        if self.root is None:
            return None
        
        t = self.root
        while t :
            if t.value == value:
                return True
            if t.value > value:
                if t.left is None:
                    return False
                else:
                    t = t.left

            elif t.value < value:
                if t.right is None:
                    return False
                else:
                    t = t.right

 

tree = BTS()
tree.insert(9)
tree.insert(0)
tree.insert(67)
tree.insert(4)
tree.insert(-1)
print(tree.contains(4))
print(tree.contains(99))
# tree.print_tree()
# print(tree.root.left.value)
# print(tree.root.right.value)