import time

# Run test class
# pytest -s tests/algorithms/test_merge_sort.py::test_merge_sort

def merge_sort_v1(arr, max_time=10):
    start_time = time.time()
    
    def merge(arr, left, mid, right):
        count_left = mid - left + 1
        count_right = right - mid

        temp_left = [0] * count_left
        temp_right = [0] * count_right

        for i in range(count_left):
            temp_left[i] = arr[left+i]
        for j in range(count_right):
            temp_right[j] = arr[mid + 1 + j]

        i, j = 0, 0
        write = left

        while i < count_left and j < count_right:
            if temp_left[i] < temp_right[j]:
                arr[write] = temp_left[i]
                i += 1
            else:
                arr[write] = temp_right[j]
                j += 1
            write +=1

        while i < count_left:
            arr[write] = temp_left[i]
            i += 1
            write += 1

        while j < count_right:
            arr[write] = temp_right[j]
            j += 1
            write += 1


    def sort(arr, left, right):
        if time.time() - start_time > max_time:
            raise TimeoutError("Function execution took more than {max_time} seconds")
        if left < right:
            mid = (left + right)//2
            sort(arr,left, mid)
            sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    sort(arr, 0, len(arr)-1)

    return arr

def merge_sort_v2(arr, max_time=10):
    start_time = time.time()
    
    def merge(arr, left, mid, right):
        count_left = mid - left + 1
        count_right = right - mid

        temp_left = arr[left:mid+1]
        temp_right = arr[mid+1:right+1]

        i, j = 0, 0
        write = left

        while i < count_left and j < count_right:
            if temp_left[i] < temp_right[j]:
                arr[write] = temp_left[i]
                i += 1
            else:
                arr[write] = temp_right[j]
                j += 1
            write +=1

        while i < count_left:
            arr[write] = temp_left[i]
            i += 1
            write += 1

        while j < count_right:
            arr[write] = temp_right[j]
            j += 1
            write += 1


    def sort(arr, left, right):
        if time.time() - start_time > max_time:
            raise TimeoutError("Function execution took more than {max_time} seconds")
        if left < right:
            mid = (left + right)//2
            sort(arr,left, mid)
            sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    sort(arr, 0, len(arr)-1)

    return arr