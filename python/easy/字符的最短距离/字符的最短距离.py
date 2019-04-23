class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        main_index = [i for i,e in enumerate(S) if e == C]  #enumerate返回枚举对象
        for index, element in enumerate(S):
            if index in main_index:
                res.append(0)
            else:
                res.append(min([abs(index - temp_index) for temp_index in main_index]))
        return res
