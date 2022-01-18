#WAP to input any 3 digit number and check whether it is Palindrome number or not.

n=int(input("enter a three digit number:"))
a=str(n)
if a[2]==a[0]:
 print(f"{n} is palindrome ")
else:
 print(f"{n} is not palindrome ")
    
 