# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :

#insertion sort, gizem
def insertionSort(array):
    # Dizi boyunca elemanlar üzerinde tarama yapar
    for i in range(1, len(array)):

        key = array[i]
        # key anahtar değerinden büyük olan elemanları bulundukları durumdan
        # bir geriye olacak şekilde kaydırma işlemi yapılır. kendinde küçük ilk değeri
        # görene kadar kaydırma işlemi devam eder.
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# seren
def binary_insertion_sort(array):
    for i in range(1,len(array)):
        x=array[i]
        left=0
        right= i-1
        while left <= right:
            pivot=(left + right)//2
            if x < array[pivot]:
                right=pivot-1
            else:
                left=pivot+1

        for j in reversed(range(left, i)):
          array[(j+1)]= array[j]

        array[left]=x

        
array = [12, 11, 13, 5, 6, 8, 97, 57, 22]
insertionSort(array)
print(array)
