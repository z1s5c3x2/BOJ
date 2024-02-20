list1 = sorted([list(map(int,input().split())) for _ in range(int(input()))],key= lambda x: (x[1],x[0]))

answer = 0
now = 0

for x,y in list1:
    if now <= x:
        answer +=1
        now = y
        
print(answer)