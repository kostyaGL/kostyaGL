import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Rebalance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        print('max', self.max_heap, 'min', self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


a = MedianFinder()
a.add_num(1)
print(a.find_median())
a.add_num(2)
print(a.find_median())
a.add_num(3)
print(a.find_median())
a.add_num(4)
print(a.find_median())
a.add_num(5)
print(a.find_median())
a.add_num(6)
print(a.find_median())

"""
1, 2, 3, 4, 5, 6
max_heap = [-1, 3]
min_heap = [2, 4]
"""