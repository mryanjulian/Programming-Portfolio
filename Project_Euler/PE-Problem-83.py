#This program finds the minimum path sum from the top left to the bottom right of the matrix in the file PE-83-matrix attainable by moving up, down, left, or right.

#This strategy implements Dijkstra's algorithm.

f = open("PE-83-matrix.txt")
matrix = [[int(entry) for entry in line.split(',')] for line in f.readlines()]
f.close()

m = len(matrix)
n = len(matrix[0])

#paths[(i,j)] stores the minimum path sum from the left side to coordinate (i,j)
paths = {(i,j):float('inf') for j in range(0,n) for i in range(0,m)}
start = (0,0)
paths[start] = matrix[start[0]][start[1]]
current = start
unvisited = {(i,j) for i in range(0,m) for j in range(0,n)}
while len(unvisited)>0:
	if current[0]>0: paths[(current[0]-1,current[1])] = min(paths[(current[0]-1,current[1])],paths[current]+matrix[current[0]-1][current[1]])
	if current[0]<m-1: paths[(current[0]+1,current[1])] = min(paths[(current[0]+1,current[1])],paths[current]+matrix[current[0]+1][current[1]])
	if current[1]<n-1: paths[(current[0],current[1]+1)] = min(paths[(current[0],current[1]+1)],paths[current]+matrix[current[0]][current[1]+1])
	if current[1]>0: paths[(current[0],current[1]-1)] = min(paths[(current[0],current[1]-1)],paths[current]+matrix[current[0]][current[1]-1])
	unvisited.remove(current)
	tempmin = float('inf')
	for node in unvisited:
		if paths[node]<tempmin:
			current = node
			tempmin = paths[current]

print paths[(m-1,n-1)]
