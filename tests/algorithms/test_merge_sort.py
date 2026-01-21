import scr.algorithms.merge_sort as ms

def test_merge_sort_v1():
    test_arr = [99,3,4,67,101]
    sorted_arr = ms.merge_sort_v1(test_arr)
    print(sorted_arr)

    assert sorted_arr == [3,4,67,99,101]

def test_merge_sort_v2():
    test_arr = [99,3,4,67]
    sorted_arr = ms.merge_sort_v2(test_arr)
    print(sorted_arr)

    assert sorted_arr == [3,4,67,99]