#This program finds the largest possible product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid in the file PE-11-grid.txt

f = open("PE-11-grid.txt")
rows = f.readlines()
f.close()
grid = []
for i in range(0,20):
	grid.append(rows[i].split(' '))
maxprod = 1

#Row products:
for i in range(0,20):
	for j in range(0,17):
		prod = int(grid[i][j])*int(grid[i][j+1])*int(grid[i][j+2])*int(grid[i][j+3])
		if prod>maxprod:
			maxprod = prod

#Column products:
for i in range(0,17):
	for j in range(0,20):
		prod = int(grid[i][j])*int(grid[i+1][j])*int(grid[i+2][j])*int(grid[i+3][j])
		if prod>maxprod:
			maxprod = prod

#Downward diagonal products:
for i in range(0,17):
	for j in range(0,17):
		prod = int(grid[i][j])*int(grid[i+1][j+1])*int(grid[i+2][j+2])*int(grid[i+3][j+3])
		if prod>maxprod:
			maxprod = prod

#Upward diagonal products:
for i in range(3,20):
	for j in range(0,17):
		prod = int(grid[i][j])*int(grid[i-1][j+1])*int(grid[i-2][j+2])*int(grid[i-3][j+3])
		if prod>maxprod:
			maxprod = prod

print maxprod
