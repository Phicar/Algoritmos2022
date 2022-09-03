#Dado A = {a,..,j}
#palindromo
#recursivamente
#anagramas
import random
A = "abcdefghij"
def An(n):
	global A
	if n==1:
		return A
	B = An(n-1)
	C =[]
	for x in B:
		for y in range(len(A)):
			C.append(x+A[y])
	return C

# Punto uno iterativamente
def An2(n):
	global A
	C = []
	for i in range(10**n):
		s = ""
		ii = i
		for j in range(n):
			r = ii%10
			s = A[r]+s
			ii//=10
		C.append(s)
	return C	

#palindromos
def pal1(x):
	for i in range(len(x)//2):
		if x[i] != x[len(x)-1-i]:
			return False
	return True
def pal2(x):
	if len(x)<=1:
		return True
	return (x[0]==x[len(x)-1]) and pal2(x[2:len(x)-1])
X = An2(3)

for x in X:
	if pal2(x):
		print(x)


n =0 # tamaño del arreglo https://sites.google.com/view/dvillami/algoritmos
P = [] #Permutacion
A = [] #arreglo a ordenar
B = [] #arreglo ordenado
V = [] #arreglo de visitados
def perm(it):
	global P,B,n,V,x
	print(it,P,V)
	if it==n:
		#VERIFICAR que la permutacion ordene
		B = [x[P[i]] for i in range(n)]
		print(B)
		return
	for j in range(n):
		if  not V[j]:
			P[it]=j #it:--->j
			V[j]= True
			perm(it+1)
			V[j]=False
			P[it]=-1
			
def anagrama():
	global n,P,B,V,x #referenciar globales
	n = len(x)
	P = [-1 for i in range(n)]
	B = [0 for i in range(n)]
	V = [False for i in range(n) ]
	perm(0)#vamos a iterar sobre las permutaciones
	return B 
x = "mar"
anagrama()
def algo(A,B):
	C = []
	i = 0
	j = 0
	while i<len(A) or j < len(B):
		if j==len(B) or (i < len(A) and A[i]<=B[j]):
			C.append(A[i])
			i+=1
		else:
			C.append(B[j])
			j+=1
	return C
def MS(A):
	if len(A)<=1:
		return A
	B = MS(A[0:len(A)//2])
	C = MS(A[len(A)//2:len(A)])
	D = algo(B,C)
	print(B,C,D)
	return D
M =[4-j for j in range(4)]
print(M,MS(M))


	

