#Binary Ebob Algoritması
def Binary_Ebob(a,b):
    g = 1
    while (a%2==0) & (b%2==0):
        a = a // 2
        b = b // 2
        g = 2 * g
    while a!=0:
        while (a%2==0): #a çift olduğu sürece ikiye bölünür
            a=a//2
        while (b%2==0):
            b=b//2
        t= abs(a-b)//2 # b çift olduğu sürece ikiye bölünür
        if a>=b :
            a=t
        else:
            b=t
    return (g*b)

a=int(input("Ebob'u alınacak büyük sayısı giriniz : "))
b=int(input("Ebob'u alınacak küçük sayısı giriniz : "))
print("EBOB(",a,",",b,") =",Binary_Ebob(a,b))