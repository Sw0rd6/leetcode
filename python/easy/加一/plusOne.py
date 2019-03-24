class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Num, ls = 0, []
        for i in range(len(digits)):
            Num += digits[i] *(10 ** (len(digits) - i - 1))
        Num = Num + 1
        for j in range(len(str(Num))):
            ls.append(int(str(Num)[j]))
        return ls
