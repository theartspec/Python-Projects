#Count the no. of digits a number
n=int(input("Enter a number: "))
count=0
while n:
    digit=n%10
    count+=1
    n=n//10
print("The number of digits",count)