"""
Merge ranges

sample:
[ {'start':1, 'end':3 }, {'start':2, 'end':4 }, {'start':5, 'end':6 }]

real time series data:
...
"""

def _pt_exists_in_range(iprange, pt):
    return True if iprange['start'] <= pt <= iprange['end'] else False


def _merge_range(merged_ranges, iprange):
    found = None
    for mrange in merged_ranges:
        start_exists = _pt_exists_in_range(mrange, iprange['start'])
        end_exists = _pt_exists_in_range(mrange, iprange['end'])
        if start_exists and not end_exists:
            mrange['end'] = iprange['end']
            found = True
            break
        elif not start_exists and end_exists:
            mrange['start'] = iprange['start']
            found = True
            break

    if not found:
        merged_ranges.append(iprange)

def merge_ranges(ipranges):
    merged_ranges = list()

    for iprange in ipranges:
        _merge_range(merged_ranges, iprange)
    return merged_ranges


if __name__ == '__main__':
    ipranges = [ {'start':1, 'end':3 }, {'start':2, 'end':4 }, {'start':5, 'end':6 }]
    print ipranges
    print merge_ranges(ipranges)
