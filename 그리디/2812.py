n,m = map(int,input().split())
str1 = input()
stk = []

for x in str1:
    while len(stk)> 0 and m > 0 and stk[-1] <x:
        stk.pop()
        m-=1
    stk.append(x)

for _ in range(m):
    stk.pop()
print(*stk,sep='')