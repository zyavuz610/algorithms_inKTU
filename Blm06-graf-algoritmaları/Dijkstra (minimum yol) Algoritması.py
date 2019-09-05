# Dijkstra Algoritması
# En küçük maliyetli yolun bulunması
# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek

# https://gist.github.com/ozdemirburak/4821a26db048cc0972c1beee48a408de




graph={
    'start': {'a': 4, 'b': 2}, 
    'a': {'b': 3, 'c': 1, 'd': 7}, 
    'b': {'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'finish': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'finish': 2}, 
    'finish': {}
    }
def dijkstra(graph, bas, bit, visited=[], distances={}, predecessors={}):
  """ src içinde yönlendirilen en kısa yol ağacını hesaplar
  """

  if bas not in graph:
    raise TypeError('böyle bir il yok')
  if bit not in graph:
    raise TypeError('böyle bir il yok')

  if bas == bit:
    # En kısa yolu oluşturur ve görüntüleriz
    path = []
    pred = bit
    while pred != None:
      path.append(pred)
      #print()
      #print("--------", pred, "-----------")
      #print()
      pred = predecessors.get(pred, None)  # ata dizisinde fınısh varmı varsa değerini döndür yoksa none

    # yolu güzel bir şekilde görüntülemek için diziyi tersine çevirir.
    readable = path[0]
    for index in range(1, len(path)):  # tersten yazdırarak sonucu elde ederiz
      readable = path[index] + '--->' + readable


    print("path: " + readable + ",   cost=" + str(distances[bit]))
  else:
    # ilk çalıştırma ise maliyeti başlatır.
    if not visited:  # sadece basta girer
      distances[bas] = 0

    # komsuları gez
    for neighbor in graph[bas]:
      if neighbor not in visited:
        new_distance = distances[bas] + graph[bas][neighbor]
        if new_distance < distances.get(neighbor, float('inf')):
          distances[neighbor] = new_distance

          predecessors[neighbor] = bas

    #print(distances, "             uzaklık")
    #print(predecessors, "          ataları")
    # ziyaret edildi olarak işaretle
    visited.append(bas)  # visited uğranmamış komşulara uğruyor
    #print(visited, "               ziyaret edilen")

    # şimdi tüm komşular ziyaret edildi: tekrar
    # 'x' mesafeli en az ziyaret edilen düğümü seçin
    # Dijskstra'yı src = 'x' ile çalıştırın
    unvisited = {}
    for k in graph:

      if k not in visited:
        #print(k)
        unvisited[k] = distances.get(k, float('inf'))
       # print(unvisited, "                 komşu olanlara değerleri , olmayanlara sonsuz yazar")

    x = min(unvisited, key=unvisited.get)
    #print(x, "               min")
    #print()
    dijkstra(graph, x, bit, visited, distances, predecessors)



dijkstra(graph,'start', 'finish')
