def longestConsecutive(nums):
    if not nums:
        return 0
    nums.sort()
    curr, _max = 1, 1
    i = 0

    while i < len(nums) - 1:
        i += 1
        if nums[i - 1] == nums[i] - 1:
            curr += 1
        elif nums[i - 1] == nums[i]:
            continue
        else:
            curr = 1
        _max = max(_max, curr)

    return _max


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
