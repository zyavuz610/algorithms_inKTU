count=0
def isDiffDigit(num):
    lst = list(str(num))
    n = len(lst)
    for i in range(n):
        lst2 = lst[i + 1:n]
        if lst[i] in lst2:
            return False
    return True


# a=random.randint(1000000000,9999999999)
#3 basamaklı için
"""for i in range(100, 1000):
        b = [int(x) for x in str(i)]
        if isDiffDigit(i) == True:
            if b[1]%2==0:
                if (b[0]+b[1]+b[2])%3==0:
                    count+=1
                    print(b)
                    """

#5 basamkalı için
"""for i in range(10000, 100000):
        b = [int(x) for x in str(i)]
        if isDiffDigit(i) == True:
            if b[4]==5:
                if b[1]!=0 and b[2]!=0 and b[3]!=0 and b[4]!=0:
                    if b[1]%2==0 and b[3]%2==0:
                        if (b[0]+b[1]+b[2])%3==0:
                            if (b[2]*10 + b[3])%4==0:
                                count+=1
                                print(b)"""



for i in range(1000000000, 10000000000):
    a = i
    if a % 10 == 0:
        b = [int(x) for x in str(a)]
        if isDiffDigit(i) == True:
            if b[1] != 0 and b[2] != 0 and b[3] != 0 and b[4] != 0 :

                if b[5] != 0 and b[6] != 0 and b[7] != 0 and b[8] != 0:

                    if (b[0] % 2) != 0 and (b[1] % 2) == 0 and (b[2] % 2)!= 0 and (b[3] % 2) == 0:

                        if b[6] % 2 != 0 and b[5] % 2 == 0 and b[7] % 2 == 0 and b[4] == 5 and b[8] % 2 != 0 and b[9]==0:

                            if (b[1] == 4 or b[1] == 8) and (b[3] == 2 or b[3] == 6) and (b[5] == 4 or b[5] == 8):

                                if b[7] == 2 or b[7] == 6:

                                    if (b[0] + b[1] + b[2]) % 3 == 0 and (b[3]+b[4]+b[5])%3==0 and (b[6]+b[7]+b[8])%3==0:
                                        print(b)


#print(count)
# # 3816547290