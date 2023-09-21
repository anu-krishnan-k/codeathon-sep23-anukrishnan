def sort_array(arr):
    """
    This function takes an array of numbers and sorts it in ascending order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = [100,180,260,310,40,535,695]
sorted_arr = sort_array(arr)
print(sorted_arr)

def test_sort_array():
    arr1 = [100,180,260,310,40,535,695]
    assert sort_array(arr1) == [40, 100, 180, 260, 310, 535, 695]

    arr2 = [1,2,3,4,5,6,7,8,9,10]
    assert sort_array(arr2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    arr3 = [10,9,8,7,6,5,4,3,2,1]
    assert sort_array(arr3) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test_sort_array()
