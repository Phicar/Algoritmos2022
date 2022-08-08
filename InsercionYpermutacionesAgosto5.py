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
