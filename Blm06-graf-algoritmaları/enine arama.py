# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek
# Youtube : 

graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']

}

graph1 = {
    '1':['2','3','4'],
    '2':['1','3','5'],
    '3':['1','2','6'],
    '4':['1'],
    '5':['2'],
    '6':['3']
    }

def bfs(graph, start):
    ziydug = []
    kuyruk = [start]
    while kuyruk:
        simdikidug = kuyruk.pop(0)
        if simdikidug not in ziydug:
            ziydug.append(simdikidug)
            kuyruk.extend(graph[simdikidug])#burda stack listemize graph listesindeki node ekledik
    return ziydug


print("Ziyaret edilen dugumler")
print (bfs(graph1, '1'))
