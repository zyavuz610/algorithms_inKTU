import sys
n = int(input())
if (n<0):
    print("Error array size must positive number")
    sys.exit(1)
arr = []
for _ in range(n):
    x = float(input())
    arr.append(x)
for i in  range(len(arr)):
    t = arr[i]
    j=i
    while j > 0 and arr[j-1] > t :
        arr[j] = arr[j-1]
        j-=1
    arr[j] = t
print(arr)