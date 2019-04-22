class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)
        #这招妙啊，'2'相当于中间变量，学到了。
