import sys
class Merge:
    def merge(self,alt, üst, b):
        if (alt >= üst):
            return 0
        alts = alt
        üsts = üst
        pivot = int((alts + üsts) / 2)
        self.merge(alts, pivot, b)
        self.merge(pivot + 1, üsts, b)
        sonalts = pivot
        ilküsts = pivot + 1
        while alts <= sonalts and ilküsts <= üsts:
            if (b[alts] < b[ilküsts]):
                alts += 1
            else:
                t = b[ilküsts]
                k = ilküsts - 1
                while k >= alts:
                    b[k + 1] = b[k]
                    k -= 1
                b[alts] = t
                alts += 1
                sonalts += 1
                ilküsts += 1
        return b


print("Enter the length of the array")
n = int(input())
if (n < 0):
    print("Error array size must positive number")
    sys.exit(1)
b = []
print("Enter numbers")
for _ in range(n):
    x = float(input())
    b.append(x)
print(b)
z = Merge()
print(z.merge(0, len(b) - 1, b))
