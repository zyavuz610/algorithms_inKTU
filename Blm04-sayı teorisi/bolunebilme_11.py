# 11'e bölünme kuralı
a=12345678901234567900
#a=input("bir sayi giriniz")
for i in range(0,len(str(a))):
    b = a % 10 #son rakamının bulunuşu
    a = a // 10 #son rakam atıldıktan sonra
    a = a - b
    print(a)
    if len(str(a))==2 or a==11:
        break

if a==11:
    print("sayiniz 11e tam bölünmektedir")
else:
     print("sayınız 11in tam katı değildir")