import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip() 
list1 = list()
savlen = len(str2)
checkchr = str2[-1]
for x in str1:
    list1.append(x)
    if  checkchr == list1[-1]:
        if ''.join(list1[len(list1)-savlen:]) == str2:
            for _ in range(savlen):
                list1.pop()

if len(list1) == 0:
    print('FRULA')
else:
    print(''.join(list1))




