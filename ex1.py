import random



def LinearSelection(A, k):
    n = len(A)
    if k <= 0 or k > n:
        print("Erro: valor 'k' inválido")
        return

    # print(f"{k=} {A=}")
    if n <= 5:
        _A = A.copy()
        _A.sort()
        # print(f"{_A=}")
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

    # print(grupos)
    # print(M)

    _m = LinearSelection(M, (len(M)+1)//2)

    # print(_m)

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
    
    # print(f"{L=} {R=}")

    if len(L) == k-1:
        return _m
    elif len(L) > k-1:
        return LinearSelection(L, k)
    else:
        return LinearSelection(R, k-len(L)-1)

    
A=[x+1 for x in range(22)]
random.shuffle(A)

A = [16, 9, 13, 5, 12, 19, 1, 10, 8, 17, 11, 3, 6, 22, 7, 15, 21, 2, 20, 14, 18, 4]

print(A)

print(LinearSelection(A,4))
#"""
for k in range(1,len(A)+1):

    num = LinearSelection(A,k)
    print(k)
    print(num)
    if num != k:
        print("Erro")
#"""