n = int(input())
if (n<0):
    print("Error array size must positive number")
    sys.exit(1)
a = []
for _ in range(n):
    k = int(input())
    a.append(k)
print(a)
min = min(a)
max = max(a)
length = max - min + 1
b = [0] * length
x = 0
while x < length:
    b[x] = 0
    x += 1
z = 0
while z < len(a):
    b[a[z] - min] =  1
    z += 1
x = 0
z = 0
while z < length:
    if(b[z]==1):
        g = z + min
        a[x] -= g
        g += a[x]
        a[x] = g - a[x]
        x += 1
    z += 1
length = 0
print(a)
