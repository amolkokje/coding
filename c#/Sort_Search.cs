using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_Search_Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = {3,3,3,3,3,3,3,3,3,3,3,3,5,5}; //{1,2,2,3,4,5,5,5,5,5,5,5,6,7,8,8,9,9}; //{1,3,4,5,6,63,52,45,7,12,89,21};
            printArray(arr);

            //bubbleSort(arr);
            //printArray(bubbleSorted_arr);
            //
            //selectionSort(arr);
            //printArray(selectionSorted_arr);

            MergeSort(arr);

            int val;
            val = binarySearch_First(arr, 3);
            Console.WriteLine("binary search first = {0}",val);
            val = binarySearch_Last(arr, 3);
            Console.WriteLine("binary search last = {0}", val);
            val = binarySearch_magicIndex(arr,0,arr.Length-1);
            Console.WriteLine("binary search magic index = {0}", val);


            binarySearch(arr, 9);

            val = binarySearchRecursive(arr,0,arr.Length,8);
            Console.WriteLine("Binary Recursive Search = {0}",val);

            factorial(5);
            factorial(10);
            int fact;
            fact=5;
            Console.WriteLine("factorial recursive of {0} is {1}",fact,factorialRecursive(fact));
            fact=10;
            Console.WriteLine("factorial recursive of {0} is {1}", fact, factorialRecursive(fact));

            fact = 5;
            Console.WriteLine("factorial recursive dynamic of {0} is {1}", fact, factorialRecursiveDynamic(fact));
            fact = 10;
            Console.WriteLine("factorial recursive dynamic of {0} is {1}", fact, factorialRecursiveDynamic(fact));

            Console.ReadLine();
        }

        static void printArray(int[] ipArr)
        {
            for (int i = 0; i < ipArr.Length; i++)
            {
                Console.Write(": {0}", ipArr[i]);                
            }
            Console.WriteLine();
            Console.WriteLine("------------------------------------");
        }

        // ASCENDING ORDER SORT ONLY

        // BUBBLE SORT
        static void bubbleSort(int[] ipArr)
        {
            for (int i = 0; i < ipArr.Length; i++)
            {
                for (int j = 0; j < ipArr.Length - 1; j++)
                {
                    if (ipArr[j] > ipArr[j + 1])
                    {
                        int temp = ipArr[j];
                        ipArr[j] = ipArr[j + 1];
                        ipArr[j + 1] = temp;
                    }
                }
            }

            printArray(ipArr);
        }

        // SELECTION SORT
        static void selectionSort(int[] ipArr)
        {
            int min_index=0;
            for (int i = 0; i < ipArr.Length-1; i++)
            {
                min_index=i;
                for (int j = i + 1; j < ipArr.Length; j++)
                {
                    if (ipArr[min_index] > ipArr[j])
                    {
                        min_index = j;
                    }
                    if (min_index != i)
                    { 
                        int temp = ipArr[min_index];
                        ipArr[min_index] = ipArr[i];
                        ipArr[i] = temp;
                    }
                }   
            }

           printArray(ipArr);
        }

        // MERGE SORT
        static void MergeSort(int[] inputArray)
        {
            int left = 0;
            int right = inputArray.Length - 1;
            InternalMergeSort(inputArray, left, right);
            printArray(inputArray);
        }

        static void InternalMergeSort(int[] inputArray, int left, int right)
        {
            int mid = 0;
            if (left < right)
            {
                mid = (left + right) / 2;
                InternalMergeSort(inputArray, left, mid);
                InternalMergeSort(inputArray, (mid + 1), right);
                MergeSortedArray(inputArray, left, mid, right);
            }
        }

        static void MergeSortedArray(int[] inputArray, int left, int mid, int right)
        {
            int index = 0;
            int total_elements = right - left + 1; //BODMAS rule
            int right_start = mid + 1;
            int temp_location = left;
            int[] tempArray = new int[total_elements];
                     

            /* Iterate through helper array. Compare the left and right
            * half, copying back the smaller element from the two halves
            * into the original array. */
            while ((left <= mid) && right_start <= right)
            {
                if (inputArray[left] <= inputArray[right_start])
                {
                    tempArray[index++] = inputArray[left++];
                }
                else
                {
                    tempArray[index++] = inputArray[right_start++];
                }
            }

            // copy over the left-over elements
            if (left > mid)
            {
                while(right_start<=right)
                    tempArray[index++] = inputArray[right_start++];
            }
            else
            {
                while(left<=mid)
                    tempArray[index++] = inputArray[left++];
            }
            
            // copy all elements to target array
            for (int i = 0, j = temp_location; i < total_elements; i++, j++)
            {
                inputArray[j] = tempArray[i];
            }
        }


        // BINARY SEARCH - for a sorted array
        static void binarySearch(int[] arr, int x)
        {
            Console.WriteLine("Searching for {0} ... ", x);
            int left = 0;
            int right = arr.Length - 1;
            int mid;
            while (left <= right)
            {
                mid = (left + right) / 2;
                if (arr[mid] < x)
                {
                    left = mid + 1;
                }
                else if (arr[mid] > x)
                {
                    right = mid - 1;
                }
                else
                {
                    Console.WriteLine("Found {0}: Index {1}", x, mid);
                    return;
                }
            }
            Console.WriteLine("not found");
        }

        static int binarySearchRecursive(int[] arr, int left, int right, int x)
        {
            int mid = 0;
            while (left < right)
            {
                mid = (left + right) / 2;
                if (x > arr[mid])
                {
                    Console.Write("mid={0}; ",mid);
                    return binarySearchRecursive(arr, mid+1, right, x);
                }
                else if (x < arr[mid])
                {
                    Console.Write("mid={0}; ", mid);
                    return binarySearchRecursive(arr,left,mid,x);
                }
                else
                {
                    return mid;
                }
            }
            Console.WriteLine("Value {0} not found",x);
            return mid;
        }

        static int binarySearch_First(int[] arr, int v)
        {
            int first = -1;
            int left = 0;
            int right = arr.Length - 1;
            int len = right - left;
            //Console.WriteLine("len={0}",len);
            while (left < right)
            {
                
                int mid = (left+right)/2;
                //Console.WriteLine("m={0}",mid);
                if (arr[mid] == v)
                {
                    first = mid;
                    right = mid - 1;
                }
                else if (arr[mid] > v)
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
                Console.WriteLine("l={0}  r={1}  f={2}",left,right, first);
                //Console.WriteLine("f={0}",first);
            }

            return first;
           
        }

        static int binarySearch_Last(int[] arr, int v)
        {
            int last=-1;
            int left = 0;
            int right = arr.Length - 1;
            while (left < right)
            {
                if (arr[right] == v)
                {
                    return right;
                }

                int mid = (left + right) / 2;
                //Console.WriteLine("m={0}", mid);
                if (arr[mid] == v)
                {
                    last = mid;
                    left = mid + 1;
                }
                else if (arr[mid] > v)
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
                //Console.WriteLine("l={0}  r={1}", left, right);
            }
            return last;
        }


        static int binarySearch_magicIndex(int[] arr, int left, int right)
        {
            if ((left < right) && (left>=0) && (right<=arr.Length))
            {
                int mid = (left + right) / 2;
                //Console.WriteLine("m={0}", mid);
                if (arr[mid] == mid)
                {
                    return mid;
                }
                    
                int rightI = Math.Max(arr[mid], mid - 1);
                right = binarySearch_magicIndex(arr, left, rightI);
                if (right!=-1)
                {
                    return right;
                }

                int leftI = Math.Min(arr[mid], mid + 1);
                left = binarySearch_magicIndex(arr, leftI, right);
                if (left != -1)
                {
                    return left;
                }                
                
                //Console.WriteLine("l={0}  r={1}", left, right);
            }
            return -1;
        }


        // FACTORIAL
        static void factorial(int x)
        {            
            int fact = 1;
            if (x == 0)
            {
                fact = 1;
                Console.WriteLine("Factorial of {0} is {1}", x, fact);
                return;
            }
            else 
            {
                for (int i = 1; i <= x; i++)
                {
                    fact = fact * i;
                }
                Console.WriteLine("Factorial of {0} is {1}", x, fact);
                return;
            }            
        }

        static int factorialRecursive(int x)
        {
            if ((x == 0) || (x == 1))
            {
                return 1;
            }
            else
            {
                return x*factorialRecursive(x-1);
            }
        }

        static int[] cache = Enumerable.Repeat(-1, 256).ToArray(); // assumption max number is 256
        static int factorialRecursiveDynamic(int x)
        {           

            if ((x == 0) || (x == 1))
            {
                if (cache[x] != -1)
                {
                    return cache[x];
                }
                else
                { 
                    cache[x]=1;
                    return cache[x];
                } 
            }
            else
            {
                if (cache[x] != -1)
                {
                    Console.WriteLine("cache[{0}]={1}",x,cache[x]);
                    return cache[x];
                }
                else
                {
                    cache[x] = x * factorialRecursiveDynamic(x - 1);
                    return cache[x];
                }
                
            }
        }


       
    }
}
