n= 12
i = 1
s=0
while i<=n+1:
	if i%5==0 or i%11==0:
		s+=1 #contandor
	i=i+1
print(s)