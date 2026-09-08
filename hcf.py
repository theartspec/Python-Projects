#to find the hcf of two numbers
a,b=map(int,input("Enter two numbers: ").split())
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        hcf=i
print("HCF of two numbers is:",hcf)