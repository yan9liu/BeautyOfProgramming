def insertHeap(heap, num):
    heap.append(num)
    i = len(heap)-1
    parent = (i-1)/2
    while parent >= 0 and heap[i] > heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent = (i-1)/2

#a = [4, 6, 2, 7, 1]
#heap = []
#for i in range(len(a)):
#    insertHeap(heap, a[i])
#print heap


def divedeEqually(a):
    size = len(a)
    if size%2 <> 0:
        print "error!"
        return

    SUM = sum(a)
    threashold = SUM/2

    heaps = []
    for i in range(size/2+1):
        heaps.append([])
    heaps[0].append(0)

    for k in range(1, size+1):
        i_max = min(k-1, size/2-1)
        i = i_max
        while i >= 0:
            for v in heaps[i]:
                insertHeap(heaps[i+1], a[k-1]+v)
            i -= 1
    print a
    print heaps

b = [1, 2, 3, 4, 5, 6]
divedeEqually(b)

