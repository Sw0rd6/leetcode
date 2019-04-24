class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        首先找到车所在的行和列
        然后根据所在的行和列匹配车所能捕获的卒数
        '''
        output = 0
        column = None
        row = None
        for i in range(len(board)):
            if 'R' in board[i]:
                row = i
                break
        column = board[row].index('R')    #R的索引也就是它的所在列
        s = ''.join(board[row])   #车所在行的所有元素
        s = s.replace('.', '')    #意义很大，把点去掉，让字符串拼接在一起，这也是主要思路
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        s = ''.join([i[column] for i in board])   #使用列表解析得到车所在列的所有元素
        s = s.replace('.', '')    #同上
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        return output
