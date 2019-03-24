'''
这道题的算法思想是牛顿迭代法，运用公式，详细见https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)
