'''
for use :↓ ↑  ↔ ↙ ↘ ↗ ↖ → ← 
graphs:

example_graph => 
{
    a:[b, c],
    b:[d],
    c:[e],
    e:[],
    d:[f],
    f:[]
}

(a) → (c)
 ↓     ↓
(b)   (e)
 ↓
(d) → (f)


* DFS: 
will visit all nodes in the graph in a liner direction before visiting the other neighbors
a -> c -> e -> b -> d -> f
explanation: from a will go to c cause c is at the top of the stack (a:[b,(c)]), then goes to (e), 
            since (e) lives alone with no neighors the function returns to (a)'s second neighbor (b) and continues from there.
            until it reaches the DEADEND which is f, the function stops executing.

- useus a stack (not the singer xD)

* BFS: 
will visit all neighbors to the starting node then their neighbors ... etc untill all are visited
(a) -> (b) -> (c) -> (d) -> (e) -> (f)
has to be implemented thru a Queue, recursion will conflict with the inner stack call of the function.
- uses a Queue

'''
from math import dist
from typing import Set


def depth_first_print (graph: dict, source_node:str) -> None:
    """
    Depth first via looping; forgot what's it called
    will go thru the graph like this:
    (a) -> (c) -> (e) returns to (a)'s second neighbor (b) -> (d) -> (f)
    """
    stack: list = [source_node]
    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node)
        for neighbor in graph[current_node]:
            stack.append(neighbor)

def depth_first_print_recursive(graph:dict, source_node:str) -> None:
    """
    Depth first in recursion
    base case: no recursive call i:e the neighbor list is empty.
    will go: (a) -> (b) -> (d) -> (f) returns to (a)'s second neghbor (c) -> (e).
    """
    print(source_node) # current location
    for neighbor in graph[source_node]:
        depth_first_print_recursive(graph, neighbor)


def breadth_first_print(graph:dict, source_node:str) -> None:
    """
    Breadth first searh:
    will go like this:
    current_node =(a) -> will but the neighbors in the queue
    queue = [(c), (b)]
    will take the last neghibor (b) as the current_node
    inserts the neighbors into the queu =[(d), (c)]
    takes (c) as current_node, puts the neighbors into queue = [(e), (d)]
    continues untill all are visited if possible
    """
    queue = [source_node]
    while( len(queue) > 0):
        current_node = queue.pop()
        print(current_node)
        for neighbor in graph[current_node]:
            queue.insert(0,neighbor)
   

'''
if the graph has paths to nodes ; 

(a) → (b) → (d)
 ↓  ↗
(c) ← (f)
 ↓
(e)
'''

def depth_first_has_path(graph:dict, source_node:str, dst:str) -> bool:
    """
    assumes there's no cycle in the graph
    """
    if source_node == dst: return True
    for neighbor in graph(source_node):
        if depth_first_has_path(graph, neighbor, dst): return True
    return False

def breadth_first_has_path(graph:dict, source_node:str, dst:str) -> bool:
    """
    """
    queue: list = [source_node]
    while len(queue) > 0:
        current_node = queue.pop()
        if current_node == dst: return True
        for neighbor in graph[current_node]:
            queue.insert(0, neighbor)
    return False


'''
adjasancy list            needs to transforms into a graph
[                           {
    [i,j],                      i:[j,k], 
    [k,i],                      j:[i],
    [m,k],        --->          k:[i,m,l],
    [k,l],                      m:[k],
    [o,n],                      l:[k],
]                               o:[n],
                                n:[o]
                            }

shape : 
    without a cycle:                with a cycle:
    (i) -- (j)                      (i) -(j)
     |                               |  ↗
    (k) -- (l)                      (k) -(l)    
     |                               |   
    (m)                             (m)    
                                        
    (o) -- (n)                      (o) -- (n)   

in problems if given a list of nodes convert it to a hash map!

'''

def build_graph(edges: list) -> dict:
    """
    takes in a list of nodes and transforms it to a graph
    """
    graph: dict[str:list] = {}
    for edge in edges:
        a,b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def has_path(graph:dict, source_node, dst_node, visited:set) -> bool:
    """
    determine if theres a path(link) from the source_node to the dst_node
    """
    if source_node == dst_node: return True # we found a link
    if source_node in visited: return False # there's no link

    visited.add(source_node) # mark source as visited
    for neighbor in graph[source_node]:
        if has_path(graph, neighbor, dst_node, visited): return True
    return False # no link/connection

def undirected_path (edges, nodeA, nodeB)-> bool:
    """"""
    graph: dict = build_graph(edges)
    return has_path(graph, nodeA, nodeB, set())







if __name__ == "__main__":
    example_graph : dict[str:str] = {
    "a":["b", "c"],
    "b":["d"],
    "c":["b", "e"],
    "d":[],
    "e":[],
    "f":["c"]
}   
    edges_list_example = [
        ["i","j"],
        ["k","i"],
        ["m","k"],
        ["k","l"],
        ["o","n"]
    ]

    # print(build_graph(edges_list_example))
    print(undirected_path(edges_list_example, "i", "n"))
    # depth_first_print(example_graph, "a")
    # depth_first_print_recursive(example_graph, "a")
    # breadth_first_print(example_graph, "a")

