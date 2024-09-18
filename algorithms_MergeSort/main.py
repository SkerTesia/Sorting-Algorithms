def main(A,l,r):
    #n = len(A)
    if l < r: #if last element bigger than small element, then part
        mid = (l +r)//2 #first el. + last el parted into two

        main(A,l,mid) #left part sorting
        main(A, mid+1, r) #right part sorting
        merge(A,l,mid,r)

def merge(A, l, mid, r):
    n1 = mid - l + 1  
    n2 = r - mid

    L = [0]*n1 #length of left array
    R = [0]*n2 #length of right array

    for i in range(0, n1):
        L[i] = A[l+i]
    for j in range(0, n2):
        R[j] = A[mid+1+j]

    #L[n1+1] = float('inf')
    #R[n1+1] = float('inf')

    i= 0 #set i & j to zero
    j= 0 

    
    for k in range(l,r): #this part is supposedly more complex
        if L[0] < R[0]:
            A[0] = L[0]
            i += 1
        else:
            A[0] = R[0]
            j += 1
            


A = [3, 4, 12, 5 ,37, 26, 1] 
n = len(A)
main(A, 0, n-1)

print("sorted array: ")
for i in range(n):
    print("%d" % A[i], end=" ")

 