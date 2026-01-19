import scr.algorithms.insertion_sort as isort

def test_insertion_sort():
    test_arr = [99,3,4,67]
    sorted_arr = isort.insertion_sort(test_arr)
    print(sorted_arr)

    assert sorted_arr == [3,4,67,99]