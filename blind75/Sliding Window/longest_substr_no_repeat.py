def lengthOfLongestSubstring(s):
    chars = {}
    _max = 0

    l = 0
    for r in range(len(s)):
        if s[r] in chars:
            l = max(chars[s[r]] + 1, l)
        chars[s[r]] = r
        _max = max(_max, r - l + 1)

    return _max


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "abba"
print(lengthOfLongestSubstring(s))

s = "aabbcd"
print(lengthOfLongestSubstring(s))
