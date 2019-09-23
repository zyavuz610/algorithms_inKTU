import math
import matplotlib.pyplot as plt
import numpy as np
import time
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
a = time.time()
z = 60000
k = 6
b = 0
arr = []
if(z > 0):
    g = 0
    while(g < z):
        a = (a*25173 + 13849) % 32768
        c = int(((a / 32768)* k) + 1)
        b += c
        g += 1
        arr.append(c)
        #print(c)
    print("toplam puan")
    print(b)
elif(z <= 0):
    print("zar atma sayısı 1 ve ya daha büyük olmalıdır")
z = np.zeros(k+1)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(k+1)
plt.bar(x_pos,z)
plt.show()
