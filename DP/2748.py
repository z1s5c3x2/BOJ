dp = [0,1]

for x in range(1,int(input())):
    dp.append(dp[x]+dp[x-1])
    
print(dp[-1])
