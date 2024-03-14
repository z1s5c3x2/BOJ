list1 = [int(input()) for _ in range(int(input()))]
answer = 0
for x in range(len(list1)-2,-1,-1):
    if list1[x] >= list1[x+1]:
        now = list1[x] - list1[x+1] +1
        list1[x] = list1[x] - now
        answer += now

print(answer)
        

        