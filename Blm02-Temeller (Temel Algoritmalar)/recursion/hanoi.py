def hanoi(n  , x, y, z):
  if(n==1):
    z.append(x.pop())
  else:
    hanoi(n-1,x ,z ,y)
    hanoi(1  ,x ,y ,z)
    hanoi(n-1 ,y ,x ,z)
  print("Çubuk1 : ",Cubuk1)
  print("Çubuk2 : ",Cubuk2)
  print("Çubuk3 : ",Cubuk3)
  print("******************")

n= int(input("Disk sayisi N : "))
Cubuk1=[]
Cubuk2=[]
Cubuk3=[]

for i in range(n,0,-1):
    Cubuk1.append(i)

print("Çubuk1 : ",Cubuk1)
print("Çubuk2 : ",Cubuk2)
print("Çubuk3 : ",Cubuk3)
print("******************")

hanoi(n,Cubuk1,Cubuk2,Cubuk3)
