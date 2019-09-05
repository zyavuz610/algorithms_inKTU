# Eratosthenes Eleği

import math

def eratosthenes (a):
    dizi = [x for x in range(a+1)]
    k = int(math.sqrt(a))    
    j = 2
    while dizi[j] <= k:
        if dizi[j] != 0:
            for l in range((j * j), a+1, j):
                dizi[l] = 0
            j = j + 1
        else:
            j = j + 1
    dizi = [x for x in dizi if x!=0]
    return dizi[1:]

a = 100 # int(input("1' den büyük üst sınır giriniz : "))

print("1 - ",a, "arasındaki asal sayılar : ",eratosthenes(a))
