stk = []

orig = '({['
giro = ')}]'

def antipod(qwe):
    return giro[orig.index(qwe)]

def func(inp):
    for c in inp:
        if (len(stk) != 0) and (c in giro) and (c != giro[orig.index(stk[-1])]):
            return False
        if len(stk) == 0:
            if c in giro:
                return False
            stk.append(c)
        else:
            if c in giro:
                if c != giro[orig.index(stk[-1])]:
                    return False
                else:
                    del stk[-1]
            else:
                stk.append(c)
    return True

res = func(input())
print('yes' if (res == True) and (len(stk) == 0) else 'no')
