"""
Array Of Products

Write a function that takes in a non-empty array of integers and
returns an array of the same length, where each element in the
output array is equal to the product of every other number in the
input array.
In other words, the value at output[i] is equal to the product
of every number in the input array other than input[i] .
Note that you're expected to solve this problem without using
division.


Sample Input
array = [5, 1, 4, 2]

Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4



"""



def arrayOfProducts1(array):
"""
Brutal way, just multiple every element, except i
O(n^2)time and O(n)space
"""
	result =[]
	for i in range(len(array)):
		product_i = 1
		for j in range(len(array)):
			if i != j:
				product_i = product_i * array[j]
		result.append(product_i)
	return result



def arrayOfProducts(array):
	"""
	treverse 3 times of array,
	1st time calculate all the left product of elements, store in leftProduct
	2nd time calculate all the right product of elements, put in rightProduct
	3rd time multiply 1st and 2nd array, then we got the result
	O(n) time,actually O(n+n+n) = O(3n) = O(n)
	O(n) space, O(n+n+n) = O(n)
	"""
	leftProduct =[1 for _ in range(len(array))]
	rightProduct = [1 for _ in range(len(array))]
	result = [1 for _ in range(len(array))]
	
	runningProduct = 1
	for i in range(len(array)):
		leftProduct[i] = runningProduct
		runningProduct *= array[i]
		
	runningProduct = 1
	for j in reversed(range(len(array))):
		rightProduct[j] = runningProduct
		runningProduct *= array[j]
		
	for k in range(len(array)):
		result[k] = leftProduct[k] * rightProduct[k]
		
	return result