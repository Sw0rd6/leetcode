class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [t[i] for i in range(len(t)) if t.count(t[i]) != s.count(t[i])][-1]
