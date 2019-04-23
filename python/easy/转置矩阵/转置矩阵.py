class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))    #*A在这里表示拆解的意思，即对矩阵拆解得到三个元组
