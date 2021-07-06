# make cycle
# break link
# return new head


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


def initialiseLinkedList(values):
    dummyHead = ListNode()
    curr = dummyHead
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


a = initialiseLinkedList([1, 2, 3, 4, 5])


def rotateRight(head, k):
    if not head:
        return head
    # Find length and tail
    curr = head
    length = 1
    while curr.next:
        curr = curr.next
        length += 1

    # Just return if no rotation
    k %= length
    if k == 0:
        return head

    # Link tail to head
    curr.next = head

    curr = head
    # Find new tail
    for _ in range(length - k - 1):
        curr = curr.next
    newHead = curr.next
    curr.next = None
    return newHead


print(rotateRight(a, 2))