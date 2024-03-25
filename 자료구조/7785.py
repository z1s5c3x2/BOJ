
dict1 = {}
for _ in range(int(input())):
    n,d= input().split()
    dict1[n] = d=='enter'
answer = []
for x,y in dict1.items():
    if y:
        answer.append(x)
answer.sort(reverse=True)

print(*answer,sep='\n')

