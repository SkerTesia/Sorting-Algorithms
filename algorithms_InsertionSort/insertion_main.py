#insertion sort
def main(A):
    n = len(A)

    for j in range(1, n): # from second el. to n-th element
        i = 0

        while A[j] > A[i]: 
            i = i+1 
        key = A[j]  
        
        for k in range(0, j-i): #k elements from first index to j-i
            A[j-k] = A[j-k-1]
        A[i] =  key 

    return A

array = [7, 43, 4, 1, 5, 9]
print(main(array))

#the pseudocode takes elements from a1 to an. However when writing code you need to consider indices rather than element no.