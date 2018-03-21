'''
pseudocode wiki

KRUSKAL(G):
1 A = ∅
2 foreach v ∈ G.V:
3    MAKE-SET(v)
4 foreach (u, v) in G.E ordered by weight(u, v), increasing:
5    if FIND-SET(u) ≠ FIND-SET(v):
6       A = A ∪ {(u, v)}
7       UNION(u, v)
8 return A



'''




def tree(graph,start):
    nodes = []
    final = {}

    for node in graph:
        nodes.append(node)


    #while nodes:
    for i in range(len(graph)):
        #print(graph[i])
        #nodes.remove(graph[i])





'''
graph = {'A': {'B':4,'F':2},
         'B': {'C':6,'F':5},
         'C': {'F':1},
         'F': {}
         }

'''
graph = {'a': {'b':4,'f':2},
         'b': {'c':6,'f':5},
         'c': {'d':3,'f':1},
         'd': {'e':2},
         'e': {'f':4},
         'f': {}
         }


print(tree(graph,'a'))
