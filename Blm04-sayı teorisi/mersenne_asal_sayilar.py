# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Gizem Bostan, Seren Öztürk
# Youtube :https://youtu.be/cZCa0kgrcdM
#gizem
#mersenne sayıları
#2^p -1 seklinde çıktı üreten sayılardır burada dikkat edilmesi gereken p değerinin asal olmasıdır.
def fonk(num):
    arr,arr2 = [],[]
    for i in range(1,num):
        if i >1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                x = pow(2, i) - 1
                # print(i,x)
                arr.append(i)
                arr2.append(x)
    return arr,arr2

primes,mersennes = fonk(100)


for i in range(len(primes)):
    print(primes[i],mersennes[i])


print(primes)
print(mersennes,end='\n')