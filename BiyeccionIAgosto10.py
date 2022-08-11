def I(A): #A permutacion
  n = len(A)
  F = [0 for i in range(n)]# poniendo m zeros
    for j in range(n):
      for i in range(j):
        if A[i]>A[j]:
          F[A[i]]+=1
  return F #moralmente: F \in  A_n
