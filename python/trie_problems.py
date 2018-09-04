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
        return ord(ch)-ord('a')  # with reference to 'a' here, but not needed as reference
 
 
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
              "Present in tire"]
 
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
        word_dict[word] = 1
    # NxM matrix
    matrix = list()
    matrix.append(['G', 'A', 'T'])
    matrix.append(['A', 'E', 'E'])
    matrix.append(['G', '0', 'T'])
    
    # --------------------------
    # SOLUTION -1
    # Compare with dict 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print 'm={}'.format(matrix[i][j])
 
if __name__ == '__main__':
    main()

