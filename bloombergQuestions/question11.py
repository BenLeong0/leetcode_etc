class MinHeap:
    def __init__(self,key=lambda x:x):
        self.heap = []
        self.key = key
        self.size = 0

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
        if pos == 0: return
        if self.key(self.heap[pos]) < self.key(self.heap[self.parent(pos)]):
            self.swap(pos,self.parent(pos))
            self.upHeap(self.parent(pos))

    def insert(self,val):
        self.size +=1
        self.heap.append(val)
        self.upHeap(self.size-1)

    def downHeap(self,pos):
        if self.rightChild(pos) < self.size:
            if self.key(self.heap[self.leftChild(pos)]) > self.key(self.heap[self.rightChild(pos)]):
                if self.key(self.heap[pos]) > self.key(self.heap[self.rightChild(pos)]):
                    self.swap(pos, self.rightChild(pos))
                    return self.downHeap(rightChild(pos))
        if self.leftChild(pos) < self.size:
            if self.key(self.heap[pos]) > self.key(self.heap[self.leftChild(pos)]):
                self.swap(pos, self.leftChild(pos))
                return self.downHeap(self.leftChild(pos))

    def extract(self):
        self.size -= 1
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.downHeap(0)
        return result


dataHeap = MinHeap(key=lambda x:x[0])
dataInput = [(1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")]
i = 1

for data in dataInput:
    dataHeap.insert(data)
    while dataHeap.size > 0:
        if dataHeap.heap[0][0] == i:
            print(dataHeap.extract()[1])
            i += 1
        else:
            break
