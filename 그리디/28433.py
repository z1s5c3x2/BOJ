import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    lst = list(map(int,input().split()))
    sumCount = 0
    ans = 0
    currentSum = 0
    for x in lst:
        if x > 0: #양수
            if currentSum >= 0:
                sumCount +=1
                currentSum = x
            elif currentSum < 0:
                if currentSum + x > 0:
                    sumCount +=2
                    currentSum += x
                else:
                    currentSum = x
                    sumCount +=1
        if x < 0: #음수
            if currentSum >= 0:
                if currentSum + x > 0:
                    currentSum += x
                else:
                    sumCount -=1
                    currentSum =  x
            elif currentSum < 0:
                currentSum += x
    if sumCount > 0:
        print('YES')
    else:
        print('NO')