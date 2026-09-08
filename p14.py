#Sum of a 5 digit number
n=int(input("Enter a 5 digit number: "))
if 10000<=n<=99999:
    sum=0
    while n:
        digit=n%10
        sum+=digit
        n=n//10
    print("Sum of digits:", sum)
else:
    print("Enter a valid 5 digit number")