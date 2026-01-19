import time

# Run test class
# pytest -s tests/algorithms/test_bubble_sort.py::test_bubble_sort

def bubble_sort(arr, max_time=10):
    start_time = time.time()

    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if time.time() - start_time > max_time:
                raise TimeoutError("Function execution took more than {max_time} seconds")
            if arr[j] > arr[j+1]:
                 arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr