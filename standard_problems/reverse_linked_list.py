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


values = [1,6,2,3,7,9,4,9]

head = initialiseLinkedList(values)

# 1 > 2 > 3 > 4
# 4 > 3 > 2 > 1

def reverseLinkedList(head):
    def f(node=head):
        if node.next.next:
            newHead = f(node.next)
            node.next.next = node
            return newHead
        node.next.next = node
        return node.next

    newHead = f()
    head.next = None
    return newHead


print(head)
print(reverseLinkedList(head))
