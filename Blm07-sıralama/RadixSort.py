# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://www.youtube.com/watch?v=78QmLHxEWlw
#gizem
#radix sort
from math import log10

def get_digit(number, base, pos):
    return (number // base ** pos) % base


def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i - 1]
    return array


def radix_sort(l, base=10):
    passes = int(log10(max(l)) + 1)
    output = [0] * len(l)

    for pos in range(passes):
        count = [0] * base

        for i in l:
            digit = get_digit(i, base, pos)
            count[digit] += 1

        count = prefix_sum(count)

        for i in reversed(l):
            digit = get_digit(i, base, pos)
            count[digit] -= 1
            new_pos = count[digit]
            output[new_pos] = i

        l = list(output)
    return output


arr = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print("sıralanmış dizi:",radix_sort(arr))