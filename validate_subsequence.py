
def main(arr, subsequence): # Verified on Leetcode
	try:
		sub_iter = iter(subsequence)
		sub_elem = next(sub_iter)

		for item in arr:
			if item == sub_elem:
				sub_elem = next(sub_iter)
	except StopIteration:
		return True
	else:
		return False
	





if __name__ == "__main__":
	is_valid_subsequence = main([1,2,3,4,5], [1, 3,4,7])
	print("Is Valid Subsequence: {}".format(is_valid_subsequence))