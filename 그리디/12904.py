str1 = input()
target = input()

while len(str1) < len(target):
    if target[-1] == 'A':
        target = target[:-1]
    else:
        target = target[:-1][::-1]
        
print(int(str1 == target))


    
