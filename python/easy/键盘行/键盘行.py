class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('ZXCVBNMzxcvbnm')
        set2 = set('ASDFGHJKLasdfghjkl')
        set3 = set('QWERTYUIOPqwertyuiop')
        
        return [x for x in words if set(x) <= set1 or set(x) <= set2 or set(x) <= set3]
