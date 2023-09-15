def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

nums = [1,2,3,1]
print(containsDuplicate(nums))