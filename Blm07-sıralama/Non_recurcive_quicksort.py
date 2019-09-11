import sys
n = int(input())
if (n<0):
    print("Error array size must positive number")
    sys.exit(1)
b = []
print("Enter numbers")
for _ in range(n):
    x = float(input())
    b.append(x)
print(b)
altdizi = 0
a = [[],[]]
a[altdizi].append(0)
a[altdizi].append(len(b) - 1)
kontrol = 1
while kontrol == 1 or altdizi >= 0:
    kontrol = 0
    alt = a[altdizi][0]
    üst = a[altdizi][1]
    altdizi -= 1
    kontrol2 = 1
    while kontrol2 == 1 or alt < üst:
        kontrol2 = 0
        alts = alt
        üsts = üst
        pivot = b[int((alt + üst)/2)]
        kontrol3 = 1
        while kontrol3 == 1 or alts <= üsts:
            kontrol3 = 0
            while b[alts] < pivot:
                alts += 1
            while b[üsts] > pivot:
                üsts -= 1
            if(alts <= üsts):
                if(alts != üsts):
                   b[üsts],b[alts] = b[alts],b[üsts]
                alts += 1
                üsts -= 1
        if(alts <üst):
            altdizi += 1
            a[altdizi][0] = alts
            a[altdizi][1] = üst
        üst = üsts
print(b)
