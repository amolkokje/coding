# ref:
# https://molchevskyi.medium.com/microsoft-interview-tasks-min-moves-to-make-string-without-3-identical-consecutive-letters-abe61ed51a10
# https://leetcode.com/discuss/interview-question/1398095/tesla-software-engineer-interview-experience

"""
3 consecutive: baaab, replace the middle a (3 / 3 == 1)
4 consecutive: baaaab, replace the third a (4 / 3 == 1)
5 consecutive: baaaaab, replace the third a (5 / 3 == 1)
6 consecutive: baaaaaab -> baabaaab -> baaab -> bab with 2 replacements (6 / 3 == 2)
10 consecutive: baaaaaaaaaab -> baabaaaaaaab -> baaaaaaab -> baaaab -> baab with 3 replacements (10 / 3 == 3)
"""


def min_moves_to_make_str_without_consecutive_letters(s: str, k: int) -> int:
    """
    Given a string s, return the minimum number of moves required to make s a string without k consecutive identical letters.
    """
    n = len(s)

    if n < 3:
        return 0

    result = 0
    i = 0
    while i < n - 1:
        dupes = 1

        while i + 1 < n and s[i + 1] == s[i]:
            i += 1
            dupes += 1
            # print(i, dupes, result)
            if dupes == k:
                # print("found")
                result += 1
                dupes = 0

        i += 1

    # print(s, result)
    return result


assert min_moves_to_make_str_without_consecutive_letters("baaab", 3) == 1
assert min_moves_to_make_str_without_consecutive_letters("baaaaab", 3) == 1
assert min_moves_to_make_str_without_consecutive_letters("baaaaaaab", 3) == 2
assert min_moves_to_make_str_without_consecutive_letters("baaaaaaaaaaab", 3) == 3
