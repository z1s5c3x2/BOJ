list1 = [ input() for _ in range(int(input()))]
#tmp = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,}
tmp = {}
for x in list1:
    ln = len(x)
    for i,a in enumerate(x):
        if a in tmp:
            tmp[a] += 10**(ln-(i+1))

        else:
            tmp[a] = 10**(ln-(i+1))

#1 Way
#rnk = 9
#ans = 0
#for x in sorted(tmp.items(), key= lambda x: x[1], reverse=True):
#    ans += tmp[x[0]]*rnk
#    rnk -=1
#print(ans)

#2 Way
rnk = 9
for x in sorted(tmp.items(), key= lambda x: x[1], reverse=True):
    for y,z in enumerate(list1):
        list1[y] = z.replace(x[0],str(rnk))
    rnk -=1
print(sum(list(map(int,list1))))