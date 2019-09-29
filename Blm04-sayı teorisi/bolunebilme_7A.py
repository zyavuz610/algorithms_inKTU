#7ye bölünme kuralı A algoritması
x = 28950308506
z=0
y = []
for i in range(0, len(str(x))):
    y.append(x%10)
    #y[i] = x % 10
    x = x // 10
print("sayının ters cevrilmiş şekli:", y)
for i in range(0, len(y)):
    if i % 6 == 0:
        z = z + y[i] * 1
    if i % 6 == 1:
        z = z + y[i] * 3
    if i % 6== 2:
        z = z+y[i] * 2
    if i % 6 == 3:
        z = z + y[i] * 6
    if i % 6 == 4:
        z = z+y[i] * 4
    if i % 6 == 5:
        z = z+y[i] * 5


print(z)
if z % 7 == 0:
    print("sayınız 7 ile tam bölünebilmektedir")
else:
    print("sayınız 7nin katı değildir")