#7ye bölünme kuralı B algoritması
#a=4259
a=int(input("sayiyi giriniz"))
for i in range(1,100):
    b=a%10
    c=a//10
    a=c*3+ b
    if a//10==0:
        #print(a)
        break

if a%7!=0:
    print("girilen sayı 7 ile tam bölünemez")
else:
    print("sayınız 7nin katıdır")