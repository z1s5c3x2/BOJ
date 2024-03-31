n = int(input())
m = int(input())
answer = 0
for _ in range(m):
    a,b = map(int,input().split())
    answer += a*b
print("Yes" if answer == n else "No")