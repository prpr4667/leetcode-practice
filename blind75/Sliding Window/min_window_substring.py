from collections import Counter


def minWindow(s, t):
    start = 0
    res, min_len = "", float("inf")
    t_chars = Counter(t)
    curr_window = {}
    matches = 0
    to_match = len(t_chars.keys())

    for end in range(len(s)):
        char = s[end]

        # track in curr window
        if char not in curr_window:
            curr_window[char] = 0
        curr_window[char] += 1

        # check for match
        if char in t_chars and t_chars[char] == curr_window[char]:
            matches += 1

        # increment start to look for a smaller substring
        while matches == to_match and start <= end:
            curr_len = end - start + 1
            # update max length
            if curr_len < min_len:
                min_len = curr_len
                res = s[start : end + 1]

            left = s[start]
            curr_window[left] -= 1
            if left in t_chars and t_chars[left] > curr_window[left]:
                matches -= 1
            start += 1

    return res


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

s = "a"
t = "aa"
print(minWindow(s, t))
