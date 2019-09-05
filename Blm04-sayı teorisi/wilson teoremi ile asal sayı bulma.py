#Asal sayılar: Wilson Teoremi

def asal_sayilar(a):
    dizi = []
    for i in range(2,a):
        asalmi=True
        for j in range(2,i):
            if i % j == 0:
                asalmi=False
                break
        if asalmi == True:
            dizi.append(i)
    return dizi

a = 100 # int(input("1' den büyük üst sınır giriniz : "))
print("1 -", a, "aralığındaki asal sayılar :")
print(asal_sayilar(a))
