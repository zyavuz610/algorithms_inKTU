import random
import matplotlib.pyplot as plt
import numpy as np
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
z = 60000
k = 13
h = 0
while(h < z):
    l = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
    random.shuffle(l)
    a = ((((( l[26] - 1) / 13) + l[27] - 1) / 13 ) + l[28] - 1 ) / 13
    print(a)
    arr.append(int(a*1000000000000) % k)
    h+=1
z = np.zeros(k)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(k)
plt.bar(x_pos,z)
plt.show()
