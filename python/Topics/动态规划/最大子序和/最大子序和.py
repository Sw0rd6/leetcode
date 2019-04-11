class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)  #动态规划核心之处，简单来说就是，每时刻的最值状态覆盖了前面的所有最值状态。
        return max(nums)
