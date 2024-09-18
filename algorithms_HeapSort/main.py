def Heapify(A, n, i):
    max = i
    leftchild = 2*i + 1
    rightchild = 2*i + 2

    if leftchild < n and A[i] < A[leftchild]:
        max = leftchild
    
    if rightchild < n and A[max] < A[rightchild]:
        max = rightchild

    if max is not i:
        temp = A[i]
        A[i] = A[max]
        A[max] = temp
        Heapify(A,n,max)


def Heapsort(A):
    n = len(A)

    for i in range(n, -1, -1):
        Heapify(A,n,i)
    
    for i in range(n-1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp

        #A[n-1] = A[n-2]
        Heapify(A, i, 0)

A = [3, 4, 12, 5 ,37, 26, 1] 
Heapsort(A)

n = len(A)
print("sorted array: ")
for i in range(n):
    print("%d" % A[i], end=" ")

#it doesnt sort 37 correctly, the rest is fine