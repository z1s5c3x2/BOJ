import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
m,n = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def checkmin(_y,_x):
    if _x == n-1 and _y == m-1:
        return 1
    if dp[_y][_x] != -1:
        return dp[_y][_x]
    dp[_y][_x] = 0
    for my,mx in zip(dy,dx):
        pos = [_y+my,_x+mx]
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= m or pos[1] >= n:
            continue
        elif lst[_y][_x] > lst[pos[0]][pos[1]]:
            dp[_y][_x] += checkmin(pos[0],pos[1])
    return dp[_y][_x]
print(checkmin(0,0))