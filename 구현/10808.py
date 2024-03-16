list1 = [0]*26
for x in input():
    list1[ord(x)-97] +=1
print(*list1)