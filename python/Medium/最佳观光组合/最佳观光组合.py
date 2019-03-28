class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        Sum, Sum_left = 0, 0
        for i in range(len(A)):
            Sum = max(Sum, Sum_left + A[i] - i) #动态规划的思想
            Sum_left = max(Sum_left, A[i] + i)  #动态规划的思想
        return Sum  
