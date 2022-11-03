pad = []
def find(x):
	global pad
	if x==pad[x][0]:
		return x
	pad[x][0]=find(pad[x][0])
	return pad[x][0]
def union(x,y):
	global pad
	px = find(x)
	py = find(y)
	if px==py: #ya estan unidos
		return
	if pad[px][1]<pad[py][1]: #la complejidad baja a casi constante
		px,py = py,px
	#Funcion de Ackerman
	pad[py][0]=px
	pad[px][1]+=pad[py][1]
def MakeSet(E,n): #n =|V|
	global pad
	pad = [[i,1] for i in range(n)]
	for i in E:
		union(i[0],i[1])
	c = 0
	for i in range(n):
		if i==pad[i][0]:
			print(pad[i][1])
			c+=1
	print(c)
A = [[0,1],[0,2],[1,2],[1,4],[3,4],[4,5],[5,6],[7,8]]
MakeSet(A,9) # complejidad O(|E|)=o(|V|**2)

