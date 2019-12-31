import sys, os, copy


class Node:
    def __init__(self, x):
        self.data = x
        self.right = None
        self.left = None

    def __repr__(self):
        return '<Node: {}>'.format(self.data)


class BinarySearchTree:
    def __init__(self, x):
        self.root = Node(x)

    def AddItem(self, x):
        current = self.root
        while current:
            if x >= current.data:
                if not current.right:
                    current.right = Node(x)
                    break
                else:
                    current = current.right
            else:
                if not current.left:
                    current.left = Node(x)
                    break
                else:
                    current = current.left

    def FindItem(self, x):
        current = self.root
        while current:
            print 'Reached: {}'.format(current.data)
            if x == current.data:
                return current
            elif x > current.data:
                current = current.right
            else:
                current = current.left

                # how to implement DeleteItem()?
                # seems to be tough as it may break the ordering in the structure
                # one way could be to break the entire tree and then reconstruct


########################################################################
# Refrence for Depth First --> PreOrder, InOrder, PostOrder: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/    

def PrintPreOrder(n):
    """
    takes the root node of BST as input and prints BST in Pre Order
    USES:
    - Used to create a copy of the tree. 
    - Used to get prefix expression on of an expression tree.
    """
    if n:
        print n.data
        PrintPreOrder(n.left)
        PrintPreOrder(n.right)


def PrintInOrder(n):
    """
    takes the root node of BST as input and prints BST in In Order
    USES:
    - print in increasing/ascending order i.e. can be used for sorting
    - NOTE: In order traversal of BST gives elements in ascending order
    """
    if n:
        PrintInOrder(n.left)
        print n.data
        PrintInOrder(n.right)


def PrintPostOrder(n):
    """
    takes the root node of BST as input and prints BST in Post Order
    USES:
    - used for deletion of node or subtree. 
        - as this goes till the child node of interest, we can delete it there
    - use to get subtree until a node since it starts from the lowest points
    """
    if n:
        PrintPostOrder(n.left)
        PrintPostOrder(n.right)
        print n.data


########################################################################


# Reference for Breadth First/ Level Order: https://www.geeksforgeeks.org/level-order-tree-traversal/

def PrintLevelOrder(node):
    """
    takes the root node of BST as input and prints BST in Level Order starting from root
    PRE-ORDER
    """
    if not node:
        return
    queue = [node]

    while queue:
        # Print front of queue and remove it from queue
        print queue[0].data,
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


########################################################################
# Print a particular level in the tree            

def PrintLevel(node, print_height, height=0):
    """
    takes root node of a tree and prints the nodes at the specified level
    PRE-ORDER
    """
    if node:
        if height == print_height:
            print node.data
            return  # because if you have reached that level, going further will only change the level number
        PrintLevel(node.left, print_height, height + 1)
        PrintLevel(node.right, print_height, height + 1)


########################################################################

def GetTreeHeight(node, height=-1):
    """
    takes tree root node and returns height of the tree
    PRE-ORDER
    """
    if node:
        height += 1
        return max(GetTreeHeight(node.left, height), GetTreeHeight(node.right, height))
    else:
        return height


########################################################################
# Binary Tree balanced
# Balanced Tree - A binary tree is balanced if for each node it holds that the number of inner nodes in the left subtree and the number of inner nodes in the right subtree differ by at most 1

def IsTreeBalanced(node):
    """
    takes tree root node and returns if the tree is balanced
    """
    if (not node) or (abs(GetTreeHeight(node.left) - GetTreeHeight(node.right)) <= 1):
        return True

    return False


########################################################################
# Book: 4.7
# Q. Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in a datastructure. NOTE:This is not necessarily a binary search tree

# Binary Tree LCA
# Least Common Ancestor (LCA): The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root 


def get_lca_binary_search_tree(node, v1, v2):
    """
    LCA of Binary Search Tree
    - takes in BST root node as input, and values v1, v2 for the nodes existing in the tree
    returns LCA
    - requirement: v1 <= v2
    """
    if node:
        # if both values are larger, then go in right subtree
        if node.data < v1 and node.data < v2:
            return get_lca_binary_search_tree(node.right, v1, v2)

        # if both values are smaller, then go in left subtree
        if node.data > v1 and node.data > v2:
            return get_lca_binary_search_tree(node.left, v1, v2)

        # if the value is middle, you have reached LCA
        if v1 <= node.data <= v2:
            return node


def get_lca_binary_tree(root, v1, v2):

    def _recurse(node, v1, v2):
        if node:
            # if we have reached the node, return it
            if node.data == v1 or node.data == v2:
                return node

            # check if the nodes exist in left/right subtree
            in_right_subtree = _recurse(node.right, v1, v2)
            in_left_subtree = _recurse(node.left, v1, v2)

            # if a node each exists in left and right subtree, we are at LCA
            if in_left_subtree and in_right_subtree:
                return node

            # if both nodes exist in left subtree, go in that direction
            if in_left_subtree and not in_right_subtree:
                return _recurse(node.left, v1, v2)

            # if both nodes exist in right subtree, go in that direction
            if in_right_subtree and not in_left_subtree:
                return _recurse(node.right, v1, v2)

    return _recurse(root, v1, v2)

"""
def GetLCA(node, v1, v2):
    ""
    #LCA of a Binary Tree
    #- takes binary tree root node, v1, v2 as inputs
    #- returns LCA 
    ""
    if node:
        if node.data == v1 or node.data == v2:
            return node

        # check if v1 or v2 exists in left subtree
        left_lca = GetLCA(node.left, v1, v2)

        # check if v2 or v2 exists in right subtree
        right_lca = GetLCA(node.right, v1, v2)

        # if node exists in both subtrees, then have found the LCA
        if left_lca and right_lca:
            return node
        if left_lca:
            return left_lca
        else:
            return right_lca
"""

########################################################################            
# Binary Tree Comparisons 

def AreTreesIdentical(n1, n2):
    """
    takes in the root node of 2 trees and compares if they are equal or not
    """
    if (not n1) and (not n2):
        return True
    elif n1 and n2:
        if n1.data != n2.data:
            return False
        return AreTreesIdentical(n1.left, n2.left) and AreTreesIdentical(n1.right, n2.right)
    else:
        return False


def ContainsTree(n1, n2):
    """
    checks if tree with root n2 is a subset of tree with root n1
    """
    if (not n1) and n2:
        return False
    elif n1 and (not n2):
        return True  # T2 is empty
    elif n1.data == n2.data and AreTreesIdentical(n1, n2):
        return True
    else:
        return ContainsTree(n1.left, n2) or ContainsTree(n1.right, n2)


# Book: 4.3
# Q. Given a sorted (increasing order) array with unique integer elements, write an algo- rithm to create a binary
# search tree with minimal height.

def bst_minimal_height(sorted_arr):
    n = len(sorted_arr)
    m = n / 2
    bst = BinarySearchTree(sorted_arr.pop(m))
    print n

    def _recurse(l, r):
        if l < r:
            m = (l + r) / 2
            if l < m < r:
                print('{}, {}, {}'.format(l, m, r))
                bst.AddItem(sorted_arr[m])
                _recurse(l, m)
                _recurse(m, r)

    _recurse(0, m)
    _recurse(m, n - 1)
    return bst.root


# Book: 4.4
# Q. Given a binary tree, design an algorithm which creates a linked list of all the nodes at
# each depth (e.g., if you have a tree with depth D,you'll have D linked lists).

from python_linked_list import LinkedList


def binary_tree_list_linked_lists(root):
    ll_list = list()

    def _recurse(node, h):
        # if LL does not exist for that level, create it
        if len(ll_list) == h:  # other case not possible
            ll_list.append(LinkedList('*'))

        ll_list[h].append(node.data)

        # recurse the depths
        if node.right:
            _recurse(node.right, h + 1)
        if node.left:
            _recurse(node.left, h + 1)

    _recurse(root, 0)
    return ll_list


if __name__ == '__main__':

    bst = BinarySearchTree(3)
    bst.AddItem(2)
    bst.AddItem(4)
    bst.AddItem(5)
    bst.AddItem(1)
    # comment down from here to make a balanced tree for testing
    bst.AddItem(6)
    bst.AddItem(9)
    bst.AddItem(0)
    bst.AddItem(2)
    bst.AddItem(7)

    find_list = [4, 10, 7]
    for find in find_list:
        if not bst.FindItem(find):
            print '-- Not Found {}'.format(find)
        else:
            print '-- Found {}'.format(find)

    print "\nPrinting Pre Order ..."
    PrintPreOrder(bst.root)
    print "\nPrinting In Order ..."
    PrintInOrder(bst.root)
    print "\nPrinting Post Order ..."
    PrintPostOrder(bst.root)
    print "\nPrinting Level Order ..."
    PrintLevelOrder(bst.root)

    level_list = [2, 1, 4]
    for level in level_list:
        print "\nPrinting Level {}...".format(level)
        PrintLevel(bst.root, level)
    print "\n"

    print 'Tree Height = {}'.format(GetTreeHeight(bst.root))
    print 'Is Tree Balanced = {}'.format(IsTreeBalanced(bst.root))

    v1 = 5.5
    v2 = 7
    print 'LCA BST of v1={}, v2={} is {}'.format(v1, v2, get_lca_binary_search_tree(bst.root, v1, v2))
    print 'LCA of v1={}, v2={} is {}'.format(v1, v2, get_lca_binary_tree(bst.root, v1, v2))
    bst2 = copy.deepcopy(bst)
    bst3 = copy.deepcopy(bst)
    bst3.AddItem(99)

    print 'AreTreesIdentical(bst, bst2)={}'.format(AreTreesIdentical(bst.root, bst2.root))
    print 'AreTreesIdentical(bst, bst3)={}'.format(AreTreesIdentical(bst.root, bst3.root))

    # TODO - this one is not working
    bst4 = BinarySearchTree(6)
    bst4.AddItem(9)
    bst4.AddItem(7)
    print 'ContainsTree(bst, bst4)={}'.format(ContainsTree(bst.root, bst4.root))
    bst4.AddItem(7.5)
    print 'ContainsTree(bst, bst4)={}'.format(ContainsTree(bst.root, bst4.root))

    print '-------------------------------'
    ip_sorted_arr = range(10)
    print 'input sorted arr={}'.format(ip_sorted_arr)
    root = bst_minimal_height(ip_sorted_arr)
    print '         bst_minimal_height(): Tree Height={}'.format(GetTreeHeight(root))

    print '-------------------------------'
    output = binary_tree_list_linked_lists(root)
    PrintLevelOrder(root)
    for ll in output:
        ll.list()
