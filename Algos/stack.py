class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1


    def push(self, value):
        new_node = Node(value)

        if self.height == 0\
            or not self.top:

            self.top = new_node
            self.height += 1
            return True
        
        old_top = self.top
        self.top = new_node
        self.top.next = old_top

        self.height += 1
        return True
    
    def pop(self):

        if self.height == 0\
            or not self.top:
            return None
        
        old_top = self.top
        self.top = old_top.next
        self.height -= 1
        return old_top

    @property
    def print_stack(self):
        t = self.top

        while t:
            print(t.value)

            t = t.next

s = Stack(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
s.pop()
# s.pop()
# s.pop()
# s.pop()
s.print_stack