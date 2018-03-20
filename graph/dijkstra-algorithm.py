def dijkstra(graph,start,end):
    minDistance = {}
    previous = {}
    unseenNodes = graph
    inf = 9999999
    path = []

    for node in unseenNodes:
        minDistance[node] = inf
    minDistance[start] = 0

    while unseenNodes:
        min = None
        for node in unseenNodes:
            if min is None:
                min = node
            elif minDistance[node] < minDistance[min]:
                min = node

        for childNode, weight in graph[min].items():
            if weight + minDistance[min] < minDistance[childNode]:
                minDistance[childNode] = weight + minDistance[min]
                previous[childNode] = min
        unseenNodes.pop(min)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = previous[currentNode]
        except KeyError:
            print('Path error')
            break
    path.insert(0,start)
    if minDistance[end] != inf:
        print(minDistance[end])
        print(path)


graph = {'A': {'B':4,'C':2},
         'B': {'C':1,'D':5},
         'C': {'D':8,'E':10},
         'D': {'Z':6,'E':2},
         'E': {'Z':3}
         }
print(dijkstra(graph,'A','Z'))
