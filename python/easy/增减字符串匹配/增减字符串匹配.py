class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        left, right, ls = 0, len(S), []     #双指针法的思想
        for i in S:
            if i == "I":
                ls.append(left)
                left += 1
            else:
                ls.append(right)
                right -= 1
        ls.append(right)
        return ls
