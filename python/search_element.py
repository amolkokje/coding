input_lists = [
[3,3,3,3,3,3,3,3,3,3,3,3,5,5],
[5,7,8,9,4,6]
]
x = 5

def test_binarySearch(input_lists, x):
    print 'testing binarySearch() ---'
    for ip_list in input_lists:        
        print 'input={}, searching={}, index={}'.format(ip_list, x, binarySearch(ip_list, x))


def binarySearch(input_list, x):
    """
    binary search on a sorted list
    None - when element not found
    index - when element found
    """
    left = 0
    right = len(input_list)-1
    while(left <= right):
        mid = (left+right)/2
        if x > input_list[mid]:
            left = mid+1
        elif x < input_list[mid]:
            right = mid-1
        else:
            return mid
    return None
    
    
if __name__ == '__main__':
    print 'searching x={}'.format(x)    
    test_binarySearch(input_lists, x)

    
