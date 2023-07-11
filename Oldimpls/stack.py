""" 
    the data structure, not to be confused with the awesome singer by the same name :P 
    https://touhoudb.com/Ar/561
"""
from Oldimpls.node import Node


class Stack:
    """Used Doubly linked list"""

    def __init__(self) -> None:
        self.length: int = 0
        self.first: Node = None
        self.last: Node = None

    def push(self, val: any) -> int:
        """
        adds a new node to the start of the stack
        """
        new_node = Node(val)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            old_first = self.first
            self.first = new_node
            old_first.previous = self.first
            self.first.next = old_first
        self.length += 1
        return self.length

    def pop(self) -> Node:
        """
        removes the last value from the stack
        """
        if self.length == 0:
            return "Nothign to remove"
        if self.length == 1:
            res = self.first
            self.first = None
            self.last = None
            self.length -= 1
            return res
        else:
            old_last = self.last
            new_last = self.last.previous
            new_last.next = None
            self.last = new_last
            self.length -= 1
            return old_last

    def print_dll(self) -> None:
        """
            for visulaizing the Doubly Linked List
        """
        if self.length == 0:
            return print("Empty List ヽ(゜▽゜　)－C<(/;◇;)/~")
        elif self.length == 1:
            return print(f"{self.first.val} <-- first\n{self.last.val} <-- last")
        else:
            current_first = self.first
            counter = 0
            while(current_first):
                if counter == 0:
                    print(current_first.val, "<- First")
                    print(current_first.next.val, "<-- first Next val")
                    print(" *** " * 5)
                elif counter == self.length - 1:
                    print(current_first.val, "<- Last ")
                    print(current_first.previous.val, "<-- last Prevoius val")
                    print(" *** " * 5)
                else:
                    print(current_first.val, "<- Node")
                    print(current_first.next.val, "<- Node next")
                    print(current_first.previous.val, "<- Node prev")
                    print(" *** " * 5)
                counter += 1
            # print(" *** " *  5)

                current_first = current_first.next


if __name__ == "__main__":
    stack = Stack()
    stack.push("vergil")
    stack.push("dante")
    stack.push("alphrad")
    stack.push("canaan")
    stack.print_dll()
    print("=== old list ===")
    print(stack.pop())
    print("=== new list ===")

    stack.print_dll()
