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

# a=int(input("Ebob'u alınacak büyük sayısı giriniz : "))
# b=int(input("Ebob'u alınacak küçük sayısı giriniz : "))
a,b = 396,120
print("EBOB(",a,",",b,") =",Euclid(a,b))
