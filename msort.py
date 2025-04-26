def mergesort(A):
    if len(A) > 1:
        mid= len(A)//2
        left= A[:mid]
        right= A[mid:]
        
        
        #recursive call on each half
        mergesort(left)
        mergesort(right)
        
        #two iterators for traversing the two halves
        i= 0
        j= 0
        
        #iterator for the main array
        k= 0
        
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                #the value rom the left half has been used
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            #move to the next slot
            k += 1
            
            #for all the remaining values
            while i < len(left):
                A[k] = left[i]
                i+=1
                k+=1
                
            while j < len(right):
                A[k] = right[j]
                j+=1
                k+=1
                
A= [59,45,23,34,66,87,90,79]
print("Unsorted Array: {}".format(A))
mergesort(A)
print("Sorte Array: {}".format(A))