# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #print(head)
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
            #print(rev)
            #print(rev.next)
            #print(p)
        return rev
        #必须点赞这道，思想就是把每次的head.next指向上一个head.val从而实现反转
