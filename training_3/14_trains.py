_ = int(input())
path1 = list(map(int, input().split()))

path1 = path1[::-1]

deadend = []

def check(path1, deadend):
    current_wagon = 1

    while len(path1) != 0:
        while len(path1) != 0:
            if path1[-1] == current_wagon:
                current_wagon += 1
                del path1[-1]
                if current_wagon in path1:
                    continue
                break
            else:
                deadend.append(path1[-1])
                del path1[-1]

        if len(path1) == 0:
            while len(deadend) != 0:
                if deadend[-1] != current_wagon:
                    return False
                else:
                    current_wagon += 1
                    del deadend[-1]
        else:
            if deadend[-1] != current_wagon and current_wagon in deadend:
                return False
            elif current_wagon in path1:
                continue
            else:
                while len(deadend) != 0 and deadend[-1] == current_wagon:
                    del deadend[-1]
                    current_wagon += 1
    return True

print('YES' if check(path1, deadend) else 'NO')
