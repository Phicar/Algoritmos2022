def osito(n):
	if n==0:
		return [[]]
	O = osito(n-1) #P([n-1])
	print()
	OO = []
	for A in O:
		AA = A.copy()
		AA.append(n) # AU{n}
		OO.append(AA)
		OO.append(A)
	return OO
print(osito(3))
