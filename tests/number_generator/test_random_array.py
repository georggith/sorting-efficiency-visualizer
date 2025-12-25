import scr.number_generator.create_random_array as ng

# Run test class
# pytest -s tests/number_generator/test_random_array.py::test_generate_random_array

def test_generate_random_array():

    length = 10
    min_val = 0
    max_val = 100
    is_float = False
    allow_negative=False
    
    arr = ng.generate_random_array(length, min_val, max_val, is_float, allow_negative)

    print(arr)

    assert len(arr) == length, 'The size of the array is incorrect'
    assert min(arr) >= min_val, 'The min value of the array is too small'
    assert max(arr) <= max_val, 'The max value of the array is too big'

def test_generate_arrays():
    min_power = 2
    max_power = 5
    arrs = ng.generate_arrays(min_power, max_power)
