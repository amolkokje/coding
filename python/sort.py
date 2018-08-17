
ip_lists = [
[1,2,3,4,5],
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
            if ip_list[j] > ip_list[i]:
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
    
def mergeSort(ip_list):    
    mid = len(ip_list)/2
    lefthalf = ip_list[:mid]
    righthalf = ip_list[mid:]

    mergeSort(lefthalf)
    mergeSort(righthalf)

    i=0 # lefthalf
    j=0 # righthalf
    k=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            ip_list[k]=lefthalf[i]
            i=i+1
        else:
            ip_list[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        ip_list[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        ip_list[k]=righthalf[j]
        j=j+1
        k=k+1
    
    
    
if __name__=='__main__':
    import copy
    for ip_list in ip_lists:
        # shallow copy -- a regular python copy a=b is a shallow copy. A shallow copy will result in another reference pointing to the same object
        # deep copy -- deep copy will create a new object same as original object, and the new reference will point to the new object
        
        bubbleSort_list = copy.deepcopy(ip_list) 
        bubbleSort(bubbleSort_list)
        
        selectionSort_list = copy.deepcopy(ip_list) 
        selectionSort(selectionSort_list)
        
        mergeSort_list = copy.deepcopy(ip_list)
        mergeSort(mergeSort_list)
        
        ip_list.sort()
        
        assert ip_list == bubbleSort_list == selectionSort_list == mergeSort_list, 'Lists not sorted correctly: ip_list={}, bubble_sort={}, selection_sort={}, mergeSort_list={}'.format(ip_list, bubbleSort_list, selectionSort_list, mergeSort_list)        
        