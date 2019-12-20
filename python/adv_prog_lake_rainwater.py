"""
Ref: https://techdevguide.withgoogle.com/paths/advanced/volume-of-water/#!

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


def get_island_ranges(arr):
    """ get list of island ranges that can hold water """
    n = len(arr)
    i = 0
    ranges = list()
    start = None
    end = None

    #####
    while i < n - 1:
        # start of the range
        if not start:
            if arr[i] > arr[i + 1]:
                start = i

        # if start of range exists, then find end of range
        elif start:
            # for ranges in middle
            if arr[i] >= arr[start]:
                ranges.append((start, i))
                start = None
                continue

        i += 1

    #####
    # for last bucket, there may be no entry of same height
    if start:
        i = start + 1
        min_value = None
        max_diff = -1
        # find the max height on the right hand side of the start found
        while i < n:
            if not min_value:
                min_value = arr[i]

            elif min_value:
                # if max diff is found, then that will be the last bucket
                diff = arr[i] - min_value
                if diff > max_diff:
                    max_diff = diff
                    end = i

            i += 1
    if end:
        ranges.append((start, end))

    return ranges


def get_volume(arr, island_range):
    """ get the volume of water held by a range """
    range_volume = 0

    # min height of the bucket end will decide the height of water level
    min_height = min(arr[island_range[0]], arr[island_range[1]])
    for i in range(island_range[0] + 1, island_range[1]):
        range_volume += min_height - arr[i]
    print 'Range={}, Volume={}'.format(island_range, range_volume)
    return range_volume


def calculate_total_volume(island_arr):
    # 1 - get ranges that can store water
    ranges = get_island_ranges(island_arr)
    print 'RANGES={}'.format(ranges)

    # 2 - calculate total volume in these ranges
    volume = 0
    for range in ranges:
        volume += get_volume(island_arr, range)
    print 'VOLUME={}'.format(volume)


if __name__ == '__main__':
    island_arr = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
    calculate_total_volume(island_arr)
