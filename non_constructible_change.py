
def main(arr):
	change = 0

	for item in sorted(arr):
		if item > change + 1:
			return change + 1

		change += item
	else:
		return change + 1

if __name__ == '__main__':
	print(main([5, 7, 2, 3, 11]))
