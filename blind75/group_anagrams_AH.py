def groupAnagrams(strs):
    result = []
    anagrams = {}

    for w in strs:
        sorted_w = "".join(sorted(list(w)))
        if sorted_w not in anagrams:
            anagrams[sorted_w] = []
        anagrams[sorted_w].append(w)

    for v in anagrams.values():
        result.append(v)

    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
