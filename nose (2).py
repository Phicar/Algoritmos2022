A = [1,3,5,7,7,7,11,13]
def BBIm(A,x,quiero):
	mini = 0
	maxi = len(A)-1
	encontre = -1
	while mini < maxi:
		m = (mini+maxi)//2
		if x<A[m]:#izquierda
			maxi=m-1
		elif x>A[m]: #derecha
			mini = m+1
		else:
			encontre = m
			if not quiero:
				maxi = m-1
			else:
				mini = m+1
				
	if A[mini]==x:
		return mini
	if encontre!= -1:
		return encontre
	return -1
def cuenta(A,x):
	A.sort()
	mini = BBIm(A,x,False)
	maxi = BBIm(A,x,True)
	if mini==-1:
		return 0
	return maxi-mini+1
print(cuenta(A,325367))