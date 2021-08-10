
def main(arr, subsequence):
	if len(subsequence) == 0:
		return True

	subiter = iter(subsequence)
	subelem = next(subiter)

	try:
		for item in arr:
			if item == subelem:
				subelem = next(subiter)
	except StopIteration:
		# import pdb; pdb.set_trace()
		return True
	else:
		return False
	





if __name__ == "__main__":
	is_valid_subsequence = main([1,2,3,4,5], [1, 3,4,7])
	print("Is Valid Subsequence: {}".format(is_valid_subsequence))