#Reverse of a number
n=int(input("Enter a number: "))
rev=0
while n:                # runs until n is not equal to zero
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reverse of the number is",rev)
