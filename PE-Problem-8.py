#This program finds the largest possible product of a sequence of 13 adjacent digits in the number stored in the file PE-8-Number

#This function computes the maximum product of n consecutive digits in the input string s
def chunkmax(s,n):
	currmax = 1
	for j in range(0,n):
		currmax*=int(s[j])
	teststr = s[0:n-1]
	testprod = currmax
	i = 0
	while i+n<len(s):
		testprod = testprod/int(s[i])*int(s[i+n])
		if testprod>currmax:
			currmax = testprod
		i+=1
	return currmax

#This section imports the number in PE-8-Number and creates a list of all segments of at least n consecutive non-zero digits
n = 13
f = open("PE-8-Number")
numstr = f.read()
chunks = numstr.split('0')
i = 0
while i < len(chunks):
	if len(chunks[i])<n:
		chunks.remove(chunks[i])
	else: i += 1

#This section computes the maximum product of n consecutive digits in any of the strings in the list chunks
maxprod = 1
for chunk in chunks:
	newval = chunkmax(chunk,n)
	if maxprod < newval:
		maxprod = newval

print maxprod
