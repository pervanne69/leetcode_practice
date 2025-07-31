from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()  # создаём фальшивый старт
    current = dummy  # указатель, по которому будем строить новый список

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next  # двигаем указатель

    # если один из списков ещё не закончился — добавляем его в конец
    current.next = list1 if list1 else list2

    return dummy.next  # пропускаем фальшивую голову

print(mergeTwoLists(ListNode(), ListNode(0)))