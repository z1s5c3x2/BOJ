list1 = []

for _ in range(int(input())):
    tmp = input().split()
    list1.append([tmp[0]]+ list(map(int,tmp[1:])))
list1.sort(key=lambda x: (x[3],x[2],x[1]))
print(list1[-1][0])
print(list1[0][0])
