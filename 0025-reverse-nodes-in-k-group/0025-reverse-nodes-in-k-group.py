class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # 1. Group lo k nodes unnaya check chey
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # 2. Next group start ni save chesuko
            next_group = kth.next

            # 3. Ee group ni reverse chey
            prev = next_group
            curr = prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 4. Reverse ayina group ni main list ki kalupu
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp

        return dummy.next