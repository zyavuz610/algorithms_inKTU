# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :

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


array1=[4,1,5,6,3,2]
binary_insertion_sort(array1)
print(array1)
