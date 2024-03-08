def is_enough_num(poss_length, num, width, height):
    max_num = (poss_length // width) * (poss_length // height)
    return max_num >= num


def binary_min_length_search(num, width, height):
    if (
        not (1 <= num <= 10**12)
        or not (1 <= width <= 10**9)
        or not (1 <= height <= 10**9)
    ):
        return None

    if width >= height:
        largest_length = width * num
    else:
        largest_length = height * num

    left_border = 1
    right_border = largest_length

    while left_border < right_border:
        current_position = (left_border + right_border) // 2
        if is_enough_num(current_position, num, width, height):
            right_border = current_position
        else:
            left_border = current_position + 1

    return left_border
