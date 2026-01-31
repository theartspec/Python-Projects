#Simple calculator
def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b==0:
        return "Division not possible"
    return a / b
print ("Simple calculator")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
choice =int(input("Enter your choice (1-4):"))
num1 =int(input("Enter first number:"))
num2 =int(input("Enter second number:"))
if choice ==1:
    print("Result =",add(num1,num2))
elif choice ==2:
    print("Result =",substract(num1,num2))
elif choice ==3:
    print("Result =",multiply(num1,num2))
elif choice ==4:
    print("Result =",divide(num1,num2))
else:
    print("Error: Invalid choice")
