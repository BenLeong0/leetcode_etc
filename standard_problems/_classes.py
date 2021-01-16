from collections import deque

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


# Binary search tree
class BSTNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if not self.root:
            return []
        result = [self.root.val]
        queue = deque([self.root])
        while queue:
            layer_size = len(queue)
            for _ in range(layer_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    result.append(node.left.val)
                else:
                    result.append(None)

                if node.right:
                    queue.append(node.right)
                    result.append(node.right.val)
                else:
                    result.append(None)
        return str(result)


    def insert(self,val,parent=None):
        if not parent:
            parent = self.root

        if not parent:
            self.root = BSTNode(val)
            return
        elif val<parent.val:
            if parent.left:
                self.insert(val,parent.left)
            else:
                parent.left = BSTNode(val)
        else:
            if parent.right:
                self.insert(val,parent.right)
            else:
                parent.right = BSTNode(val)

    def search(self,val,node=None):
        if not node:
            node = self.root

        if not node:
            return None
        elif val==node.val:
            return node
        elif val<node.val:
            if node.left:
                return self.search(val,node.left)
            else:
                return None
        else:
            if node.right:
                return self.search(val,node.right)
            else:
                return None

class SplayTree(BinaryTree):
    def find(self,val,node=None,p=None,g=None,gg=None):
        pass
