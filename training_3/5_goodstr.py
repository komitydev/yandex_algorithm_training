n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

total = 0

for i in range(len(l) - 1):
    total += min(l[i], l[i+1])

print(total)
