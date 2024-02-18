_str = input()
answer = [0,0,0,0,0,0,0,0,0,0]
for x in _str:
    answer[int(x)] +=1
res = answer[6]+answer[9] 
answer[6] = res//2
answer[9] = res-answer[6]
print(max(answer))