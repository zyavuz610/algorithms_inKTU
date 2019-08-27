def UsAlma (taban,us):
    if(us==0):
        return 1
    else :
        return taban*UsAlma(taban,us-1)
