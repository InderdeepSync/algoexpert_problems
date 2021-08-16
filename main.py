#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def evaluate(arr, depth=1):
    total = 0

    for item in arr:
        val = item
        if isinstance(item, list):
            val = evaluate(item, depth=depth + 1)

        total += val

    return total * depth


def is_palindrome(string):
    for index in range(math.floor(len(string) / 2)):
        if string[index] != string[len(string) - 1 - index]:
            return False

    return True


def caesar_cipher_encryptor(string, shift_by=2):
    return "".join(map(chr, (map(lambda num: (((num + shift_by) - 97) % 26) + 97, map(ord, string)))))


def run_length_encoding(string):
    chars = []
    run_length = 0
    prev_char = string[0]

    for ch in string:
        if prev_char != ch:
            chars.append((run_length, prev_char))

            run_length = 0

        run_length += 1
        prev_char = ch
    else:
        chars.append((run_length, prev_char))

    final_list = []
    for count, ch in chars:
        while count > 9:
            final_list.extend((str(9), ch))
            count -= 9

        final_list.extend((str(count), ch))

    return "".join(final_list)


def first_non_repeating_character(string):
    chars_map = {}  # {ch: (freq, indices)}

    for index, ch in enumerate(string):
        if ch in chars_map:
            freq, index_inner = chars_map[ch]
            chars_map[ch] = (freq + 1, [*index_inner, index])
            continue

        chars_map[ch] = (1, [index])

    result_index = None
    for ch in chars_map:
        freq, indexes = chars_map[ch]
        if freq != 1:
            continue

        result_index = min(math.inf if result_index is None else result_index, indexes[0])
    else:
        return result_index


def is_monotonic_array(arr):
    prev_slope = None

    for index in range(1, len(arr)):
        slope = arr[index] - arr[index - 1]
        if slope == 0:
            continue

        if prev_slope is not None and slope * prev_slope < 0:
            return False

        prev_slope = slope
    else:
        return True


def array_of_products(arr):
    product = 1
    zero_index = None

    for index, item in enumerate(arr):
        if item != 0:
            product *= item
        else:
            zero_index = index
            break
    else:
        res = []
        for item in arr:
            res.append(int(product / item))

        return res
    product_without_zero = 1
    for index, item in enumerate(arr):
        if index == zero_index:
            continue

        if item == 0:
            product_without_zero = 0
            break

        product_without_zero *= item

    return [0] * zero_index + [product_without_zero] + [0] * (len(arr) - zero_index - 1)


def first_duplicate_value(arr):
    for index, item in enumerate(arr):
        item = abs(item)
        if arr[item - 1] < 0:
            return item

        arr[item - 1] = -arr[item - 1]

    return -1


def merge_overlapping_intervals(intervals):
    intervals.sort(key=lambda item: item[0])
    merged_intervals = [intervals[0]]

    for index in range(1, len(intervals)):
        prev_interval = merged_intervals[-1]
        current_interval = intervals[index]

        if prev_interval[1] < current_interval[0]:
            merged_intervals.append(current_interval)
        else:
            merged_interval = [prev_interval[0], max(current_interval[1], prev_interval[1])]
            merged_intervals[-1] = merged_interval

    return merged_intervals


def max_subset_sum_no_adjacent(arr):
    if not arr:
        return
    if len(arr) == 1:
        return arr[0]
    prev_prev_max_sum = arr[0]
    prev_max_sum = max(arr[0], arr[1])

    for index in range(2, len(arr)):
        current_max_sum = max(prev_max_sum, prev_prev_max_sum + arr[index])
        prev_prev_max_sum = prev_max_sum
        prev_max_sum = current_max_sum

    return prev_max_sum


def number_of_ways_to_make_change(target, arr):
    """
    :param target: +ve
    :param arr: [SORTED]
    :return:
    """
    if target == 0:
        return 1

    if not arr:
        return 0

    no_of_ways = 0
    current_target = target

    while current_target >= 0:
        no_of_ways += number_of_ways_to_make_change(current_target, arr[:-1])
        current_target -= arr[-1]

    return no_of_ways


def number_of_ways_to_make_change2(target, arr):
    """
    :param target: +ve
    :param arr: [SORTED]
    :return:
    """
    if target == 0:
        return 1

    no_of_ways = 0
    for index in reversed(range(0, len(arr))):
        temp = target - arr[index]

        while temp >= 0:
            no_of_ways += number_of_ways_to_make_change2(temp, arr[:index])
            temp -= arr[index]

    return no_of_ways


def single_cycle_check(arr):
    assert len(arr)

    seen = []
    current_index = 0

    while current_index not in seen:
        seen.append(current_index)

        current_index = (current_index + arr[current_index]) % len(arr)

    return len(seen) == len(arr) and current_index == seen[0]


def permutations(arr):
    temp = [[arr[0]]]
    for index in range(1, len(arr)):
        temp2 = []
        for combo in temp:
            for i in range(len(combo) + 1):
                combo_copy = list(combo)
                combo_copy.insert(i, arr[index])
                temp2.append(combo_copy)

        temp = temp2
    return len(temp), temp


def powerset(arr):
    temp = [[], [arr[0]]]

    for index in range(1, len(arr)):
        temp2 = []
        for item in temp:
            temp2.append(item + [arr[index]])

        temp.extend(temp2)

    return len(temp), temp


def staircase_traversal(height, max_steps):  # Gives Time Limit Exceeded on LeetCode
    ways = [[num] for num in range(1, min(max_steps, height) + 1)]
    while list(filter(lambda w: sum(w) < height, ways)):
        new_ways = [way for way in ways if sum(way) == height]
        for way in ways:
            for step in range(1, max_steps + 1):
                if sum(way) + step > height:
                    break
                new_ways.append(way + [step])

        ways = new_ways

    return len(ways), ways


def staircase_traversal_elegant(height, max_steps, cache):  # Verified on LeetCode
    if height in (1, 0):
        return 1
    elif height in cache:
        return cache[height]

    result = 0
    for step in filter(lambda s: height - s >= 0, range(1, max_steps + 1)):
        result += staircase_traversal_elegant(height - step, max_steps, cache)

    cache[height] = result
    return result


def balanced_brackets(string):
    closing = {")": "(", "]": "[", "}": "{"}

    temp = []
    for ch in string:
        if ch not in closing:
            temp.append(ch)
            continue

        if temp[-1] == closing[ch]:
            temp.pop()
        else:
            return False

    return len(temp) == 0


def sunset_views(building_heights, direction="EAST"):
    buildings_indices = range(len(building_heights))
    if direction == "EAST":
        buildings_indices = reversed(buildings_indices)

    result = []
    max_height_till_now = -math.inf

    for index in buildings_indices:
        height = building_heights[index]
        if height > max_height_till_now:
            result.append(index)
            max_height_till_now = height

    return result


def longest_palindromic_substring(string):  # Verified in LeetCode
    def calc_longest_palindromic_substring(beg, end):
        temp_substring = ""
        while beg >= 0 and end < len(string) and string[beg] == string[end]:
            temp_substring = string[beg: end + 1]
            beg -= 1
            end += 1

        return temp_substring

    if len(string) <= 1:
        return string

    longest_substring = string[0] if string[0] != string[1] else string[0: 2]

    for index in range(2, len(string)):
        if string[index] not in (string[index - 1], string[index - 2]):
            continue

        temp1 = calc_longest_palindromic_substring(index - 1, index)
        temp2 = calc_longest_palindromic_substring(index - 2, index)

        longest_substring = max(temp1, temp2, longest_substring, key=lambda x: len(x))

    return longest_substring


def valid_ip_addresses(string, no_of_dots=3):  # Verified in LeetCode
    def is_invalid_ip_component(ip_substring_component):
        return ip_substring_component.startswith("0") and len(ip_substring_component) >= 2

    if no_of_dots == 0:
        if 0 <= int(string) <= 255 and not is_invalid_ip_component(string):
            return [string]
        else:
            return []

    valid_addresses = []
    for index in range(1, len(string)):
        if int(string[:index]) > 255:
            break

        if is_invalid_ip_component(string[:index]):
            continue

        sub_addresses = valid_ip_addresses(string[index:], no_of_dots - 1)
        valid_addresses.extend([string[:index] + "." + sub_address for sub_address in sub_addresses])

    return valid_addresses


def largest_range(arr):  # Verified on LeetCode
    hash_set = {num: False for num in arr}

    result = []
    for key in hash_set:
        if hash_set[key]:
            continue

        temp1 = key
        while hash_set.get(temp1 - 1, None) is not None:
            hash_set[temp1 - 1] = True
            temp1 -= 1

        temp2 = key
        while hash_set.get(temp2 + 1, None) is not None:
            hash_set[temp2 + 1] = True
            temp2 += 1

        result.append([temp1, temp2])

    return max(result, key=lambda r: r[1] - r[0])


def zigzag_traversal(matrix):
    left = 1
    result = []
    for index_sum in range(len(matrix) + len(matrix[0]) - 1):
        if left == 1:
            row_index = max(0, index_sum - len(matrix[0]) + 1)
            col_index = min(index_sum, len(matrix[0]) - 1)
            # while row_index < len(matrix) and col_index >= 0:
            #     result.append(matrix[row_index][col_index])
            #     row_index += 1
            #     col_index -= 1
            #
            # left = False
        else:
            row_index = min(index_sum, len(matrix) - 1)
            col_index = max(0, index_sum - (len(matrix) - 1))

        while 0 <= col_index < len(matrix[0]) and len(matrix) > row_index >= 0:
            result.append(matrix[row_index][col_index])
            row_index += left
            col_index -= left

        left = left * -1

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(evaluate([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
    print("Is Palindrome: {}".format(is_palindrome('abcedecxxcedecba')))

    print("Caesar Cypher Encrypted: {}".format(caesar_cipher_encryptor("wxbz", 3)))

    print("Run-Length Encoding: {}".format(run_length_encoding("AAAAAAAAAAAAAAAAAAAAAAAABBCCCCDD")))

    print("First Non Repeating Character: {}".format(first_non_repeating_character("abcdcaf")))

    print("Is Monotonic Array: {}".format(is_monotonic_array([3, 1, -10, -1100, -1100, -1101, -1102, -9001])))

    print("Array of Products: {}".format(array_of_products([5, 0, 0, 2])))

    print("first Duplicate Value {}".format(first_duplicate_value([2, 1, 1, 2, 3, 3, 4])))

    print("Merged Intervals: {}".format(merge_overlapping_intervals([[1, 3], [2, 5], [5, 6], [7, 10], [8, 9]])))

    print("Max Subset Sum No Adjacent: {}".format(max_subset_sum_no_adjacent([7, 10, 12, 7, 9, 14])))

    print("Number of Ways to make change: {}".format(number_of_ways_to_make_change(10, [1, 5, 10, 25])))

    print("Single Cycle Check: {}".format(single_cycle_check([2, 3, 1, -4, -4, 2])))
    print("Single Cycle Check: {}".format(single_cycle_check([1, -1, 1, -1])))
    print("Powerset: {}".format(powerset([1, 2, 3, 4])))
    print("Staircase Traversal: {}".format(staircase_traversal(1, 2)))
    print("Staircase Traversal Elegant: {}".format(staircase_traversal_elegant(1, 2, dict())))

    print("Balanced Brackets: {}".format(balanced_brackets("(([]()()){})")))
    print("Sunset Views: {}".format(sunset_views([3, 5, 4, 4, 3, 1, 3, 2], "EAST")))

    print("Longest Palindromic Substring: {}".format(longest_palindromic_substring("abababcc")))
    print("Possible Valid IP Addresses: {}".format(valid_ip_addresses("0000", 3)))

    print("Largest Range: {}".format(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])))

    input_matrix = [[1, 3, 4, 10, 11],
                    [2, 5, 9, 12, 19],
                    [6, 8, 13, 18, 20],
                    [7, 14, 17, 21, 24],
                    [15, 16, 22, 23, 25]]
    print("Zigzag Traversal: {}".format(zigzag_traversal(input_matrix)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
