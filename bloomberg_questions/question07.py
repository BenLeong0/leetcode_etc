class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key  = key
        self.val  = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        arr = [(self.key, self.val)]
        curr = self
        while curr.next:
            curr = curr.next
            arr.append((curr.key, curr.val))
        return str(arr)


class LRUCache:
    def __init__(self, capacity):
        self.c = capacity
        self.length = 0
        self.head = Node()
        self.end = self.head
        self.hash = {}

    def __repr__(self):
        return str(self.head) + '\n' + str(self.hash)

    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            if self.end == node:
                self.end = self.end.prev
                self.end.next = None
            else:
                node.prev.next, node.next.prev = node.next, node.prev
            self.insertAtFront(self.hash[key])
            if self.head == self.end:
                self.end = self.head.next
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            if self.end == node:
                self.end = self.end.prev
                self.end.next = None
            else:
                node.prev.next, node.next.prev = node.next, node.prev
            self.insertAtFront(self.hash[key])
            if self.head == self.end:
                self.end = self.head.next

        else:
            if self.length == self.c:
                del self.hash[self.end.key]
                self.end = self.end.prev
                self.end.next = None
            else:
                self.length += 1

            self.insertAtFront(Node(key=key, val=value))
            self.hash[key] = self.head.next
            if self.length == 1:
                self.end = self.head.next


    def insertAtFront(self,node):
        up = self.head.next
        self.head.next = node
        node.next, node.prev = up, self.head
        if up:
            up.prev = node


sol = LRUCache(1)
sol.put(2,1)
print(sol)
print(sol.get(2))
print(sol)
print(sol.end)
sol.put(3,2)
print(sol)
print(sol.get(2))
print(sol)
print(sol.get(3))
