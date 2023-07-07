class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vert1, vert2 ):
        if vert1 in self.adj_list.keys() \
        and vert2 in self.adj_list.keys():
            self.adj_list[vert1].append(vert2)
            self.adj_list[vert2].append(vert1)
            return True
        return False

    def remove_edge(self, vert1, vert2):
        if vert1 in self.adj_list.keys() \
        and vert2 in self.adj_list.keys():
            if vert2 in self.adj_list[vert1]:
                self.adj_list[vert1].remove(vert2)
            if vert1 in self.adj_list[vert2]:
                self.adj_list[vert2].remove(vert1)
            return True
        return False

    def remove_ver(self, vert):
        if vert in self.adj_list.keys():
            for l in self.adj_list[vert]:
                self.adj_list[l].remove(vert)
            self.adj_list.pop(vert)
            return True
        return False

    def print_graph(self):
        for v in self.adj_list:
            print(f"{v} : {self.adj_list[v]}")
            






g = Graph()
g.add_vertex("Canaan")
g.add_vertex("Vergil")
g.add_vertex("Dante")
g.add_vertex("Maria")
g.add_edge("Canaan", "Dante")
g.add_edge("Canaan", "Vergil")
g.add_edge("Dante", "Vergil")
g.add_edge("Maria", "Vergil")
g.add_edge("Maria", "Dante")
g.add_edge("Maria", "Canaan")
g.print_graph()
# g.remove_edge("Canaan", "Dante")
# g.remove_edge("Canaan", "Vergil")
g.remove_ver("Maria")
print("----"* 20)
g.print_graph()