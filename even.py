#Niven number
# a number is said to be Niven number if the sum of the digits divides the number
n=int(input("Enter a number: "))
t=n
sum=0
while n:
    digit=t%10
    sum+=digit
    n=n//10
if t%sum==0:
    print("Niven number")
else:
    print("Not Niven number")