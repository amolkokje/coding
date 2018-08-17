


############################################################
# factorial - whole numbers i.e. >=0

def factorial(x):
    fact = 1
    if not x <= 1:
        for i in range(1, x+1):
            fact *= i
    return fact
       

############################################################
# factorial recursive method - whole numbers i.e. >=0

def factorialRecursive(x):
    if x <= 1:
        return 1
    return x*factorialRecursive(x-1)
    
    
############################################################
# factorial recursive method, with cache - whole numbers i.e. >=0
# Memoization - In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again
# 

def memoize(func):
    class memodict(dict):
        # this will cache if the element does not exist in the dict
        def __missing__(self, key):
            print 'caching {}'.format(key)
            ret = self[key] = func(key)
            return ret
    # need to return a callable, so returning the __getitem__() method
    return memodict().__getitem__
    
def memoizefunc(func):
    print 'creating cache...'
    cache = dict()
    
    def wrapper(x):
        # this will add to the existing object in memory
        if x not in cache:
            print 'caching {}'.format(x)
            cache[x] = func(x)
        return cache[x]    
    return wrapper
   
#@memoize   
@memoizefunc
def factorialMemo(x):
    return factorial(x)


    

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 9, 10, 9]
    for num in nums:
        #print 'num={}, factorial={}, factorialRecursive={}'.format(num, factorial(num), factorialRecursive(num))
        print 'num={}, factorial={}'.format(num, factorialMemo(num))