# Ask user to input n1 and n2. print even numbers between them using for loop
n1=int(input("n1="))
n2=int(input("n2="))
for i in range(n1,n2,1):
    if(i%2==0):
        print("n1=%d"%(i))
    
