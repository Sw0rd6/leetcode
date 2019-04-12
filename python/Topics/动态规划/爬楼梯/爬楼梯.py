#爬楼梯为动态规划问题（斐波那契数列思想）
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2]
        if n < 3:
            return res[n-1]
        else:
            for i in range(2, n):
                res.append(res[i-1] + res[i-2])     # res[i] = res[i-1] + res[i-2] # 其中res[i]越界
            return res[-1]
