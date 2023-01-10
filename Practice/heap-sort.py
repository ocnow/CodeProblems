def heapifyIthNode(arr,i,sz):
    lft = 2 * i + 1
    rght = 2 * i + 2
    largest = i

    if lft < sz and arr[lft] > arr[largest]:
        largest = lft
    
    if rght < sz and arr[rght] > arr[largest]:
        largest = rght

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapifyIthNode(arr,largest,sz)

def heapSort(arr):
    sz = len(arr)
    for i in range(sz//2-1,-1,-1):
        heapifyIthNode(arr,i,sz)

    for i in range(sz-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapifyIthNode(arr,0,i)

    print(arr)

arr = [10,9,1000,500,253,129,981,111]
heapSort(arr)

