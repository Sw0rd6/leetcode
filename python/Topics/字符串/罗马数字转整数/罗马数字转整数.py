class Solution:
    def romanToInt(self, s: str) -> int:
        i, Sum = 0, 0
        Dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i < len(s):
            if i < len(s) - 1:
                if s[i:i+2] in "IV IX XL XC CD CM":
                    Sum += Dict[s[i+1]] - Dict[s[i]]
                    i += 2
                else:
                    Sum += Dict[s[i]]
                    i += 1
            else:
                Sum += Dict[s[i]]
                i += 1
        s = int(Sum)
        return s
