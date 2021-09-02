def rec_sum_two_elements(arr, arr_sum=[]):
    if len(arr) == 1:
        return arr_sum
    else:
        arr_sum.append(arr[0] + arr[1])
        arr.pop(0)
        return rec_sum_two_elements(arr, arr_sum)
