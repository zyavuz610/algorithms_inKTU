# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk, Emre Kardal, Ömer Melek, Ömer Çifte

import sys
n = int(input())
if (n<0):
    print("Error array size must positive number")
    sys.exit(1)
b = []
for _ in range(n):
    x = float(input())
    b.append(x)
print(b)
i=0
while i < int((len(b) / 2) + 1):
    j = 0
    while j + 1 < len(b):
        if(b[j]>b[j + 1]):
            b[j + 1] -= b[j]
            b[j] += b[j + 1]
            b[j + 1] = b[j] - b[j + 1]
        j += 2
    j = 1
    while j + 1 < len(b):
        if (b[j] > b[j + 1]):
            b[j + 1] -= b[j]
            b[j] += b[j + 1]
            b[j + 1] = b[j] - b[j + 1]
        j += 2
    i += 1
print(b)
