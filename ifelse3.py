#WAP to input any 3 digit number and check weather it is an Armstrong number or not?
#e.g.  no=153   then 1*1*1 + 5*5*5 + 3*3*3  => 153
n=int(input("enter a three digit  number:"))
temp=n
sum=0

while n>0:
   a=(n%10)
   sum=sum+(a*a*a) 
   n=n//10
if(sum==temp):
       print(f"{temp} is armstrong number")
else:
       print(f"{temp} is not armstrong number")
       