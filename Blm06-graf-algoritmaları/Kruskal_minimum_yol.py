# KRUSKAL ALGORİTMASI
# En küçük maliyetli yolun bulunması, Dijsktra'ya alternatif
# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek

graph={
    'A':{'B':7 ,'D':5 },
    'B':{'A':7 ,'C':8 ,'D':9,'E':7},
    'C':{'B':8 ,'E':5},
    'D':{'A':5 ,'B':9 ,'E':7,'F':6},
    'E':{'B':7,'C':5,'D':7 ,'F':8,'G':9},
    'F':{'D':6 ,'E':8 ,'G':11},
    'G':{'E':9 ,'F':11 }
}


graph7={
    's': {'a': 4, 'b': 2}, 
    'a': {'s':4,'b': 3, 'c': 1, 'd': 7}, 
    'b': {'s':2,'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'f': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'f': 2}, 
    'f': {'c':7,'d':2}
    }


graph8 = {'s': {'a': 2, 'b': 1},
            'a': {'s': 2, 'b': 4, 'c':8},
            'b': {'s': 1, 'a': 4, 'd': 2},
            'c': {'a': 8, 'd': 7, 't': 4},
            'd': {'b': 2, 'c': 7, 't': 5},
            't': {'c': 4, 'd': 5}}


Vertices=list(graph.keys())
edges = []
s=[]
f=[]
minimum_spanning_tree = []
parent = dict()
rank = dict()

def make_set(node):
    parent[node] = node #Burada her düğüme kendisini parent diye atadı PARENT = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G'}
    rank[node] = 0  # HEr düğümün değerini baslarken 0 olarak atadı RANK = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
    #print(parent)
    #print(rank)


def find(node): # atası olmayanlara kendisini ata olarak dödürür
    if parent[ node] != node:  # yani düğümün atası kendisi değilse 
        parent[node] = find(parent[node])
    return parent[node] # o düğümün in PARENT ini döndürür


def union(node1, node2):
    root1 = find(node1)  #burda bir daha kontrol edilmesinin nedeni parazit döngü oluşturmamak
    root2 = find(node2)

    #print(root1,root2) # A D , C E , D F , D B , D E , E G
    if root1 != root2:
        if rank[root1] > rank[root2]:  # root1 in degeri root2 den BÜYÜK OLMADIGI SÜRECE root2 nin parentine root1 ata
            parent[root2] = root1
        else:
            parent[root1] = root2       # diğer durumlarda root1 in parenti her zaman root2
            #print(parent)               # {'A': 'D', 'B': 'D', 'C': 'E', 'D': 'E', 'E': 'E', 'F': 'D', 'G': 'G'}
        if rank[root1] == rank[root2]:
            rank[root2] += 1
            #print(rank)


def kruskal(graph):
    for i in graph:
        j=0
        while j < len(graph[i].values()):#graph[i] nin degerlerinin sayısı
            s=list(graph[i].values())    #graphtaki sayı degerleri
            f=list(graph[i].keys())      #graphtaki value harfleri
            k = (s[j],i,f[j])            #k burada bir tuple 
            j=j+1
            edges.append(k)                # herseferinde oluşturduğumuz tuple 'ı edges listemize ekledik
    edges.sort()                       # edges listemizi sıraladık küçükten büyüğe doğru

    for node in Vertices:
        make_set(node)          # bu fonksiyon cagrılarak bütün düğümler başlangıçta rankı = 0 değerine atanır ve Parentleri de kendileri olarak atanmış olur 
        
  

    
    for edge in edges: # Edges listesi içinde dolan
        weight, node1, node2 = edge #  ve edge in  her bir elemanını ( weight , vertice1 , vertice2 ) şeklinde ata
        if find(node1) != find(node2):  # find fonksiyonu edges listesindeki ikili durumlardan birtanesini parent kontrolu yaparak elenmesini sağlar yani atası aynı olanları almıyor  örn: (1,s,b) , (1,2,s) ... 
            union(node1, node2)
            #print(union(node1,node2))
            minimum_spanning_tree.append(edge)

    return sorted(minimum_spanning_tree)



print (kruskal(graph))
