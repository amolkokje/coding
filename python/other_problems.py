import sys

## Q:: Calculate the number of 2s in numbers from 0-n

def calculate_twos(x):
    count = 0
    print 'Number of 2s in {}:'.format(x)
    x = abs(x)        
    while x >= 1:
        if x%10 == 2:
            count+=1
        x = x/10
    print count

    
## Q:: O(logN) solution to find 2 numbers in an array that sum up to a target value

def two_numbers_sum_target(arr, target):
    """    
    Binary Search approach only works with sorted array and non-repeating elements
    """
    
    def _helper(i, left, right, target):
        if left < right:
            mid = (left+right)/2
            sum = arr[i]+arr[mid]
            if (mid != i) and (sum == target):
                return mid
            if sum > target:
                right=right-1
            elif sum < target:
                left=left+1
            return _helper(i, left, right, target)    

    print 'arr={}, target={}'.format(arr, target)            
    arr_len = len(arr)   
    for i in range(arr_len):
        found = _helper(i, 0, arr_len, target)
        if found:
            return i, found
        
    
## Q:: O(logN) solution to find 3 numbers in an array that sum up to a target value    
    
def three_numbers_sum_target(arr, target):
    print 'arr={}, target={}'.format(arr, target)            
    found_list = []
    arr_len = len(arr)    
    for i in range(arr_len):
        two_sum_target = target - arr[i]
        
        for j in range(arr_len):
            if j != i:
                n1, n2 = two_numbers_sum_target(arr, two_sum_target)
                if n1 and n2:
                    return i, n1, n2
    
    
    
if __name__ == '__main__':

    """
    for num in [2, 45546, 1, 0, -3242]:
        calculate_twos(num)
    """

    arr = [2,3,4,5,6,7]
    arr.sort()
    print two_numbers_sum_target(arr, 5)
    print three_numbers_sum_target(arr, 12)

