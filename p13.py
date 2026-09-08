#Palindrome
n=int(input("Enter a number: "))
temp=n
rev=0
while n:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==temp:
    print("Palindrome")
else:
    print("Not palindrome")