#CellMax por Felipe 
ns = list(map(int, input().split())) # Personas y pisos
n = ns[0]
s = ns[1]

q2 = [0 for i in range(s)]

for i in range(n):
        x = list(map(int, input().split()))
        if q2[x[0]-1] < x[1]: # Comprobando que sea el mayor t.
                q2[x[0]-1] = x[1]
q = []
for i in range(s-1, -1, -1):
        q.append(q2[i])

t = [0] # Tiempo en cada piso
for i in range(1, s):
        if t[i-1]+1 < q[i]:
                t.append(q[i])
        else:
                t.append(t[i-1]+1)

print(t[s-1]+1)
#Permutaciones
a = int(input())
fac = [1]
for n in range(1,21): #progrmacion dinamica de abajo pa arriba
        fac.append(fac[n-1]*n)
for c in range(a):
        s = input()
        N = int(input())
        res = ""
        vis = [False for i in range(len(s))]
        for k in range(len(s)-1,-1,-1):
                q = N//fac[k]
                c=0
                #print(k,fac[k],q,vis)
                for r in range(len(s)):
                        if not vis[r]:
                                if c==q:
                                        vis[r]=True
                                        res+=s[r]
                                        break
                                c+=1

                N=N%fac[k]
        print(res)
#quimica???
import math
def tal(n):
        s = 0
        rad =2*math.pi/360.0
        ang = 360.0/(2*n)
        for i in range(1,n//2+n%2):
                s+= abs(math.sin(i*rad*ang))
        return 2*s+1
print(tal(2))
print(tal(4))
print(tal(200))

