import time
import math
import matplotlib.pyplot as plt
import numpy as np
fig_size = [19.2,10.8]
plt.figure(figsize=fig_size)
a = time.time()
a = a * (a- a/159835753)
a = pow(a,0.5)
a = pow(a,2)
z = input()
if(z == 'int'):
    a = a % 1500
    print(int(a))
elif(z == 'double'):
    a = a*math.pi % 357.56365
    print(a)
else:
    print("error")