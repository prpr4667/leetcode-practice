# Given a string, s, that represents a DNA subsequence, and a number k, return all the contiguous subsequences (substrings) of length k that occur more than once in the string.


def find_repeated_sequences(s, k):
    if len(s) <= k:
        return []

    code = {"A": 1, "C": 2, "G": 3, "T": 4}
    hashes, result = set(), set()
    curr_hash = 0
    for start in range(len(s) - k + 1):
        if start == 0:
            for r in range(k):
                curr_hash = curr_hash * 10 + code[s[r]]
        else:
            curr_hash = (curr_hash % (pow(10, k - 1))) * 10
            curr_hash = curr_hash + code[s[start + k - 1]]

        if curr_hash in hashes:
            result.add(s[start : start + k])
        hashes.add(curr_hash)

    return result


inputs_string = [
    "ACGT",
    "AGACCTAGAC",
    "AAAAACCCCCAAAAACCCCCC",
    "GGGGGGGGGGGGGGGGGGGGGGGGG",
    "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT",
    "TTTTTGGGTTTTCCA",
    "AAAAAACCCCCCCAAAAAAAACCCCCCCTG",
    "ATATATATATATATAT",
]
inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

for i in range(len(inputs_k)):
    print(i + 1, ".\tInput Sequence: '", inputs_string[i], "'", sep="")
    print("\tk: ", inputs_k[i], sep="")
    print(
        "\tRepeated Subsequence: ",
        find_repeated_sequences(inputs_string[i], inputs_k[i]),
    )
    print("-" * 100)
