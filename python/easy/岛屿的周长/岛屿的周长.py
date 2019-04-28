class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Sum = 0
        for i in range(1, len(grid) + 1):
            line = grid[i - 1]
            for j in range(1, len(line) + 1):
                if line[j - 1] == 1:
                    Sum += 4
                    #print(Sum)
                    if i > 1 and grid[i - 2][j - 1] == 1:
                        Sum -= 2
                    #print(Sum)
                    if j < len(line):
                        if line[j - 1] == 1 and line[j] == 1:
                            Sum -= 2
                    #print(Sum)
                else:
                    continue
        return Sum
