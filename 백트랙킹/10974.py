N = int(input())

def bt(list1):
    global N
    if len(list1) == N:
        print(*list1)
        return
    for x in range(1,N+1):
        if x not in list1:
            list1.append(x)
            bt(list1)
            list1.pop()
            
    

bt([])