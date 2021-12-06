

class Node:
    def __repr__(self) -> str:
        return "one node weak, many nodes doubly weak （︶^︶）"
    def __init__(self, val:any) -> None:
        self.val = val
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __repr__(self) -> str:
        return "a linked list with prevoius pointer !!"

    def __init__(self) -> None:
        self.head :Node = None 
        self.tail : Node = None
        self.length : int = 0

    def push(self, val :any) -> bool :
        """
         adds a value at the end of the list
        """
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.length += 1
        return new_node

    def pop(self):
        """
        removes the very last node from the DLL
        """
        old_tail = None
        if self.length <= 0: return "list is empty fool!!"
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.previous
            old_tail = self.tail
            self.tail = new_tail
            self.tail.next = None
        self.length -= 1
        return old_tail 

    def shift(self):
        """
            removes the head node 
        """
        old_head = self.head
        if self.length <= 0: return "list is empty fool!!"
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next
            self.head = new_head
            self.head.previous = None
        self.length -= 1
        return old_head

    def un_shift(self, value):
        """
            Add a node to the begginningg of the DLL
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            old_head.previous = self.head
            self.head.next = old_head
        self.length += 1
        return self.head.val

    def get (self, idx) -> Node:
        """
        returns the node at the index given
        """
        if idx < 0 or idx >= self.length: return None

        if idx >= self.length // 2 :
            # go from the tail
            current_tail = self.tail
            counter = self.length -1 # the index
            while(current_tail):
                if counter == idx:
                    return current_tail
                current_tail = current_tail.previous
                counter -= 1 
        elif idx <= self.length //2 :
            # go ftom the head
            current_head = self.head
            counter = 0 # from the start
            while (current_head):
                if counter == idx:
                    return current_head
                current_head = current_head.next
                counter += 1  

    def set(self,idx, value ):
        """
        updates the value at the given index
        """
        node = self.get(idx)
        if node:
            node.val = value
            return True
        return False

    def insert(self, idx, value):
        """
        inserts a node at the given index
        """
        if idx < 0 or idx > self.length: return False
        if idx == 0 : return not not self.un_shift(value)
        if idx == self.length: return not not self.push(value)

        else :
            new_node = Node(value)
            previous_node = self.get(idx -1)
            temp: Node = previous_node.next

            previous_node.next = new_node
            new_node.previous = previous_node
            new_node. next = temp
            temp.previous = new_node

            
        self.length += 1
        return True

    def remove(self, idx):
        """
        deletes the node at the given index
        """
        if idx < 0 or idx >= self.length : return None
        if idx == 0 : return self.shift()
        if idx == self.length -1 : return  self.pop() # it's the last element so just remove it 

        previous_node = self.get(idx - 1)
        node_to_delete = previous_node.next

        previous_node.next = node_to_delete.next
        previous_node.next.previous = previous_node
        self.length -= 1
        return True


    def reverse(self):
        """
        reverses the DLL in place
        """

        current_head = self.head

        self.head = self.tail
        self.tail = current_head

        previous_node = None
        next_node = None

        for i in range(0, self.length):
            next_node = current_head.next 
            current_head.next = previous_node
            current_head.previous = current_head
            previous_node = current_head
            current_head = next_node

        return self.head
    def print_dll(self) -> None:
        """
            for visulaizing the Doubly Linked List
        """
        if self.length == 0: return print("Empty List ヽ(゜▽゜　)－C<(/;◇;)/~")
        elif self.length == 1 : return print(f"{self.head.val} <-- head\n{self.tail.val} <-- tail")
        else:
            current_head = self.head
            counter = 0
            while(current_head):
                if counter == 0:
                    print(current_head.val, "<- Head")
                    print(current_head.next.val, "<-- Head Next val")
                    print(" *** " *  5)
                elif counter == self.length -1:
                    print(current_head.val, "<- Tail ")
                    print(current_head.previous.val, "<-- Tail Prevoius val")
                    print(" *** " *  5)
                else:
                    print(current_head.val, "<- Node")
                    print(current_head.next.val, "<- Node next")
                    print(current_head.previous.val, "<- Node prev")
                    print(" *** " *  5)
                counter += 1
            # print(" *** " *  5)

                current_head = current_head.next


        


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push("canaan")
    dll.push("alphrad")
    dll.push("dante")
    dll.push("vergil")
    dll.print_dll()
    print("=== old list ===")
    print(dll.reverse())
    print("=== new list ===")

    dll.print_dll()