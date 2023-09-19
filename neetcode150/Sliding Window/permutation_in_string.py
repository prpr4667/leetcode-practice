from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    s1_chars = {}
    for c in s1:
        if c not in s1_chars:
            s1_chars[c] = 0
        s1_chars[c] += 1

    k = len(s1)

    for start in range(len(s2) - k + 1):
        if start == 0:
            for r in range(k):
                if s2[r] in s1_chars:
                    s1_chars[s2[r]] -= 1
        else:
            print(start, start + k - 1, s2[start - 1], s2[start + k - 1])
            if s2[start - 1] in s1_chars:
                s1_chars[s2[start - 1]] += 1
            if s2[start + k - 1] in s1_chars:
                s1_chars[s2[start + k - 1]] -= 1

        if checkMatch(s1_chars):
            return True

    return False


def checkMatch(window):
    for key, val in window.items():
        if val != 0:
            return False
    return True


# s1 = "ab"
# s2 = "eidbaooo"
# print(checkInclusion(s1, s2))

s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))
