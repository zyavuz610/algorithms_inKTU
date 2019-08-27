# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek
# Youtube : 


graph = {
    'A' : ['B','F'],
    'B' : ['A','C','D','F'],
    'C' : ['B','D'],
    'D' : ['B','C','E','F'],
    'E' : ['D','F'],
    'F' : ['A','B','D','E']
}


def addEdge( u, v):
    graph[u].append(v)
    graph[v].append(u)
def rmvEdge(u, v):
    for i, k in enumerate(graph[u]):
        if k == v:
            graph[u].pop(i)
    for i, k in enumerate(graph[v]):
        if k == u:
            graph[v].pop(i)
def DFSCount(v, visited):

    dizi = list(graph.keys())
    a = dizi.index(v)


    count = 1
    visited[a] = True

    for i in graph[v]:
        a = dizi.index(i)

        if visited[a] == False:
            count = count + DFSCount(i, visited)

    return count

def isValidNextEdge(u, v):

    V=len(graph)


    if len(graph[u]) == 1:
        return True
    else:

        visited = [False] * (V)
        count1 = DFSCount(u, visited)

        rmvEdge(u, v)
        visited = [False] * (V)
        count2 = DFSCount(u, visited)


        addEdge(u, v)

        return False if count1 > count2 else True
def printEulerUtil(u):

    for v in graph[u]:
        if isValidNextEdge(u,v):
            print(u,v)
            rmvEdge(u,v)
            printEulerUtil(v)

def printEulerTour():
    u = 'C'

    for i in graph:

        if len(graph[i]) % 2 != 0:
            u = i
            break

    print("\n")
    printEulerUtil(u)

printEulerTour()



