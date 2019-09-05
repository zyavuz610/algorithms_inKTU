# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :


# seren

#Euclid Algoritması
def Euclid(a,b):
  while b != 0:
    x=a
    a=b
      
    b= x - b  
    print(x,a,b)
    if(a<b):
        a,b=b,a
        
    # b = x % b  yazılarak doğrudan sonuca ulaşılabilir
  ebob = a
  return ebob

#Genişletilmiş Euclid Algoritması
def Euclid2 (a,b) :
    if b==0 :
        x=1
        y=0
        return a
        print("ax + by =",a," denklemini sağlayan x ve y sayıları: x = ",x,", y = ",y)

    else:
        x1, x2, y1, y2 = 0, 1, 1, 0
        while b != 0:
            q = a // b
            temp = a
            a = b
            b = temp % b
            x = x2-q*x1
            y= y2 - q*y1
            x2=x1
            x1=x
            y2=y1
            y1=y
            x=x2
            y=y2
            print(q,a,b,x2,x1,y2,y1) # tablo 4.3 için
            # yukarıda ki adımları bu şekilde yazarak da gerçeleyebiliriz:
            #q, b, a = b // a, a, b % a
            #x1, x2 = x2, x1 - q * x2
            #y1, y2 = y2, y1 - q * y2
        print("ax + by =", a, " denklemini sağlayan x ve y sayıları: x = ", x, ", y = ",y )
        return a

# a=int(input("Ebob'u alınacak büyük sayısı giriniz : "))
# b=int(input("Ebob'u alınacak küçük sayısı giriniz : "))
a,b = 4864,3458
print("EBOB(",a,",",b,") =",Euclid2(a,b))
