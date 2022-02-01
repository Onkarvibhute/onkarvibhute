#wap to input number of minimum seven digit.check that reverse of first three digits are matching to last digit 
n=int(input("enter number:"))#1234567
a=str(n)
b=a[-3:]
c=a[:3]
print(f"{a[-3:-1]}")
print(f"{a[:3]}")
if(b==c):
    print("digits are repeated")
else:
    print("digits are not repeated")
        
    
    
    