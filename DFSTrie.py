def letAnum(xx):
	return ord(xx) - ord("a") #chr a ASCII
def dfs(x,s):
	vis[x]=True
	if D[x]:
		print(s)
	gradSal = B[x] #contiene caracteres
	gradSal.sort()
	for yy in range(len(gradSal)):
		y = gradSal[yy]
		#print(y)
		if not vis[F[x][letAnum(y)]]:
			dfs(F[x][letAnum(y)],s+y)
B = [[]] # vertice -> letra
F = [[-1 for i in range(26)]] # letra -> vertice

A =["aba","hola","abc","ho","z"] #el conjunto X \subset A^*
D = [False ] #Nos dice que vertices son terminales(que pertenecen a X)

for i in range(len(A)): #iteramos las palabras
	r = 0 # raiz
	for j in range(len(A[i])): # iterar sobre letras
		iden = letAnum(A[i][j])
		if F[r][iden] == -1: #no he visto a iden en r
			idenArbol = len(B) #identificacion de nuevo vertice
			B.append([])
			F.append([-1 for k in range(26)])
			B[r].append(A[i][j]) #el vert r mira la letra A[i][j]
			F[r][iden] = idenArbol
			D.append(False)
		if j == len(A[i])-1:
			D[F[r][iden]] = True
		r = F[r][iden]

print(B)
print(F)
print(D)
vis = [False for i in range(len(B))]
dfs(0,"")
