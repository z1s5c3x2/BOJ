import sys
input = sys.stdin.readline
n = int(input())
cntdict = dict()
ilist = list(map(int, input().split()))
stk2 = []
if n == 1:
    print(-1)
else:
    stk = []
    for idx , num in enumerate(ilist):
        if num in cntdict:
            cntdict[num] +=1
        else:
            cntdict[num] = 1
    for idx , num in enumerate(ilist):  
        while len(stk) > 0 and cntdict[ilist[stk[-1]]] < cntdict[num]:
            ilist[stk[-1]] = num
            stk.pop()
        stk.append(idx)
    for x in stk:
        ilist[x] = -1
    print(' '.join(map(str,ilist )))