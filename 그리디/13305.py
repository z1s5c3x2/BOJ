n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

now = list2[0]
answer = 0

for x in range(n-1):
    if list2[x] < now:
        now = list2[x]
    answer += now * list1[x]
print(answer)