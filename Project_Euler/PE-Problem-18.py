#This program computes the maximum total value attainable by traveling down the triangle in the file PE-18-triangle.txt via adjacent entries and summing as you go.

#Create an array containing all the entries of the triangle so triangle[i][j] is the jth entry in the ith row.
f = open("PE-18-triangle.txt")
lines = f.readlines()
f.close()
triangle = []
for i in range(0,len(lines)):
	triangle.append([])
	for entry in lines[i].split(' '):
		triangle[i].append(int(entry))

#memoize the maximum value attainable by starting at (i,j) and proceeding downward from there.
values = triangle
i = len(triangle)-2
while i>=0:
	for j in range(0,len(triangle[i])):
		values[i][j] = max(triangle[i][j]+values[i+1][j],triangle[i][j]+values[i+1][j+1])
	i-=1

print values[0][0]
