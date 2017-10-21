#This program computes the Gram-Schmidt Orthonormalization of the matrix in the file matrix.txt

import numpy as np

f = open("matrix.txt")
A = f.readlines()
f.close()
M = []
for i in range(0,len(A)):
	M.append(A[i].split(' '))
V = np.zeros((len(M),len(M[0])))
for i in range(0,len(M)):
	for j in range(0,len(M[0])):
		V[i,j] = float(M[i][j])
Q = np.zeros((V.shape[0],V.shape[1]))
Q[:,0] = V[:,0]/np.sqrt(np.dot(V[:,0],V[:,0]))
for j in range(1,V.shape[1]):
	Vprime = V[:,j]
	for i in range(0,j):
		Vprime = Vprime - np.dot(Q[:,i],V[:,j])*Q[:,i]
	if np.all(Vprime==0): Q[:,j] = np.zeros(V.shape[0])
	else: Q[:,j] = Vprime/np.sqrt(np.dot(Vprime,Vprime))

print Q
