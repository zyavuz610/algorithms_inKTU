1#inplace stable merge sort
dizi = [2,6,0,1,79,3,8,5]
def inplacestablesort(alt,ust):
    mid=(alt+ust)//2
    print(mid)
    inplacestablesort(alt,mid)
    inplacestablesort(mid+1, ust)
    merge(alt,mid,ust,(mid-alt),(ust-mid))
   



def merge(alt,pivot,ust, len1,len2):
    if(len1==0) or len2==0:
        return
    if len1+len2==2:
        if dizi[pivot]<dizi[alt]:
            temp=dizi[alt]
            dizi[alt]=pivot
            pivot=temp
            return
    if len1>len2:
        len11=len1//2
        firstcut=alt+len11
        secondcut=lower(pivot,ust,firstcut)
        len22=secondcut- pivot
    else:
        len22=len2//2
        secondcut=pivot+len22
        firstcut=upper(alt,pivot,secondcut)
        len11=firstcut-alt

    rotate(firstcut,pivot,secondcut)
    newmid = (firstcut+len22)
    merge(alt, firstcut, newmid,len11,len22)
    merge(newmid,secondcut,ust,len1-len11)

def lower(alt,ust,val):
    len=ust-alt
    while len>0:
        half=len//2
        mid=alt+half
        if dizi[mid]<dizi[val]:
            alt=mid+1
            len=len-half-1
        else:
            len=half
    return alt
def upper(alt, ust , val):
    len=ust-alt
    while len>0:
        half = len // 2
        mid = alt + half
        if dizi[mid] > dizi[val]:
            len=half
        else:
            ust=mid+1
            len=len-half-1
        return ust
def reverse (alt , ust ):
    while alt<ust:
       alt=alt+1
       ust=ust-1
       temp=alt
       alt=ust
       ust=temp
def rotate(alt , mid , ust ):
    reverse(alt,mid-1)
    reverse(mid,ust-1)
    reverse(alt,ust-1)

n = len(dizi)
inplacestablesort(0,n-1)
print(dizi)

