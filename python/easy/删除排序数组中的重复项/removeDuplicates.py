class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <2:
            return len(nums)
        resLen = 1
        currentNum = nums[0]
        for i in range(1,len(nums)):
            if(currentNum != nums[i]):
                nums[resLen] = nums[i]
                currentNum = nums[i]
                resLen += 1
        return resLen
