class MaxHeap():
    def __init__(self) -> None:
        self.heap = []

    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index -1 ) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)] :
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left = self._left_child(index)
            right = self._right_child(index)

            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left
            
            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        item_2_remove = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        
        return item_2_remove

    @property
    def print_heap(self):
        for idx,i in enumerate(self.heap):
            print(f"|{idx}|{i}|", end=" ")
        print("\n")


mh = MaxHeap()
mh.heap = [99,72,61,58]
mh.print_heap
mh.insert(100)
mh.print_heap
mh.remove()
mh.remove()
mh.print_heap

