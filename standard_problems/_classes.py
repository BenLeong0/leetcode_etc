# Linked lists
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
class DoublyLinkedNode:
    def __init__(self, val=0, next=None, prev=None):
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
def initialiseLinkedList(values):
    dummyHead = ListNode()
    curr = dummyHead
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


# Heaps (kwarg key function for custom comparisons (eg lambda x:x[0]))
class MinHeap:
    def __init__(self,key=lambda x:x):
        self.heap = []
        self.key = key

    def __repr__(self):
        return str(self.heap)

    def parent(self, pos):
        return (pos-1)//2

    def leftChild(self,pos):
        return 2*pos+1

    def rightChild(self,pos):
        return 2*pos+2

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def upHeap(self,pos):
        while self.key(self.heap[pos]) < self.key(self.heap[self.parent(pos)]):
            if pos == 0:
                break
            self.swap(pos,self.parent(pos))
            pos = self.parent(pos)

    def insert(self,val):
        self.heap.append(val)
        self.upHeap(len(self.heap)-1)

    def downHeap(self,pos):
        while True:
            if self.rightChild(pos) < len(self.heap):
                if self.key(self.heap[self.leftChild(pos)]) > self.key(self.heap[self.rightChild(pos)]):
                    self.swap(pos, self.rightChild(pos))
                    pos = self.rightChild(pos)
                    continue
            if self.leftChild(pos) < len(self.heap):
                self.swap(pos, self.leftChild(pos))
                pos = self.leftChild(pos)
            else:
                break

    def extract(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.downHeap(0)
        return result
class MaxHeap:
    def __init__(self,key=lambda x:x):
        self.heap = []
        self.key = key

    def __repr__(self):
        return str(self.heap)

    def parent(self, pos):
        return (pos-1)//2

    def leftChild(self,pos):
        return 2*pos+1

    def rightChild(self,pos):
        return 2*pos+2

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def upHeap(self,pos):
        while self.key(self.heap[pos]) > self.key(self.heap[self.parent(pos)]):
            if pos == 0:
                break
            self.swap(pos,self.parent(pos))
            pos = self.parent(pos)

    def insert(self,val):
        self.heap.append(val)
        self.upHeap(len(self.heap)-1)

    def downHeap(self,pos):
        while True:
            if self.rightChild(pos) > len(self.heap):
                if self.key(self.heap[self.leftChild(pos)]) < self.key(self.heap[self.rightChild(pos)]):
                    self.swap(pos, self.rightChild(pos))
                    pos = self.rightChild(pos)
                    continue
            if self.leftChild(pos) > len(self.heap):
                self.swap(pos, self.leftChild(pos))
                pos = self.leftChild(pos)
            else:
                break

    def extract(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.downHeap(0)
        return result
