class Solution:
        #32ms
    def removeElement(self, nums: list[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index
        # 48ms
    def removeElement2(self, nums: list[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        nums.sort()
        return len(nums)


