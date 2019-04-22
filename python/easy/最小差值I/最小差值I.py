class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxVal = max(A)
        minVal = min(A)
        if maxVal - minVal > K * 2:
            return maxVal - (K * 2) - minVal
        else:
            return 0
