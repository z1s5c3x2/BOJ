import sys

input = sys.stdin.readline
n,money,startprice,g = map(int,input().split())
nboardsize = 4*n-8
goldkey = [input().rstrip() for _ in range(g)]

Specialplacd = [input().strip() for _ in range(nboardsize)]
mapsize = 4*n-4
board = ['']+['' for _ in range(mapsize)]
chkbuy = [True for _ in range(len(board))]

for x in range(1,len(board)):
    if x == 1:
        board[x] = 'S1'
    elif n == x:
        board[x] = 'S2'
    elif 2*n-1 == x:
        board[x] = 'S3'
    elif 3*n-2 == x:
        board[x] = 'S4'
    else:
        board[x] = Specialplacd.pop(0)
        if board[x] == 'G':
            chkbuy[x] = True
        elif board[x].split()[0] == 'L':
            chkbuy[x] = False

now = 1
savs3 = 0
bank = 0
gidx = 0
dicelst =[list(map(int,input().split())) for _ in range(int(input()))]
 

isgetdice = True
def getdice():
    if len(dicelst) == 0:
        return -1
    d1,d2 = dicelst.pop(0)

    return [d1+d2,d1==d2]

def island():
    global isgetdice
    isgetdice =True
    for _ in range(3):
        wer = getdice()
        
        if wer == -1:
            break
        elif wer[1]:
            break

prres = False
while True:

    if isgetdice:
        wer = getdice()
        if wer == -1:
            break
        now +=wer[0]

    if now > mapsize:
        while now > mapsize:
            money += startprice
            now -= mapsize
    if now ==0:
        now +=1    
    
    
    nowinfo = board[now].split()
    
    if nowinfo[0] =='L' and not chkbuy[now] and int(nowinfo[1]) <= money:
        money -= int(nowinfo[1])
        chkbuy[now] = True
    elif nowinfo[0] == 'G':

        nowinfo.append(goldkey[gidx].split()[0])
        nowinfo.append(goldkey[gidx].split()[1])
        gidx +=1
        if gidx >= len(goldkey):
            gidx = 0
        if nowinfo[1] == '1':
            bank -= int(nowinfo[2])
            money += int(nowinfo[2])
        elif nowinfo[1] == '2':
            bsav = int(nowinfo[2])
            if bsav > money:
                print('LOSE')
                prres = True
                break
            bank += bsav
            money -= bsav
        elif nowinfo[1] == '3':
            
            s3pr = int(nowinfo[2])
            if s3pr > money:
                print('LOSE')
                prres = True
                break
            savs3 += s3pr
            money -= s3pr
        elif nowinfo[1] == '4':
            now += int(nowinfo[2])
            isgetdice = False
            continue
            
    else:
        if nowinfo[0] == 'S2':
            island()
        elif nowinfo[0] == 'S3':
            money += savs3
            savs3 = 0
        elif nowinfo[0] == 'S4':
            money += startprice
            now = 1
            isgetdice = False
            continue
    isgetdice = True

if not prres:
    if False in chkbuy:
        print('LOSE')
    else:
        print('WIN')


