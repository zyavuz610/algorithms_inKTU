
def Toplam(sayi):
    if (sayi==1):
        return 1
    else :
        return sayi + Toplam(sayi-1)


print(Toplam(15))
