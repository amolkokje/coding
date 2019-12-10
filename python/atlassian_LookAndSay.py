def look_say(num):
    """
    num to convert
    :param num: input number
    :return: convert num to say
    """

    # convert num to list of numbers
    num_list = [int(s) for s in str(num)]
    len_num = len(num_list)

    output = ''  # string to store output
    i = 0
    while i < len_num:
        c = 1  # counter to manage count of duplicates
        while True:
            # if array is not out of bound and duplicate exists, increment the count
            if i + c < len_num and num_list[i] == num_list[i + c]:
                c += 1
            else:
                # if no more duplicates, break the loop
                break

        output += '{}{}'.format(c, num_list[i])  # append to output string
        i += c  # move the index forward

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
    ips = [1, 11, 21, 1211, 111221]
    for ip in ips:
        print 'look_say({}) = {}'.format(ip, look_say(ip))

    n = 11
    d = 2
    print 'look_say_depth({},{}) = {}'.format(n, d, look_say_depth(n, d))
