class Solution:
    def isPalindrome(self, x: int) -> bool:
        y,temp = 0,x
        while x > 0:
            l = len(str(x))
            #print(l)
            a = x % 10
            #print(a,x)
            y += a * (10 ** (l-1))
            #print(y)
            x //= 10
        if temp == y:
            return True
        else:
            return False
