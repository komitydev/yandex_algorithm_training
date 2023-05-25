with open("input.txt") as f:
    l = f.readlines()
    n, _, _ = [ int(x) for x in l[0].split() ]
    matrix = [ x.split() for x in l[1:n+1] ]
    queries = [ [ int(i) for i in x.split() ] for x in l[n+1:] ]
    new_matrix = [ [ 0 ] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1) ]

for j in range(1, len(new_matrix)):
    for i in range(1, len(new_matrix[0])):
        new_matrix[j][i] = int(matrix[j-1][i-1]) + new_matrix[j-1][i] + new_matrix[j][i-1] - new_matrix[j-1][i-1]

for k in queries:
    s = new_matrix[k[2]][k[3]] + new_matrix[k[0]-1][k[1]-1] - new_matrix[k[2]][k[1]-1] - new_matrix[k[0]-1][k[3]]
    print(s)
