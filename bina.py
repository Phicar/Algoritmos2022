A = [1,3,5,7,11,13]
def BBI(A,x):
	mini = 0
	maxi = len(A)-1
	while mini < maxi:
		m = (mini+maxi)//2
		if x==A[m]:
			return m
		if x<A[m]:#izquierda
			maxi=m-1
		else: #derecha
			mini = m+1
	if A[mini]==x:
		return mini
	return -1
def BBR(A,x):
	if len(A)==0:
		return -1
	if len(A)==1:
		if x==A[0]:
			return 0
		return -1
	if x==A[len(A)//2]:
		return len(A)//2
	if x<A[len(A)//2]:
		return BBR(A[0:len(A)//2],x)
	D = BBR(A[len(A)//2:len(A)],x)
	if D==-1:
		return -1
	return D+len(A)//2
for i in range(1,15):
	print(i,BBI(A,i),BBR(A,i))