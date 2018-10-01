import copy

class Node:
    def __init__(self, x):
        self.data = x
        self.right = None
        self.left = None
        


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
    """ 
    if not node:
        return
    queue = [node]
    
    while queue:
        # Print front of queue and remove it from queue
        print queue[0].data,
        node = queue.pop(0)
     
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
     
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

            
########################################################################
# Print a particular level in the tree            
            
def PrintLevel(node, print_height, height=0):
    if node: 
        if height == print_height:
            print node.data, 
        PrintLevel(node.left, print_height, height+1)
        PrintLevel(node.right, print_height, height+1)
            
            

########################################################################

def GetTreeHeight(node, height=0):    
    """
    takes tree root node and returns height of the tree
    """
    if node:
        left_height = right_height = height
        if node.left:
            left_height = GetTreeHeight(node.left, height+1)
        if node.right:
            right_height = GetTreeHeight(node.right, height+1)
        
        if left_height >= right_height:
            return left_height
        else:
            return right_height
            
            
########################################################################
# Binary Tree balanced
# Balanced Tree - A binary tree is balanced if for each node it holds that the number of inner nodes in the left subtree and the number of inner nodes in the right subtree differ by at most 1

def IsTreeBalanced(node, height=0):
    """
    takes tree root node and returns if the tree is balanced
    """
    if (not node) or (abs(GetTreeHeight(node.left) - GetTreeHeight(node.right)) <= 1):
        return True
        
    return False
        

########################################################################
# Binary Tree LCA
# Least Common Ancestor (LCA): The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root 


def GetBSTLCA(node, v1, v2):
    """
    LCA of Binary Search Tree
    - takes in BST root node as input, and values v1, v2 for the nodes existing in the tree
    returns LCA
    - requirement: v1 <= v2
    """
    if node:
        if node.data < v1 and node.data < v2:
            return GetBSTLCA(node.right, v1, v2)
        elif node.data > v1 and node.data > v2:
            return GetBSTLCA(node.left, v1, v2)            
        elif v1 <= node.data <= v2:
            return node
        
def GetLCA(node, v1, v2):
    """
    LCA of a Binary Tree
    - takes binary tree root node, v1, v2 as inputs
    - returns LCA 
    """
    if node:
        if node.data == v1 or node.data == v2:
            return node
        
        left_lca = GetLCA(node.left, v1, v2)
        right_lca = GetLCA(node.right, v1, v2)
        
        if left_lca and right_lca:
            return node
        if left_lca: 
            return left_lca 
        else:
            return right_lca

            
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
        return True # T2 is empty
    elif n1.data == n2.data and AreTreesIdentical(n1, n2): 
        return True
    else:    
        return ContainsTree(n1.left, n2) or ContainsTree(n1.right, n2)
        
            
    
if __name__=='__main__':
    
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
            
    find_list = [4,10,7]
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
    print 'LCA BST of v1={}, v2={} is {}'.format(v1, v2, GetBSTLCA(bst.root, v1, v2).data)
    print 'LCA of v1={}, v2={} is {}'.format(v1, v2, GetLCA(bst.root, v1, v2).data)
    
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
    
