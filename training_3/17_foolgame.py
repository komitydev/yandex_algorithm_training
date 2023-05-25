with open('input.txt') as f:
    inp = f.readlines()
    f, s = inp[0].rstrip().split(), inp[1].lstrip().split()

minCard = min(min(f), min(s))
maxCard = max(max(f), max(s))

maxRounds = 10**6
curRound = 0

while curRound < maxRounds:
    fc = f[0]
    sc = s[0]
    if fc < sc:
        if fc == minCard and sc == maxCard:
            s = s[1:]
            f = f[1:]
            f.append(fc)
            f.append(sc)
        else:
            f = f[1:]
            s = s[1:]
            s.append(fc)
            s.append(sc)
    if sc < fc:
        if sc == minCard and fc == maxCard:
            f = f[1:]
            s = s[1:]
            s.append(fc)
            s.append(sc)
        else:
            s = s[1:]
            f = f[1:]
            f.append(fc)
            f.append(sc)
    if f == []:
        print('second', curRound+1)
        break
    if s == []:
        print('first', curRound+1)
        break
    curRound += 1

if curRound == maxRounds:
    print('botva')
