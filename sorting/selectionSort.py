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
	currentId = 0
	for currentId in range(0,len(array) - 1):
		smallestId = currentId
		for i in range(currentId + 1,len(array)):
			if array[smallestId] > array[i]:
				smallestId = i
		#swap
		array[smallestId],array[currentId] = array[currentId],array[smallestId]
		currentId += 1
	return array

print("input:",array)
print("output:",selectionSort(array))


			