class Solution:
    def titleToNumber(self, s: str) -> int:
        results = 0
        for i, item in enumerate(s):
            results = results + ((ord(item) - 64) * (26 ** (len(s) - 1 - i)))
        return results
