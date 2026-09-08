#prime or not prime (method 2)
n=int(input("Enter a number: "))
flag=0
for i in range(2,(n//2)+1): #need not go till the end pf teh number, we only we need to go till half of the number, for eg n=25
    if n%i==0:  # Check whether the number is divisible by i.
        flag=1
        break
    
if flag==1:
    print("Not a prime number")
else:
    print("Prime number")