class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1,N + 1):
            s = bin(i)[2:]
            if s in S:
                continue
            else:
                return False
        return True
