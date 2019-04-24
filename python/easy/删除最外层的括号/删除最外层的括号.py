class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ls = []
        string = ''
        for i in range(len(S)):
            ls.append(S[i])
            if ls.count('(') == ls.count(')'):
                string += ''.join(ls[1:-1])
                ls = []
        return string
