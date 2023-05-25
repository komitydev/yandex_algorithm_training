n, k = list(map(int, input().split()))

l = [ 0 ] * k + [ 1 ] + [ 0 ] * (n - 1)

for i in range(k, n + k):
    for j in range(1, k + 1):
        l[i] += l[i - j]

print(l[-1])
