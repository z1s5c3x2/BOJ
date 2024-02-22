import sys
input = sys.stdin.readline

for _ in range(int(input())):
    list1 = sorted( [list(map(int,input().split())) for _ in range(int(input()))], key= lambda x:x[0])
    mx = 0
    cnt = 1
    for x in range(1,len(list1)):
        if list1[x][1] < list1[mx][1]:
            cnt +=1
            mx = x        
    print(cnt)