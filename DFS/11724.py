import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(s,d):
    
    visited[s] = True
    for x in list1[s]:
        if not visited[x]:
            dfs(x,d+1)

n,m = map(int,input().split())
list1 = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    list1[a].append(b)
    list1[b].append(a)

visited = [False] * (n+1)
cnt = 0

for x in range(1,n+1):
    if not visited[x]:
        if not list1[x]:
            cnt +=1
            visited[x]
        else:
            dfs(x,0)
            cnt +=1
print(cnt)