t = input()
p = input()
tmx = len(t)
pmx = len(p)
pi = [0]*pmx

l = 0 
for x in range(1,pmx):
    while l > 0 and p[x] != p[l]:
        l = pi[l-1]
    if p[x] == p[l]:
        l +=1
        pi[x] = l

answer = []
cnt = 0
l = 0
for x in range(tmx):
    while l > 0 and t[x] != p[l]:
        l = pi[l-1]
    if t[x] == p[l]:
        if l == pmx-1:
            cnt +=1
            answer.append(x-pmx+2)
            l = pi[l]
        else:
            l+=1

print(cnt)
print(*answer)