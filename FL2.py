#ask user to input any number and print its factorial
from math import factorial


n1=int(input("n1="))
fact=1

for i in range(0,n1,1):
    fact=fact*(n1-i)
    
    
print("factorial of %d is %d"%(n1,fact))