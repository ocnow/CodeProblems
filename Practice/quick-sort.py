def partition(arr,low,high):
    pivot_index = low + (high-low)//2
    

    partition_ele_place = low-1

    for j in range(low,high+1,1):
        if arr[j] < arr[pivot_index]:
            partition_ele_place +=1
            if partition_ele_place == pivot_index:
                partition_ele_place += 1
            arr[j],arr[partition_ele_place] = arr[partition_ele_place],arr[j]
            print("here:"+str(arr))
        
    partition_ele_place +=1    
        
    arr[partition_ele_place],arr[pivot_index] = arr[pivot_index],arr[partition_ele_place]
    print(arr)
    return partition_ele_place

def quickSort(arr,low,high):

    if low < high:
        partition_place = partition(arr,low,high)
        quickSort(arr,low,partition_place-1)
        quickSort(arr,partition_place+1,high)
    
    return arr

def quickThat(arr):
    quickSort(arr,0,len(arr)-1)
    print(arr)

arr = [4,5,3,7,2]
quickThat(arr)