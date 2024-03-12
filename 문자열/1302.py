strdict = {}

for _ in range(int(input())):
    _str = input()
    if _str in strdict:
        strdict[_str] += 1
    else:
        strdict[_str] =1
        
print(sorted(strdict.items(),key= lambda x: (-x[1],x[0]),reverse=True)[-1][0])

