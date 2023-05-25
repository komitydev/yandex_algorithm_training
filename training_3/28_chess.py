m, n = list(map(int, input().split()))

matr = [ [ 0 ] * n for _ in range(m) ]

all_ways = 0

matr[0][0] = 1

for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i - 1 >= 0 and j - 2 >= 0:
            one = matr[i-1][j-2]
        else:
            one = 0
        if i - 2 >= 0 and j - 1 >= 0:
            two = matr[i-2][j-1]
        else:
            two = 0
        matr[i][j] = one + two

print(matr[-1][-1])
