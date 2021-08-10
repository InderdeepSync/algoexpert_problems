
def main(arr, summ):
	seen = set()

	for item in arr:
		if summ - item in seen:
			return True
		seen.add(item)
	else:
		return False




if __name__ == "__main__":
	print (main([1,4,7,2,0], -2))