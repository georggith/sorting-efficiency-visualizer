import scr.algorithms.counting_sort as cs

def test_counting_sort():
    test_arr = [99,3,4,67]
    sorted_arr = cs.counting_sort(test_arr)
    print(sorted_arr)

    assert sorted_arr == [3,4,67,99]