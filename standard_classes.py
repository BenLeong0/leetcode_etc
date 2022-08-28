from typing import List, Optional


class ListNode:
    def __init__(self, val: int=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

    def __repr__(self):
        arr = [self.val]
        curr = self
        while curr.next:
            curr = curr.next
            arr.append(curr.val)
        return str(arr)


class DoublyLinkedNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional['DoublyLinkedNode'] = None,
        prev: Optional['DoublyLinkedNode'] = None,
    ):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        arr = [self.val]
        curr = self
        while curr.next:
            curr = curr.next
            arr.append(curr.val)
        return str(arr)


def initialiseLinkedList(values: List[int]):
    dummyHead = ListNode()
    curr = dummyHead
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next
