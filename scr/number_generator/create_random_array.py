import random

def generate_arrays(min_power, max_power):
    arrays = {}
    base = 10
    for power in range(min_power, max_power):
        arr_length = base**power
        new_arr = generate_random_array(arr_length,0,10000)
        arrays[arr_length] = new_arr
    return arrays

def generate_random_array(length, min_val, max_val, is_float=False, allow_negative=False):
    """
    Generates an array of random numbers based on specified constraints.
    """
    # Boundary Adjustment: If negative numbers are NOT allowed, 
    # ensure the floor is at least 0.
    start_point = min_val if allow_negative else max(0, min_val)
    
    # Validation: Ensure the range is logical
    if start_point > max_val:
        return "Error: Min value cannot be greater than Max value."

    random_numbers = []
    
    for _ in range(length):
        if is_float:
            # random.uniform provides a floating point between two bounds
            num = random.uniform(start_point, max_val)
        else:
            # random.randint provides an integer including both endpoints
            num = random.randint(start_point, max_val)
            
        random_numbers.append(num)
        
    return random_numbers