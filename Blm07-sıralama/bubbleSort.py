# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :

#bubble sort, gizem 
def bubble_Sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]


array= [64, 34, 25, 12, 22, 11, 90]
bubble_Sort(array)
print("Dizinin eleman sayisi:", len(array))
print("Sorted array is:",array)
