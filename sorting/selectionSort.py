"""
Selection Sort
Write a function that takes in an array of integers and returns a
sorted version of that array. Use the Selection Sort algorithm to
sort the array.
If you're unfamiliar with Selection Sort, we recommend watching
the Conceptual Overview section of this question's video
explanation before starting to code.


Sample Input
array = [8, 5, 2, 9, 5, 6, 3]


Sample Output
[2, 3, 5, 5, 6, 8, 9]


"""






array = [8, 5, 2, 9, 5, 6, 3]


#O(n^2) time, O(1) space
def selectionSort(array):
	for currentIdx in range(len(array)-1):
		smallestIdx = currentIdx
		for j in range(currentIdx + 1,len(array)):
			if array[j] < array[smallestIdx]:
				smallestIdx = j
		array[smallestIdx],array[currentIdx] = array[currentIdx],array[smallestIdx]
	return array

print("input:",array)
print("output:",selectionSort(array))


			