n,m = map(int,input().split())
list1 = [input() for _ in range(n)]
list2 = [input() for _ in range(m)]
answer = sorted(list(set(list1) & set(list2)))
print(len(answer))
for x in range(len(answer)):
    print(answer[x])