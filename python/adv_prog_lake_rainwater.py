"""
Ref: https://www.geeksforgeeks.org/trapping-rain-water/

CHALLENGE:
Imagine an island that is in the shape of a bar graph. When it rains, certain areas of the island fill up with
rainwater to form lakes. Any excess rainwater the island cannot hold in lakes will run off the island to the west or
east and drain into the ocean.

Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) that can
compute the total volume (capacity) of water that could be held in all lakes on such an island given an array of the
heights of the bars. Assume an elevation map where the width of each bar is 1.

Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2],
return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)
"""

def maxWater(arr) :

    # To store the maximum water
    # that can be stored
    n = len(arr)
    res = 0

    # For every element of the array
    for i in range(1, n - 1):

        # Find the maximum element on its left
        left_max = max(arr[:i+1])

        # Find the maximum element on its right
        right_max = max(arr[i:])

        # Water height at any point is determined by the min of the max heights in the left/right of the point
        # it is also dependent on the height of land at that point
        res += min(left_max, right_max) - arr[i]

    return res

if __name__ == '__main__':
    island_arr = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
    print maxWater(island_arr)
