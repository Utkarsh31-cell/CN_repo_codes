import heapq
def kthLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    n = len(lst)
    for i in range(k, n):
        if heap[0] < lst[i]:
            heapq.heapreplace(heap, lst[i])
    return heap[0]

    # heap = lst[:]
    # heapq._heapify_max(heap)

    # # Get the kth largest element from the max-heap
    # kth_largest = heapq.nlargest(k, heap)[ -1 ]

    # return kth_largest


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
