with open('input.txt') as f:
    inp = [ l.replace('\n', '').replace(' ', '') for l in f.readlines() ]

inp = [ l for l in inp if l != '' ]

dct = {}

for item in inp:
    for i in item:
        try:
            dct[i] += 1
        except:
            dct[i] = 1

dct = dict(sorted(dct.items(), key=lambda x: ord(x[0])))

m = max(dct.values())

for d in dct:
    dct[d] = m - dct[d]

for i in range(m):
    for d in dct:
        if dct[d] == 0:
            print("#", end="")
        else:
            dct[d] -= 1
            print(" ", end="")
    print()

for i in dct:
    print(i, end="")
