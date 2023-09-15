def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        _sum = numbers[l] + numbers[r]
        if _sum == target:
            return [l + 1, r + 1]
        elif _sum < target:
            l += 1
        else:
            r -= 1
    return [-1, -1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))
