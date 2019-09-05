# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk, Emre Kardal, Ömer Melek, Ömer Çifte

#bubble sort 
def bubble_Sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

def bidirectional_bubble_sort(array):
    n = len(array)//2
    while(n > 0):
        m = n
        while(m > 0):
            i = 0
            while(i < len(array) - m ):
                if(array[i] > array[i + m]):
                    array[i + m] -= array[i]
                    array[i] += array[i + m]
                    array[i + m] = array[i] - array[i + m]
                i+=1
            m = int(m/2)
        n = int(n / 2)
    flag = 1
    while(flag == 1):
        flag = 0
        j = 0
        while (j < len(array) - 1):
            if (array[j] > array[j + 1]):
                array[j + 1] -= array[j]
                array[j] += array[j + 1]
                array[j + 1] = array[j] - array[j + 1]
                flag = 1
            j+=1

array= [64, 34, 25, 12, 22, 11, 90]
# bubble_Sort(array)
bidirectional_bubble_sort(array)
print("Sıralı Dizi:",array)
