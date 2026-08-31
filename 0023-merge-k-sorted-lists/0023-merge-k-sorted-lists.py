# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        result = None

        for head in lists:
            result = self.mergeTwoLists(result, head)

        return result

    def mergeTwoLists(self, l1, l2):

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:

            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 or l2

        return dummy.next

        