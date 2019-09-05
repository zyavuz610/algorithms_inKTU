# engel rasgele sayı üretme algoritması
# Youtube: https://youtu.be/nvH1LIxpDOA
import math
import time
import matplotlib.pyplot as plt
import numpy as np
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
h = 2
K = 10000000
a = time.time() % 1
print(a)
z = 60000
if(z > 0 and a < 1 and a > 0):
    g = 0
    while(g < z):
        a = pow((a + math.pi),8)
        a = a % 1
        #print(a)
        arr.append(int(a*K % h))
        g+=1
elif (z <= 0):
    print("Üretilecek sayı 1 ve ya daha büyük olmalıdır")
else:
    print("çekirdek değer 0 ile 1 arası olmalıdır")
z = np.zeros(h)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(h)
plt.bar(x_pos,z)
plt.show()
