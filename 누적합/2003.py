n,m = map(int,input().split())
list1 = list(map(int,input().split()))

l,r = 0,1
cnt = 0
result = list1[0]
while True:
    if result <m:
        if r<n:
            result += list1[r]
            r+=1
        else:
            break
    else:
        if result == m:
            cnt +=1
        result -= list1[l]
        l += 1
    
print(cnt)