#Count the number odd numbers in a number
n=int(input("Enter a number: "))
count=0
while n:
    digit=n%10
    if digit%2!=0:
        count+=1
    n=n//10
print("no. of odd digits in a number",count)