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


array = [12, 11, 13, 5, 6, 8, 97, 57, 22]
insertionSort(array)
print(array)
