#bear and bigbrother problem codeforces
a,b=map(int,input().split())
count=0
while a<=b:
    a=a*3
    b=b*2
    if a>b:
        count+=1
        break
print(count)
