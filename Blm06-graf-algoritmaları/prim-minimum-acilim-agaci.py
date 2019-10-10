# Prim Algoritmas
# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek
# Youtube : 

graph={
    'A':{'B':5 ,'F':5 },
    'B':{'A':5 ,'C':1 ,'G':2},
    'C':{'B':1 ,'D':3},
    'D':{'C':3 ,'G':3 ,'E':2},
    'E':{'D':2 ,'F':2},
    'F':{'A':5 ,'E':2 ,'G':3},
    'G':{'B':2 ,'D':3 ,'F':3 },
    }



graph1={
    'A':{'B':5 ,'F':5 },
    'B':{'A':5 ,'C':1 ,'G':2},
    'C':{'B':1 ,'D':3},
    'D':{'C':3 ,'G':3 ,'E':2},
    'E':{'D':2 ,'F':2},
    'F':{'A':5 ,'E':2 ,'G':3,'S':1},
    'G':{'B':2 ,'D':3 ,'F':3 },
    'S':{'F':1}}




graph2={
     '1' : {'3':14, '2':30},
     '2' : {'1':30, '5':6, '6':18},
     '3' : {'1':14, '4':26, '7':32},
     '4' : {'3':26, '5':4, '6':5},
     '5' : {'4':4, '2':6, '7':15},
     '6' : {'2':18, '4':5, '7':3},
     '7' : {'6':3, '5':15, '3':32}
  
}


graph3={
    'A':{'B':7 ,'D':5 },
    'B':{'A':7 ,'C':8 ,'D':9,'E':7},
    'C':{'B':8 ,'E':5},
    'D':{'A':5 ,'B':9 ,'E':7,'F':6},
    'E':{'B':7,'C':5,'D':7 ,'F':8,'G':9},
    'F':{'D':6 ,'E':8 ,'G':11},
    'G':{'E':9 ,'F':11 }
}


graph4={
    's': {'a': 4, 'b': 2}, 
    'a': {'s':4,'b': 3, 'c': 1, 'd': 7}, 
    'b': {'s':2,'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'f': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'f': 2}, 
    'f': {'c':7,'d':2}
    }


graph5 = {'s': {'a': 2, 'b': 1},
            'a': {'s': 2, 'b': 4, 'c':8},
            'b': {'s': 1, 'a': 4, 'd': 2},
            'c': {'a': 8, 'd': 7, 't': 4},
            'd': {'b': 2, 'c': 7, 't': 5},
            't': {'c': 4, 'd': 5}}


s=[]
visited=[]
path=[]
edges=[]
inf=float('inf')

def Prim(u):
        PrintEdgelist(u)       #bu fonksiyon seçilen düğümün kenarlarını edges lstesine ekler ve bu listeyi sort eder             
        #print("Tüm kenarlar",edges)
        EdgeControl(edges)         # edges listesi içerisinde bir birinin tersi tuple lar varsa bunlardan birini silecek örn: ( 3,D,G) ,(3,G,D)
        print("Tüm kenarlar (TErs olan silindikten sonra)",edges)
        w1,n1,n2=edges[0]
        Z=(w1,n2,n1)
        PathControl(Z,path,edges)              # burda edges[0] ın tersi path içinde varsa bunu almaya gerek yok edges içinden çıkarıyoruz
        X=edges.pop(0)                  # eğer edges[0] ın tersi path içinde yoksa path e eklemek için bunu alıyoruz 
        w2,n3,n4=X

        if n4 in visited : #edges boş kalınca hata veriyor bundan dolayı edges sonuna (inf,inf,inf) tuple koydum ve enson bunu görünce işlemler sonlanacak
            edges.append((inf,inf,inf))
            VisitedControl(edges,visited)
            X=edges[0]
            w2,n3,n4=X
       
        print("secilen kenar",X)
        print("kalan kenar ", edges)
        
        if n4 != inf:
            if n4 not in visited:
                path.append(X)
                print("---------->>>>     YOL",path)
                print()
                Prim(n4)        
        return path

def PrintEdgelist(u):      # Seçilen her düğümün kenarlarını Edges listesine ekler ve bu listeyi küçükten büyüğe doğru sıralar
        visited.append(u)
        print(visited)
        s=list(graph[u].values())
        f=list(graph[u].keys())
        for i in range(0,len(graph[u])):
            k=(s[i],u,f[i])                   # seçile düğümün değeri,kendisi,komşusu şeklinde tuple oluştur ( weight , node , neighbour )
            edges.append(k)                   # oluşturulan tuple herseferinde listene at
        edges.sort()                          #listeyi her seferinde sırala

def EdgeControl(edges): #Edges listesi içerisinde birbirinin tersi yönde olan kenar varsa siliyoruz
    for edge in edges:
            w1,n1,n2=edge
            Z=(w1,n2,n1)
            if Z in edges:#tersi varsa tersini çıkar
                edges.remove(Z)
            else:
                None

def VisitedControl(edges,visited):
    w2,n3,n4=edges[0]
    if n4 in visited:
        print(edges[0],"-",n4,"daha önce ziyaret edilmiş mi? edilmişse bu kenarı edges listesinden çıkar ")
        edges.pop(0)
        VisitedControl(edges,visited)


def PathControl(Z,path,edges):
    print(Z,"Path içerisinde varsa sil")
    if Z in path:
        edges.pop(0)         # eğer Z kenarı daha önce yola eklenmişse bunu edges ten çıkarmalıyız burda sildik
        w1,n1,n2=edges[0] 
        Z=(w1,n2,n1)         
        PathControl(Z,path,edges)    # edgesten bir durumu cıkardıktan sonra burda bir sonraki durumu kontrol ediyoruz varmı yokmu diye


        
x=Prim('A')
print()
print("--------------Y-O-L------------>>",x)