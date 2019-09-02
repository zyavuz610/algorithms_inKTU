# Dijkstra Algoritması
# En küçük maliyetli yolun bulunması
# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek


graph2 = []

graph={
    'start': {'a': 4, 'b': 2}, 
    'a': {'b': 3, 'c': 1, 'd': 7}, 
    'b': {'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'finish': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'finish': 2}, 
    'finish': {}
    }

infinity = float("inf")  # infinity sonsuzluk

costs = {}               # cost maliyet
costs["a"] = 4
costs["b"] = 2
costs["c"] = infinity
costs["d"]= infinity
costs["finish"] = infinity


processed=[]              # üzerinde işlem yapılmış düğümler
result=[]

def find_lowest_cost_node(costs):     # ucuz maliyeti buluyor
  lowest_cost = float("inf")
  lowest_cost_node = None

  for node in costs:       # her düğüm üzerinde dön

    cost = costs[node]    # node un degerlerini verir

    if cost < lowest_cost and node not in processed:                # şimdiye kadarki en düşük maliyet ve işlenmemişse
      lowest_cost = cost                                             # yeni en düşük maliyet olarak güncelle
      lowest_cost_node = node
  return lowest_cost_node


node = find_lowest_cost_node(costs)   # İşlenmemiş en düşük maliyetli düğümü bul


while node is not None:  # Bütün düğümler işlenmişse yani none dan farklı oluncaya kadar dön diyor, döngü sona erer 

  cost = costs[node]

  neighbors = graph[node]
  for n in neighbors.keys():  # Bu düğümün tüm komşularını dolaş
    for i in processed:
      if i !=n :

        new_cost = cost + neighbors[n]     
        if costs[n] > new_cost:           # Daha ucuz bir düğüm bulduysak, bu düğüm üzerinden ilerle
          costs[n] = new_cost             # Bu düğüm için maliyetleri güncelle
  processed.append(node)              # Bu düğümü işlenmiş olarak işaretle
  node = find_lowest_cost_node(costs) # İşlenecek bir sonraki düğümü bul ve döngüye devam et burda en küçük düğümü 
  result.append(node)


for i in range(len(result)-1):
    print(result[i])
