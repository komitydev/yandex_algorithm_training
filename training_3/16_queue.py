que = []

def push(num):
    global que
    que.append(num)
    print('ok')

def pop():
    global que
    if len(que) == 0:
        print('error')
    else:
        print(que[0])
        que = que[1:]

def clear():
    global que
    que = []
    print('ok')

def size():
    print(len(que))

def front():
    if len(que) == 0:
        print('error')
    else:
        print(que[0])

def exit():
    print('bye')
    return True

def getFunc(command):
    if 'exit' in command:
        exit()
        return True
    if 'front' in command:
        front()
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
