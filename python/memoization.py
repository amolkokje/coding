#### DECORATORS

# function to for memoize decorator for functions that takes in multiple args
# if you want one function for all
def memoize_multi_args(func):
    cache_dict = dict()

    def wrapper(*args, **kwargs):
        key = str(args) + str(**kwargs)
        if key not in cache_dict.keys():
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return wrapper


# function to for memoize decorator for functions that take in a single argument
# pythonic, fast
def memoize_single_arg(func):
    class memodict(dict):
        def __missing__(self, key):
            self[key] = func(key)
            return self[key]

    return memodict().__getitem__


#### FACTORIAL

def fact_normal(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact


@memoize_single_arg
def fact_memoize_single(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact_memoize_single(x - 1)


@memoize_multi_args
def fact_memoize_multi(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact_memoize_multi(x - 1)


#### FIND DISTANCE BETWEEN 2 POINTS IN A MATRIX
# Assumption: dest >= src

def is_valid(src, pt):
    """ if the pt is before src, then it is invalid """
    if pt[0] >= src[0] and pt[1] >= src[1]:
        return True
    else:
        return False


def unique_paths(src, dest):
    if src == dest:
        # reached the src from the destination, return 1 to indicate a path has been identified
        print '***REACHED***'.format()
        return 1

    else:
        c = 0
        # for all the valid pts from the dest, see if the path reaches the src. If it does, then add the count
        for pt in [(dest[0] - 1, dest[1] - 1), (dest[0] - 1, dest[1]), (dest[0], dest[1] - 1)]:
            if is_valid(src, pt):
                c += unique_paths(src, pt)
        # return the sum of all paths found
        return c


@memoize_multi_args
def unique_paths_memoize(src, dest):
    if src == dest:
        print '***REACHED***'.format()
        return 1

    else:
        c = 0
        for pt in [(dest[0] - 1, dest[1] - 1), (dest[0] - 1, dest[1]), (dest[0], dest[1] - 1)]:
            if is_valid(src, pt):
                c += unique_paths_memoize(src, pt)
        return c


if __name__ == '__main__':
    nums = [1, 0, 5, 6]
    for num in nums:
        print 'num={}, fact={}, fact_memoizeS={}, fact_memoizeMulti={}'.format(
            num, fact_normal(num), fact_memoize_single(num), fact_memoize_multi(num))

    print '****************************************'
    src_dest_pts = [[(1, 1), (2, 6)],
                    [(1, 1), (3, 6)]
                    ]

    print ' *** NO MEMOIZATION - You can see that the function has to recurse so many times!'
    for src_dest_pt in src_dest_pts:
        print 'src={}, dest={}, paths={}'.format(src_dest_pt[0],
                                                 src_dest_pt[1],
                                                 unique_paths(src_dest_pt[0], src_dest_pt[1]))

    print ' *** MEMOIZATION - You can see here that the function uses cached values and returns fast as it does' \
          'not need to recurse'
    for src_dest_pt in src_dest_pts:
        print 'src={}, dest={}, paths={}'.format(src_dest_pt[0],
                                                 src_dest_pt[1],
                                                 unique_paths_memoize(src_dest_pt[0], src_dest_pt[1]))
