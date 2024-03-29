list1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

n = input()

answer = 0

for x in range(len(n)):
    for y in list1:
        if n[x] in y:
            answer += list1.index(y)+3

print(answer)