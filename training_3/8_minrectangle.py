with open("input.txt") as f:
    inp = [ l.replace("\n", "") for l in f.readlines() ]

fElem = inp[1].split()
minHor = int(fElem[0])
maxHor = int(fElem[0])

minVer = int(fElem[1])
maxVer = int(fElem[1])

inp = inp[2:]

for item in inp:
    item = item.split()
    item = int(item[0]), int(item[1])

    if item[0] < minHor:
        minHor = item[0]
    if item[0] > maxHor:
        maxHor = item[0]

    if item[1] < minVer:
        minVer = item[1]
    if item[1] > maxVer:
        maxVer = item[1]

print(minHor, minVer, maxHor, maxVer)
