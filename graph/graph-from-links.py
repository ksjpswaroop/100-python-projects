def graph(link):
    node = {}
    for i in range(0,len(link)):
        #if i not in node[i]:
        #node[i].append(link[i][1])
        #node.insert(i,link[i][0])
        #else:
        #    node.insert(i,link[i])
        node[link[i][0]] = link[i][1]
        print(node)




link = [[1,2],[2,3],[2,4],[3,4]]
graph(link)
