#Insercion
import random
def Insercion(A):
	for p in range(1,len(A)):
		j= p-1 #parando a la izq. del pivot
		x = A[p]
		while j>-1 and A[j]>x:#mientras pueda poner x a izq
			A[j+1]=A[j] #empujando para hacer campo a x
			j-=1
		A[j+1]=x
	return A
A = [random.randint(1,100) for i in range(10)]
print(A)
print(Insercion(A))	



#inversiones
#O(n**2)
def inv(A): #A arreglo que define permut
	B = [] #las inversiones
	n = len(A)
	for i in range(n):
		for j in range(n):
			if i<j and A[i]>A[j]:
				B.append([i,j])
	return B
def Cycles(A):
	n = len(A)
	V = [False for i in range(n)]
	B =[]
	for i in range(n):
		if V[i]: 
			continue
		j = i
		C=[]
		while not V[j]:
			C.append(j)
			V[j]=True
			j=A[j]
			
			
		#V[i]=True
		B.append(C)
	return B

			
	
n =0 # tamaño del arreglo https://sites.google.com/view/dvillami/algoritmos
P = [] #Permutacion
A = [] #arreglo a ordenar
B = [] #arreglo ordenado
V = [] #arreglo de visitados
def perm(it):
	global P,B,n,V,A
	if it==n:
		#VERIFICAR que la permutacion ordene
		print(P,Cycles(P))
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
A =[5,32,1]
#sort()