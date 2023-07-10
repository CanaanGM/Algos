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


    def __r_contains(self, node, value):
        if node is None:
            return False
        
        if value == node.value:
            return True
        
        if value < node.value:
            return self.__r_contains(node.left, value)
        
        if value > node.value:
            return self.__r_contains(node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left =  self.__r_insert(node.left, value)
        
        if value > node.value:
            node.right =  self.__r_insert(node.right, value)
        
        return node

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)

        self.__r_insert(self.root, value)

 
    def __delete_node(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left =  self.__delete_node(node.left, value)
        
        if value > node.value:
            node.right =  self.__delete_node(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            
            if node.right is None:
                node = node.left
            
            elif node.left is None:
                node = node.right

            else:
                min_val = self.min_value(node.right)
                node.value = min_val
                node.right = self.__delete_node(node.right, min_val)
            

        return node
    
    def min_value(self, node):
        while node.left:
            node = node.left
        return node.value
 
    def r_delete(self, value):
        if not self.root:
            return None
        
        return self.__delete_node(self.root, value)
 
    def print_tree(self):
        """
        prints all tree nodes

        TODO: find a way to print the tree to the terminal elegantly, there's a package that add colors and stuff
        """
        # go left
        # print root
        # go right
        visited: list = []

        def traverse(node: Node) -> None:
            if node.left:
                print(node.left.value, "<-- left side node")
                traverse(node.left)
            visited.append(node)
            print(node.value, "<-- root node")
            if node.right:
                print(node.right.value, "<-- right side node")
                traverse(node.right)
        traverse(self.root)
        return visited
 

tree = BTS()
tree.r_insert(9)
tree.r_insert(0)
tree.r_insert(67)
tree.r_insert(4)
tree.r_insert(-1)
tree.print_tree()
tree.r_delete(4)

tree.print_tree()
# print(tree.min_value(tree.root.right))
print(tree.r_contains(99))
# print(tree.root.left.value)
# print(tree.root.right.value)