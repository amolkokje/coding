using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trees_Graphs_Csharp
{
    class Program
    {
        static void Main(string[] args)
        {

            MinHeap mh = new MinHeap();
            HeapNode hNode = new HeapNode();
            
            mh.AddItem(10);            
            mh.AddItem(100);            
            mh.AddItem(30);            
            mh.AddItem(40);            
            mh.AddItem(55);
            mh.AddItem(25);
            mh.AddItem(27);
            mh.AddItem(5);
            mh.Print();
            mh.RemoveItem(40);
            mh.Print();
            mh.PopMin();
            mh.Print();

            Console.WriteLine("Press ENTER to continue...");
            Console.ReadLine();


            //ReferenceEquals:
            //https://msdn.microsoft.com/en-us/library/ms379572(v=vs.80).aspx

            BinarySearchTree bst = new BinarySearchTree();
            bst.InitializeBST(5);
            bst.AddNode(9);
            bst.AddNode(3);
            bst.AddNode(4);
            bst.AddNode(2);
            bst.AddNode(6);
            bst.AddNode(2); 
            bst.AddNode(7);
            bst.AddNode(8);            
            bst.AddNode(10);
            bst.AddNode(1);

            BinarySearchTree bst2 = new BinarySearchTree();
            bst2.InitializeBST(9);
            bst2.AddNode(6);
            bst2.AddNode(10);
            bst2.AddNode(7);
            bst2.AddNode(8);
            bst2.AddNode(2);
            
            BSTcalc cal = new BSTcalc();
            int height = cal.getHeight(bst.root);
            Console.WriteLine("Tree Height = {0}",height);
            cal.IsBalanced(bst.root);
            cal.LCA(bst.root,4,7);
            cal.bstLCA(bst.root, 4, 7);
            cal.containsTree(bst.root,bst2.root);
            cal.getPaths(bst.root);


            Console.WriteLine("Printing Pre Order ...");
            PrintBST_PreOrder(bst.root);
            Console.WriteLine();
            Console.WriteLine("--------------------");

            Console.WriteLine("Printing In Order ...");
            PrintBST_InOrder(bst.root);
            Console.WriteLine();
            Console.WriteLine("--------------------");

            Console.WriteLine("Printing Post Order ...");
            PrintBST_PostOrder(bst.root);
            Console.WriteLine();
            Console.WriteLine("--------------------");

            Console.WriteLine("END ---");
            Console.ReadLine();
        }

        public class TreeNode
        {
            public int Data;
            public TreeNode left;
            public TreeNode right;
        }

        public class HeapNode
        {
            public int Data;
        }


        // MSDN -----------------
        public class BinarySearchTree
        {
            public TreeNode root;

            public void InitializeBST(int x)
            {
                if (root == null)
                {
                    root = new TreeNode();
                    root.Data = x;
                    root.left = null;
                    root.right = null;
                    Console.WriteLine("BST initialized with root {0}",x);
                }
            }
            
            public void AddNode(int x)
            {
                Console.WriteLine("Add node {0}",x);

                TreeNode current = new TreeNode();
                current = root;

                TreeNode newNode = new TreeNode();
                newNode.Data = x;
                newNode.right = null;
                newNode.left = null;

                while (current != null)
                {
                    Console.Write("x={0}, current={1}, ",x,current.Data);
                    if (current.left != null)
                    {
                        Console.Write("currLEFT={0}, ",current.left.Data);
                    }
                    if (current.right != null)
                    {
                        Console.Write("currRIGHT={0}, ", current.right.Data);
                    }
                    Console.WriteLine();



                    if (x > current.Data)
                    {
                        if (current.right == null)
                        {
                            current.right = new TreeNode();
                            current.right = newNode;
                            Console.WriteLine("Added Node {0} in right sub-tree under {1} ---",x, current.Data);
                            return;
                        }
                        else
                        {
                            current = current.right;
                        }
                    }
                    else if (x <= current.Data)
                    {
                        if (current.left == null)
                        {
                            current.left = new TreeNode();
                            current.left = newNode;
                            Console.WriteLine("Added Node {0} in left sub-tree under {1} ---", x, current.Data);
                            return;
                        }
                        else
                        {
                            current = current.left;
                        }
                    }
                }
            }

        }
        
        public static void PrintBST_PreOrder(TreeNode root)
        {            
            TreeNode current = new TreeNode();
            current = root;
            if (current != null)
            {
                Console.Write("{0}, ", current.Data);
                PrintBST_PreOrder(current.left);
                PrintBST_PreOrder(current.right);                
            }
        }

        public static void PrintBST_InOrder(TreeNode root)
        {
            TreeNode current = new TreeNode();
            current = root;
            if (current != null)
            {                
                PrintBST_InOrder(current.left);
                Console.Write("{0}, ", current.Data);
                PrintBST_InOrder(current.right);
            }
        }

        public static void PrintBST_PostOrder(TreeNode root)
        {
            TreeNode current = new TreeNode();
            current = root;
            if (current != null)
            {
                PrintBST_PostOrder(current.left);
                PrintBST_PostOrder(current.right); 
                Console.Write("{0}, ", current.Data);                
            }
        }

        public class BSTcalc
        {
            // ---------------------------------------------------------------------------------------
            // get the height of a tree
            static int leftHeight = 0;
            static int rightHeight = 0;
            public int getHeight(TreeNode root)
            {
                if (root == null)
                {
                    return 0;
                }

                if (root.right != null)
                {
                    rightHeight++;
                    getHeight(root.right);
                }

                if (root.left != null)
                {
                    leftHeight++;
                    getHeight(root.left);
                }

                Console.WriteLine("rightHeight={0}, leftHeight={1}", rightHeight, leftHeight);
                if (leftHeight >= rightHeight)
                    return leftHeight;
                else
                    return rightHeight;
            }

            // ---------------------------------------------------------------------------------------
            // check if a tree is balanced
            public bool IsBalanced(TreeNode root)
            {
                leftHeight = 0;
                rightHeight = 0;
                
                bool _isbal = IsBalanced_helper(root);
                if (_isbal == false)
                    Console.WriteLine("Tree not balanced");
                else
                    Console.WriteLine("Tree balanced");

                Console.WriteLine("rightHeight={0}, leftHeight={1}", rightHeight, leftHeight);
                return _isbal;
            }

            bool IsBalanced_helper(TreeNode root)
            {
                if (root == null)
                {
                    return true;
                }

                if (root.right != null)
                {
                    rightHeight++;
                    IsBalanced_helper(root.right);
                }

                if (root.left != null)
                {
                    leftHeight++;
                    IsBalanced_helper(root.left);
                }

                if (Math.Abs(rightHeight - leftHeight) > 1)
                {                    
                    return false;
                }
                else {
                    return true;
                }
            }

            // ---------------------------------------------------------------------------------------
            // get LCA of 2 nodes in a BST tree
            // specific for BST, optimized
            public void bstLCA(TreeNode root, int v1, int v2)
            {
                TreeNode lca = bstLCA_helper(root, v1, v2);
                Console.WriteLine("LCA Node for BST nodes {0} and {1} = {2}", v1, v2, lca.Data);
            }

            TreeNode bstLCA_helper(TreeNode root, int v1, int v2)
            {
                if (root == null)
                    return null;

                if (root.Data < v1 && root.Data < v2)
                    return bstLCA_helper(root.right, v1, v2);

                else if (root.Data > v1 && root.Data > v2)
                    return bstLCA_helper(root.left, v1, v2);

                else if (root.Data > v1 && root.Data < v2)
                    return root;

                else
                    return null; // only a placeholder to avoid having a path that returns nothing 
                
            }

            // ---------------------------------------------------------------------------------------
            // get LCA of 2 nodes in any binary tree
            // general for any kind of tree            
            public void LCA(TreeNode root, int v1, int v2)
            {
                TreeNode lca = LCA_helper(root,v1,v2);
                Console.WriteLine("LCA Node for nodes {0} and {1} = {2}",v1,v2,lca.Data);
            }

           TreeNode LCA_helper(TreeNode root, int v1, int v2)
            {
                if (root == null)
                    return null;

                if ((root.Data == v1) || (root.Data == v2))
                   return root;
               
               TreeNode x=LCA_helper(root.right,v1,v2);
               TreeNode y=LCA_helper(root.left,v1,v2);

               if (x != null && y != null)
                   return root;
               else if (x != null && y == null)
                   return x;
               else if (x == null && y != null)
                   return y;
               else
                   return null;  // just a placeholder to avoid having a path that returns nothing            
               
                
            }

           // ---------------------------------------------------------------------------------------
            // check is a tree T2 is subtree of tree T1
           public void containsTree(TreeNode r1, TreeNode r2)
           {               
               bool treeFound = containsTree_helper(r1,r2);
               if (treeFound)
                   Console.WriteLine("T2 is a subtree");
               else
                   Console.WriteLine("T2 is not a subtree");
           }

           bool containsTree_helper(TreeNode r1, TreeNode r2)
           {
               if (r1==null && r2!=null)
                   return false;  // reached end of T1, but did not find any T2 node

               else if (r1!=null && r2 == null)
                   return true;  // T2 is empty

               else if (r1 == null && r2 == null)
                   return true;  // T1, T2 both empty

               else if (r1.Data == r2.Data)
                   return matchTree(r1, r2);

               else 
                   return (containsTree_helper(r1.right,r2) || containsTree_helper(r1.left,r2));
               
           }

            // checks if 2 binary trees are identical
           bool matchTree(TreeNode r1, TreeNode r2)
           {
               if ((r1==null && r2!=null) || (r1!=null && r2==null))
                   return false;
               if (r1==null && r2==null)
                   return true;
               else if (r1.Data == r2.Data)
                   return (matchTree(r1.right, r2.right) && matchTree(r1.left, r2.left));
               else
                   return false;                    
           }

            // ---------------------------------------------------------------------------------------
            // print path from root node to all nodes of a tree   
            // here, taking value of a node is the distance to that node from its parent
           public static int root_value;
           public void getPaths(TreeNode root)
           {
               if (root == null)
                   Console.WriteLine("Path=0");
               else
               {
                   root_value = root.Data;
                   getPaths_helper(root, 0);
               }                   
           }

           void getPaths_helper(TreeNode root, int path)
            {
                int sum_path = path + root.Data;
                Console.WriteLine("Path from root to Node {0} = {1}",root.Data, (sum_path-root_value));

                if (root.right != null)
                    getPaths_helper(root.right, sum_path);

                if (root.left != null)
                    getPaths_helper(root.left, sum_path);
            }


        
        }





        public class MinHeap
        {
            List<HeapNode> elements;

            // constructor
            public MinHeap()
            {
                elements = new List<HeapNode>();
            }

            public void Heapify()
            {
                for (int i = elements.Count - 1; i > 0; i--)
                {
                    // calculate the index of parent node
                    int parentPosition;
                    // child nodes of n -> 2n+1, 2n+2
                    if (i % 2 == 0)
                    {
                        parentPosition = (i - 2) / 2;
                    }
                    else
                    {
                        parentPosition = (i - 1) / 2;
                    }
                    parentPosition = parentPosition >= 0 ? parentPosition : 0;                    

                    // compare child nodes with parent. replace, if smaller
                    if (elements[i].Data < elements[parentPosition].Data)
                    {
                        HeapNode tmp = elements[parentPosition];
                        elements[parentPosition] = elements[i];
                        elements[i] = tmp;
                    }                    
                }
            }

            public void AddItem(int val)
            {
                Console.WriteLine("Add item {0}", val);
                HeapNode item = new HeapNode();
                item.Data = val;
                elements.Add(item); // add element to the end of the list
                Heapify();                
            }

            public void RemoveItem(int val)
            {
                Console.WriteLine("Remove item with value {0}", val);
                HeapNode item = new HeapNode();
                item.Data = val;
                int last = elements.Count - 1;

                // get the index of the the first occurence of item
                int index = -1;
                for (int i = 0; i < elements.Count; i++)
                {
                    if (val == elements[i].Data)
                    {
                        index = i;
                        break;
                    }
                }                
                 
                if (index == -1)
                {
                    Console.WriteLine("No element with value {0} found.", item.Data);
                    return;
                }
                else
                {
                    elements[index] = elements[last]; // replace the value at the index with value of last item in the list
                    elements.RemoveAt(last); // remove the last element of the list, as there is a duplicate value now at the index
                    Heapify();
                }                
            }

            public void PopMin()
            {
                RemoveItem(elements[0].Data);
            }

            public void Print()
            { 
                Console.Write("Print MinHeap: ");
                foreach (HeapNode i in elements)
                {
                    Console.Write("{0}, ",i.Data);
                }
                Console.WriteLine();
            }

        }
    }
}

