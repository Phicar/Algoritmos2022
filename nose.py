def mult(A,B):
	a = len(A) #filas de A
	b = len(A[0])#colum de A
	b1 = len(B) #filas de B
	c = len(B[0]) # colm de B
	if not b==b1:
		return
	AB = [[0 for j in range(c)] for i in range(a)]
	for i in range(a):
		for j in range(c):
			for k in range(b):
				AB[i][j]+=A[i][k]*B[k][j]
	return AB
print(mult([[1,2,3,4]],[[1],[1],[1],[1]]))
		
