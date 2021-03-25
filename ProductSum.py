"""

Product Sum

Write a function that takes in a "special" array and returns its
product sum.
A "special" array is a non-empty array that contains either
integers or other "special" arrays. The product sum of a "special"
array is the sum of its elements, where "special" arrays inside it
are summed themselves and then multiplied by their level of
depth.
The depth of a "special" array is how far nested it is. For instance,
the depth of [] is 1 ; the depth of the inner array in [[]] is
2 ; the depth of the innermost array in [[[]]] is 3 .
Therefore, the product sum of [x, y] is x + y ; the product
sum of [x, [y, z]] is x + 2 * (y + z) ; the product sum
of [x, [y, [z]]] is x + 2 * (y + 3z) .


Sample Input
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample Output
12

"""


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

#O(n) Time, n is all the elementin array, including all sub array's and sub elements
#O(d) space, d is the depth of the greatest depth of the sub element
def productSum(array,multiplier = 1):
	#for the array, top multiplier is 1
	#we can NOT set multiplier = 1 in the function,heve to be before it.
	#otherwise the multiplier will always be 1,the recursive will get logical error
	sum = 0
	for element in array:
		if type(element) is list:
			#don't forget sum + the sub element result
			sum = sum + productSum(element,multiplier + 1)
		else:
			sum = sum + element
	return sum * multiplier

print("input array:",array)
print("output:",productSum(array,multiplier=1))

