import heapq
from collections import Counter


def topKFrequent_heap(nums, k):
    freq = {}

    for n in nums:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1

    heap = []
    for key, val in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            if heap[0][0] < val:
                heapq.heappush(heap, (val, key))
                heapq.heappop(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


def topKFrequent(nums, k):
    freq = [[] for _ in range(len(nums) + 1)]
    count = {}
    result = []

    for n in nums:
        if n not in count:
            count[n] = 0
        count[n] += 1

    for num, frequency in count.items():
        freq[frequency].append(num)

    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result


nums = [3, 0, 2, 0]
k = 2
print(topKFrequent(nums, k))
