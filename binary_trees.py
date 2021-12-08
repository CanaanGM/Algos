from node import Node
from Queueueueueueue import Queue


class BinarySearchTree:
    def __repr__(self) -> str:
        return "I'm but a humble search tree of the binary kind"

    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, value):
        """
        Adds a new value to the tree
        """
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current_root = self.root
            while(True):
                if value == current_root.val:
                    return None
                if value < current_root.val:
                    if not current_root.previous:
                        current_root.previous = new_node
                        return True
                    else:
                        current_root = current_root.previous

                elif value > current_root.val:
                    if not current_root.next:
                        current_root.next = new_node
                        return True
                    else:
                        current_root = current_root.next

    def find(self, value):
        """
        looks thru thr tree
        returns the value if found or None if not
        """
        if self.root == None:
            return None

        current_root = self.root
        found = False

        while not found and current_root:
            if value < current_root.val:
                current_root = current_root.previous
            elif value > current_root.val:
                current_root = current_root.next
            else:
                found = True
        return current_root

    def breadth_first_search(self):
        """
        goes thru the tree horizantally 
        """
        queue: list = []  # my custom Q didn't work, debug later (っ °Д °;)っ
        visited: list = []
        current_node: Node = self.root
        queue.append(current_node)

        while len(queue):
            current_node = queue.pop()
            visited.append(current_node)
            if current_node.previous:
                queue.append(current_node.previous)
            if current_node.next:
                queue.append(current_node.next)
        return visited

    # ! hits the recursion depth, same code work in js tho
    #!! no, i was stupid and was using the global (local to the scope of this funciton) vairable ＞︿＜
    def depth_first_search_PREorder(self):
        """
        goes thru the leafs before the sibling nodes
         (Canaan)
        /        \
     (Alphrad)   (Dante)
                    \  
                   (Vergil)
        returns --> [Canaan, Dante, Vergil, Alphrad]
        """
        visited: list = []

        def traverse(node: Node) -> None:
            """ helper for bfs"""
            visited.append(node)
            if node.next:
                traverse(node.next)
            if node.previous:
                traverse(node.previous)
        traverse(self.root)
        return visited

    def depth_first_search_POSTorder(self):
        """
        goes thru the branch of the nodes first before coming back to it 
         (Canaan)
        /        \
     (Alphrad)   (Dante)
                    \  
                   (Vergil)

        returns --> [ Vergil, Dante, Alphrad, Canaan]
        """
        visited: list = []

        def traverse(node: Node) -> None:
            if node.next:
                traverse(node.next)
            if node.previous:
                traverse(node.previous)
            visited.append(node)
        traverse(self.root)
        return visited

    def depth_first_search_INorder(self):
        """
        goes thru the tree all the way to the left then the root then the right
         (Canaan)
        /        \
     (Alphrad)   (Dante)
                    \  
                   (Vergil)
        returns --> [Alphrad, Canaan, Dante, Vergil]
        """
        visited: list = []

        def traverse(node: Node) -> None:
            if node.previous:
                traverse(node.previous)
            visited.append(node)
            if node.next:
                traverse(node.next)
        traverse(self.root)
        return visited

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
            if node.previous:
                print(node.previous, "<-- left side node")
                traverse(node.previous)
            visited.append(node)
            print(node, "<-- root node")
            if node.next:
                print(node.next, "<-- right side node")
                traverse(node.next)
        traverse(self.root)
        return visited


if __name__ == "__main__":
    tree = BinarySearchTree()

    #
    #                 (Canaan)
    #               /         \
    #         (Alphrad)      (Dante)
    #                            \
    #                           (Vergil)
    #                          /
    #                      (Maria)
    #                       /
    #                   (Lady)

    tree.insert("Canaan")
    tree.insert("Alphrad")
    tree.insert("Dante")
    tree.insert("Vergil")
    tree.insert("Maria")
    tree.insert("Lady")
    print(tree.breadth_first_search())
    # dies off cause of recausion depth
    print(tree.depth_first_search_PREorder(), "\t <-- Pre Order")
    print(tree.depth_first_search_POSTorder(), "\t <-- Post Order")
    print(tree.depth_first_search_INorder(), "\t <-- In Order")

    # print(tree.find("Vergil"))
    # tree.print_tree()
