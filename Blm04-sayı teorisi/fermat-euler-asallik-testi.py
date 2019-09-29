#fermat_euler
import math
def fermat_euler (a):
    b= pow(2,a-1)-1
    if( b % a == 0):
        print(a, "asaldır")
        return True
    else:
        print(a, "asal değildir")
        return False

a=int(input("Bir sayı giriniz : "))
fermat_euler(a)