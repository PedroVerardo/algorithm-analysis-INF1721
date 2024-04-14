import random
from sort import bubbleSort


def LinearSelection(A, k):
    n = len(A)
    if k <= 0 or k > n:
        print("Erro: valor 'k' inválido")
        return

    if n <= 5:
        _A = A.copy()
        _A = bubbleSort(_A)
        return _A[k-1]

    M=[] # Lista de medianas
    for i in range(n//5):
        grupo = A[5*i:5*i+5]
        grupo = bubbleSort(grupo)
        M.append(grupo[2])
    
    if n%5 != 0:
        grupo = A[5*i+5:]
        grupo = bubbleSort(grupo)
        M.append(grupo[len(grupo)//2])

    _m = LinearSelection(M, (len(M)+1)//2)

    L = [] # Lista de elementos menores que _m
    R = [] # Lista de elementos maiores que _m
    count = 0 # Contador de elementos iguais a _m

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


if __name__ == "__main__":
    def SortSelection(A: list, k: int) -> int:
        _a = A.copy()
        _a.sort()
        return _a[k-1]
    #"""
    A=[random.randint(0,100) for x in range(1000)]
    for k in range(1,len(A)+1):

        result = SortSelection(A,k)
        num = LinearSelection(A,k)
        if num != result:
            print("Erro")
        else:
            print("OK")
    #"""