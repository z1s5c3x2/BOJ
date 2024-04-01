a=int(input())
b=int(input())
A1= a//100
ans=A1*100
while ans%b!=0:
    ans +=1
print(str(ans)[-2:])