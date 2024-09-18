#selection sort alg. 
def main(A):
    
    n = len(A)
    for i in range(0, n-1):                                  #i runs from first el. to last el. in array
        min = i                                              # smallest element is set to the first element
        for j in range(i+1, n):                              # j runs from element i+1 to the last element + 1 (because you need to sort the last element as well)
            if A[j] < A[min]:                                #if the j-th element is smaller than the current smallest element, the j-th element is set to minimum el.
                min = j 
                
        temp = A[i]   #swap elements                         #last step is to swap the elements
        A[i] = A[min]
        A[min] = temp
    return A   

array = [7, 3, 5, 1, 2, 4]
print(main(array))
    
