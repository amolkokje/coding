import sys, copy

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
    

## Q:: Find total unique paths from a point in matrix to another point in matrix    
   
def unique_paths(stop_x, stop_y, start_x, start_y, m, n, visited_cells_orig):
    if stop_x == start_x and stop_y == start_y:
        return 1
        
    visited_cells = copy.deepcopy(visited_cells_orig)
    visited_cells[stop_x][stop_y] = True
        
    no_paths = 0
    if stop_x-1 >= 0 and not visited_cells[stop_x-1][stop_y]:
        no_paths += unique_paths(stop_x-1, stop_y, start_x, start_y, m, n, visited_cells)

    if stop_y-1 >= 0 and not visited_cells[stop_x][stop_y-1]:
        no_paths += unique_paths(stop_x, stop_y-1, start_x, start_y, m, n, visited_cells)        
        
    if stop_x+1 < m and not visited_cells[stop_x+1][stop_y]:
        no_paths += unique_paths(stop_x+1, stop_y, start_x, start_y, m, n, visited_cells)

    if stop_y+1 < n and not visited_cells[stop_x][stop_y+1]:
        no_paths += unique_paths(stop_x, stop_y+1, start_x, start_y, m, n, visited_cells)            
    
    return no_paths
   
  
## Q:: Generate permutations of a list

def generate_permutations(ip_list, take_count):
    
    print 'Generating permutations for {}, taking only {} at a time'.format(ip_list, take_count)
    n = len(ip_list)
    visited = [None]*n
    depth = 0
    word = []
    
    def permute(ip_list, word_orig, visited_orig, i):
        """
        ip_list --> input list
        word --> string generated so far
        visited_ --> list of visited cells
        i --> index of cell to visit
        """
        
        if visited_orig[i]:
            return
        
        visited = copy.deepcopy(visited_orig)
        word = copy.deepcopy(word_orig)
        
        word.append(ip_list[i])        
        visited[i] = True
        
        if len(word) == take_count:
            print 'PERMUTATION = {}'.format(''.join(word))
            return
            
        for k in range(n):
            permute(ip_list, word, visited, k)
            
    for i in range(n):
        permute(ip_list, word, visited, i)
        
        
        
        
        
    
   
if __name__ == '__main__':

    """
    for num in [2, 45546, 1, 0, -3242]:
        calculate_twos(num)
    """

    arr = [2,3,4,5,6,7]
    arr.sort()
    print two_numbers_sum_target(arr, 5)
    print three_numbers_sum_target(arr, 12)

    # m-rows, n-cols    
    m = 3
    n = 7
    start_x, start_y = 1, 1
    stop_x, stop_y = 2, 6
    print 'no of paths with matrix {}x{} from ({},{}) to ({},{}) are {}'.format(m,n,start_x,start_y, stop_x,stop_y, unique_paths(stop_x=2, stop_y=6, start_x=1, start_y=1, m=m, n=n, visited_cells_orig=[ [None]*n for _ in range(m) ]))

    # permutations
    ip_word_list = ["AMOL", "AMI"]
    for ip_word in ip_word_list:
        generate_permutations(ip_list=ip_word, take_count=2)