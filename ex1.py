import random

def LinearSelection(A, k):
    n = len(A)
    if k <= 0 or k > n:
        print("Erro: valor 'k' inválido")
        return

    if n <= 5:
        _A = A.copy()
        _A.sort()
        return _A[k-1]

    grupos = []
    M=[]
    for i in range(n//5):
        grupo = A[5*i:5*i+5]
        grupo.sort() # Trocar
        grupos.append(grupo)
        M.append(grupo[2])
    
    if n%5 != 0:
        grupo = A[5*i+5:]
        grupo.sort() # Trocar
        grupos.append(grupo)
        M.append(grupo[len(grupo)//2])

    _m = LinearSelection(M, (len(M)+1)//2)

    L = []
    R = []
    count = 0

    for i in A:
        if i < _m:
            L.append(i)
        elif i > _m:
            R.append(i)
        else:
            count += 1

    if len(L) > k-1:
        return LinearSelection(L, k)
    
    elif len(L) + count > k-1:
        return _m
    
    else:
        return LinearSelection(R, k-len(L)-count)

    
A=[x+1 for x in range(22)]
random.shuffle(A)

#"""
for k in range(1,len(A)+1):

    num = LinearSelection(A,k)
    if num != k:
        print("Erro")
    else:
        print("OK")
#"""