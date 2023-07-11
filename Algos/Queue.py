from Node import SmallNode

class Queue:
    def __init__(self, value) -> None:
        new_node = SmallNode(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    
    def enqueue(self, value):
        new_node = SmallNode(value)

        if not self.first\
            or self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return True
        
        old_last = self.last
        self.last = new_node
        self.last.next = old_last
        self.length += 1
        return True
    
    def dequeue(self):

        if not self.first\
        or self.length == 0:       
            return None
        
        if self.length == 1:
            t = self.first
            self.first = None
            self.last = None
            return t
        prev = self.last
        
        while prev:
            if prev.next == self.first:
                t = self.first
                prev.next = None
                self.first = prev
                self.length -= 1
                return t
            prev = prev.next
        return None

    @property
    def print(self):
        t = self.last
        while t:
            print(t.val)
            t = t.next


q = Queue(10)

q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print
