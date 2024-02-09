dp = [0,1,2,3]
n = int(input())
if n <= 3:
    print(n)
else:
    for x in range(3,n):
        dp.append( (dp[x-1]+dp[x])%15746 )
    print(dp[n])