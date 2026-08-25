# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currnode = ListNode()
        readnode = head
        while(readnode):
            node = ListNode()
            currnode.val = readnode.val
            node.next = currnode
            currnode = node
            readnode = readnode.next

        return currnode.next
