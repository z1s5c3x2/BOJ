_str = input()
_str = _str.replace("XXXX","AAAA")
_str = _str.replace("XX","BB")

if _str.find('X') != -1:
    print(-1)
else:
    print(_str)
