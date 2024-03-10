a,b,c = map(int,input().split())
answer =0 
if a==b and b==c:
    answer =a*1000 +10000
elif a==b:
    answer = a*100 + 1000
elif b==c:
    answer = c*100 + 1000
elif a == c:
    answer = a*100 + 1000
else:
    answer = max([a,b,c]) * 100

print(answer)
