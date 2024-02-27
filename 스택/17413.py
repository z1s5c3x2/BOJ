stk = []
tag = ''
answer = ''
def stkToAns():
    global answer
    while stk:
        answer += stk.pop()
for x in input():
    if x == '<':
        stkToAns()
        tag += x
    elif x == '>':
        answer += tag +'>'
        tag =''
    elif x ==' ' and not tag:
        stkToAns()
        answer += ' '
    elif tag:
        tag += x
    else:
        stk.append(x)
stkToAns()
print(answer)