import math
import matplotlib.pyplot as plt
import numpy as np
import time
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
a = time.time()
z = 60000
k = 10000
b = 0
arr = []
if(z > 0):
    g = 0
    while(g < z):
        a = (a * time.time()) + time.time()
        a = a % 65536 + 1
        c = int(((((a / 32768) + 1) / 4) * k) + 1)
        b += c
        g += 1
        arr.append(c)
        print(c)
    print("toplam puan")
    print(b)
elif(z <= 0):
    print("zar atma sayısı 1 ve ya daha büyük olmalıdır")
else:
    print("Zarın yerde durabilmesi için minimum 3 köşesi olmalıdır")
z = np.zeros(k+1)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(k+1)
plt.bar(x_pos,z)
plt.show()