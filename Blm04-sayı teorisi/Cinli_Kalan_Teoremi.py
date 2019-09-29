# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://www.youtube.com/watch?v=kAG-HKyR-Qs
#gizem
#çinlilerin kalan teoremi

print("x=1(mod7)")
print("x=2(mod5)")
print("x=5(mod6)")
m = [7, 5, 6]
M = [1, 2, 3]
M0 = 1
for i in range(0, len(m)):
    M0 = M0 * m[i]
print(M0)
for i in range(0, len(m)):
    M[i] = M0 // m[i]
    print(M[i])

print("M1*y1=1(mod7)")
print("M2*y2=2(mod5)")
print("M3*y3=5(mod6)")

x = M[0] % 7
y = M[1] % 5
z = M[2] % 6
print(x, y, z)

for i in range(1, 20):
    if(2*i)%7==1:
        print("y1=",i)
        break


for j in range(1, 20):
    if(2*j)%5==2:
        print("y2=",j)
        break




for k in range(1, 20):
    if(5*k)%6==5:
        print("y3=",k)
        break
X = i * M[0] + j * M[1] + k * M[2]
print("oluşan sayımız=", X)