using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Other_Problems
{
    class Program
    {
        static int c;
        static Dictionary<string, int> tracker = new Dictionary<string, int>();
        static int[,] cache = new int[101, 101];
        static void Main(string[] args)
        {

            Utility util = new Utility();

            // MagicLeap Onsite - Hardik Shah
            // Q:: Given a NxN matrix and a dictionary of words. print all the words in the matrix that exist in the dictionary.
            char[,] mat = new char[3,3];
            mat[0,0]='G';
            mat[0,1]='A';
            mat[0,2]='T';
            mat[1,0]='A';
            mat[1,1]='E';
            mat[1,2]='E';
            mat[2,0]='G';
            mat[2,1]='O';
            mat[2,2]='T';
            Dictionary<string, int> dict = new Dictionary<string, int>();
            Dictionary<string, int> dictTracker = new Dictionary<string, int>();
            dict["GET"] = 1;
            dict["GATE"] = 1;
            dict["ATE"] = 1;
            dict["GAG"] = 1;
            dict["GOT"] = 1;
            dict["TAG"] = 1;

            Console.WriteLine("Hardik Shah(MagicLeap) BETTER METHOD - converting the input dictionary of words to a trie");
            Trie dTrie = new Trie();
            foreach (KeyValuePair<string, int> pair in dict)
            {
                //Console.WriteLine("d='{0}'", pair.Key);
                dTrie.Insert(pair.Key);
            }
            bool existsTrie = dTrie.Search("GET");
            Console.WriteLine("Exists={0}",existsTrie);
            bool[,] isVisited = new bool[3, 3];
            char[] sb = new char[9];
            
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    isVisited[i, j] = false;
                }
                Console.WriteLine();
            }

            dictTracker.Clear();
            var watch = System.Diagnostics.Stopwatch.StartNew();
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    Console.WriteLine("Starting from: [{0},{1}] ...", i, j);
                    for (int ki = 0; ki < 3; ki++)
                    {
                        for (int kj = 0; kj < 3; kj++)
                        {
                            isVisited[ki, kj] = false;
                        }
                    }
                    isVisited[i, j] = true;
                    util.MatrixWordsTrie(isVisited, dTrie, mat, sb, 0, i, j, dictTracker);
                }
            }
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine("Execution Time= {0}",elapsedMs);

            Console.WriteLine("--------------------------------------");
            Console.ReadLine();

            Console.WriteLine("SLOWER METHOD - using dictionary of words as input");
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    Console.Write("{0}, ",mat[i,j]);
                    isVisited[i, j] = false;
                }
                Console.WriteLine();
            }
            //dictTracker.Clear();
            //isVisited[0, 2] = true;
            //util.MatrixWords(isVisited, dict, mat, sb, 0, 0, 2, dictTracker);

            dictTracker.Clear();
            watch.Start();
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    Console.WriteLine("Starting from: [{0},{1}] ...",i,j);                    
                    for (int ki = 0; ki < 3; ki++)
                    {
                        for (int kj = 0; kj < 3; kj++)
                        {                     
                            isVisited[ki, kj] = false;
                        }
                    }
                    isVisited[i, j] = true;
                    util.MatrixWords(isVisited, dict, mat, sb, 0, i, j, dictTracker);
                }
            }
            watch.Stop();
            elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine("Execution Time= {0}", elapsedMs);

            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();


            // 5, 10, 15 -- total 100
            int sum = 0;
            List<int> pathss = new List<int>();
            int[] b = new int[100];
            int l = -1;
            int result = countWays(20, b, l);
            Console.WriteLine("r={0}",result);

            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();



            string s = "a*b*c*";
            string p = "aaabbcc";
            Console.WriteLine("isMatch s={0}  p={1}  result={2}",s,p,isMatch(s,p));
            isMatch(s, p);
            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();

            // Q:: Calculate the number of 2s in numbers from 0-n;
            int n = 400;
            int num2 = 0;
            c = 0;
            for (int i = 1; i <= n; i++)
            {
                c = calclate2s(i);
                num2 = num2 + c;
            }
            Console.WriteLine("Number of 2s in numbers from 0-{0} = {1}",n,num2);

            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();

            // Q:: O(n) solution to find 2 numbers in an array that sum up to a target value
            int[] intArr={-2,-1, 0, 3, 5, 6, 7, 9, 13, 14};
            int target = 4;
            PrintPairsSum(intArr,4);

            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();

            // Q:: O(n^2) solution to find 3 numbers in an array that sum up to a target value
            for (int i = 0; i < intArr.Length; i++)
            {
                // x+y+z=target ==> x+y=target-z
                int subTarget = (target - intArr[i]);
                Console.WriteLine("{0}: Target={1}  subTarget={1}",intArr[i],target,subTarget);
                PrintPairsSum3(intArr, subTarget,i);
            }

            // NOTE: This logic can be carried forward to higher numbers. 

            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();


            // Q:: Find total unique paths from a point in matrix to another point in matrix
            int startX = 1;
            int startY = 1;
            int stopX = 2;
            int stopY = 6;
            int m = 3;
            n = 7;
            c = 0;
            int paths = UniquePaths(stopX, stopY, startX, startY, m, n);
            Console.WriteLine("No of unique paths = {0}",paths);
            
            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();

            // Q:: Find all permutations, combinations, powerset/subsets of a given string - Graph approach
            // if integer array --> same logic applies
            // code reference: http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
            // reference: https://www.youtube.com/watch?v=nYFd7VHKyWQ
            string str = "ABC";            
            char[] arr = str.ToCharArray();
            bool[] visited = new bool[arr.Length];
            for (int i = 0; i < arr.Length; i++)
            {
                visited[i] = false;
            }
            char[] branch = new char[arr.Length];  // array to store the string permutation. Element at each index has equivalent recursion depth
            c = 0;
            tracker.Clear();
            Console.WriteLine("PERMUTATIONS:: ");            
            GeneratePermutations(arr, branch, -1, visited);
            // NOTE: if we want to get rid of repeating strings(if we have repeating characters), then store the values in a static hash, and if the values are repeated, then ignore them

            Console.ReadLine();
            Console.WriteLine("------------------------------------------------------------------------------------------------------------");

            Array.Clear(branch, 0, arr.Length);
            c = 0;
            int k = 2; // combination of k elements from given n elements i.e. select k elements
            Console.WriteLine("COMBINATIONS:: ");
            GenerateCombinations(arr, k, 0, branch, 0);

            Console.ReadLine();
            Console.WriteLine("------------------------------------------------------------------------------------------------------------");

            // to generate subsets of size k1-k2, call the GenerateCombinations() method for k=k1-k2
            // to generate a powerset, call the GenerateCombinations() method for k=0-arr.Length
            Array.Clear(branch, 0, arr.Length); 
            c = 0;
            Console.WriteLine("POWERSET: ");
            for (k = 0; k < arr.Length+1; k++)
            {
                GenerateCombinations(arr, k, 0, branch, 0);    
            }

            Console.ReadLine();
            Console.WriteLine("------------------------------------------------------------------------------------------------------------");

            // Q:: find first non-repeating character by iterating through the length of the string only once and by using constant space.
            string ip_string = "abacdbefgh";
            char[] ip_string_arr = ip_string.ToCharArray();
            int[] char_occurance = new int[256];
            Array.Clear(char_occurance, 0, char_occurance.Length - 1);

            for (int i = 0; i < ip_string_arr.Length; i++)
            {
                int chr = (int)ip_string_arr[i];
                char_occurance[chr]++;
            }

            for (int i = 0; i < char_occurance.Length; i++)
            {
                if (char_occurance[i] == 1)
                {
                    char ch = (char)i;
                    Console.WriteLine("first non-repeating char is {0}", ch);
                    break;
                }
            }

            
            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();
            
            // Q:: find missing element in an AP
            int[] ap_array = { 1, 3, 5, 7, 9, 13, 15 };
            int diff = Math.Min((ap_array[1] - ap_array[0]), (ap_array[2] - ap_array[1]));
            diff = Math.Min((ap_array[3] - ap_array[2]), diff);
            Console.WriteLine("Diff = {0}", diff);
            int found = 0;
            for (int i = 1; i < ap_array.Length; i++)
            {
                //Console.WriteLine("i={0}    i-1={1}",ap_array[i],ap_array[i-1]);   
                if ((ap_array[i] - ap_array[i - 1]) > diff)
                {
                    Console.WriteLine("Missing Element = {0}", ap_array[i] - diff);
                    found = 1;
                    break;
                }
            }

            if (found == 0)
                Console.WriteLine("No Missing element");


            Console.WriteLine("------------------------------------------------------------------------------------------------------------");
            Console.ReadLine();
                        
            
            // Q:: Find the largest substring palindrome in a given string. 
            //ex: input: abbac output: abba


            Console.ReadLine();
        }
        
        static void GeneratePermutations(char[] arr, char[] branch, int level, bool[] visited)
        {
            int k = 1; 
            if (level == arr.Length-1) // if you want to select only few elements, and not all from the given set, replace level==<> with level==k
            {                
                string s = new string(branch);                
                if (!tracker.ContainsKey(s))
                {
                    c++;
                    // Reached the last level - print the string    
                    Console.WriteLine("{0}: {1}", c, s);
                    tracker[s] = 1;
                }
                return;
            }

            for (int i = 0; i < arr.Length; i++)
            {               

                if (!visited[i])
                {
                    level++;
                    branch[level] = arr[i];
                    visited[i] = true;                    
                    GeneratePermutations(arr, branch, level, visited);
                    visited[i] = false; 
                    level--;
                }
            }
        }        

        static void GenerateCombinations(char[] arr, int k, int startId, char[] branch, int numElem)
        { 
            if (numElem == k) // NOTE: there is only 1 possible combinbation with all elements i.e. n=k
            {   
                c++;
                string s = new string(branch);
                Console.WriteLine("{0}: {1}",c,s);
                return;
            }
    
            for (int i = startId; i < arr.Length; ++i)
            {
                branch[numElem] = arr[i];
                numElem++;
                startId++;
                GenerateCombinations(arr, k, startId, branch, numElem);
                numElem--;
            }
        }

        static int UniquePaths(int stopX, int stopY, int startX, int startY, int m, int n)
        {
            // Returns count of possible paths to reach cell at row number m and column
            // number n from the topmost leftmost cell (cell at 1, 1)
            if (stopX == startX || stopY == startY)
                return 1;

            // If diagonal movements are allowed then the last addition is required.
            //return UniquePaths(m - 1, n, startX, startY) + UniquePaths(m, n - 1, startX, startY) + UniquePaths(m + 1, n, startX, startY) + UniquePaths(m, n+1, startX, startY);

            /// LOOKS LIKE THIS ONE IS NOT NEEDED
            ///if (stopY == startY)
            ///    return UniquePaths(stopX-1,stopY,startX,startY,m,n);
            ///
            ///if (stopX == startX)
            ///    return UniquePaths(stopX, stopY-1, startX, startY, m, n);

            //int tc = 0;
            //tc = 

            if (cache[m, n] != 0)
            {
                return cache[m, n];
            }
            else
            {
                // If diagonal movements are allowed then the last addition is required.
                cache[m, n] = UniquePaths(stopX - 1, stopY, startX, startY, m, n) + UniquePaths(stopX, stopY - 1, startX, startY, m, n);
                return cache[m, n];
            }
            //if (stopX < m-1)
            //{
            //    tc += UniquePaths(stopX + 1, stopY, startX, startY, m, n);
            //}
            //
            //if (stopY < n-1)
            //{
            //    tc += UniquePaths(stopX, stopY+1, startX, startY, m, n);
            //}

            //Console.WriteLine("tc={0} y={1} x={2}", tc, stopY, stopX); 
            //Console.ReadLine();
            //return tc;
        }

        // Q:: O(n) solution to find 2 numbers in an array that sum up to a target value        
        static void PrintPairsSum(int[] arr, int target)
        {
            int first = 0;
            int last = arr.Length - 1;
            int sum = -9999;

            while (first < last)
            { 
                sum=arr[first]+arr[last];
                if (sum == target)
                {
                    Console.WriteLine("{0}+{1}={2}",arr[first], arr[last], target);
                    first++;
                    last--;
                }
                else if (sum > target)
                {
                    last--;
                }
                else 
                {
                    first++;
                }
            }
        }

        // Q:: for extending the above 2 number solution to 3 numbers
        static void PrintPairsSum3(int[] arr, int target, int i)
        {
            int first = 0;
            int last = arr.Length - 1;
            int sum = -9999;

            while (first < last)
            {
                sum = arr[first] + arr[last];
                if (first == i)
                {
                    first++;
                }
                else if (last == i)
                {
                    last--;
                }
                else if (sum == target)
                {
                    Console.WriteLine("{0}+{1}={2}", arr[first], arr[last], target);
                    first++;
                    last--;
                }
                else if (sum > target)
                {
                    last--;
                }
                else
                {
                    first++;
                }
            }
        }

        // calculate the number of 2s in a number
        static int calclate2s(int num_ip)
        {
            int num = num_ip;
            int rem;
            int count=0;
            while (num != 0)
            {
                rem = num % 10;
                if (rem == 2)
                {
                    count++;
                }
                num = num / 10;
            }
            //Console.WriteLine("Num2s in {0} = {1}",num_ip,count);
            return count;
        }


        static int calculateNums(int num, int target)
        { 
            // target--> check how many of these in 0-num
            int num2s=-1;

            // convert number to int array
            List<int> numList = new List<int>();

            while (num != 0)
            {
                int rem = num % 10;
                numList.Add(rem);
                num = num / 10;
            }


            for (int i = numList.Count; i >= 0; i--)
            { 
                
            }


            return num2s;
        }


        static bool isMatch(string s, string p)
        {
            char[] s1 = s.ToCharArray(); // raw string
            char[] p1 = p.ToCharArray(); // string with regex
            List<char> pChar = new List<char>();
            int count = 0;
            char c;
            // compress p1
            for (int i = 1; i < p1.Length; i++)
            {
                if (p1[i] == p1[i - 1])
                {
                    count++;
                }
                else
                {
                    pChar.Add(p1[i-1]);
                    pChar.Add(Convert.ToChar(count));
                    Console.Write("{0}{1}", p1[i - 1], count);
                    count=0;
                }
            }

            //int len = Math.Max(s1.Length,p1.Length);
            //
            //for (int i = 0; i < len-1; i++)
            //{ 
            //    if(s1[i+1]=='*')
            //    {
            //        // do nothing
            //    }
            //    else if (s[i+1]=='.')
            //    {
            //        if (s[i]!=p[i])
            //        {
            //            return false;
            //        }
            //    }
            //}
            
            
            return false;

        }



        static int countWays(int n, int[] b, int l)
        {
            if (n < 0)
            {
                return 0;
            }
            else if (n == 0)
            {
                for (int i = 0; i < b.Length; i++)
                {
                    Console.Write("{0}:",b[i]);
                }
                Console.WriteLine();
                    return 1;
            }
            else
            {
                l++;
                b[l] = n;                
                return countWays(n - 5, b, l) + countWays(n - 10, b, l); // +countWays(n - 15, paths);
            }
        }

        /*
        static void matrixWords(bool[,] isVisited, Dictionary<string,int> dict, char[,] mat, StringBuilder sb, int x, int y)
        {
            sb.Append(mat[x, y]);
            string s = sb.ToString();
            Console.WriteLine("s='{0}'",s);
            if (dict.ContainsKey(s))
            {
                Console.WriteLine("Found Word='{0}'  at X={1}, Y={2}.",s,x,y);
            }
                        
            isVisited[x, y] = true;

            int kx=-1;
            int ky=-1;
            for (kx=-1; kx<2; kx++)
            {
                for (ky=-1; ky<2; ky++)
                {
                    if (kx==0 && ky==0)
                    {
                        continue;
                    }
                    else
                    {
                        //Console.WriteLine("x={0},y={1}",x,y);
                        if ((isValidIdx(3,3,x+kx,y+ky)) && (!isVisited[x+kx,y+ky]))
                        {
                            matrixWords(isVisited, dict, mat, sb, x+kx, y+ky);
                        }
                    }
                }
            }
            
            //if ((isValidIdx(3,3,x+1,y)) && (!isVisited[x + 1, y]))
            //{
            //    matrixWords(isVisited, dict, mat, sb, x + 1, y);
            //}            
            //
            //
            //    if ((isValidIdx(3,3x,y+1)) && (!isVisited[x, y+1]))
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x, y+1);
            //    }
            //
            //
            //if (x-1>-1)
            //{
            //    if (!isVisited[x-1, y])
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x-1, y);
            //    }
            //}
            //
            //if (y-1>-1)
            //{
            //    if (!isVisited[x, y-1])
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x, y-1);
            //    }
            //}
            //
            //if (x - 1 > -1 && y - 1 > -1)
            //{
            //    if (!isVisited[x-1, y - 1])
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x-1, y - 1);
            //    }
            //}
            //
            //if (x+1<3 && y+1<3)
            //{
            //    if (!isVisited[x+1, y+1])
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x+1, y+1);
            //    }
            //}
            //
            //if (x-1>-1 && y+1<3)
            //{
            //    if (!isVisited[x-1, y+1])
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x-1, y+1);
            //    }
            //}
            //
            //if (x+1<3 && y-1>-1)
            //{
            //    if (!isVisited[x+1, y-1])
            //    {
            //        matrixWords(isVisited, dict, mat, sb, x+1, y-1);
            //    }
            //}


        }

        static bool isValidIdx(int sizeX, int sizeY, int x, int y)
        {
            if (x < sizeX && x > -1 && y < sizeY && y > -1)
            { 
                return true;
            }
            else
            {
                return false;
            }
        }
        */
    }



    public class Utility
    {

        public void MatrixWords(bool[,] isVisited, Dictionary<string, int> dict, char[,] mat, char[] sb, int level, int x, int y, Dictionary<string,int> dictTracker)
        {
            sb[level]=mat[x,y];
            string s = new string(sb);
            s = s.Substring(0,level);
            
            if (dict.ContainsKey(s))
            {
                if (!dictTracker.ContainsKey(s))
                {
                    Console.WriteLine("Found Word='{0}'  at X={1}, Y={2}.", s, x, y);
                    dictTracker[s] = 1;
                }                
            }

            if (level == 9)
            {
                return;
            }

            //isVisited[x, y] = true;            

            int kx = -1;
            int ky = -1;
            for (kx = -1; kx < 2; kx++)
            {
                for (ky = -1; ky < 2; ky++)
                {
                    if (kx == 0 && ky == 0)
                    {
                        continue;
                    }
                    else
                    {                        
                        if ((IsValidIdx(3, 3, x + kx, y + ky)) && (!isVisited[x + kx, y + ky]))
                        {
                            isVisited[x+kx,y+ky]=true;
                            level++;
                            MatrixWords(isVisited, dict, mat, sb, level, x + kx, y + ky, dictTracker);
                            isVisited[x + kx, y + ky] =false;
                            level--;
                        }
                    }
                }
            }
                        


        }

        public void MatrixWordsTrie(bool[,] isVisited, Trie tt, char[,] mat, char[] sb, int level, int x, int y, Dictionary<string, int> dictTracker)
        {
            sb[level] = mat[x, y];
            string s = new string(sb);
            s = s.Substring(0, level);
            //Console.WriteLine("s={0}",s);
            //Console.ReadLine();    
            if (tt.Search(s))
            {
                if (!dictTracker.ContainsKey(s))
                {
                    Console.WriteLine("Found Word='{0}'  at X={1}, Y={2}.", s, x, y);
                    dictTracker[s] = 1;
                }
            }

            if (level == 9)
            {
                return;
            }

            //isVisited[x, y] = true;            

            int kx = -1;
            int ky = -1;
            for (kx = -1; kx < 2; kx++)
            {
                for (ky = -1; ky < 2; ky++)
                {
                    if (kx == 0 && ky == 0)
                    {
                        continue;
                    }
                    else
                    {
                        if ((IsValidIdx(3, 3, x + kx, y + ky)) && (!isVisited[x + kx, y + ky]))
                        {
                            isVisited[x + kx, y + ky] = true;
                            level++;
                            MatrixWordsTrie(isVisited, tt, mat, sb, level, x + kx, y + ky, dictTracker);
                            isVisited[x + kx, y + ky] = false;
                            level--;
                        }
                    }
                }
            }
            
        }


        public bool IsValidIdx(int sizeX, int sizeY, int x, int y)
        {
            if (x < sizeX && x > -1 && y < sizeY && y > -1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

    }


    // Diagram Reference: https://visualstudiomagazine.com/articles/2015/10/20/text-pattern-search-trie-class-net.aspx

    public class Trie
    {
        private readonly TrieNode _root;

        public Trie()
        {
            _root = new TrieNode('^',0,null);
        }

        public TrieNode Prefix(string s)
        {
            var currentNode = _root;
            var result = currentNode;

            foreach (var c in s)
            {
                currentNode = currentNode.FindChildNode(c);
                if (currentNode == null)
                    break;
                result = currentNode;
            }

            return result;
        }

        // finds the last node of the matching char sequence, and inserts new node at the end. 
        public void Insert(string s)
        {
            var commonPrefix = Prefix(s);
            var current = commonPrefix;

            for (var i = current.Depth; i < s.Length; i++)
            {
                var newNode = new TrieNode(s[i], current.Depth + 1, current);
                current.Children.Add(newNode);
                current = newNode;
            }

            current.Children.Add(new TrieNode('$', current.Depth + 1, current));
        }

        // checks to see it the Trie contains the string. 
        // get the last matching char using Prefix() method. If for this Node, there is no Child node of value '$', then it means this word is not in the Dictionary
        // Another check, compare the depth of the node with string length, it it matches then the char count is equal.
        public bool Search(string s)
        {
            var prefix = Prefix(s);
            if ((prefix.FindChildNode('$') != null) && (prefix.Depth == s.Length))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        // finds the string, and goes to its child node '$'
        // then moves up deleting nodes one by one until there exists another child node(which would make up another string).
        public void Delete(string s)
        {
            if (Search(s))
            {
                var node = Prefix(s).FindChildNode('$');

                while (node.IsLeaf())
                {
                    var parent = node.Parent;
                    parent.DeleteChildNode(node.Value);
                    node = parent;
                }
            }
        }
    }

    public class TrieNode
    {
        public char Value { get; set; }
        public List<TrieNode> Children { get; set; }
        public TrieNode Parent { get; set; }
        public int Depth { get; set; }

        public TrieNode(char value, int depth, TrieNode parent)
        {
            Value = value;
            Children = new List<TrieNode>();
            Depth = depth;
            Parent = parent;
        }


        // returns true if Node has no children
        public bool IsLeaf()
        {
            return Children.Count == 0;
        }

        public TrieNode FindChildNode(char c)
        {
            foreach (var child in Children)
                if (child.Value == c)
                    return child;

            return null;
        }

        public void DeleteChildNode(char c)
        {
            for (var i = 0; i < Children.Count; i++)
                if (Children[i].Value == c)
                    Children.RemoveAt(i);
        }
    }
}



