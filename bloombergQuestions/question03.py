import binarytree as bt

class ProductHeap:
    def __init__(self):
        self.heap = []
        self.hash = {}

    def __repr__(self):
        return str(self.heap) + '\n' + str(self.hash)

    def parent(self, i):
        if i == 0:
            return -1
        return i//2

    def children(self, i):
        if len(self.heap) < 2 * i + 2:
            return []
        elif len(self.heap) == 2 * i + 2:
            return [self.heap[2 * i + 1]]
        else:
            return [self.heap[2 * i + 1], self.heap[2 * i + 2]]

    def addData(self, data):
        if data['name'] in self.hash:
            self.heap[self.hash[data['name']]]['volume'] += data['volume']
            self.hash[data['name']] = self.up_heap(self.hash[data['name']])
        else:
            self.heap.append(data)
            self.hash[data['name']] = self.up_heap(len(self.heap)-1)

    def up_heap(self, id):
        parent_id = self.parent(id)
        if parent_id >= 0:
            if self.heap[id]['volume'] > self.heap[parent_id]['volume']:
                self.heap[id], self.heap[parent_id] = self.heap[parent_id], self.heap[id]
                self.hash[self.heap[id]['name']] = id
                self.hash[self.heap[parent_id]['name']] = parent_id
                return self.up_heap(parent_id)
        return id

    def down_heap(self, id):
        child_vals = self.children(id)
        if child_vals:
            child_id = 2*id+1+(child_vals[-1]['volume']>child_vals[0]['volume'])
            if self.heap[id]['volume'] < self.heap[child_id]['volume']:
                self.heap[id], self.heap[child_id] = \
                  self.heap[child_id], self.heap[id]
                self.hash[self.heap[id]['name']] = id
                self.hash[self.heap[child_id]['name']] = child_id
                return self.down_heap(child_id)
        return id

    def extract(self):
        root = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self.hash[self.heap[0]['name']] = 0
        del self.hash[root['name']]
        self.down_heap(0)
        return root

    def topResults(self, k):
        savedHeap = [x.copy() for x in self.heap]
        savedHash = self.hash.copy()
        print('========== Top', k, 'results: ==========')
        for i in range(k):
            print(i+1,':',self.extract())
        self.heap = savedHeap
        self.hash = savedHash


Exchange = ProductHeap()

Exchange.addData({'name': 'vodafone', 'volume': 20})
Exchange.addData({'name': 'bt', 'volume': 20})
Exchange.addData({'name': 'vodafone', 'volume': 30})
Exchange.addData({'name': 'tmobile', 'volume': 80})
Exchange.addData({'name': '3', 'volume': 10})

print(Exchange)
Exchange.topResults(3)
