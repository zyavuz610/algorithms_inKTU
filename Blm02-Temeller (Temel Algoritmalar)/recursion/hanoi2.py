def TowerOfHanoi(n , from_, to_, aux_): 
    if n == 1: 
        print("Disk 1",from_,"dan",to_,"ya taşındı")
        return
    TowerOfHanoi(n-1, from_, aux_, to_) 
    print("Disk",n,from_,"dan",to_,"ya taşındı") 
    TowerOfHanoi(n-1, aux_, to_, from_) 
          
 
n = 7
TowerOfHanoi(n, "A","B", "C")  
# A, C, B kuleleri var 
