class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return ""
        res = "1"
        for i in range(n - 1):
            tar, count, newres = res[0], 0, ""
            for j in res:
                if j == tar:
                    count = count + 1
                else:
                    newres = newres + str(count) + tar
                    tar, count = j, 1
            res = newres + str(count) + tar
        return res
