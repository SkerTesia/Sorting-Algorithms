#bubble sort alg. 

def main(A):
    n = len(A)

    for i in range(0, n-2):                             # i runs from the first element to the next-to-last element   (wait! why do we need i?)
        for j in range(0, n-1):                         # j runs from the first element to the last element (should j run from 1?)
            if A[j] > A[j+1]:                           #if j is bigger than j+1
                temp = A[j+1]                           #then swap elements
                A[j+1] = A[j]
                A[j] = temp 
    return A

array = [15, 7, 6, 2, 14, 13]
print(main(array))