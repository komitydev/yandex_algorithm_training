with open('input.txt') as f:
    n, m = f.readline().split()
    n = int(n)
    m = int(m)

    cost = list(list(map(int, s.replace("\n", "").split())) for s in f.readlines())

cum_cost = [ [ -1 ] * (m + 1) for _ in range(n+1) ]

cum_cost[1][1] = cost[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            continue
        if cum_cost[i-1][j] == -1:
            minimum = cum_cost[i][j-1]
        elif cum_cost[i][j-1] == -1:
            minimum = cum_cost[i-1][j]
        else:
            minimum = min(cum_cost[i-1][j], cum_cost[i][j-1])

        cum_cost[i][j] = cost[i-1][j-1] + minimum

print(cum_cost[-1][-1])
