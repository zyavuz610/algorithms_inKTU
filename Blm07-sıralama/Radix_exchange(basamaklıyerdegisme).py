# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk, Emre Kardal, Ömer Melek, Ömer Çifte

import sys
import math
def getradix(number,radix):
    return (int(number)>>int(radix))&0x01
def exchange(alt,üst,basamak,b):
    if(üst > alt and basamak >= 0):
        alts=alt
        üsts=üst
        kontrol2 = 1
        while kontrol2== 1 or alts < üsts:
           kontrol2 = 0
           while getradix(b[alts],basamak)==0.0 and alts <üsts:
               alts+=1
           while getradix(b[üsts],basamak)==1.0 and alts <üsts:
               üsts-=1
           b[alts],b[üsts] = b[üsts],b[alts]
        if(getradix(b[üst],basamak)==0.0):
            üsts+=1
        exchange(alt, üsts - 1, basamak - 1, b)
        exchange(alts, üst, basamak - 1, b)
def radixexchangesort(maxdd,b):
    max = maxdd
    exchange(0,len(b)-1,math.log(2,max)+1,b)
print("Enter the length of the array")
n = int(input())
if (n<0):
    print("Error array size must positive number")
    sys.exit(1)
b = []
print("Enter numbers")
for _ in range(n):
    x = float(input())
    b.append(x)
print(b)
#maxdd dizinin uzunlugudur.
maxdd = len(b)
radixexchangesort(maxdd,b)
print(b)
