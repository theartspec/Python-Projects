#codeforces 466a
# n = total number of days of travel, m = no. of days you can travel using metro card. 
# a = cost of normal ticket, b = cost of metro card
n,m,a,b=map(int,input().split()) #taking user inputs
if m*a<b: #if the cost of m tickets with normal price is less than metro card then he will take a normal ticket
    print(n*a)
elif n%m==0: #if the number of days is divisible by m then he will take metro card
    print((n//m)*b)
else:
    print((n//m)*b+ min(b,(n%m)*a)) #if the number of days is not divisible by m then he will take metro card for n//m days and for remaining days he will take normal ticket or metro card whichever is cheaper
    