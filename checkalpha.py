if __name__ == '__main__':
    s = raw_input()
    alp = False
    dig = False
    alnum = False
    lowr = False
    upr = False
    for i in s:
        if i.isalnum():
            alnum = True
    for i in s:
        if i.isalpha():
            alp = True
            break
    for i in s:
        if i.isdigit():
            dig = True
            break
    for i in s:
        if i.islower():
            lowr = True
            break
    for i in s:
        if i.isupper():
            upr = True
            break
    if alnum:
        print(True)
    else:
        print(False)
    if  alp:
        print(True)
    else:
        print(False)
    if  dig:
        print(True)
    else:
        print(False)
    if  lowr:
        print(True)
    else:
        print(False)
    if  upr:
        print(True)
    else:
        print(False)
