#This program finds the minimum path sum from the upper left to the lower right of the matrix in the file PE-81-matrix attainable by moving only down or to the right.

f = open("PE-81-matrix.txt")
matrix = [[int(entry) for entry in line.split(',')] for line in f.readlines()]
f.close()

m = len(matrix)
n = len(matrix[0])

#paths[i][j] stores the minimum path sum from the upper left corner to coordinate (i,j)
paths = [[0 for j in range(0,n+1)] for i in range(0,m+1)]
paths[0][0] = matrix[0][0]
for i in range(1,m): paths[i][0] = paths[i-1][0]+matrix[i][0]
for j in range(1,n): paths[0][j] = paths[0][j-1]+matrix[0][j]
for i in range(1,m):
	for j in range(1,n):
		paths[i][j] = min(paths[i-1][j],paths[i][j-1])+matrix[i][j]

print paths[m-1][n-1]
