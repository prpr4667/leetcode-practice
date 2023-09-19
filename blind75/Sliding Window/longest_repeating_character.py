def characterReplacement(s: str, k: int) -> int:
    start, max_len = 0, 0
    frequency = {}

    for end in range(len(s)):
        right = s[end]
        frequency[right] = 1 + frequency.get(right, 0)

        if end - start + 1 - max(frequency.values()) <= k:
            max_len = max(max_len, end - start + 1)
        else:
            frequency[s[start]] -= 1
            start += 1

    return max_len


s = "AABABBA"
k = 1
print(characterReplacement(s, k))
