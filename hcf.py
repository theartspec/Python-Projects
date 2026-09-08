#to find the hcf and lcm of two numbers
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf = i
print ("HCF/GCD = " ,hcf) 
lcm=(a*b)//hcf
print("LCM = ",lcm)
        
