import time

# Run test class
# pytest -s tests/algorithms/test_bubble_sort.py::test_bubble_sort

def bubble_sort(arr):
    start_time = time.time()

    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if time.time() - start_time > 10:
                raise TimeoutError("Function execution took more than 10 seconds")
            if arr[j] > arr[j+1]:
                 arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr