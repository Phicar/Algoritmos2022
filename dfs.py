A=[]
vis=[]
def dfs(x):
	global A,vis
	vis[x]=True #visito a x
	print("-->",x+1)
	for y in A[x]: #itero el grado de x
		if not vis[y]: # si no lo he visitado...visitelo
			dfs(y)
def dfs2(x):
	global A,vis
	pila = []
	pila.append(x)
	while len(pila)>0:
		y = pila.pop()
		print("-->",y+1)
		vis[y]=True
		for z in A[y]:
			if not vis[z]:
				pila.append(z)
def compConex(AA):
	global A,vis
	A = AA
	vis = [False for i in range(len(AA))]
	cc = 0 #numero de comp con.(i.e., cc)
	for i in range(len(AA)):
		if not vis[i]: #si no lo visite, es nueva cc.
			cc+=1
			dfs2(i)
	return cc
#print(compConex([[1,4],[0,2],[1],[],[0]]))
print(compConex([[2,3,4,5],[2,4],[0,1],[4,0],[0,1,3],[0,6],[5]]))