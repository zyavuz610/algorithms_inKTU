ilkdeger , ikincideger = 1,1  #fibonacci ilk 2 indis değeri 1 olduğu için 1 ataması yaptık.
sayi = int(input("Hesaplamak istediğiniz sayıyı yazınız : "))
print(ilkdeger)
print(ikincideger)

i=2     # İlk 2 indisi yazdırdığımız için artık 3. indis değerinden itibaren yazdırıyoruz.
while i<=sayi:
 ilkdeger , ikincideger = ikincideger , ilkdeger + ikincideger
 print(ikincideger)
 i=i+1  # i+=1 şeklinde de yazılabilir.
