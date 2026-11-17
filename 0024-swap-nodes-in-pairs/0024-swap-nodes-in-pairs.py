class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Pair undannantha varaku swap chey
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap chese 3 links
            first.next = second.next
            second.next = first
            prev.next = second

            # Next pair ki move avvu
            prev = first

        return dummy.next