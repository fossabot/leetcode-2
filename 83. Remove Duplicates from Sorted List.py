class Solution(object):
    def deleteDuplicates(self, head):
        initial = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        head = initial
        return head

