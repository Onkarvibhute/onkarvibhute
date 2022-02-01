'''
print following pattern for n times

when n=5
11 12 13 14 15
11 12 13 14 
11 12 13 
11 12 
11 
'''
from msvcrt import kbhit

n=int(input("n="))
i=j=z=1
k=n
while(n>=i):
    while(k>=j):
        print("%d" %(z), end=" ")
        j+=1
        z+=1
    i+=1
    print("\n")
    j=1
    k-=1
    z=1
    

