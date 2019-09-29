# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://www.youtube.com/watch?v=XbB-mS9kcm0
#gizem
#shell sort
array= [14, 46, 43, 27, 57, 41, 45, 21, 70]
h = 1
while (h * 3 + 1) < len(array):
    h = 3 * h + 1

while h > 0:
    for i in range(int(h) -1, len(array)):
        b = array[i]
        j = i
        while j >= int(h) and array[j - int(h)] > b:
            array[j] = array[j - int(h)]
            j -= int(h)
        array[j] = b
    h //= 3

print("Dizinin eleman sayisi:", len(array))
print("sıralanmış dizi:",array)