import sys
input = sys.stdin.readline
n = int(input())
ilist = list(map(int, input().split()))
lis = [ilist[0]]

def bis(l,r,t):
    while l<r:
        mid = (l+r)//2
        if lis[mid] < t:
            l = mid+1
        else:
            r = mid
    return r

for x in range(1,n):
    if lis[-1] < ilist[x]:
        lis.append(ilist[x])
    else:
        idx = bis(0,len(lis),ilist[x])
        lis[idx] = ilist[x]
print(len(lis))
