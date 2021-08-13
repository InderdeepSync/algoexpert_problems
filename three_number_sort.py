
def three_number_sort(arr, three_numbers):
    num1_end = -1

    for index in range(len(arr)):
        if arr[index] == three_numbers[0]:
            del arr[index]
            arr.insert(0, three_numbers[0])
            num1_end += 1
        elif arr[index] == three_numbers[1]:
            del arr[index]
            arr.insert(num1_end + 1, three_numbers[1])
        else:
            pass





if __name__ == "__main__":
    input_arr = [1, 0, 0, -1, -1, 0, 1, 1]
    three_number_sort(input_arr, [0, 1, -1])

    print("After Sorting: {}".format(input_arr))