class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        if x == 0:
            return 0
        else:
            while x > 0:
                b = len(str(x))
                a = x % 10
                num += a * (10 ** (b-1))
                x //= 10
                b -= 1
            while x < 0:
                b = len(str(x))
                a = abs(x) % 10
                num += a * (-10 ** (b-2))
                x = -(abs(x) // 10)
                b -= 1
            if num < -2 ** 31 or num > 2 ** 31 -1:
                return 0
            else:
                return num
