import math

def four_number_sum(arr, target):  # Converting 4Sum to 3Sum
    arr.sort()

    quadruples = []

    for index1 in range(len(arr)):
        for index2 in range(index1 + 1, len(arr)):
            if arr[index1] + arr[index2] > target:
                break
            current_sum = arr[index1] + arr[index2]
            required_sum = target - current_sum
            start = index2 + 1
            end = len(arr) - 1

            while start < end:
                temp_sum = arr[start] + arr[end]
                if temp_sum == required_sum:
                    quadruples.append((arr[index1], arr[index2], arr[start], arr[end]))
                    start += 1
                    end -= 1
                elif temp_sum < required_sum:
                    start += 1
                else:
                    end -= 1

    return quadruples

def four_number_sum_elegant(arr, target):
    cache = {}
    quadruples = []
    for index1 in range(len(arr)):
        for index2 in range(index1 + 1, len(arr)):
            current_sum = arr[index1] + arr[index2]
            required_sum = target - current_sum

            if required_sum in cache:
                quadruples.extend([(arr[index1], arr[index2], *pair) for pair in cache[required_sum]])

        for index3 in range(index1):
            temp_sum = arr[index3] + arr[index1]
            pair = (arr[index3], arr[index1])
            if temp_sum in cache:
                cache[temp_sum].append(pair)
            else:
                cache[temp_sum] = [pair]

    return quadruples


if __name__ == "__main__":
    result = four_number_sum_elegant([7, 6, 4, -1, 1, 2], 15)
    print("Four Number Sum: {}".format(result))