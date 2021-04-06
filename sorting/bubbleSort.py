"""
Bubble Sort
Write a function that takes in an array of integers and returns a
sorted version of that array. Use the Bubble Sort algorithm to sort
the array.
If you're unfamiliar with Bubble Sort, we recommend watching the
Conceptual Overview section of this question's video explanation
before starting to code.


Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output
[2, 3, 5, 5, 6, 8, 9]


"""

#O(n^2) time, O(1) space
def bubbleSort(array):
	isSorted = False
	#if we didn't do any swap, then the array is sorted, quit while loop
	while isSorted == False:
		#suppose it is sorted, then compare each pair
		#if we did swap, then it means not sorted yet, so set isSorted to Flase
		isSorted = True
		for i in range(len(array) - 1):
			if array[i] > array [i + 1]:
				array[i],array[i+1] = array[i+1],array[i]
				isSorted = False
	return array
