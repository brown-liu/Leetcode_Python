arraylist = [10, 30, 33, 66, 99]
target = 99
expected = [2, 3]


class Solution:
    def twoSum(self, nums, target):
        # using a dict here is much easier, no need to worry about index, only the key and value
        li = {}
        for index, num in enumerate(nums):
            n = target - num
            if n not in li:
                li[num] = index
            else:
                print(li)
                return [li[n], index]


two_sum = Solution()

if two_sum.twoSum(arraylist, target) == expected:
    print('answer is correct')
