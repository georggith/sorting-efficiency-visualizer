import time

# Run test class
# pytest -s tests/algorithms/test_counting_sort.py::test_counting_sort 

def counting_sort(arr, max_time=10):
    start_time = time.time()

    min_val = min(arr)
    max_val = max(arr)

    freq = [0] * (max_val - min_val + 1)

    for num in arr:
        freq[num-min_val] += 1
        if time.time() - start_time > max_time:
            raise TimeoutError("Function execution took more than {max_time} seconds")        

    sorted_arr = []
    for i, count in enumerate(freq):
        sorted_arr.extend([i + min_val]*count)
        if time.time() - start_time > max_time:
            raise TimeoutError("Function execution took more than {max_time} seconds")

    return sorted_arr