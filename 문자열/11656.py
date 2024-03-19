str1 = input()
stk = []
for x in range(len(str1)):
    stk.append(str1[x:])

print(*sorted(stk),sep='\n')