pad= [[]]
def find(x): # encuentra el rtepresentante de equiv.
	#global pad	|
	if x==pad[x][0]: #x es raiz
		return x
	return find(pad[x][0])
def union(x,y):
	global pad
	px = find(x)
	py = find(y)
	if px==py: #no quiero hacer nada si ya tenía repres. iguales
		return
	pad[py][0]=px #hago que el nuevo rep de la union sea el
	pad[px][1]+=pad[py][1]#rep de x.
	#print(x,y,px,py,pad)
def makeSet(G,n): #G= [[a,b] si (a,b) es arista], n= #vert.
	global pad
	pad = [[x,1] for x in range(n)]
	for y in G:
		union(y[0],y[1]) # unir a con b.
	cc = 0 #num de comp conex.
	for x in range(n):
		if x== pad[x][0]:
			cc+=1
			print("->"+str(pad[x][1]))
	print(cc)
makeSet([[1,3],[2,5],[2,6],[4,5],[4,6]],7)		
	