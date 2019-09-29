#sezgisel yontem
# asallık testi
import math
def sezgisel_yontem (a):
    max = int((a - 1) / 2)
    k = int(math.sqrt(a))
    dizi = [i for i in range(a + 1)]
    print(dizi)
    b = 0
    j = 1
    while (b < max):
        n = (2 * j) + 1
        b = int((n * n) / 2)
        for x in range(b, max + 1, n):
            dizi[x] = 0
        j = j + 1

    dizi = [x for x in dizi if x != 0]
    dizi = [x for x in dizi if x < max]

    asal_dizi = [0 for i in range(len(dizi) + 1)]
    asal_dizi[0] = 2
    j = 1
    for i in dizi:
        asal_dizi[j] = (2 * i) + 1
        j = j + 1
    return asal_dizi

print(sezgisel_yontem(20))