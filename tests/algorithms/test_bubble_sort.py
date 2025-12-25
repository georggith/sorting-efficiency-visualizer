import scr.algorithms.bubble_sort as bs

def test_bubble_sort():
    test_arr = [99,3,4,67]
    sorted_arr = bs.bubble_sort(test_arr)
    print(sorted_arr)

    assert sorted_arr == [3,4,67,99]