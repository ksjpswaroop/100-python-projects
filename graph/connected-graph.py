def bfs(graph,start):
    final = {}
    for i,j in graph:
        try:
            final[i].append(j)
        except KeyError:
            final[i] = [j]
    print(final)
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            nextto = final[node]

            for i in nextto:
                queue.append(i)
    print(visited)


link_1 = [['A','B'],['B','C'],['B','D'],['C','D'],['D','A']]
link_2 = [['A','B'],['B','C'],['C','D'],['D','A']]
link_3 = [['A','B'],['A','C'],['B','C'],['C','D'],['D','E'],['E','A']]
bfs(link_1,'A')
bfs(link_2,'A')
bfs(link_3,'A')
