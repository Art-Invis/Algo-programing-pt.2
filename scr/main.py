def is_monotonic(array):
    increase, decrease = True, True

    for i in range(len(array) - 1):
        if not (array[i] >= array[i + 1]):
            decrease = False
        if not (array[i] <= array[i + 1]):
            increase = False

    return increase or decrease

nums = [1, 2, 3, 4, 5]
func = is_monotonic(nums)
print(func)
