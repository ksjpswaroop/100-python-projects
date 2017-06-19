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
    if sum(odd) == 2:
        print("Eulerian path")
    elif sum(odd) == 0 :
        print("Eulerian circuit")
    else:
        print("Not an eulerian path")


link_1 = [['A','B'],['B','C'],['B','D'],['C','D'],['D','A']]
link_2 = [['A','B'],['B','C'],['B','D'],['C','D']]
link_3 = [['A','B'],['A','C'],['B','C'],['B','D'],['C','D'],['C','A']]
eulerian(link_1)
eulerian(link_2)
eulerian(link_3)
