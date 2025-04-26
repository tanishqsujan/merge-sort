#merge A1 and A2 to A3
def mergetwo(A1, A2, m, n):
    #size of A3
    A3= [None] * (m+n)
    i=0
    j=0
    k=0
    
    #traversing both arrays
    while i < m and j < n:
        #comparing the current elements of A1 and A2
        if A1[i] < A2[j]:
            A3[k] = A1[i]
            k= k+1
            i= i+1
        else:
            A3[k] = A2[j]
            k= k+1
            j= j+1
            
    
    #remaining items for first array
    while i < m:
        A3[k] = A1[i]
        k= k+1
        i= i+1
        
    #remaining items of second array
    while j < n:
        A3[k] = A2[j]
        k= k+1
        j= j+1
    print("Merged Arrays: ")
    for i in range(m + n):
        print(str(A3[i]), end = " ")
        
        
#driver code
#m is size of A1 and n is size of A2

A1= [3,5,7,9]
m= len(A1)

A2= [10,23,39,45]
n= len(A2)
mergetwo(A1, A2, m, n)
        
        