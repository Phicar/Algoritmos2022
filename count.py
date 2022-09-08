import random
def maximo(x):
	m = -1
	for i in range(len(x)):
		if m< x[i]:
			m= x[i]
	return m
def countSort(x):
	xx = []
	m = maximo(x) #O(n)
	b = [0 for i in range(m+1)] #O(m)
	for i in range(len(x)): #O(n)
		b[x[i]]+=1 #Balde en la posicion x_i le
			   # sumo uno.
				#ESTO ES FRECUENCIA!!!				
	#print(b)
	for i in range(len(b)): #O(n+m)
		for j in range(b[i]):
			xx.append(i)
	return xx #O(n+m)
a = [random.randint(1,10) for i in range(15)]
print(a)
print(countSort(a))