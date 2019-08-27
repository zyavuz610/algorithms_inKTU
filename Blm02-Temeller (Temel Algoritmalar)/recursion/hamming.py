
# Hamming sayıları, 2,3 ve 5’ten başka diğer asal bölene sahip olmayan dizilerdir. Örnek verecek olursak hamming dizisi şöyledir.

# İlk 60 Hamming Sayısı: 2 3 4 5 6 8 9 10 12 15 16 18 20 24 25 27 30 32 36 40 45 48 50 54 60… şeklinde gider.


def ishamming(sayi):
    if(sayi==1):
        return 1
    elif(sayi % 2== 0):
        return ishamming(sayi/2)
    elif (sayi % 3== 0):
        return ishamming(sayi/3)
    elif (sayi % 5 == 0):
        return ishamming(sayi/5)
    else:
        return 0

def hamming(sayi):
    if(sayi==1):
        return 1
    hamming(sayi-1)
    if(ishamming(sayi)):
        print(sayi)

hamming(20)
