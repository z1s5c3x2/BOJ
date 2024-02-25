from collections import deque

n,k =  map(int,input().split())
list1 = deque( x for x in range(1,n+1) )
answer = []
while list1:
    for _ in range(k-1):
        list1.append(list1.popleft())
    answer.append(list1.popleft())

print(str(answer).replace("[","<").replace("]",">"))