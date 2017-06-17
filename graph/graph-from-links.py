def find_graph(graph):
    final = {}
    for i,j in graph:
        try:
            final[i].append(j)
        except KeyError:
            final[i] = [j]
    print(final)



link = [['A','B'],['B','C'],['B','D'],['C','D']]
find_graph(link)
