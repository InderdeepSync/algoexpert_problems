
def main(arr):
	left = 0
	right = len(arr) - 1

	result = []
	while(left <= right):
		# import pdb; pdb.set_trace()
		if arr[left] > arr[right]:
			result.insert(0, arr[left])
			left += 1
		else:
			result.insert(0, arr[right])
			right -= 1

	print(result)






if __name__ == "__main__":
	main([16, 9, 0, 49, 81])