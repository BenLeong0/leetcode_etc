class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __repr__(self):
        arr = [self.val]
        curr = self
        while curr.next:
            curr = curr.next
            arr.append(curr.val)
        return str(arr)

def flatten(head):
    def childList(node):
        curr = Node(next=node)
        nextNode = curr.next
        while nextNode:
            curr = nextNode
            nextNode = curr.next
            if curr.child:
                firstChild, lastChild = childList(curr.child)
                curr.child = None
                curr.next, firstChild.prev = firstChild, curr
                lastChild.next = nextNode
                if nextNode:
                    nextNode.prev = lastChild

        # If the final node had children, then this moves curr to its final descendant
        while curr.next:
            curr = curr.next
        return node, curr

    childList(head)
    return head
