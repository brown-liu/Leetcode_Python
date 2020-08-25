class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            if target == 0:
                return 0
            elif target > max(nums):
                return len(nums)
            else:
                for item in nums:
                    if item > target:
                        return nums.index(item)


import random

a = random.randint(0, 20)
b = random.randint(0, 20)

nums = []
for i in range(a):
    nums.append(random.randint(0, 20))

nums.sort()
