# Wrong Answer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        next_nodes = []
        while head is not None:
            nodes.append(head.val)
            next_nodes.append(head.next)
            head = head.next
            
        tail = ListNode(None)
        for i in range(1, len(nodes)+1):
            tail.val = nodes[-i]
            tail.next = ListNode(next_nodes[-i])
            tail = tail.next
            
        return tail
            
