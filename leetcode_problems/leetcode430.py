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

def flatten_recursive(head):
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


def flatten_dfs(head):
    if not head:
        return head
    stack = [head]
    dummyHead = Node()
    curr = dummyHead
    while stack:
        node = stack.pop()
        if node.next:
            stack.append(node.next)
        if node.child:
            stack.append(node.child)
        curr.next, node.prev = node, curr
        node.child = None
        curr=node
    curr.next=None
    dummyHead.next.prev=None
    return dummyHead.next
