def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        
        # recursive call on each half
        mergesort(left)
        mergesort(right)
        
        # two iterators for traversing the two halves
        i = 0
        j = 0
        k = 0
        
        # merge the temp arrays back into A
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        
        # for all the remaining values
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
                
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

# take input from user
n = int(input("Enter the number of elements in the array: "))
A = []

print("Enter the elements one by one:")
for _ in range(n):
    elem = int(input())
    A.append(elem)

print("Unsorted Array:", A)
mergesort(A)
print("Sorted Array:", A)
