from _classes import ListNode, initialiseLinkedList

values = [1,6,2,3,7,9,4,9]
head = initialiseLinkedList(values)

# 1 > 2 > 3 > 4
# 4 > 3 > 2 > 1

def reverseLinkedListRecursive(head):
    def reverse(curr=head):
        if not curr:
            return curr
        if not curr.next:
            return curr

        newHead = reverse(curr.next)
        curr.next.next = curr
        return newHead

    newHead = reverse()
    if head:
        head.next = None
    return newHead


def reverseLinkedListIterative(head):
    prev = None
    curr = head
    nxt  = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


print(head)

head = reverseLinkedListRecursive(head)
print(head)

head = reverseLinkedListIterative(head)
print(head)
