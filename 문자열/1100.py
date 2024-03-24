list1 = []
for _ in range(8):
    list1.append(input())
answer = 0
for y in range(8):
    for x in range(8):
        if (x+y) % 2==0 and list1[y][x] == 'F':
            answer +=1
print(answer)