n = int(input())
str1 = [input() for _ in range(n)]

answer = [0,0]

for x in range(n):
    tmp = ''

    for y in range(n):
        tmp += str1[y][x]


    for s1 in str1[x][:].split('X'):
        if '..' in s1:
            answer[0] += 1

    for s1 in tmp.split('X'):
        if '..' in s1:
            answer[1] +=1
    

print(*answer)


