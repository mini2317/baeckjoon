import sys
sys.setrecursionlimit
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.capacity = 4 * self.length
        self.tree = [0] * self.capacity
        self.arr = arr
        self._init_(0, self.length - 1, 1)

    def _init_(self, start, end, idx):
        if start == end:
            self.tree[idx] = self.arr[start]
            return self.arr[start]
        mid = (start + end) // 2
        value = self._init_(start, mid, idx * 2) + self._init_(mid + 1, end, idx * 2 + 1)
        self.tree[idx] = value
        return value

    def getSum(self, rangeOfValue):
        return self._getSumRecursion_(rangeOfValue, 0, self.length - 1, 1)
    
    def _getSumRecursion_(self, rangeOfValue, start, end, idx):
        if rangeOfValue[1] < start or rangeOfValue[0] > end: return 0
        if rangeOfValue[0] <= start and rangeOfValue[1] >= end: return self.tree[idx]
        mid = (start + end) // 2
        return self._getSumRecursion_(rangeOfValue, start, mid, idx * 2) + self._getSumRecursion_(rangeOfValue, mid + 1, end, idx * 2 + 1)

    def append(self, item):
        self.length += 1
        self.capacity += 4
        self.tree += [0, 0, 0, 0]
        self.arr.append(item)
        self._init_(0, self.length - 1, 1)
    
    def update(self, start, end, ):
        self.length += 1
        self.capacity += 4
        self.tree += [0, 0, 0, 0]
        self.arr.append()
        self._init_(0, self.length - 1, 1)
    
tree = SegmentTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(tree.tree)
s = tree.getSum((4, 6))
print(s)