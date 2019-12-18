import sys, os, copy


# SAMPLE QUESTION: Text app, suggestions. Write a function that would return list of suggestions to display.
# SAMPLE QUESTION: Implement auto-complete
# - As you start typing, suggestions are prompted --> Trie
# - The suggestions are listed in the order of priority for most used/context -> Weights

class WeigthedTrieNode(object):
    """ node that also tracks the weight or the number of times this word was looked up """

    def __init__(self, value):
        self.value = value
        self.children = list()
        self.end_of_word = False  # indicates if node is end of word
        self.weight = None


class WeightedTrie(object):
    """ trie with additional functionality """

    def __init__(self):
        self.root = WeigthedTrieNode(None)  # Trie root node is always None valued
        self.max_depth = 0  # max depth of the trie tree

    def insert(self, word):
        """ insert word in the trie """
        # start from root
        current = self.root
        n = len(word)

        # check if each letter of the word exists in the trie tree
        i = 0
        while i < n:
            node_found = False

            # check if the char exists in trie tree, and if it does go to it
            for trie_node in current.children:
                if trie_node.value == word[i]:
                    current = trie_node
                    i += 1
                    node_found = True
                    break

            # if the char does not exist, then add and go to it
            if not node_found:
                new_trie_node = WeigthedTrieNode(word[i])
                current.children.append(new_trie_node)
                current = new_trie_node
                i += 1

        # for the last char added, set the end_of_word=True as it is end of word
        current.end_of_word = True
        current.weight = 0

        if n > self.max_depth:
            self.max_depth = n

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

        # if end of word reached, then increment weight to indicate popularity/frequency of access
        if current.end_of_word:
            current.weight += 1

        return (True, True if current.end_of_word else False)

    def search_prefix(self, word_prefix):
        words_with_prefix_list = list()
        word = word_prefix

        prefix_found, end_of_word = self.search(word_prefix)
        if not prefix_found:
            return words_with_prefix_list

        # go till the prefix node
        current = self.root
        word_formed = ''

        ###########################
        # 1 - reach prefix node

        n = len(word_prefix)
        i = 0

        while i < n:

            for trie_node in current.children:
                if trie_node.value == word[i]:
                    current = trie_node
                    i += 1
                    word_formed += trie_node.value
                    break

            if word_formed == word_prefix:
                break

        ###########################
        # 2 - get all words from the prefix
        all_words_weights = list()  # list to store all words with that prefix

        def _get_words(current_node, word_formed):
            """ helper method to recurse DFS to create words starting from the prefix """
            word_formed_local = copy.deepcopy(word_formed)
            for child in current_node.children:
                if child.end_of_word:
                    all_words_weights.append((word_formed_local + child.value, child.weight))
                _get_words(child, word_formed_local + child.value)

        # recurse DFS to create list of all words formed from the prefix node onwards
        _get_words(current, word_formed)
        return all_words_weights

    def sort_words_by_weights(self, words_weights_list):
        """ sorts the words found by their weights to return """
        n = len(words_weights_list)
        for _ in range(n):
            for i in range(n - 1):
                if words_weights_list[i][1] < words_weights_list[i + 1][1]:
                    words_weights_list[i], words_weights_list[i + 1] = \
                        words_weights_list[i + 1], words_weights_list[i]
        return words_weights_list


if __name__ == '__main__':

    input_words = ['AMOL', 'KOKJE', 'AMEYA', 'ANAND', 'ANITA']
    words_trie = WeightedTrie()
    for word in input_words:
        words_trie.insert(word)

    # create some hits
    words_trie.search('AMOL')
    words_trie.search('AMOL')
    words_trie.search('AMOL')

    words_trie.search('AMEYA')
    words_trie.search('AMEYA')

    words_trie.search('ANAND')
    words_trie.search('ANAND')
    words_trie.search('ANAND')
    words_trie.search('ANAND')
    words_trie.search('ANAND')

    prefixes = ['A', 'AM', 'AN']
    for prefix in prefixes:
        words_with_prefix = words_trie.search_prefix(prefix)
        print 'PREFIX={}, WORDS WITH PREFIX={}'.format(prefix, words_with_prefix)

        words_with_prefix_sorted = words_trie.sort_words_by_weights(words_with_prefix)
        print 'PREFIX={}, WORDS SORTED BY WEIGHTS={}'.format(prefix, words_with_prefix_sorted)
