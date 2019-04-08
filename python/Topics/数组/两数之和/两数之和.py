class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        size=0
        while size < len(nums):
            if target-nums[size] in d:
                if d[target-nums[size]] < size:
                    return [d[target-nums[size]],size]  #因为题目已经假设了每种输入只会对应一个答案
            else:
                d[nums[size]] = size
            size = size + 1
