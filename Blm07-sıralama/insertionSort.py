# https://youtu.be/FrSElf7uglE
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

# Youtube: https://youtu.be/NJQOGp7L-_k
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

# Youtube: https://youtu.be/iPYtzOfJoxA
def straight_insertion_sort(arr):
    for i in  range(len(arr)):
        t = arr[i]
        j=i
        while j > 0 and arr[j-1] > t :
            arr[j] = arr[j-1]
            j-=1
        arr[j] = t
        
array = [12, 11, 13, 5, 6, 8, 97, 57, 22]
#insertionSort(array)
straight_insertion_sort(array)
print(array)
