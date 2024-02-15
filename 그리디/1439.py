_str = input()

list1 = [_str.split('0'),_str.split('1')]

list1[0] = len(list1[0]) - list1[0].count('')
list1[1] = len(list1[1]) - list1[1].count('')

print(min(list1))
