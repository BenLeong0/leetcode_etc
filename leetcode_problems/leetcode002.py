class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        arr = [self.val]
        curr = self
        while curr.next:
            curr = curr.next
            arr.append(curr.val)
        return str(arr)


def arrayToLinkedList(arr):
    head = ListNode()
    curr = head
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return head.next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    carry = 0
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = (val1 + val2 + carry)
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next

    if carry > 0:
        curr.next = ListNode(carry)

    return dummyHead.next


l1 = arrayToLinkedList([2,4,3])
l2 = arrayToLinkedList([5,6,4])

print(addTwoNumbers(l1, l2))
