from collections import deque

n,m = map(int,input().split())
list1 = deque(map(int,input().split()))
stk = []
cnt = 0

def fe(_list,_t):
    try:
        return _list.index(_t)
    except ValueError:
        return 999

while len(stk) < n and list1:
    x = list1[0]
    if x not in stk:
        stk.append(x)
    list1.popleft()

while list1:
    x = list1[0]
    if len(stk) < n:
        stk.append(x)
    elif x not in stk:         
        stk.remove(max(stk,key= lambda x: fe(list1,x)))
        stk.append(x)
        cnt += 1
        
    list1.popleft()

print(cnt)
