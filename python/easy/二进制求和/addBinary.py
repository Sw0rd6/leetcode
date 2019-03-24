class Solution:
    def addBinary(self, a: str, b: str) -> str:
        Sum1, Sum2 = 0, 0
        for i in range(len(a)):
            Sum1 += int(a[i]) * (2 ** (len(a) - i - 1))
        for j in range(len(b)):
            Sum1 += int(b[j]) * (2 ** (len(b) - j - 1))
        Sum = Sum1 + Sum2
        return bin(Sum)[2:]
        
