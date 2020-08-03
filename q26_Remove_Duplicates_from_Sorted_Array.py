class Solution:
    def removeDuplicates1(self, nums) -> int:
        length = 0
        li = len(nums)
        for i in range(li - 1):
            if nums[i] != nums[i + 1]:
                length += 1
        return length + 1

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_

li=[1,2,2,2,3,4,4,5,5,6,7]
solution=Solution()
a1=solution.removeDuplicates1(li)
a2=solution.removeDuplicates2(li)
print(f'a1=>{a1}\na2=>{a2}')