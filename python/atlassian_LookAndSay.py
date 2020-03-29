def look_say(num):
    """
    num to convert
    :param num: input number
    :return: convert num to say
    """

    # convert num to list of numbers
    nums = [int(s) for s in str(num)]
    n = len(nums)

    output = ''  # string to store output
    i = 0
    while i < n:
        c = 1  # counter to manage count of duplicates
        j = i + 1
        while j < n:
            if nums[j] != nums[i]:
                break
            else:
                c += 1
                j += 1

        output += '{}{}'.format(c, nums[i])
        i += c

    return output


def look_say_depth(num, depth):
    """
    convert num for the depth count
    :param num: number to convert
    :param depth: depth to iterate on
    :return: converted number
    """
    output = num  # start with output same as num, since if depth is 1, its the same as input num

    # iterate over depth, as need to apply look_say for the depth count
    for dep in range(depth):
        output = look_say(output)  # replace the output with new output at that depth
        print 'Depth [{}]: Output [{}]'.format(dep, output)

    return output


if __name__ == '__main__':

    # input as (depth, number)
    ips = [(1, 1),
           (1, 11),
           (1, 21),
           (1, 1211),
           (1, 111221),
           (2, 11)
           ]
    for ip in ips:
        depth, number = ip
        print '-------------'
        print 'number=[{}], depth=[{}], LookAndSay=[{}]'.format(number, depth, look_say_depth(number, depth))
