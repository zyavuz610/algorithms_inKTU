# Youtube : https://youtu.be/gJf1uBUuy3Q

import sys
import matplotlib.pyplot as plt
import numpy as np
import time
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
K = 10000000
q = time.time()%10
print(q)
a = 60000
eb = 2
if(int(q*K)%5==0 and int(q*K)%2==0):
    q+=1
else:
    if(a>=1):
        c = 0
        while(c < a):
            q = q*147
            q = q % 1
            c+=1
            #print("%1.7f"%(q))
            arr.append(int(q*K % eb))
    else:
        print("the number should  be positive number. ")
print("sayılar: \n")
print(arr)
z = np.zeros(eb)
for i in arr:
    z[i] = z[i] + 1
print(z)
x_pos = np.arange(eb)
plt.bar(x_pos,z)
plt.show()
