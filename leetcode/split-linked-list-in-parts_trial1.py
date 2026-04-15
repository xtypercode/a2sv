# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next

        cur, ans = head, []
        for i in range(k):
            part = (n // k)
            if i < n % k:
                part += 1

            dummy = temp = ListNode(-1)
            while cur and part > 0:
                temp.next = ListNode(cur.val)
                temp = temp.next
                cur = cur.next
                part -= 1

            ans.append(dummy.next)
            
        return ans