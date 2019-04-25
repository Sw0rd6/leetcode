class Solution:
    def calPoints(self, ops: List[str]) -> int:
        Sum, temp, j = 0, [], 0
        for i in range(len(ops)):
            if ops[i] == "+":
                temp.append(temp[i - 1 - j] + temp[i - 2 - j])
                Sum += temp[i - 1 - j] + temp[i - 2 - j]
            elif ops[i] == "C":
                Sum -= temp[i - 1 - j]
                temp.remove(temp[i  - 1 - j])
                j += 2
            elif ops[i] == "D":
                temp.append(temp[i - 1 - j] * 2)
                Sum += temp[i - 1 - j] * 2
            else:
                temp.append(int(ops[i]))
                Sum += int(ops[i])
            #print(temp, Sum)
        return Sum
