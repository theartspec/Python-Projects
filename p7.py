#prime and not prime (method 2)
n=int(input("Enter a number: "))
flag=0
for i in range(2,n):
    if n%i==0:  # Check whether the number is divisible by i.
        flag=1
        break
    
if flag==1:
    print("Not a prime number")
else:
    print("Prime number")