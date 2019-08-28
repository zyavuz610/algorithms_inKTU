def downheap(b,k,n):
    t = b[k - 1]
    while(k <= n/2):
        j = 2*k
        if(j < n and b[j - 1] < b[j]):
            j+=1
        if(t >= b[j - 1]):
            break
        else:
            b[k - 1] = b[j - 1]
            k = j
    b[k - 1] = t
def heapsort(b):
    n = len(b)
    k = int(n/2)
    while(k>0):
        downheap(b,k,n)
        kontrol = 1
        while(kontrol == 1 or n > 1):
            kontrol=0
            b[0] -= b[n - 1]
            b[n - 1] += b[0]
            b[0] = b[n - 1] - b[0]
            n-=1
            downheap(b, 1, n)
        k-=1

n = int(input())
if (n<0):
    print("Error array size must positive number")
    sys.exit(1)
b = []
for _ in range(n):
    x = int(input())
    b.append(x)
print(b)
heapsort(b)
print(b)