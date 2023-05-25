n = int(input())
cost = tuple( int(x) for x in input().split() )

stk = []
res = [ -69 ] * len(cost)

for i in range(0, len(cost)):
    while True:
        if len(stk) == 0:
            stk.append( (cost[i], i) )
            break
        s = stk[-1]
        if s[0] > cost[i]:
            res[s[1]] = i
            del[stk[-1]]
        else:
            stk.append( (cost[i], i) )
            break

for s in stk:
    res[s[1]] = -1

print(" ".join(map(str, res)))
