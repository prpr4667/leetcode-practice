def productExceptSelf(nums):
    prod = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        prod[i] = prod[i - 1] * nums[i - 1]

    multiplier = 1
    for i in range(len(prod) - 1, -1, -1):
        prod[i] *= multiplier
        multiplier *= nums[i]

    return prod


nums = [3, 4, 1, 5]
print(productExceptSelf(nums))

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))
