# wap to print frist n numbers whose frist and last digit addition not grater than 5
n=int(input("enter the value grater than 50:"))
sum1=0
sum2=0
num=0

a=str(n)
b=len(a)
while(n>50 and num<=n):
 num+=1
 if(num<=9):
    sum1=num 
    if(sum1<5):
      print(f"{num}")
 else:
    sum2=num//(10**(b-1))+num%10
    if(sum2<5):
      print(f"{num}")