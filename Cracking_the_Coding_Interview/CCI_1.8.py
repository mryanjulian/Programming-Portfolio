import sys

matrix = eval(sys.argv[1])

def zeroize(m):
    if len(m) == 0 or len(m[0]) == 0: return False
    rows = []
    cols = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                rows.append(i)
                cols.append(j)
    print rows, cols
    for i in rows:
        for j in range(len(m[0])):
            m[i][j] = 0
    for j in cols:
        for i in range(len(m)):
            m[i][j] = 0
    return m

print zeroize(matrix)