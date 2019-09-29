# distribution sort
arr = [6, 2, 4, 3, 1, 3, 4, 3]
maksimum = max(arr) # 6
counter = [0 for i in range(maksimum + 1)]
buffer = [0 for i in range(len(arr))]
print(counter)
for i in arr:
    counter[i] += 1  # counter = [0,1,1,3,2,0,1]
print(counter)
for i in range(1,len(counter)):
    counter[i] += counter[i-1]
print(counter)
for i in reversed(range(0,len(counter)+1)):
    indis = counter[arr[i]]
    buffer[indis-1] = arr[i]
    counter[arr[i]] -= 1
print(counter)
print(buffer)
for i in range(len(buffer)):
    arr[i] = buffer[i]
print(counter)
print(buffer)  # buffer = [-,-,-,-,-,-,-,-]