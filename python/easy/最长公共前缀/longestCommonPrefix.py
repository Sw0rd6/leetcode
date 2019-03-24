class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Strings = ""
        j = 0
        while True:
            ls = []
            for i in range(len(strs)):
                if j < len(strs[i]):
                    ls.append(strs[i][j])
                else:
                    return Strings
            ls = set(ls)
            if len(ls) == 1:
                j += 1
                Strings += "".join(list(ls))
                continue
            else:
                return Strings
        else:
            return ""
