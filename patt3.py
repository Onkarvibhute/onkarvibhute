'''
print following patterns for n times
when n=5
A B C D E
a b c d e
A B C D E
a b c d e
A B C D E
'''
n=int(input("n="))
i=j=count=0

while(n>=i):
    while(n>=j):
        if(i%2==0):
            z=65
            while(n>=count):
                print("%c" %(z), end=" ")
                z+=1
                count+=1
        if(i%2!=0):
            z=97
            while(n>=count):
                print("%c" %(z), end=" " )
                z+=1
                count+=1
        j+=1
        
    i+=1
    count=j=0
    print("\n")   
         
                   