import sys, os, copy

ip_lists = [
    [5, 8, 1, 3, 7, 9, 2],
    [8, 7, 5, 2, 3, 4, 1, 0],
    [12, 2, 13, 4, 25],
    [2, 32, 4, 5, 7, 8, 4, 5],   # QS low-key not working for this case!
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
        for i in range(n - 1):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


############################################################
# selection sort - ascending

def selectionSort(arr):
    """
    this will modify the object directly. So no need to return
    """
    n = len(arr)
    for i in range(n - 1):
        mi = i  # index for min value
        for j in range(i + 1, n):
            if arr[j] < arr[mi]:
                mi = j  # update the index for min value

        # swap with index of min value
        if mi != i:
            arr[mi], arr[i] = arr[i], arr[mi]


############################################################
# merge sort - ascending
# Merges two subarrays of arr[]. 
#   First subarray is arr[l..m] 
#   Second subarray is arr[m+1..r]

def merge(arr, l, m, r):
    new = list()  # add sorted list to new array, and replace in original at the end
    i = l
    j = m + 1

    while i <= m and j <= r:
        if arr[i] < arr[j]:
            new.append(arr[i])
            i += 1
        else:
            new.append(arr[j])
            j += 1

    while i <= m:
        new.append(arr[i])
        i += 1

    while j <= r:
        new.append(arr[j])
        j += 1

    arr[l:r + 1] = new  # r+1 i.e. include r as well in the range


# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) / 2

        # Sort first and second halves 
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # merge the sorted halves
        merge(arr, l, m, r)


# https://www.geeksforgeeks.org/python-program-for-quicksort/
def quick_sort(arr):
    def partition(low, high):
        i = low  # index to start putting elements on the left from
        pivot = arr[high]  # can be any random value - at x`min/max/median(index, not value) of the range

        # go until one element before the last, as the last will be swapped, since its the pivot
        for j in range(low, high):
            # move elements lower than pivot to the left hand side
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]  # move the pivot here to ensure its included in the range
        return i  # this is the last point till which the elements have been pivoted

    def quicksort(low, high):
        if low < high:
            # get partitioned sub-ranges
            pi = partition(low, high)

            # sort sub-ranges
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)

    quicksort(0, len(arr) - 1)


def quick_sort_low_key(arr):
    def partition(low, high):
        # since setting pivot as 'low', start an element after that
        i = low + 1
        pivot = arr[low]

        # need to go until the from an element after the first element(pivot) to the very last element
        # in the range now
        for j in range(low + 1, high + 1):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i - 1], arr[low] = arr[low], arr[i - 1]
        return i

    def quicksort(low, high):
        #raw_input('{}:{}'.format(low, high))
        if low < high:
            # get partitioned sub-ranges
            pi = partition(low, high)

            # sort sub-ranges
            quicksort(low, pi - 1)
            quicksort(pi, high-1) ### SOME PROB HERE

    quicksort(0, len(arr) - 1)


# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        # Keep moving the elements up till find an element where the key>arr[j]. This is where the key
        # needs to be inserted
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':

    for ip_list in ip_lists:
        # shallow copy -- a regular python copy a=b is a shallow copy. A shallow copy will result in another reference pointing to the same object
        # deep copy -- deep copy will create a new object same as original object, and the new reference will point to the new object

        print '\n\n*** INPUT = {}'.format(ip_list)

        #qs_list = copy.deepcopy(ip_list)
        #quick_sort(qs_list)
        #print 'High Key: Quick Sort = {}'.format(qs_list)

        qs_list = copy.deepcopy(ip_list)
        quick_sort_low_key(qs_list)
        print 'Low Key: Quick Sort = {}'.format(qs_list)
        raw_input()
        continue

        is_list = copy.deepcopy(ip_list)
        insertion_sort(is_list)
        print 'Insertion Sort = {}'.format(is_list)

        bubbleSort_list = copy.deepcopy(ip_list)
        bubbleSort(bubbleSort_list)
        print 'Bubble Sort = {}'.format(bubbleSort_list)

        selectionSort_list = copy.deepcopy(ip_list)
        selectionSort(selectionSort_list)
        print 'Selection Sort = {}'.format(selectionSort_list)

        mergeSort_list = copy.deepcopy(ip_list)
        mergeSort(mergeSort_list, 0, len(mergeSort_list) - 1)
        print 'Merge Sort = {}'.format(mergeSort_list)
