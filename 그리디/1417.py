n = int(input())
t = int(input())
list1 = sorted([int(input()) for _ in range(n-1)] , reverse=True)
cnt = 0

if n == 1:
    print(0)

else:

    while list1[0] >= t:
        t += 1
        list1[0] -= 1
        cnt += 1
        list1.sort(reverse=True)

    print(cnt)

1520b1b