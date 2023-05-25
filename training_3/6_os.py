with open('input.txt') as f:
    sectorcount = int(f.readline())
    oscount = int(f.readline())
    sectors = [ tuple( map(int, f.readline().split()) )  for _ in range(oscount)]

res = [ True ] * oscount

for i in range(oscount):
    if res[i] == False:
        continue

    a, b = sectors[i]
    
    for j in range(i, oscount):
        if j <= i:
            continue
        if res[i] == False:
            continue

        c, d = sectors[j]

        if (c <= b or c <= a) and d >= b:
            res[i] = False
            break
        if c <= a and (d >= a or d >= b):
            res[i] = False
            break
        if a <= d and c <= b:
            res[i] = False
            break

count = 0

for r in res:
    if r == True:
        count += 1

print(count)
