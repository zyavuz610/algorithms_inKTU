import sys
import matplotlib.pyplot as plt
import numpy as np
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
arr = []
q = 3.1415929
a = 60000
eb = 2
if(int(q*10000000)%5==0):
    print("the last number should not be 5")
    sys.exit(1)
elif(int(q*10000000)%2==0):
    print("the last number should not be double. ")
    sys.exit(1)
else:
    if(a>=1):
        c = 0
        while(c < a):
            q = q*147
            q = q % 1
            c+=1
            print("%1.7f"%(q))
            arr.append(int(q*1000000 % eb))
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