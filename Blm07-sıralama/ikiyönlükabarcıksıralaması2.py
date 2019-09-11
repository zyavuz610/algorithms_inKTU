# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk, Emre Kardal, Ömer Melek, Ömer Çifte

import sys
h = int(input())
if (h < 0):
    print("Error array size must positive number")
    sys.exit(1)
b = []
for _ in range(h):
    x = float(input())
    b.append(x)
print(b)
n = int(len(b)/2)
while(n > 0):
    m = n
    while(m > 0):
        i = 0
        while(i < len(b) - m ):
            if(b[i] > b[i + m]):
                b[i + m] -= b[i]
                b[i] += b[i + m]
                b[i + m] = b[i] - b[i + m]
            i+=1
        m = int(m/2)
    n = int(n / 2)
kontrol = 1
while(kontrol == 1):
    kontrol = 0
    j = 0
    while (j < len(b) - 1):
        if (b[j] > b[j + 1]):
            b[j + 1] -= b[j]
            b[j] += b[j + 1]
            b[j + 1] = b[j] - b[j + 1]
            kontrol = 1
        j+=1
print(b)
