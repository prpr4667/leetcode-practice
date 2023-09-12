def isAnagram(s: str, t: str) -> bool:
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1

    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] == 0:
            del count[c]

    return len(count) == 0


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
