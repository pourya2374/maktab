
input()
heights = list(map(int, input().split(' ')))


def find_max_area(input_list: list, start_index: int, stop_index: int) -> int:
    if start_index >= stop_index:
        return 0

    min_value = min(input_list[start_index:stop_index])
    min_index = input_list.index(min_value)

    right = find_max_area(input_list, min_index+1, stop_index)
    current = (stop_index - start_index) * min_value
    left = find_max_area(input_list, start_index, min_index)
    return max([right, current, left])


print(find_max_area(heights, 0, len(heights)))
