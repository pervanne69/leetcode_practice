from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]):
    values = []
    current = head
    while head:
        values.append(current.val)
        current = current.next
    left, right = 0, len(values) - 1
    if left == right:
        return True
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1

    return True


print(isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))