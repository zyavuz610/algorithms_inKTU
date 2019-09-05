# Youtube: https://youtu.be/vvqPKSaUq-w

import matplotlib.pyplot as plt
import numpy as np
import time
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
K = 1000000000000000
g = 6
def blum(p,q,t):
    if(p == q or t < 1):
        print("error p = q")
        return 0
    m = p*q
    s = int(time.time()*K) % m
    z = 1
    while(z<=t):
        s = pow(s,2) % m
        arr.append(int(s % g))
        #print(int(s % g))
        z+=1

blum(30000000091,40000000003,60000)
z = np.zeros(g)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(g)
plt.bar(x_pos,z)
plt.show()
