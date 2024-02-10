n = int(input())
cnt = 0
result = 0
for x in range(1,n):
    cnt +=1
    result += x
    if n-result < x+1:
        break
print(cnt if cnt != 0 else 1)
