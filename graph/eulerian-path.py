def eulerian(graph):
    final = {}
    for i,j in graph:
        try:
            final[i].append(j)
        except KeyError:
            final[i] = [j]
    print(final)
    odd = []
    for key,val in final.items():
        if (len(val)) % 2 != 0:
            odd.append(1)
    if sum(odd) == 0 or sum(odd) == 2:
        print("Eulerian path")
    else:
        print("Not an eulerian path")


link_1 = [['A','B'],['B','C'],['B','D'],['C','D'],['D','A']]
link_2 = [['A','B'],['B','C'],['B','D'],['C','D']]
eulerian(link_1)
eulerian(link_2)
