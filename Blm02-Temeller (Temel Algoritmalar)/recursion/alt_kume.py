def yaz(basamak,hafiza):
    if(basamak==eleman_sayisi):
        for i in range(eleman_sayisi):
            if(hafiza[i]!=0):
                print(" ",(i+1))
        print("\n")
        return 0
    hafiza[basamak]=0
    yaz(basamak+1,hafiza)
    hafiza[basamak]=1
    yaz(basamak+1,hafiza)

eleman_sayisi = 3
hafiza = list(range(eleman_sayisi))
yaz(0,hafiza)
