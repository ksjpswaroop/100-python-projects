def dijkstra(graph,start,end):
    cost = []
    visited = [start]
    previous = []
    queue = []

    for node in graph:
        queue.append(node)

    while queue:
        for i in graph:
            for j in graph[i]:
                print(graph[i])
                print(graph[i][j])
            #min between graphs and remove it from queue and append it to visited
            #queue.remove()
            #add cost







graph = {'A': {'B':4,'C':2},
         'B': {'C':1,'D':5},
         'C': {'D':8,'E':10},
         'D': {'Z':6,'E':2},
         'E': {'Z':3}
         }
print(dijkstra(graph,'A','Z'))
