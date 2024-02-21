n = int(input())
answer = n
cnt = 0
while True:
    if answer == n and cnt > 0:
        print(cnt)
        break
    lastn = str(n)[-1]
    n = sum(map(int,str(n if n <10 else n*10).strip()))
    n = int(lastn+str(n)[-1])
    cnt +=1
