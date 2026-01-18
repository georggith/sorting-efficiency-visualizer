import time
from scr.algorithms.quick_sort import quick_sort
from scr.algorithms.bubble_sort import bubble_sort
from scr.algorithms.counting_sort import counting_sort
from scr.number_generator.create_random_array import generate_arrays
from scr.algorithms.build_in import buildin_standard_sort

class run_algorithms():

    min_array_size = 1
    max_array_size = 9

    min_value = 0
    max_value = 10000

    # Set the max duration before the algorithm stops to 10 seconds
    run_time_max_duration = 10

    def sort_array(self, sample_arrays, sorting_func, algo):
        durations = {}

        for length, arr in sample_arrays.items():
            start_time = time.time() 
            try:
                sorting_func(arr[:])
            except TimeoutError as e:
                print("Sorting was aborded, because the sorting took more than 10 seconds")
                durations[length] = self.run_time_max_duration
                break
            end_time = time.time()
            durations[length] = end_time - start_time
        
        print(f'{algo} times')
        for length, duration in durations.items():
            print(f'Length = {length:,}; Duration: {duration}')
        
        return durations

    def easy_compare(self):
        start_time = time.time()
        sample_arrays = generate_arrays(self.min_array_size, self.max_array_size, self.min_value, self.max_value)
        end_time = time.time()

        print(f'Time to create Random Arrays: {end_time-start_time}')

        result_data = {}
        result_data["Build in list.sort()"] = self.sort_array(sample_arrays, buildin_standard_sort, "Build in list.sort()")
        result_data["Bubble Sort"] = self.sort_array(sample_arrays, bubble_sort, "Bubble Sort")
        result_data["Quick Sort"] = self.sort_array(sample_arrays, quick_sort, "Quick Sort")
        result_data["Counting Sort"] = self.sort_array(sample_arrays, counting_sort, "Counting Sort")

        return result_data