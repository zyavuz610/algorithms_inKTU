# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk, Emre Kardal, Ömer Melek, Ömer Çifte

def selectionSort(list):
    for i in range(len(list)):

        min_index = i


        for j in range(i + 1, len(list)):
            if list[ min_index] > list[j]:
                min_index= j

        temp = list[i]
        list[i] = list[ min_index]
        list[ min_index] = temp

    return list

total_numbers=int(input())
array = []
for _ in range(total_numbers):
    array.append(float(input()))
print(selectionSort(array))
