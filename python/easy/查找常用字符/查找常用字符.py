class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        import functools as func
        return list(func.reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())
