import time

# Run test class
# pytest -s tests/algorithms/test_insertion_sort.py::test_insertion_sort

def insertion_sort(arr, max_time=10):
    start_time = time.time()
    
    for i in range(1, len(arr)):
        if time.time() - start_time > max_time:
            raise TimeoutError("Function execution took more than {max_time} seconds")
        key = arr[i]
        j=i-1

        while j >=0 and arr[j] > key:
            if time.time() - start_time > max_time:
                raise TimeoutError("Function execution took more than {max_time} seconds")
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key

    return arr