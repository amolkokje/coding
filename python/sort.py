
ip_lists = [
[8,7,5,2,3,4,1,0],
[12,2,13,4,25],
[2,32,4,5,7,8,4,5],
]

## python listName.sort() method sorts the list in place

############################################################
# bubble sort - ascending

def bubbleSort(ip_list):
    """
    this will modify the object directly. So no need to return
    """
    list_length = len(ip_list)
    for i in range(list_length):
        for j in range(list_length-1):
            if i > j and ip_list[j] > ip_list[i]:
                ip_list[i], ip_list[j] = ip_list[j], ip_list[i]
    

############################################################
# selection sort - ascending

def selectionSort(ip_list):
    """
    this will modify the object directly. So no need to return
    """
    list_length = len(ip_list)
    for i in range(list_length-1):
        min_index = i
        for j in range(i+1, list_length):
            if ip_list[i] > ip_list[j]:
                ip_list[i], ip_list[j] = ip_list[j], ip_list[i]
    


############################################################
# merge sort - ascending
# Merges two subarrays of arr[]. 
#   First subarray is arr[l..m] 
#   Second subarray is arr[m+1..r] 
def merge(arr, l, m, r): 
    
    n1 = (m + 1) - l
    n2 = r - m  
    
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(n1): 
        L[i] = arr[l + i] 
  
    for j in range(n2): 
        R[j] = arr[(m + 1) + j] 
        
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
            k += 1
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
        
