import time
def quick_sort(arr):
    start_time = time.time()
    quick_sort_inner(arr, start_time)

def quick_sort_inner(arr, start_time):
    if time.time() - start_time > 10:
        raise TimeoutError("Function execution took more than 10 seconds")

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_inner(left, start_time) + middle + quick_sort_inner(right, start_time)