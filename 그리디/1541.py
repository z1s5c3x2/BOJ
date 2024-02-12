list1 = input().split('-')

answer = 0

for x in list1[0].split('+'):
    answer += int(x)

for x in list1[1:]:
    for y in x.split("+"):
        answer -= int(y)
        
print(answer)