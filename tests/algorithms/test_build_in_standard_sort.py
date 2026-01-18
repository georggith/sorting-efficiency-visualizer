import scr.algorithms.build_in as bi

# Run test class
# pytest -s tests/algorithms/test_build_in_standard_sort.py::test_buildin_standard_sort

def test_buildin_standard_sort():
    test_arr = [99,3,4,67]
    sorted_arr = bi.buildin_standard_sort(test_arr)
    print(sorted_arr)

    assert sorted_arr == [3,4,67,99]