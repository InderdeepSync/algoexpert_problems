#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from functools import reduce
from typing import List


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
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
