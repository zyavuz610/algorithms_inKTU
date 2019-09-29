# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://www.youtube.com/watch?v=4GC45mDkBeQ
#gizem
#a^k mod n algoritması
a = 5
k = 596
n = 1234
print(a, "^", k, "mod", n)
b = 1
if k == 0:
    print(b)
k = list((bin(int(k))))
del k[0]
del k[0]
print(k)
A = a
if k[9] == "1":
    b = a
    print(b)
for i in range(1, len(k)):
    print(A, "^2 mod 1234 =",end="")
    A = (A * A) % n
    print(" ",A)
    if k[9 - i] == "1":
        b = ((A * b) % n)
print("işlemin sonucu",b)