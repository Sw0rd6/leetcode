class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str1 = str(bin(n))[2:][::-1]
        while len(str1)<32:
            str1 += '0'
        return int(str1,2)
