import math
import matplotlib.pyplot as plt
import numpy as np
import time
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
a = math.pi
z = 60000
h = 2
k = 6
b = 0
if(z > 0):
    g = 0
    while(g < z):
        a = (a * time.time()%1001) + time.time()%97
        a = (a % k) + 1
        b += int(a)
        g += 1
        print(a)
        arr.append(int(a*100000000000) % h)
    print("toplam puan")
    print(b)
elif(z <= 0):
    print("zar atma sayısı 1 ve ya daha büyük olmalıdır")
z = np.zeros(h)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(h)
plt.bar(x_pos,z)
plt.show()