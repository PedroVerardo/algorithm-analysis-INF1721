import numpy as np

def bubbleSort(A: np.ndarray) -> np.ndarray:
    n = len(A)

    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
                
    return A