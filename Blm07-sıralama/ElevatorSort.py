# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://www.youtube.com/watch?v=j-UdoOZ8134
#gizem
#elevator sort 
array = [12, 11, 13, 5, 6, 8, 4]
def elevator(array):
    bottom = 0
    while bottom < len(array) - 1:
        if array[bottom] > array[bottom + 1]:
            array[bottom], array[bottom + 1] = array[bottom+1], array[bottom]
            if bottom > 0:
                bottom-=1
        else:
            bottom+=1


print("düzenlenmemiş dizi:", array)
elevator(array)
print(array)