class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the second half
        second = slow.next
        slow.next = prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge the two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2