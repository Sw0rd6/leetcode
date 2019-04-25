class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for i in ops:
            length = len(scores)

            if i == 'C':
                scores.pop(length-1)
            elif i == 'D':
                score = scores[length-1] * 2
                scores.append(score)
            elif i == '+':
                score = scores[length-2] + scores[length-1]
                scores.append(score)
            else:
                scores.append(int(i))
        
        return sum(scores)
