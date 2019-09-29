#asallık testi
import math
def asallik_testi (a):
    dizi = []
    b = int(math.sqrt(a))
    for i in range(2, b):
        asalmi = True
        for j in range(2, i):
            if i % j == 0:
                asalmi = False
                break
        if asalmi == True:
            dizi.append(i)
    for i in dizi:
        bolundu = False
        if(a % i == 0):
            bolundu = True
            break
    if bolundu == False :
            print(a,"asal sayidir.")
    else :
            print(a,"asal değildir.")

print(asallik_testi(1001))