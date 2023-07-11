from typing import Any

from Oldimpls.node import SmallNode


class SinglyLinkedList:
    def __repr__(self) -> str:
        return \
            f"I'm a glorious singly linked list!!!, i contain {self.head.val}, next to it {self.tail.next}, {self.tail.val} and my lenth is {self.length}"
    head = None
    tail = None
    length: int = 0

    def push(self, value: any) -> bool:
        """
            Adds a value to linked list
        """
        node = SmallNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def pop(self):
        """
            Removes the last node from the link
        """
        if not self.head or self.length == 0:
            return "Linked list is empty fool!"
        if self.length == 1:
            self.head = None
            self.tail = None
            return "List is empty"
        current_head = self.head
        while current_head.next:
            new_tail = current_head
            current_head = current_head.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_head.val

    def print_values(self) -> None:
        """ just for visualizing 
        Prints all node values in the linked list
        """
        curent_node = self.head
        while curent_node:
            print(curent_node.val)
            curent_node = curent_node.next

    def shift(self):
        """
            Removes an element from the start (head) of the linked list
        """
        if not self.head:
            return "The list is empty"
        if self.length == 0:
            self.head = None
            self.tail = None
        removed_head = self.head
        self.head = removed_head.next
        self.length -= 1
        return removed_head

    def un_shift(self, value) -> bool:
        """
            add a new value to the start of the list
        """

        if not self.head:
            self.head = SmallNode(value)
            self.tail = SmallNode(value)
        else:
            current_head = self.head
            self.head = SmallNode(value)
            self.head.next = current_head
        self.length += 1
        return self

    def get(self, indx: int) -> SmallNode:
        """
            traverses the tree untill it finds the node at the given index
            returns that node
        """
        if indx < 0 or indx >= self.length:
            return None
        counter: int = 0
        target_node: SmallNode = None
        current_head: SmallNode = self.head
        while(current_head):
            if counter == indx:
                target_node = current_head
            current_head = current_head.next
            counter += 1
        return target_node

    def set(self, indx: int, value) -> bool:
        """
            updates node`s value at the given index to given value
        """
        old_node: SmallNode = self.get(indx)
        if old_node:
            old_node.val = value
            return True
        return False

    def insert(self, indx: int, value) -> bool:
        """
        adds a new value at the given index
        """
        if indx < 0 or indx > self.length:
            return False
        if indx == self.length:
            return self.push(value)
        if indx == 0:
            # hahaha this is cool, double negate . i negate yor negation kaiba !!
            return not not self.un_shift(value)

        new_node = SmallNode(value)  # create a new node
        previous_node = self.get(indx - 1)  # get the node bfore the inde
        temp = previous_node.next  # save the connection to the previous node
        previous_node.next = new_node  # insert the newly created node
        new_node.next = temp  # load the connection
        self.length += 1
        return True

    def delete(self, indx) -> Any:
        """
         delets the node at the given index 
         returns a bool depending on success
        """

        if indx < 0 or indx >= self.length:
            return None
        if indx == 0:
            return self.shift()
        if indx == self.length - 1:
            return self.pop()  # it's the last element so just remove it

        prev_node = self.get(indx - 1)
        node_to_delete = prev_node.next

        prev_node.next = node_to_delete.next

        self.length -= 1
        return node_to_delete

    def reverse(self):
        """
            reverse the linked list In Place
        """
        # swap the head and tail
        current_head = self.head

        self.head = self.tail
        self.tail = current_head

        # create 2 place holders to save the next and previous nodes
        previous_node = None
        next_node = None

        # loop thru the list
        while(current_head):
            next_node = current_head.next
            current_head.next = previous_node
            previous_node = current_head
            current_head = next_node

        return self.head.val


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.push("Canaan")
    singly_linked_list.push("Alphrad")
    singly_linked_list.push("Maria")
    print(singly_linked_list.push("Len len"))

    singly_linked_list.print_values()
    print("&*&" * 10)
    # print(singly_linked_list.pop())
    # print(singly_linked_list.pop())
    # print(singly_linked_list.pop())
    # print(singly_linked_list.pop())
    # print(singly_linked_list.shift())
    # print(singly_linked_list.un_shift("Dante"))
    # print(singly_linked_list.get(0))
    # print(singly_linked_list.insert(0, "Kanaan"))
    print(singly_linked_list.reverse())

    print("&*&" * 10)
    singly_linked_list.print_values()

    # print(singly_linked_list.head.val, "\t: head \n",singly_linked_list.tail.val, "\t: tail \n",singly_linked_list.length, "\t: length \n")
