import numpy as np
import time
import matplotlib.pyplot as plt
import tqdm

def bubbleSort(A: np.ndarray) -> np.ndarray:
    n = len(A)

    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
                
    return A

def SortSelection(A, k):
    Aord = bubbleSort(A)
    return Aord[k]

def create_vector(upper: int, lower: int, size: int) -> np.ndarray:
    return np.random.rand(size)*(upper-lower) + lower

def compare_vectors(A: np.ndarray, B: np.ndarray) -> bool:
    return np.array_equal(A, B)

def compare_algos(selection1,
                  selection2,
                  n: int,
                  upper: int,
                  lower: int) -> None:
    
    time_selection1 = []
    time_selection2 = []

    for i in tqdm.tqdm(range(1,11), desc="instances progress"):
        sum1 = 0
        sum2 = 0
        for j in tqdm.tqdm(range(1,11), desc="mean of times progress"):
            A = create_vector(upper, lower, n*i)
            B = A.copy()

            start_1 = time.time()
            selection1(A,5)
            end_1 = time.time()

            sum1 += end_1 - start_1

            start_2 = time.time()
            selection2(B,5)
            end_2 = time.time()

            sum2 += end_2 - start_2
            
        time_selection1.append(sum1/10)
        time_selection2.append(sum2/10)
        sum1 = 0
        sum2 = 0
    
    for i in range(1,10):
        print(f"Time for n = {n*i}:")
        print(f"Selection 1: {time_selection1[i-1]}")
        print(f"Selection 2: {time_selection2[i-1]}")
        print("\n")

    plt.plot(range(1,10), time_selection1, label='Selection 1', c="blue")
    plt.plot(range(1,10), time_selection2, label='Selection 2', linestyle='dashed', c="red")
    plt.title('Time comparison')
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.show()
    
    return 0
    

if __name__ == '__main__':
    compare_algos(SortSelection, SortSelection, 1000, 100000, 1)
