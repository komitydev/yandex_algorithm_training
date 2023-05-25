stk = []

def push(num):
    global stk
    stk.append(num)
    print('ok')

def pop():
    global stk
    if len(stk) == 0:
        print('error')
    else:
        print(stk[-1])
        stk = stk[:-1]

def clear():
    global stk
    stk = []
    print('ok')

def size():
    print(len(stk))

def back():
    if len(stk) == 0:
        print('error')
    else:
        print(stk[-1])

def exit():
    print('bye')
    return True

def getFunc(command):
    if 'exit' in command:
        exit()
        return True
    if 'back' in command:
        back()
    if 'size' in command:
        size()
    if 'clear' in command:
        clear()
    if 'pop' in command:
        pop()
    if 'push' in command:
        push(int(command.split()[1]))
    return False

with open("input.txt") as f:
    inp = [ l.replace("\n", "") for l in f.readlines() ]

for l in inp:
    if getFunc(l):
        break
