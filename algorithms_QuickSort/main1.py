
# normal quicksort

''' 
def Quicksort(A, l, r): #left and right slots
    if (r-l) < 1: # if the rightmost element is smaller or equal to one return  -> if the array is 1 or 0 elements 
        return
    else: 
        part = Partition(A,l,r) #partition the array, return the parting element 
        Quicksort(A, l, part-1)
        Quicksort(A, part+1,r)
        print("left", (A, l, part-1))
        print("right", (A, part+1,r))
        
 
def Partition(A,l,r): 
    piv = r
    div = l 

    for j in range(l, r): #j is l+1 (index 1) to r(index n-1)
        if A[j] <= A[piv]: #if j in the Array is smaller than the random number chosen as pivot 

            temp = A[j]
            A[j] = A[div]
            A[div] = temp

            div += 1 
   
            
        else: #if j in the Array is bigger than pivot   #swaping the last element with the divider 
            temp = A[piv] 
            A[piv] = A[div]
            A[div] = temp

            div += 1 #!!!!!
   
    return div

#Array
A = [7, 3, 26, 8, 5, 53, 4] 
A2 = [7, 16 , 32, 5, 8 ,66, 3, 56]  
n = len(A)

Quicksort(A, 0, n-1)


print("sorted array:")
print(A)

'''


#randomized quicksort 
import random 

def Quicksort(A, l, r): #left and right slots
    if (r-l) <= 1: # if the rightmost element is smaller or equal to one return  -> if the array is 1 or 0 elements 
        return
    else:
        print("a:", A)
        p = ChoosePivot(l,r) #pivot function
        part = Partition(A,p,l,r) #partition the array, return the parting element 
        Quicksort(A, l, part-1)
        Quicksort(A, part+1,r)
        print("left", (A, l, part-1))
        print("right", (A, part+1,r))
        
 
def Partition(A,p,l,r): 
    temp = A[r] #change random pivot with the rightmost element
    A[r] = A[p]
    A[p] = temp
    
    piv = r #set the previously chosen pivot as current pivot (since it is the rightmost element, you use r)
    div = l
    
    
    for j in range(l, r): 
        if A[j] <= A[piv]: #if j in the Array is smaller than the random number chosen as pivot
                    temp = A[j]
                    A[j] = A[div]
                    A[div] = temp

                    div += 1

        else:
            temp = A[piv] 
            A[piv] = A[div]
            A[div] = temp

            div += 1 #!!!!

    return div

def ChoosePivot(l, r):
    piv = random.randrange(l,r) #randomly chooses pivot 
    print("piv", piv)
    return piv
    

#Array
A = [7, 3, 26, 8, 5, 53, 4] 
A2 = [7, 16, 32, 5, 8, 66, 3, 56]
n = len(A2)

Quicksort(A2, 0, n-1)


print("sorted array:")
print(A2)
