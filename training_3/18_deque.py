deque = []

def push_front(num):
    global deque
    deque = [ num ] + deque
    print('ok')


def push_back(num):
    global deque
    deque.append(num)
    print('ok')

def pop_front():
    global deque
    if len(deque) == 0:
        print('error')
    else:
        print(deque[0])
        deque = deque[1:]

def pop_back():
    global deque
    if len(deque) == 0:
        print('error')
    else:
        print(deque[-1])
        deque = deque[:-1]

def front():
    if len(deque) == 0:
        print('error')
    else:
        print(deque[0])

def back():
    if len(deque) == 0:
        print('error')
    else:
        print(deque[-1])

def size():
    print(len(deque))

def clear():
    global deque
    deque = []
    print('ok')

def exit():
    print('bye')
    return True

# ===============================

def getFunc(command):
    if 'push_front' in command:
        push_front(int(command.split()[1]))
        return False
    if 'push_back' in command:
        push_back(int(command.split()[1]))
        return False
    if 'pop_front' in command:
        pop_front()
        return False
    if 'pop_back' in command:
        pop_back()
        return False
    if 'front' in command:
        front()
        return False
    if 'back' in command:
        back()
        return False
    if 'size' in command:
        size()
        return False
    if 'clear' in command:
        clear()
        return False
    if 'exit' in command:
        exit()
        return True
    return False

with open("input.txt") as f:
    inp = [ l.replace("\n", "") for l in f.readlines() ]

for l in inp:
    if getFunc(l):
        break
