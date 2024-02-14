ansList = ''
for _ in range(int(input())):
    n = int(input())

    list1 = [ list(map(int,input().split())) for _ in range(2)]
    if n > 1:
        list1[0][1] += list1[1][0]
        list1[1][1] += list1[0][0]

    for x in range(2,n):
        list1[0][x] += max(list1[1][x-1],list1[1][x-2])
        list1[1][x] += max(list1[0][x-1],list1[0][x-2])

    ansList += '{}\n'.format(max(list1[0][n-1],list1[1][n-1]))

print(ansList)