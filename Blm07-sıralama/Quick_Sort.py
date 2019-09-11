import sys
def hs(b,alt,üst):
    alts = alt
    üsts = üst
    pivot = b[int((alt+üst)/2)]
    kontrol3 = 1
    while kontrol3 == 1 or alts <= üsts:
        kontrol3 = 0
        while b[üsts] > pivot:
            üsts -= 1
        while b[alts] < pivot:
            alts += 1
        if(alts <= üsts):
            if(alts != üsts):
                b[üsts],b[alts] = b[alts],b[üsts]
            üsts-=1
            alts+=1
    if(alt<üsts):
        hs(b,alt,üsts)
    if(üst>alts):
        hs(b,alts,üst)
print("Enter the length of the array")
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
hs(b,0,len(b)-1)
print(b)
