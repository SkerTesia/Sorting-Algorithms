def CountingSort(A, m):
    
    C = [0]* (max(A) + 1)
    k = len(A)
    m = max(A)


    for i in range(0, m+1):
        C[i] = 0
    
    for j in range(1, k):
        C[A[j]] += 1

    for i in range(1, m+1):
        C[i] +=  C[i-1]
    
    B = [0]* (len(A))

    for j in range(len(A)-1, 1, -1):
        B[C[[A[j]]]] = A[j]
        C[A[j]] -= 1

A = [7, 3, 4, 23, 5, 2, 15]
n = len(A)




print(CountingSort(A, n))

CountingSort()