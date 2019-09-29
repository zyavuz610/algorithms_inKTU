# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://www.youtube.com/watch?v=IcryqKzeiPw
#gizem
#shaker sort 
array = [66, 34, 67, 2, 9, 16]
change = True

while change:
    max_state = len(array)
    min_state = 1
    change = False
    for i in range(min_state, max_state):
        if array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i-1], array[i]
            change = True
    max_state -= 1
    if not change:
        break

    for i in range(max_state - 1, min_state, -1):
        if array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i-1], array[i]
            change = True
    min_state += 1

print("Dizinin eleman sayisi:", len(array))
print("sıralanmış dizi:",array)