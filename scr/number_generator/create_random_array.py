import numpy as np

def generate_arrays(min_power, max_power, min_value, max_value):
    arrays = {}
    base = 10
    for power in range(min_power, max_power):
        arr_length = base**power
        new_arr = generate_random_array(arr_length,min_value,max_value)
        arrays[arr_length] = new_arr
    return arrays

def generate_random_array(length, min_val, max_val, allow_floats=False, allow_negative=False):
    """
    Generates an array of random numbers based on specified constraints.
    """

    # Validation: Ensure the start point is bigger than or equal to 0 if negatives are not allows
    if min_val < 0 and allow_negative==False:
        return "Error: Min value cannot smaller than 0 if negatives are not allowed."

    # Validation: Ensure the range is logical
    if min_val > max_val:
        return "Error: Min value cannot be greater than Max value."

    # use num py to create a array of random numbers
    if allow_floats:
        random_numbers = np.random.randint(min_val, max_val, length, dtype=np.float32)
    else:
        random_numbers = np.random.randint(min_val, max_val, length, dtype=np.int32)
        
    return random_numbers