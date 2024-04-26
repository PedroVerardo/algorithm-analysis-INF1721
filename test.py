import numpy as np
import time
import matplotlib.pyplot as plt
import tqdm
from linear_selection import LinearSelection
from sort import bubbleSort

def SortSelection(A:np.array, k: int) -> int:
    Aord = bubbleSort(A)
    return Aord[k - 1]

def create_vector(upper: int, lower: int, size: int) -> np.ndarray:
    return np.random.rand(size)*(upper-lower) + lower

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
            tam = len(A)
            B = A.copy()

            start_1 = time.time()
            r1 = selection1(A,tam//2)
            end_1 = time.time()

            sum1 += end_1 - start_1

            start_2 = time.time()
            r2 = selection2(B,tam//2)
            end_2 = time.time()

            sum2 += end_2 - start_2

            try:
                assert r1 == r2
            except AssertionError:
                print("Error! The results are different!")
            
        time_selection1.append(sum1/10)
        time_selection2.append(sum2/10)
        sum1 = 0
        sum2 = 0
    
    for i in range(1,11):
        print(f"Time for n = {n*i}:")
        print(f"Selection 1: {time_selection1[i-1]}")
        print(f"Selection 2: {time_selection2[i-1]}")
        print("\n")

    plt.plot(range(10), time_selection1, label='Selection 1', c="blue")
    plt.title('Time comparison')
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.savefig('linear.png', dpi=500)
    plt.plot(range(10), time_selection2, label='Selection 2', linestyle='dashed', c="red")
    plt.savefig('sort.png', dpi=500)
    
    plt.show()
    
    return 0
    

if __name__ == '__main__':
    compare_algos(LinearSelection, SortSelection, 1000, 100000, 1)
