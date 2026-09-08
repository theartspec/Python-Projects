#Sum of a 5 digit number
n=int(input("Enter a 5 digit number: "))
temp=n
count=0
    while temp:
        c+=1
        t=t//10
sum=0
if count==5:
    while n:
        digit=n%10
        sum=sum+digit
        n=n//10
    print("Sum of digits:", sum)
else:
    print("Enter a valid 5 digit number")
