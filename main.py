#!/usr/bin/env python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import re

from suffix_tree import SuffixTree


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


def ambiguous_measurements(measuring_cups, low, high):
    # measuring_cups.sort(key=lambda cup: (cup[0], cup[1]))

    if len(measuring_cups) == 0:
        return 0

    no_of_ways = 0
    current_high = high
    current_low = low
    while current_low >= 0 and current_high >= 0:
        no_of_ways += ambiguous_measurements(measuring_cups[: -1], current_low, current_high)
        current_low -= measuring_cups[-1][0]
        current_high -= measuring_cups[-1][1]

    if current_low <= 0 <= current_high:
        no_of_ways += 1

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


def max_sum_increasing_subsequence(arr):
    max_sums_including_current = arr.copy()
    sequences = [None] * len(arr)
    for index1 in range(1, len(arr)):
        for index2 in range(0, index1):
            if arr[index2] >= arr[index1]:
                continue

            prospective_sum = max_sums_including_current[index2] + arr[index1]
            if max_sums_including_current[index1] < prospective_sum:
                max_sums_including_current[index1] = prospective_sum
                sequences[index1] = index2

    temp_index = max_sums_including_current.index(max(max_sums_including_current))
    result = []
    while temp_index is not None:
        result.append(arr[temp_index])
        temp_index = sequences[temp_index]

    return result


def lcs(input1, input2):
    cache = dict()

    def _calculate_lcs_and_save_in_cache(str1, str2):
        str_pair = (str1, str2)
        if str_pair not in cache:
            cache[str_pair] = longest_common_subsequence(str1, str2)
        return cache[str_pair]

    def longest_common_subsequence(string1, string2):
        if len(string1) == 0 or len(string2) == 0:
            return ""

        if string1[0] == string2[0]:
            return string1[0] + _calculate_lcs_and_save_in_cache(string1[1:], string2[1:])

        return max(_calculate_lcs_and_save_in_cache(string1[1:], string2),
                   _calculate_lcs_and_save_in_cache(string2[1:], string1),
                   key=len)

    return longest_common_subsequence(input1, input2)


def min_number_of_jumps(arr):
    if len(arr) == 1:
        return 0

    min_jumps = math.inf
    for jump_size in range(1, arr[0] + 1):
        if jump_size >= len(arr):
            break
        min_jumps = min(min_jumps, min_number_of_jumps(arr[jump_size:]))

    return min_jumps + 1


def min_number_of_jumps_with_caching(arr, start, cache):
    if len(arr) - 1 == start:
        return 0
    min_jumps = float("inf")

    for jump_size in range(1, arr[start] + 1):
        effective_start = start + jump_size
        if effective_start >= len(arr):
            break
        if effective_start not in cache:
            cache[effective_start] = min_number_of_jumps_with_caching(arr, effective_start, cache)

        min_jumps = min(min_jumps, cache[effective_start])

    return min_jumps + 1


def water_area(arr):
    max_right = [0]

    for index3 in reversed(range(0, len(arr) - 1)):
        max_right.insert(0, max(max_right[0], arr[index3 + 1]))

    max_left = [0]
    for index2 in range(1, len(arr)):
        max_left.append(max(max_left[-1], arr[index2 - 1]))

    area = 0
    for index, item in enumerate(arr):
        water_possible = max(0, min(max_left[index], max_right[index]) - item)
        area += water_possible

    return area


def knapsack(items, max_bag_capacity):
    if max_bag_capacity == 0 or len(items) == 0:
        return 0

    if items[-1][1] > max_bag_capacity:
        temp = float("-inf")
    else:
        temp = items[-1][0] + knapsack(items[: -1], max_bag_capacity - items[-1][1])

    return max(knapsack(items[: -1], max_bag_capacity), temp)


def knapsack_with_dynamic_programming(items, max_bag_capacity):
    def _get_items_producing_value_at(row_index, col_index):
        result = []

        while row_index and col_index:
            if values[row_index][col_index] == values[row_index - 1][col_index]:
                pass
            else:
                result.append(items[row_index - 1])
                col_index -= items[row_index - 1][1]
            row_index -= 1
        return result

    values = [[0 for _ in range(max_bag_capacity + 1)] for _ in range(len(items) + 1)]

    for index1 in range(1, len(values)):
        for index2 in range(1, len(values[0])):
            current_item_weight = items[index1 - 1][1]
            if current_item_weight > index2:
                temp = float("-inf")
            else:
                temp = current_item_weight + values[index1 - 1][index2 - current_item_weight]

            values[index1][index2] = max(values[index1 - 1][index2], temp)

    return _get_items_producing_value_at(len(values) - 1, len(values[0]) - 1)


def disk_stacking(disks):
    def _get_sequence(height):
        result = []
        while height:
            disk = disks[heights.index(height)]
            result.append(disk)
            height = height - disk[2]

        return result

    disks.sort(key=lambda disk: disk[2])

    heights = list(map(lambda disk: disk[2], disks))
    for index1 in range(len(disks)):
        current_disk = disks[index1]
        for index2 in range(index1):
            other_disk = disks[index2]
            if current_disk[0] >= other_disk[0] and current_disk[1] >= other_disk[1] and current_disk[2] >= other_disk[
                2]:
                heights[index1] = max(heights[index1], current_disk[2] + heights[index2])

    return _get_sequence(max(heights))


def numbers_in_pi(string, start, nums):
    if string[start:] in nums:
        return 0

    min_number_of_spaces = math.inf
    for index in range(start + 1, len(string)):
        if string[start: index] not in nums:
            continue

        min_number_of_spaces = min(min_number_of_spaces, 1 + numbers_in_pi(string, index, nums))

    return min_number_of_spaces


def max_sum_subarray(matrix, size):
    def _create_sums_arr():
        sums = matrix.copy()

        for index1 in range(len(matrix)):
            for index2 in range(len(matrix[0])):
                upper_matrix_sum = sums[index1 - 1][index2] if index1 != 0 else 0
                left_matrix_sum = sums[index1][index2 - 1] if index2 != 0 else 0
                upper_left_matrix_sum = sums[index1 - 1][index2 - 1] if index1 != 0 and index2 != 0 else 0
                sums[index1][index2] = matrix[index1][
                                           index2] + upper_matrix_sum + left_matrix_sum - upper_left_matrix_sum

        return sums

    assert size <= len(matrix) and size <= len(matrix[0])
    sums_array = _create_sums_arr()

    max_sum_submatrix = float("-inf")
    for i in range(size - 1, len(matrix)):
        for j in range(size - 1, len(matrix[0])):
            temp1 = sums_array[i - size][j] if i - size >= 0 else 0
            temp2 = sums_array[i][j - size] if j - size >= 0 else 0
            temp3 = sums_array[i - size][j - size] if i - size >= 0 and j - size >= 0 else 0
            submatrix_sum = sums_array[i][j] - temp1 - temp2 + temp3

            max_sum_submatrix = max(max_sum_submatrix, submatrix_sum)

    return max_sum_submatrix


def is_interleave(s1, s2, target_string):
    possible_strings = map(lambda p: p["value"], _interleave(s1, s2))
    return target_string in possible_strings


def _interleave(s1, s2):
    if not s1:
        return [{"value": s2, "index": len(s2)}]

    possibilities = []
    temp = _interleave(s1[1:], s2)

    for possibility in temp:
        for index in range(len(possibility["value"]) + 1):
            if index > possibility["index"]:
                break
            temp2 = possibility["value"][:index] + s1[0] + possibility["value"][index:]
            possibilities.append({"value": temp2, "index": index})

    return possibilities


def generate_parenthesis(num):
    result = []

    def _generate(prefix, opening_remaining, closing_remaining):
        if not closing_remaining and not opening_remaining:
            result.append(prefix)
            return

        if opening_remaining > 0:
            _generate(prefix + "{", opening_remaining - 1, closing_remaining)
        if closing_remaining > opening_remaining:
            _generate(prefix + "}", opening_remaining, closing_remaining - 1)

    _generate("", num, num)
    return result


def largest_rectangle_under_skyline(buildings):
    largest_rectangle_area = 0
    areas_accumulated = {}

    for index, building in enumerate(buildings):
        for height in list(areas_accumulated.keys()):
            if height > building:
                del areas_accumulated[height]
                continue
            areas_accumulated[height] += height
            largest_rectangle_area = max(largest_rectangle_area, areas_accumulated[height])

        temp2 = buildings[index - 1] if index != 0 else 0
        for b in range(building, temp2, -1):
            areas_accumulated[b] = b
            largest_rectangle_area = max(largest_rectangle_area, b)

    return largest_rectangle_area


def longest_substring_without_duplication(input_string):
    _, (start, end) = _longest_substring_without_duplication(input_string, 0, len(input_string))
    return input_string[start: end]


def _longest_substring_without_duplication(string, start, end):
    if start == end - 1:
        return (start, end), (start, end)

    longest_left, longest_overall = _longest_substring_without_duplication(string, start + 1, end)

    temp = string.find(string[start], longest_left[0], longest_left[1])
    if temp == -1:
        longest_left = start, longest_left[1]
    else:
        longest_left = start, temp

    return longest_left, max(longest_left, longest_overall, key=lambda a: a[1] - a[0])


def longest_substring_without_duplication_iterative(input_string):  # TODO To be implemented
    pass


def underscorify_substring(input_string, substring):
    # TODO Similar Idea to merging overlapping Intervals
    pass


def multi_string_search(input_string, words):
    tree = SuffixTree(char="/", children=[])
    for word in words:
        tree.add_suffix_to_tree(word)

    words_found = set()
    for index, ch in enumerate(input_string):
        temp = index
        sub_tree = tree
        while temp < len(input_string):
            sub_tree = sub_tree.get_child_with_char(input_string[temp])
            if not sub_tree:
                break

            if SuffixTree.has_char_in_children(sub_tree, "*"):
                words_found.add(input_string[index: temp + 1])

            temp += 1

    return words_found


def max_profit_with_k_transactions(profits, start, k):
    if k == 0 or start == len(profits) - 1:
        return 0

    for i in range(start + 1, len(profits)):
        if profits[i - 1] < profits[i]:
            break
    else:
        return 0

    result = max_profit_with_k_transactions(profits, start + 1, k)

    for i in range(start + 1, len(profits)):
        temp_profit = profits[i] - profits[start]
        if temp_profit > 0:
            max_profit = temp_profit + max_profit_with_k_transactions(profits, i + 1, k - 1)
        else:
            max_profit = max_profit_with_k_transactions(profits, i + 1, k)

        result = max(result, max_profit)

    return result

def apartment_hunting(apartments, buildings_to_consider):
    # Exact Same Idea as Min Rewards Problem
    data = {}
    for building in buildings_to_consider:
        data[building] = [float("inf")] * len(apartments)
        temp = 0
        while temp != len(apartments):
            if building in apartments[temp]:
                data[building][temp] = 0
            else:
                data[building][temp] = data[building][temp - 1] + 1

            temp += 1

        temp = len(apartments) - 2
        while temp >= 0:
            data[building][temp] = min(data[building][temp], data[building][temp + 1] + 1)
            temp -= 1

    return data

def right_smaller_than(arr):
    mapped_arr = [{"value": item, "index": index} for index, item in enumerate(arr)]

    result = [0] * len(arr)
    update_not_required = set()
    for index, item in enumerate(sorted(mapped_arr, key=lambda a: a["value"])):
        update_not_required.add(item["index"])
        for i in range(0, item["index"]):
            if i in update_not_required:
                continue

            result[i] += 1

    return result


def palindrome_partitioning_min_cuts(string):
    cache = {}

    def __cachify_palindrome_partitioning(start):
        if start not in cache:
            cache[start] = _palindrome_partitioning_min_cuts(start)

        return cache[start]

    def _palindrome_partitioning_min_cuts(start):
        if is_palindrome(string[start:]):
            return 0
        min_cuts = len(string) - start - 1

        for i in range(start + 1, len(string)):
            if not is_palindrome(string[start:i]):
                continue
            min_cuts = min(min_cuts, 1 + __cachify_palindrome_partitioning(i))

        return min_cuts

    return _palindrome_partitioning_min_cuts(0)


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

    print("Max Sum Increasing Subsequence: {}".format(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7])))
    print("Longest Common Subsequence: {}".format(lcs("zxvvyzw", "xkykzpw")))

    print("Minimum Number of Jumps: {}".format(min_number_of_jumps([2, 0, 0])))
    print("Minimum Number of Jumps(With Caching): {}".format(
        min_number_of_jumps_with_caching([3, 2, 1, 0, 1], 0, dict())))

    print("Water Area: {}".format(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])))
    print("Knapsack Problem With Dynamic Programming: {}".format(
        knapsack_with_dynamic_programming([[1, 2], [4, 3], [5, 6], [6, 7]], 10)))
    print("Disk Stacking: {}".format(disk_stacking([[2, 2, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]])))
    print("Numbers in PI: {}".format(numbers_in_pi("3141592", 0, ["3141", "5", "31", "2", "4159", "9", "42"])))
    print("Maximum Sum SubArray: {}".format(max_sum_subarray(input_matrix, 3)))
    print("Is Interleaved String: {}".format(is_interleave("dbbca", "aabcc", "aadbbcbcac")))
    print("Generate Valid Parenthesis Combinations: {}".format(generate_parenthesis(3)))
    print("Ambiguous Measurements: {}".format(ambiguous_measurements([[200, 210], [450, 465], [800, 850]], 2100, 2300)))

    print("Largest Rectangle Under Skyline: {}".format(largest_rectangle_under_skyline([2, 1, 5, 6, 2, 3])))
    print("Longest Substring Without Duplication: {}".format(longest_substring_without_duplication("clementisacap")))

    underscorify_string = "testthis is a testtest to see if testestest works"
    print("Underscorify SubString: {}".format(underscorify_substring(underscorify_string, "test")))

    print("Multi-String Search: {}".format(
        multi_string_search("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"])))
    print("Max Profit with K Transactions: {}".format(
        max_profit_with_k_transactions([5, 11, 3, 50, 60, 90], k=2, start=0)))
    print("Palindrome Partitioning Min Cuts: {}".format(palindrome_partitioning_min_cuts("noonabbad")))
    print("Apartment Hunting: {}".format(
        apartment_hunting([["SC"], ["G"], ["G", "SC"], ["SC"], ["SC", "ST"]], ["G", "SC", "ST"])))
    print("Right Smaller Than: {}".format(right_smaller_than([8, 5, 11, -1, 3, 4, 2])))
