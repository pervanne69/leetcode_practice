from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return run2(l1, l2)


def run1(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def run2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    first_number = []
    second_number = []
    carry = 0
    while l1:
        first_number.append(l1.val)
        l1 = l1.next
    while l2:
        second_number.append(l2.val)
        l2 = l2.next
    result = [0 for _ in range(max(len(first_number), len(second_number)))]
    for i in range(min(len(first_number), len(second_number))):
        ans = first_number[i] + second_number[i]
        result[i] = (ans + carry) % 10
        if len(str(ans + carry)) == 2:
            carry = (ans + carry) // 10
        else:
            carry = 0
    if abs(len(first_number) - len(second_number)) > 0:
        if len(first_number) > len(second_number):
            for j in range(i + 1, len(first_number)):
                ans = first_number[j] + carry
                result[j] = ans % 10
                if len(str(ans)) == 2:
                    carry = ans // 10
                else:
                    carry = 0
        else:
            for j in range(i + 1, len(second_number)):
                ans = second_number[j] + carry
                result[j] = ans % 10
                if len(str(ans)) == 2:
                    carry = ans // 10
                else:
                    carry = 0
        if len(str(ans)) == 2:
            result.append(ans // 10)
    elif carry != 0:
        result.append(carry)
    if not result:
        return None

    l_result = ListNode(result[0])
    current = l_result

    # Добавляем остальные узлы
    for i in range(1, len(result)):
        current.next = ListNode(result[i])
        current = current.next

    return l_result


s = Solution()
# l_result1 = s.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
# l_result2 = s.addTwoNumbers(ListNode(8, ListNode(3, ListNode(2))), ListNode(9, ListNode(2, ListNode(1))))
l_result3 = s.addTwoNumbers(ListNode(9), ListNode(1, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9,
                                                                                                              ListNode(
                                                                                                                  8,
                                                                                                                  ListNode(
                                                                                                                      9,
                                                                                                                      ListNode(
                                                                                                                          9,
                                                                                                                          ListNode(
                                                                                                                              9)))))))))))
