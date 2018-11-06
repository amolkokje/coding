
ip_lists = [
[8,7,5,2,3,4,1,0],
[12,2,13,4,25],
[2,32,4,5,7,8,4,5],
]

## python listName.sort() method sorts the list in place

############################################################
# bubble sort - ascending

def bubbleSort(arr):
    """
    this will modify the object directly. So no need to return
    """
    n = len(arr)
    for _ in range(n):
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
    

############################################################
# selection sort - ascending

def selectionSort(arr):
    """
    this will modify the object directly. So no need to return
    """
    n = len(arr)
    for i in range(n-1):
        mi = i
        # find index for min value
        for j in range(i+1, n):
            if arr[j] < arr[mi]: 
               mi = j
        # swap with index of min value    
        if mi != i:
            arr[mi], arr[i] = arr[i], arr[mi]
                


############################################################
# merge sort - ascending
# Merges two subarrays of arr[]. 
#   First subarray is arr[l..m] 
#   Second subarray is arr[m+1..r] 
import copy      

def merge(arr, l, m, r): 

    # NOTE: When slicing arrays, note that the last index is not included. Eg. d=range(5) -> d[3:5]=[3,4]     
    L = copy.deepcopy( arr[l:m+1] )  # l->m ---- this will give equal division because m=(l+r)/2 will give us floor value in m
    R = copy.deepcopy( arr[m+1:r+1] )  # m+1->r
    n1 = len(L)
    n2 = len(R)
    
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1            
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1    
    
    # Copy the remaining elements of L[], if there are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there are any 
    while j < n2:     
        arr[k] = R[j] 
        j += 1
        k += 1

        
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r:   
        m = (l+r)/2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        
        # merge the sorted halves
        merge(arr, l, m, r)     
        
    
    
if __name__=='__main__':
    import copy
    for ip_list in ip_lists:
        # shallow copy -- a regular python copy a=b is a shallow copy. A shallow copy will result in another reference pointing to the same object
        # deep copy -- deep copy will create a new object same as original object, and the new reference will point to the new object
        
        bubbleSort_list = copy.deepcopy(ip_list) 
        bubbleSort(bubbleSort_list)
        print bubbleSort_list
                
        selectionSort_list = copy.deepcopy(ip_list) 
        selectionSort(selectionSort_list)
        print selectionSort_list
        
        mergeSort_list = copy.deepcopy(ip_list)
        mergeSort(mergeSort_list, 0, len(mergeSort_list)-1)  
        print mergeSort_list
        
        ip_list.sort()
                
        assert ip_list == bubbleSort_list == selectionSort_list == mergeSort_list, 'Lists not sorted correctly: ip_list={}, bubble_sort={}, selection_sort={}, mergeSort_list={}'.format(ip_list, bubbleSort_list, selectionSort_list, mergeSort_list)        
        
