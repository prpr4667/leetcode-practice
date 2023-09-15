def twoSum(nums, target: int):
    indexes = {}

    for i, n in enumerate(nums):
        if target - n in indexes:
            return [i, indexes[target - n]]

        indexes[n] = i
    return [-1, -1]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
