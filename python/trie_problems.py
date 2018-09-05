import sys
import copy

"""
MagicLeap Onsite - Hardik Shah
Q:: Given a NxN matrix and a dictionary of words. print all the words in the matrix that exist in the dictionary.
"""

# SOLUTION - navigate through each element of the matrix, and compare found words with words in a dict
# comparison can be made easy by storing words from dict in a trie/prefix tree

# SOLUTION -1
# Compare with dict 


# SOLUTION -2    
# Compare by converting dict to trie
#### DONT KNOW HOW TO USE A TRIE HERE??


# TRIE IMPLEMENTATION - STUDY IF TIME?
# Python implementation: https://www.geeksforgeeks.org/trie-insert-and-search/ --> not required to know
# need to know what trie is: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

# Python program for insert and search
# operation in a Trie
 
class TrieNode:
     
    # Trie node class
    def __init__(self):
        # 26 elements for each alphabet character a-z, assume all lower case
        self.children = [None]*26
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
 
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self, ch):         
        """
        Converts key current character into index
        use only 'a' through 'z' and lower case         
        """
        #return ord(ch)-ord('a')  # with reference to 'a' here, but not needed as reference
        return ord(ch)-ord('a')
 
 
    def insert(self,key):         
        """
        If not present, inserts key into trie
        If the key is prefix of trie node, just marks leaf node
        """    
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
    def search(self, key):
        """ 
        Search key in the trie
        Returns true if key presents in trie, else false
        """
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return pCrawl != None and pCrawl.isEndOfWord
 
 
# driver function
def main():
    
    # -------------------------
    # TRIE code
    
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key)
 
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
    
    
    # ---------------------
    # INPUTS for problem
    
    # dict of words
    words_list = ['GET', 'GATE', 'ATE', 'GAG', 'GOT', 'TAG']
    word_dict = dict()
    for word in words_list:
        word_dict[word.lower()] = 1
    # NxM matrix
    matrix = list()
    matrix.append(['G', 'A', 'T'])
    matrix.append(['A', 'E', 'E'])
    matrix.append(['G', 'O', 'T'])
    
    # --------------------------
    # SOLUTION -1
    
    m = len(matrix)  # no of rows
    n = len(matrix[0])  # no of cols
    
    def matrix_search(is_visited, x, y, letter_list):
        
        """
        - Python variables are names/aliases to objects, so changing a variable will change the object too.
        - This is very important to understand when passing "mutable"(list, dict, set) vales to a function as it passes the name/alias to the object, and modifying the variable changes the original object.
        - So, you only want to use the value, then its okay, but if you want to modify the value and then use it, do a deepcopy to copy the whole object. Shallow copy(default copy using operator =) will create another name/alias for the object.        
        
        EXAMPLE-1::
        a = 5
        def test(x):
            x = 4
        test(a)    
        print a --> 5  i.e. Fine with immutable objects
     
     
        EXAMPLE-2::
        ll = ['a', 'b']
        def test2(x):
            x = [1,2,3]
        test3(ll)
        print ll --> ['a', 'b'] i.e. Fine because here 'x' points to a new object [1,2,3]
        
        EXAMPLE-3::
        ll = ['a', 'b']
        def test3(x):
            x.append('c')
        test3(ll)
        print ll --> ['a', 'b', 'c'] i.e. Not like other languages, because the object passed gets modified here.
            
        """        
        
        """
        NOTE: 
        - Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable. 
        - Objects of built-in types like (list, set, dict) are mutable. 
        - Custom classes are generally mutable
        """
        letter_list_local = copy.deepcopy(letter_list)
        letter_list_local.append(matrix[x][y])
        
        is_visited_local = copy.deepcopy(is_visited)
        is_visited_local[x][y] = True
        
        word = ''.join(letter_list_local)
        if word in word_dict.keys():
            print 'Found word = {}'.format(word)
            
        if (x-1 >= 0) and (not is_visited_local[x-1][y]):
            matrix_search(is_visited_local, x-1, y, letter_list_local)
            
        if (x+1 < m) and (not is_visited_local[x+1][y]):
            matrix_search(is_visited_local, x+1, y, letter_list_local)
            
        if (y-1 >= 0) and (not is_visited_local[x][y-1]):
            matrix_search(is_visited_local, x, y-1, letter_list_local)
            
        if (y+1 < n) and (not is_visited_local[x][y+1]):
            matrix_search(is_visited_local, x, y+1, letter_list_local)

        
    for i in range(m):
        for j in range(n):
            ## to track if the cell in the matrix has been visited            
            """
            # The below with not work with mutable types and will give weird behvior. Reference: https://stackoverflow.com/questions/13382774/initialize-list-with-same-bool-value            
            # mat = [[0]*3]*3
            # mat[0][0] = 1, will change all cause [[1,0,0], [1,0,0], [1,0,0]] 
            # Solution -- use comprehension instead, as below
            """
            is_visited = [[False for _ in range(n)] for _ in range(m)]
            
            print 'Starting Search from element [{},{}]'.format(i, j)
            matrix_search(is_visited, i, j, list())
            

            
if __name__ == '__main__':
    main()

