import sys
import copy

"""
ML Onsite - Hardik Shah
Q:: Given a NxN matrix and a dictionary of words. print all the words in the matrix that exist in the dictionary.
"""

# SOLUTION - navigate through each element of the matrix, and compare found words with words in a dict
# comparison can be made easy by storing words from dict in a trie/prefix tree

# SOLUTION -1
# Compare with dict 


# SOLUTION -2    
# Compare by converting dict to trie

# TRIE IMPLEMENTATION:
# Python implementation: https://www.geeksforgeeks.org/trie-insert-and-search/ --> not required to know
# need to know what trie is: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

# Ref: https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
"""
Its worth mentioning that search engines probably have more complexity to their tries, since they will return certain 
terms based on how popular they are, and likely have some additional logic to determine the weight associated with 
certain terms in their trie structures. 
"""


# APPLICATIONS:
# 1. Storing Dictionary (smaller space -> nodes with letters instead of many strings, faster search
# -> DFS instead of iterating through a list)
# 2. Auto Complete (Trie + Weights on nodes to indicate popularity)

# Python program for insert and search operation in a Trie

class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self.children = list()
        self.end_of_word = False  # indicates if node is end of word

    def __repr__(self):
        return '<TN:{}:{}>'.format(self.value, self.end_of_word)


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)  # Trie root node is always None valued

    def insert(self, word):
        """ insert word in the trie """
        # start from root
        current = self.root

        # check if each letter of the word exists in the trie tree
        for w in word:
            node_found = None

            # check if the char exists in trie tree, and if it does go to it
            for trie_node in current.children:
                if trie_node.value == w:
                    node_found = trie_node
                    break

            # if the char does not exist, then add and go to it
            if node_found is not None:
                current = node_found
            else:
                new_trie_node = TrieNode(w)
                current.children.append(new_trie_node)
                current = new_trie_node

        # for the last char added, set the end_of_word=True as it is end of word
        current.end_of_word = True

    def search(self, word):
        """ search for word in the trie. Return a tuple containing info (str_can_form_a_word, found_word) """
        current = self.root
        n = len(word)

        i = 0
        while i < n:
            node_found = False

            for trie_node in current.children:
                if trie_node.value == word[i]:
                    current = trie_node
                    i += 1
                    node_found = True
                    break

            if not node_found:
                return (False, False)

        return (True, True if current.end_of_word else False)

    def search_prefix(self, prefix):

        # go till the last letter node
        current = self.root
        for w in prefix:
            found = False
            for child in current.children:
                if child.value == w:
                    current = child
                    found = True
            if not found:
                # There is no word for the prefix
                return

        # have reached current, so from here find the words that can be formed
        output = list()

        def _recurse(node, formed):
            if node.end_of_word:
                output.append(formed)

            if node.children:
                for child in node.children:
                    _recurse(child, formed + child.value)

        _recurse(current, prefix)
        return output

    def remove(self, word):
        print 'removing {}'.format(word)
        current = self.root

        # recurse till the end of word, and delete nodes as you come back up
        # - if the node has no children, delete it
        # - if the node has children, then just mark the end_of_word as False

        node_stack = list()

        # go to the end of the word and come back up
        for w in word:
            found = None
            for node in current.children:
                if w == node.value:
                    found = node
                    break
            if found is not None:
                current = found
                node_stack.append(current)
            else:
                # word is not found
                return

        #print 'node stack = {}'.format(node_stack)

        ## reached the end of word - so it has to be a word. If not, do not attempt to delete

        remove_child = None

        # last node is a special case
        # if the last node has children, mark it as not the end and return. No need to delete anything
        current = node_stack.pop(-1)
        if current.children:
            current.end_of_word = False
            return
        else:
            remove_child = current

        # if last node does not have children, then keep on deleting until reach:
        # - node with end_of_word
        # - node with children

        while node_stack:
            current = node_stack.pop(-1)

            if remove_child is not None:
                #print '---> removing child {}'.format(remove_child)
                for i in range(len(current.children)):
                    if current.children[i].value == remove_child.value:
                        current.children.pop(i)
                        break

            if len(current.children)>0 or current.end_of_word:
                #print '--> has children OR end of word'
                return

            remove_child = current

    def show(self):
        output = list()

        def _recurse(node, formed):
            if node.end_of_word:
                output.append(formed)

            for child in node.children:
                _recurse(child, formed + child.value)

        _recurse(self.root, '')
        return output


#######################################################
## SOLUTION -1 
#######################################################

def matrix_search_simple(matrix, words_dict):
    m = len(matrix)  # no of rows
    n = len(matrix[0])  # no of cols

    print '*****\nSimple Matrix Search ----'

    def matrix_search(is_visited, x, y, letter_list):

        """
        - Python variables are names/aliases to objects, so changing a variable will change the object too.
        - This is very important to understand when passing "mutable"(list, dict, set) vales to a function as it passes
        the name/alias to the object, and modifying the variable changes the original object.
        - So, you only want to use the value, then its okay, but if you want to modify the value and then use it, do a
        deepcopy to copy the whole object. Shallow copy(default copy using operator =) will create another name/alias
        for the object.
        
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
        if is_visited[x][y]:
            return

        letter_list_local = copy.deepcopy(letter_list)
        letter_list_local.append(matrix[x][y])

        is_visited_local = copy.deepcopy(is_visited)
        is_visited_local[x][y] = True

        word = ''.join(letter_list_local)
        if word in words_dict.keys():
            print 'Found word = {}'.format(word)

        if (x - 1 >= 0) and (not is_visited_local[x - 1][y]):
            matrix_search(is_visited_local, x - 1, y, letter_list_local)

        if (x + 1 < m) and (not is_visited_local[x + 1][y]):
            matrix_search(is_visited_local, x + 1, y, letter_list_local)

        if (y - 1 >= 0) and (not is_visited_local[x][y - 1]):
            matrix_search(is_visited_local, x, y - 1, letter_list_local)

        if (y + 1 < n) and (not is_visited_local[x][y + 1]):
            matrix_search(is_visited_local, x, y + 1, letter_list_local)

    for i in range(m):
        for j in range(n):
            ## to track if the cell in the matrix has been visited            
            """
            # The below with not work with mutable types and will give weird behvior. 
            Reference: https://stackoverflow.com/questions/13382774/initialize-list-with-same-bool-value            
            # mat = [[0]*3]*3
            # mat[0][0] = 1, will change all cause [[1,0,0], [1,0,0], [1,0,0]] 
            # Solution -- use comprehension instead, as below
            """
            is_visited = [[False for _ in range(n)] for _ in range(m)]

            print 'Starting Search from element [{},{}]'.format(i, j)
            matrix_search(is_visited, i, j, list())


#######################################################
## SOLUTION -2
#######################################################

def matrix_search_trie(matrix, words_dict):
    m = len(matrix)  # no of rows
    n = len(matrix[0])  # no of cols

    print '*****\nTrie Matrix Search ----'

    # store all words in a trie
    words_trie = Trie()
    for word in words_dict.keys():
        words_trie.insert(word)

    def matrix_search(is_visited, x, y, letter_list):
        """ helper method to recurse search """
        if is_visited[x][y]:
            return

        letter_list_local = copy.deepcopy(letter_list)
        letter_list_local.append(matrix[x][y])

        is_visited_local = copy.deepcopy(is_visited)
        is_visited_local[x][y] = True

        word = ''.join(letter_list_local)
        search, end_of_word = words_trie.search(word)

        if search:
            # if found, and is end of word, then print it
            if end_of_word:
                print 'Found word = {}'.format(word)

            # look for other words
            if (x - 1 >= 0) and (not is_visited_local[x - 1][y]):
                matrix_search(is_visited_local, x - 1, y, letter_list_local)

            if (x + 1 < m) and (not is_visited_local[x + 1][y]):
                matrix_search(is_visited_local, x + 1, y, letter_list_local)

            if (y - 1 >= 0) and (not is_visited_local[x][y - 1]):
                matrix_search(is_visited_local, x, y - 1, letter_list_local)

            if (y + 1 < n) and (not is_visited_local[x][y + 1]):
                matrix_search(is_visited_local, x, y + 1, letter_list_local)

        else:
            # if not found, then return
            return

    for i in range(m):
        for j in range(n):
            ## to track if the cell in the matrix has been visited            
            is_visited = [[False for _ in range(n)] for _ in range(m)]
            print 'Starting Search from element [{},{}]'.format(i, j)
            matrix_search(is_visited, i, j, list())


# driver function
def main():
    # -------------------------
    keys = ["the", "a", "there", "anaswe", "any", "by", "their", "therea", "thereab"]
    test_trie = Trie()
    for k in keys:
        test_trie.insert(k)

    print test_trie.show()
    test_trie.remove("therea")
    print test_trie.show()
    test_trie.remove("thereab")
    print test_trie.show()
    sys.exit()

    check_keys = ['the', 'these', 'their', 'thaw', 'ana', 'b']
    for ck in check_keys:
        print 'ck={}, search_exists={}'.format(ck, test_trie.search(ck))

    # ---------------------
    # INPUTS for problem

    # dict of words
    words_list = ['GET', 'GATE', 'ATE', 'GAG', 'GOT', 'TAG']
    print 'WORDS LIST={}'.format(words_list)

    words_dict = dict()
    for word in words_list:
        words_dict[word] = 1

    # NxM matrix
    matrix = list()
    matrix.append(['G', 'A', 'T'])
    matrix.append(['A', 'E', 'E'])
    matrix.append(['G', 'O', 'T'])

    matrix_search_simple(matrix, words_dict)
    matrix_search_trie(matrix, words_dict)


if __name__ == '__main__':
    main()
