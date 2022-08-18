n= 66464
i = 1
s=0
while i<=n:
	if i%5==0 or i%11==0:
		s+=1 #contandor
	i=i+1
print(s)
print(n//5+n//11-n//55)
