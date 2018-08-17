input_lists = [
[3,3,3,3,3,3,3,3,3,3,3,3,5,3],
[5,7,8,9,4,6],
[2,3,4,5,5,8]
]
x = 5


magic_index_input_lists = [
[-1,0,1,3,8,9],
[-4,-5,0,2,4],

]



def test_binarySearch(input_lists, x):
    print 'testing binarySearch() ---'
    #for ip_list in input_lists:
    #    ip_list.sort()
    #    print 'binarySearch: input={}, searching={}, index={}'.format(ip_list, x, binarySearch(ip_list, x))
    #    print 'binarySearchRecursive_helper: input={}, searching={}, index={}'.format(ip_list, x, binarySearchRecursive_helper(ip_list, x))
    #    print 'binarySearch_Last: input={}, searching={}, index={}'.format(ip_list, x, binarySearch_Last(ip_list, x))
    #    print 'binarySearch_First: input={}, searching={}, index={}'.format(ip_list, x, binarySearch_First(ip_list, x))
        
    for ip_list in magic_index_input_lists:
        print 'binarySearchMagicIndex_helper: input={}, index={}'.format(ip_list, binarySearchMagicIndex_helper(ip_list))
        
############################################################
# binary search - sorted array
# works with repeating elements in the list
        
def binarySearch(input_list, x):
    """
    binary search on a sorted list
    None - when element not found
    index - when element found
    """
    left = 0
    right = len(input_list)-1
    while left <= right:
        mid = (left+right)/2
        if x > input_list[mid]:
            left = mid+1
        elif x < input_list[mid]:
            right = mid-1
        else:
            return mid
    return None
    
############################################################
# binary search recursive method - sorted array
# works with repeating elements in the list

def binarySearchRecursive(x, left, right, ip_list):
    if left <= right:
        mid = (left+right)/2
        if x > ip_list[mid]:
            return binarySearchRecursive(x, mid+1, right, ip_list)
        elif x < ip_list[mid]:
            return binarySearchRecursive(x, left, mid-1, ip_list)
        else:
            return mid
            
def binarySearchRecursive_helper(ip_list, x):
    return binarySearchRecursive(x, 0, len(ip_list)-1, ip_list)


############################################################
# binary search last - sorted array
# e.g. [3,5,6,7,7,8]. Index of 7 is 4
# works with repeating elements in the list
    
def binarySearch_Last(ip_list, x):
    left = 0
    right = len(ip_list)-1
    last = None
    while left <= right:
        mid = (left+right)/2
        if x > ip_list[mid]:
            left = mid+1
        elif x < ip_list[mid]:
            right = mid-1
        else:
            last = mid
            left = mid+1
    return last


############################################################
# binary search first - sorted array
# e.g. [3,5,6,7,7,8]. Index of 7 is 3
# works with repeating elements in the list

def binarySearch_First(ip_list, x):
    left = 0
    right = len(ip_list)-1
    first = None
    while left <= right:
        mid = (left+right)/2
        if x > ip_list[mid]:
            left = mid+1
        elif x < ip_list[mid]:
            right = mid-1
        else:
            first = mid
            right = mid-1
    return first
    
############################################################
# binary search magic index - sorted array
# i.e. find index in sorted array such that ip_list[i]==i
# e.g. [-1,0,1,3,8,9]. Magic index is 3.
# NOTE: tests indicate that this algo goes in infinite loop when list has repeating elements. Example: [3,5,6,7,7,8]
# this can also be made non-recursive like the implementation of binarySearch()

def binarySearchMagicIndex(ip_list, left, right):
    while left <= right:
        mid = (left+right)/2
        if ip_list[mid] == mid:
            return mid        
        elif mid > ip_list[mid]:
            return binarySearchMagicIndex(ip_list, mid+1, right)
        else:    
            return binarySearchMagicIndex(ip_list, left, mid-1)

def binarySearchMagicIndex_helper(ip_list):
    return binarySearchMagicIndex(ip_list, 0, len(ip_list)-1)
    

    
if __name__ == '__main__':
    print 'searching x={}'.format(x)    
    test_binarySearch(input_lists, x)

    
