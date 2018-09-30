
num_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}


def compress_num(num, to_string=False):
    # convert to string to able to access as array elements
    nums = str(num)
    n = len(nums)
    say = ""
    i = 0
    
    while i < n-1:
        if nums[i] == nums[i+1]:
            c = 2
            for j in range(i+2, n):
                if nums[j] != nums[i]:
                    break
                c += 1
            
            if to_string:
                say += '{} {}s, '.format(num_map[c], nums[i])
            else:
                say += '{}{}'.format(c, nums[i])
                
            i += c
            
        else:
            if to_string:
                say += '{} {}s, '.format(num_map[1], nums[i])
            else:
                say += '{}{}'.format(1, nums[i])
            i += 1
          
    # this is to cover the case when the last digit is not compressed using the loop before, and is left out
    # just add it in
    if i == n-1:
        if to_string:
                say += '{} {}s, '.format(num_map[1], nums[i])
        else:
            say += '{}{}'.format(1, nums[i])
        
    if to_string:
        return say[:-2]  # to remove ending ', '
    else:
        return say
        

    
def LookAndSay(num, depth=1):
        
    for _ in range(depth-1):        
        num = compress_num(num)
        
    return compress_num(num, True)    
    
    
    
if __name__ == '__main__':    
    ips = [1, 11, 21, 1211, 111221]
    for ip in ips:
        print 'LookAndSay({}) = {}'.format(ip, LookAndSay(ip))
        
    n = 11
    d = 2
    print 'LookAndSay({},{}) = {}'.format(n, d, LookAndSay(n, depth=d))    
        
    