class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        #&是按位与，|是按位或，^是按位异或，~是按位取反，>>是右移运算符，<<是左移运算符
        
