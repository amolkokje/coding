
# ----------------------------------------------------------
# TEST-4
# ----------------------------------------------------------


class PolygonUtils:

    def __init__(self):
        pass

    # Please note that the function definition does not need the context here, and can be defined as a static
    # method here. This definition is picked up from the problem, and hence not changed.
    def is_point_in_poly(self, x, y, poly):
        n = len(poly)
        inside = False

        p1x, p1y = poly[0]
        for i in range(n+1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside


# ----------------------------------------------------------
# TEST-2
# ----------------------------------------------------------


def find_mirrors(in_file, out_file):
    """
    takes file handle for input file containing list of words, also output file handle for dumping 
    mirrored results in.
    :param in_file: input file handle used for reading file
    :param out_file: output file handle used for writing to file
    :return: None
    """
    words_list = [line.rstrip() for line in in_file.readlines()]    
    for word in words_list:
        # use slicing to get a reversed word as it is the fastest way
        reverse_word = word[::-1]
        # check the following before dumping it to output list:
        #  - if the reversed word exists in the list/input file
        #  - if palindrome i.e. the word and reversed word are not the same
        if reverse_word in words_list and reverse_word != word:
            out_file.write("{0}/{1}\n".format(word, reverse_word))
    
    
# ----------------------------------------------------------
# TEST-1
# ----------------------------------------------------------


def is_prime(num):
    """
    this function checks if a number is prime or not.
    prime number is a natural number greater than one and has no positive divisors other than 1 and itself.
    :param num: number to check
    :return: boolean
    """
    if num < 4:
        return True
    elif num >= 4:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        # not a natural number
        return False