def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        num = nums[i]
        l, r = i + 1, len(nums) - 1

        while l < r:
            _sum = nums[l] + nums[r]
            if _sum == -num:
                result.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif _sum > -num:
                l += 1
            else:
                r -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
nums = [0, 0, 0]
print(threeSum(nums))
