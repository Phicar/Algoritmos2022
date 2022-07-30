n =0 # tamaño del arreglo https://sites.google.com/view/dvillami/algoritmos
P = [] #Permutacion
A = [] #arreglo a ordenar
B = [] #arreglo ordenado
V = [] #arreglo de visitados
def perm(it):
	global P,B,n,V,A
	if it==n:
		#VERIFICAR que la permutacion ordene
		B = [A[P[i]] for i in range(n)]
		estaOrdenado = True
		for i in range(n-1):
			if B[i]>B[i+1]:
				estaOrdenado =False
			if not estaOrdenado:
				break
		if estaOrdenado:
			print(P,B)
		return
	for j in range(n):
		if  not V[j]:
			P[it]=j #it:--->j
			V[j]= True
			perm(it+1)
			V[j]=False
			
def sort():
	global n,P,B,V,A #referenciar globales
	n = len(A)
	P = [0 for i in range(n)]
	B = [0 for i in range(n)]
	V = [False for i in range(n) ]
	perm(0)#vamos a iterar sobre las permutaciones
	return B 
A =[5,32,1,2,2]
sort()
