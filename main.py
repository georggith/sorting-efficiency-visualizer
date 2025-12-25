import time
from scr.algorithms.quick_sort import quick_sort
from scr.algorithms.bubble_sort import bubble_sort
from scr.algorithms.counting_sort import counting_sort
from scr.number_generator.create_random_array import generate_arrays

def sort_array(sample_arrays, sorting_func, algo):
    durations = {}

    for length, arr in sample_arrays.items():
        start_time = time.time() 
        try:
            sorting_func(arr[:])
        except TimeoutError as e:
            print("Sorting was aborded, because the sorting took more than 10 seconds")
            durations[length] = 10
            break
        end_time = time.time()
        durations[length] = end_time - start_time
    
    print(f'{algo} times')
    for length, duration in durations.items():
        print(f'Length = {length:,}; Duration: {duration}')

if __name__ == "__main__":
    start_time = time.time()
    sample_arrays = generate_arrays(1,9)
    end_time = time.time()

    print(f'Time to create Random Arrays: {end_time-start_time}')

    sort_array(sample_arrays, bubble_sort, "Bubble Sort")
    sort_array(sample_arrays, quick_sort, "Quick Sort")
    sort_array(sample_arrays, counting_sort, "Counting Sort")
