import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = list([list(map(int,input().rstrip())) for _ in range(n)])
vislist = [[[0]*2 for _ in range(m)] for _ in range(n)]
vislist[0][0][0] = 1

veclst = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs():
    q = deque([[0,0,0]])
    while q:
        now = q.popleft()
        if now[0] == n-1 and now[1] == m-1:
            return vislist[now[0]][now[1]][now[2]]
        for vec in veclst:
            vy,vx,b = now[0]+vec[0],now[1]+vec[1],now[2]
            if 0<= vy <n and 0<= vx < m:
                if board[vy][vx] == 1 and now[2] == 0:
                    vislist[vy][vx][1] = vislist[now[0]][now[1]][0]+1
                    q.append([vy,vx,1])
                elif board[vy][vx] == 0 and vislist[vy][vx][now[2]] == 0:
                    vislist[vy][vx][now[2]] = vislist[now[0]][now[1]][now[2]] +1
                    q.append([vy,vx,now[2]])
    return -1
print(bfs())
