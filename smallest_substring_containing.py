
def smallest_substring_containing(string, target):  # Verified on Leetcode
    def _have_achieved_all_characters():
        for char in target_chars_map:
            if char not in current_status or current_status[char] < target_chars_map[char]:
                return False
        return True

    target_chars_map = {}
    for ch in target:
        target_chars_map[ch] = target_chars_map.get(ch, 0) + 1

    left = right = 0
    minimum_substring = None

    current_status = {}
    all_characters_achieved = False
    while True:
        if all_characters_achieved:
            left_character = string[left]
            if left_character in current_status:
                potential_minimum_substring = (left, right)
                if minimum_substring:
                    minimum_substring = min(minimum_substring, potential_minimum_substring, key=lambda x: x[1] - x[0])
                else:
                    minimum_substring = potential_minimum_substring

                current_status[left_character] -= 1
                if current_status[left_character] < target_chars_map[left_character]:
                    all_characters_achieved = False

            left += 1
        else:
            if right == len(string):
                break
            right_character = string[right]
            if right_character in target_chars_map:
                current_status[right_character] = current_status.get(right_character, 0) + 1
                all_characters_achieved = _have_achieved_all_characters()

            right += 1

    return string[minimum_substring[0]: minimum_substring[1]] if minimum_substring else ""


if __name__ == "__main__":
    print("Smallest Substring Containing: {}".format(smallest_substring_containing("ADOBECODEBANC", "ABC")))