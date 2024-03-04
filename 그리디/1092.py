import math
n = int(input())
list1 = sorted(list(map(int,input().split())))
m = int(input())
list2 = sorted(list(map(int,input().split())))
h = 0
if list2[-1] > list1[-1]:
    print(-1)
else:    
    clist = [0] * len(list1)
    c = 0
    avg = math.ceil(len(list2)/len(list1))
    ln = len(list1)-1
    for x in list2:
        if c == ln:
            clist[c] +=1
        elif clist[c] < avg and list1[c] >= x:
            clist[c] +=1
        else:
            c +=1
            clist[c] +=1
            

    print(clist)