'''
print following pattern n times
when n=5
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
'''

i=1 
j=1 
k=1 
L=5
n=int(input("n="))
while(n>=i):
    while(n>=j):
        if(i%2!=0):
            while(n>=k):
                print("%d" %(k), end=" ")
                k+=1
                
        if(i%2==0):
            while(L>0):
                print("%d" %(L), end=" " )  
                
                L+=-1
        j+=1
    print("\n")
    i+=1
    j=k=1
    L=5
    
       
              