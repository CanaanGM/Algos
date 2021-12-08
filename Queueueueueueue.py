"enouph queque more pew pew"

from node import Node


class Queue:
    """Used Doubly linked list"""

    def __init__(self) -> None:
        self.length: int = 0
        self.first: Node = None
        self.last: Node = None

    def enqueue(self, val: any) -> int:
        """
        adds a new node to the end of the stack
        """
        new_node = Node(val)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            old_last = self.last
            self.last = new_node
            old_last.next = self.last
            self.last.previous = old_last
        self.length += 1
        return self.length

    def pop(self) -> Node:
        """
        removes the first value from the stack
        """
        if self.length == 0:
            return None
        if self.length == 1:
            res = self.first
            self.first = None
            self.last = None
            self.length -= 1
            return res
        else:
            old_first = self.first
            new_first = self.first.next
            new_first.previous = None
            self.first = new_first
            self.length -= 1
            return old_first

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
    queue = Queue()
    print("=== old list ===")
    queue.enqueue("vergil")
    queue.enqueue("dante")
    queue.enqueue("alphrad")
    queue.enqueue("canaan")
    queue.print_dll()
    print(queue.pop().val)
    print(queue.enqueue("canaan"))
    print(queue.enqueue("sparda"))

    print("=== new list ===")

    queue.print_dll()
