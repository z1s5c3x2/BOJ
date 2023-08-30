import sys
input = sys.stdin.readline

n,m = map(int,input().split())

applelst = [list(map(int,input().split())) for _ in range(m)]
movecnt = int(input())
movelst = []
snklst = [[1,1]]
for _ in range(movecnt):
    _str = input().split()
    movelst.append([int(_str[0]),_str[1]])
cnt = 0
nowvec = [1,1,90]
while True:
    cnt +=1
    if nowvec[2] == 0: # up
        nowvec[0] -=1
    elif nowvec[2] == 90: # right
        nowvec[1] +=1
    elif nowvec[2] == 180: # down
        nowvec[0] +=1
    elif nowvec[2] == 270: # left
        nowvec[1] -=1

    for x in range(1,len(snklst)):
        if nowvec[0] == snklst[x][0] and nowvec[1] == snklst[x][1]:
            print(cnt)
            exit()

    for x in range(len(snklst)-1,0,-1):
        snklst[x] = list(snklst[x-1])
    snklst[0] = list([nowvec[0],nowvec[1]])

    if len(movelst) > 0 and  movelst[0][0] == cnt:
        if movelst[0][1] == 'D': # right
            nowvec[2] += 90
        else: # left
            nowvec[2] -= 90

        if nowvec[2] > 270:
            nowvec[2] = 0
        elif nowvec[2] < 0:
            nowvec[2] = 270
        movelst.pop(0)

    for x in range(0,len(applelst)):
        if applelst[x][0] == nowvec[0] and applelst[x][1] == nowvec[1]: # getapple
            _tmp = list(snklst[-1])
            if nowvec[2] == 0: # up
                _tmp[0] +=1
            elif nowvec[2] == 90: # right
                _tmp[1] -=1
            elif nowvec[2] == 180: # down
                _tmp[0] -=1
            elif nowvec[2] == 270: # left
                _tmp[1] +=1

            snklst.append(_tmp)
            applelst.pop(x)
            break

    if nowvec[0] < 1 or nowvec[0] > n or nowvec[1] < 1 or nowvec[1] > n:
        print(cnt)
        break