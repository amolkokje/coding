using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedLists_Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("--------------------------------------------------------");
            Console.WriteLine("DOUBLY LINKED LIST ---");
            DoublyLinkedList dl = new DoublyLinkedList();
            dl.Initialize(10);            
            dl.Print();
            dl.AddLast(20);
            dl.AddLast(30);
            dl.AddLast(40);
            dl.AddLast(50);
            dl.AddLast(60);
            dl.Print();
            dl.AddFirst(5);
            dl.Print();
            dl.PrintReverse();
            dl.DeleteNode(5);
            dl.Print();
            dl.DeleteNode(60);
            dl.DeleteNode(30);
            dl.Print();
            dl.PrintReverse();
            dl.Reverse();
            dl.Print();
            Console.ReadLine();

            Console.WriteLine("--------------------------------------------------------");
            Console.WriteLine("LINKED LIST ---");
            LinkedList ll = new LinkedList();
            ll.InitializeLinkedList(10);
            ll.PrintLinkedList();
            ll.AddNodeLast(20);
            ll.AddNodeLast(30);
            ll.AddNodeLast(40);
            ll.AddNodeLast(50);
            ll.AddNodeLast(60);
            ll.PrintLinkedList();

            LinkedList l2 = new LinkedList();
            //l2.InitializeLinkedList(10);
            //l2.PrintLinkedList();
            //l2.AddNodeLast(20);
            //l2.AddNodeLast(30);
            //l2.AddNodeLast(40);
            //l2.AddNodeLast(50);
            //l2.AddNodeLast(60);
            //l2.AddNodeLast(70);
            l2.PrintLinkedList();

            CompareLL(ll,l2);

            ll.AddNodeFirst(5);
            ll.PrintLinkedList();

            ll.FindNode(20);
            ll.FindNode(5);
            ll.FindNode(55);
            ll.RemoveNode(40);
            ll.PrintLinkedList();

            ll.PrintReverse();

            ll.ReverseLL();
            ll.PrintLinkedList();

            ll.RemoveNodeLast();
            ll.PrintLinkedList();

            ll.RemoveNodeFirst();
            ll.PrintLinkedList();

            ll.DetectCircularLL();
            Console.ReadLine();

            Console.WriteLine("--------------------------------------------------------");
            Console.WriteLine("STACK ---");
            Stack s1 = new Stack();
            s1.InitializeStack(3);
            s1.Push(4);
            s1.Push(5);
            s1.Push(6);
            s1.Push(7);
            s1.Print();
            s1.Pop();
            s1.Print();

            Console.WriteLine("--------------------------------------------------------");
            Console.WriteLine("QUEUE ---");
            Queue q1 = new Queue();
            q1.InitializeQueue(9);
            q1.Enqueue(8);
            q1.Enqueue(7);
            q1.Enqueue(6);
            q1.Enqueue(5);
            q1.Print();
            q1.Dequeue();
            q1.Print();

            Console.WriteLine("END --- ");
            Console.ReadLine();

        }

        static void CompareLL(LinkedList l1, LinkedList l2)
        {
            Node c1 = new Node();
            Node c2 = new Node();
            c1 = l1.head;
            c2 = l2.head;

            while ((c1 != null) && (c2 != null))
            {                                
                if (c1.Data == c2.Data)
                {
                    c1 = c1.Next;
                    c2 = c2.Next;
                }
                else
                {
                    Console.WriteLine("Linked Lists are not Equal...");
                    return;
                }
            }


            // --
            if ((c1 == null) && (c2 != null))
            {
                Console.WriteLine("Linked Lists not same length");
            }
            else if ((c1 != null) && (c2 == null))
            {
                Console.WriteLine("Linked Lists not same length");
            }
            else 
            {
                Console.WriteLine("Linked Lists EQUAL");
            }
            
        }
    }

    public class Node
    {
        public int Data;
        public Node Next;
    }

    public class DoubleNode
    {
        public int Data;
        public DoubleNode Next;
        public DoubleNode Prev;
    }

    public class DoublyLinkedList
    {
        DoubleNode head;
        DoubleNode last;

        public void Initialize(int x)
        {
            if (head == null)
            {
                head = new DoubleNode();
                head.Data = x;
                head.Next = null;
                head.Prev = null;
                last = new DoubleNode();
                last = head;
                Console.WriteLine("Initialize Doubly Linked List with head {0}",x);
            }
        }

        public void AddLast(int x)
        {
            DoubleNode current = new DoubleNode();
            current = head;

            DoubleNode newNode = new DoubleNode();
            newNode.Data = x;
            newNode.Next = null;
            newNode.Prev = null;
           
            Console.WriteLine("Add Node {0} to the Last", x);
            //while (current.Next != null)
            //{
            //    current = current.Next;
            //}
            //current.Next = newNode;
            //newNode.Prev = current;

            newNode.Prev = last;
            last.Next = newNode;
            last = last.Next;
            //last = newNode;
            return;
        }

        public void AddFirst(int x)
        {
            
            DoubleNode newNode = new DoubleNode();
            newNode.Data = x;
            newNode.Next = head;
            newNode.Prev = null;

            head.Prev = newNode;            
            head = newNode;
        }

        public void DeleteNode(int x)
        {
            DoubleNode current = new DoubleNode();
            current = head;

            DoubleNode prev = new DoubleNode();
            prev = head; // =current

            while (current != null)
            {
                if (current.Data == x)
                {
                    if (prev == head) // head 
                    {
                        current.Next.Prev = null;
                        head = current.Next;
                        Console.WriteLine("Removed Head Node {0}", x);
                        return;
                    }
                    else if (current == last) // last
                    {
                        current.Prev.Next = null;
                        last = current.Prev;
                        Console.WriteLine("Removed Last Node {0}", x);
                        return;
                    }
                    else // node in between
                    {
                        prev.Next = current.Next;
                        current.Next.Prev = prev;
                        Console.WriteLine("Removed Node {0} in Between", x);
                        return;
                    }                    
                }
                prev = current;
                current = current.Next;
            }
            Console.WriteLine("Node with value {0} not found.",x);
        }

        public void Print()
        {
            DoubleNode current = new DoubleNode();
            current = head;
            Console.Write("Printing Doubly Linked List: ");
            while (current != null)
            {
                Console.Write("{0}, ",current.Data);
                current = current.Next;
            }
            Console.WriteLine();
        }

        public void PrintReverse()
        {
            DoubleNode current = new DoubleNode();
            current = last;
            Console.Write("Printing Doubly Linked List in Reverse: ");
            while (current != null)
            {
                Console.Write("{0}, ",current.Data);
                current = current.Prev;
            }
            Console.WriteLine();
        }

        public void Reverse()
        {
            DoubleNode p = new DoubleNode();
            DoubleNode c = new DoubleNode();
            DoubleNode n = new DoubleNode();

            Console.WriteLine("Reverse Doubly Linked List");
            c = head;
            last = head;
            p = c.Prev; // null
            
            while (c.Next != null)
            {
                n = c.Next;
                c.Next = c.Prev;
                c.Prev = n;

                p = c;
                c = n;
            }
            c.Next = p;
            c.Prev = null;

            head = c;

        }

    }



    public class LinkedList
    {
        public Node head;

        public void InitializeLinkedList(int x)
        {
            if (head == null)
            {
                Console.WriteLine("Adding new element {0}", x);
                head = new Node();
                head.Data = x;
                head.Next = null;
            }
            else
            {
                Console.WriteLine("ERROR: LL not empty");
            }
        }

        public void PrintLinkedList()
        {
            Node current = new Node();
            current = head;
            Console.Write("Printing Linked List: ");
            if (current == null)
            {
                Console.WriteLine("Empty Linked List");
                return;
            }


            while (current.Next != null)
            {
                Console.Write("{0}, ",current.Data);
                current = current.Next;
            }
            Console.Write("{0}, ", current.Data);
            Console.WriteLine("");
        }

        public void AddNodeLast(int x)
        {
            Node newNode = new Node();
            newNode.Data = x;
            newNode.Next = null;
            
            Node current = new Node();
            current = head;

            Console.WriteLine("Adding new node at last {0}",x);
            while (current.Next != null)
            {                
                current = current.Next;                
            }
            current.Next = newNode;
        }

        public void AddNodeFirst(int x)
        {
            Node current = new Node();
            current = head;

            Node newNode = new Node();
            newNode.Data = x;
            newNode.Next = head;

            Console.WriteLine("Adding node before first {0}",x);
            head = newNode;
        }

        public void FindNode(int x)
        {
            Node current = new Node();
            current = head;
            int index = 0;
            while (current.Next != null)
            {
                if (current.Data == x)
                {
                    Console.WriteLine("Found node {0} at index {1}", x, index);
                    return;
                }
                index++;
                current = current.Next;
            }
            Console.WriteLine("Node {0} not found", x); 
        }

        public void RemoveNode(int x)
        {
            Node current = new Node();
            current = head;

            Node previous = new Node();
            previous = head;

            int index = 0;
            while (current.Next != null)
            {
                if (current.Data == x)
                {
                    Console.WriteLine("Found node {0} at index {1}. Removing...", x, index);
                    previous.Next = current.Next;
                    return;
                }
                index++;
                previous = current;
                current = current.Next;
            }
            Console.WriteLine("Node {0} not found");
        }

        public int RemoveNodeLast()
        {
            Node current = new Node();
            current = head;

            Node prev = new Node();
            prev = head;

            int val;

            Console.WriteLine("Removing Last Node of Linked List");
            while (current.Next != null)
            {
                prev = current;
                current = current.Next;
            }
            val = current.Data;
            prev.Next = null;
            return val;
        }

        public int RemoveNodeFirst()
        {
            Node current = new Node();
            current = head;
            int val = current.Data;
            Console.WriteLine("Removing First Node of Linked List");
            head = current.Next;
            return val;
        }

        public void ReverseLL()
        {
            Node prev = new Node();
            Node current = new Node();
            Node next = new Node();

            Console.WriteLine("Reversing Linked List");
            current = head;
            prev = null;
            while (current != null)
            {
                next = current.Next;
                current.Next = prev;
                prev = current; 
                current = next;               
            }
            head = prev;
        }

        public void PrintReverse()
        {
            Console.WriteLine("Printing LL in reverse order:");
            if (head == null)
            {
                return;
            }
            else
            {
                PrintReverse_helper(head);
            }
        }

        public void PrintReverse_helper(Node printNode)
        {
            if (printNode == null)
            {                
                return;
            }
            else
            {
                PrintReverse_helper(printNode.Next);
                Console.WriteLine("{0}", printNode.Data);
            }
        }
        
        public void DetectCircularLL()
        {
            Node slow = new Node();
            Node fast = new Node();
            slow = head;
            fast = head;

            while ((fast!=null) && (fast.Next != null))
            {
                slow = slow.Next;
                fast = fast.Next.Next;
                if (slow == fast)
                {
                    Console.WriteLine("Linked List is Circular");
                    return;
                }                
            }
            Console.WriteLine("Linked List is not Circular");
        }
    }

    

    public class Stack
    {
        LinkedList l1;

        public void InitializeStack(int x)
        {
            if (l1 == null)
            {
                l1 = new LinkedList();
                l1.InitializeLinkedList(x);
            }            
        }

        public void Push(int x)
        {            
            l1.AddNodeLast(x);
        }

        public void Pop()
        {
            int val = l1.RemoveNodeLast();
            Console.WriteLine("Popped {0}", val);
        }

        public void Print()
        {
            l1.PrintLinkedList();
        }

        public void Peek()
        { 
            // print last element
        }
    }

    public class Queue
    {
        LinkedList l2;

        public void InitializeQueue(int x)
        {
            if (l2 == null)
            {
                l2 = new LinkedList();
                l2.InitializeLinkedList(x);
            }
        }

        public void Enqueue(int x)
        {
            l2.AddNodeFirst(x);
        }

        public void Dequeue()
        {
            int val = l2.RemoveNodeLast();
            Console.WriteLine("Dequeue: Retrieved {0}",val);
        }

        public void Print()
        {
            l2.PrintLinkedList();
        }
    }
}
    