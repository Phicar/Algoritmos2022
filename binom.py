	#Si yo quiero iterar sobre una union
	#disjunta, los fors son no anidados.
	#Si, en cambio, quiero iterar sobre
	#el producto cartesiano de dos conj.
	# entonces los fors son anidados.

def A(n,k):
	if n==1:
		if k>-1 and k<2:
			return [str(k)]
		return []
	P = A(n-1,k-1)
	S = A(n-1,k)
	PS = []
	for x in P:
		PS.append(x+"1")
	for x in S:
		PS.append(x+"0")
	return PS
print(A(5,3))
######################################
def binom(n,k):
	if n==0:
		if k==0:
			return 1
		return 0
	return binom(n-1,k)+binom(n-1,k-1)
nn = 10
for n in range(nn):
	for k in range((nn-n)//2):
		print(" ",end = " ")
	for k in range(n+1):
		print(binom(n,k),end = " ")
	print()