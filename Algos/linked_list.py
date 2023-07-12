class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.length < 2:
            return

        sorted_until = None

        while sorted_until != self.head.next:
            current = self.head
            while current.next != sorted_until:
                next_node = current.next
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                current = current.next
            sorted_until = current

    def selection_sort(self):
        if self.length < 2:
            return
        current = self.head
        while current.next is not None:
            smallest = current
            inner_current = current.next
            while inner_current is not None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next
            if smallest != current:
                current.value, smallest.value = smallest.value, current.value
            current = current.next
        self.tail = current

    def insertion_sort(self):
        if self.length < 2:
            return

        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None

        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next

            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while (
                    search_pointer.next is not None
                    and current.value > search_pointer.next.value
                ):
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current

        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp


    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy
    
        while self.head and other_head :
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
    
        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
    
        self.head = dummy.next
        self.length += other_list.length

    def _merge(self, other_list):
        dummy = Node(0)
        combined = dummy
        other_l = other_list.head
        while self.head and other_l:
            if self.head.value > other_l.value:
                combined.next = other_l
                other_l = other_l.next
            else:
                combined.next = self.head
                self.head = self.head.next
            combined = combined.next
            
        if self.head:
            combined.next = self.head
        else:
            combined.next = other_l
            self.tail = other_list.tail

        self.head = dummy.next
        self.length += other_list.length

"""Bubble sort"""
def test_bubble():
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.bubble_sort()

    print("\nSorted Linked List:")
    my_linked_list.print_list()


    """
        EXPECTED OUTPUT:
        ----------------
        Linked List Before Sort:
        4
        2
        6
        5
        1
        3

        Sorted Linked List:
        1
        2
        3
        4
        5
        6

    """

"""Selection sort"""
def test_selection():
    print("-*-" * 30)
    print("selection sort")
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.selection_sort()

    print("\nSorted Linked List:")
    my_linked_list.print_list()


    """
        EXPECTED OUTPUT:
        ----------------
        Linked List Before Sort:
        4
        2
        6
        5
        1
        3

        Sorted Linked List:
        1
        2
        3
        4
        5
        6

    """


def test_merge():

    l1 = LinkedList(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)


    l2 = LinkedList(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)

    l1.merge(l2)

    l1.print_list()


    """
        EXPECTED OUTPUT:
        ----------------
        1 
        2 
        3 
        4 
        5 
        6 
        7
        8

    """


test_merge()
