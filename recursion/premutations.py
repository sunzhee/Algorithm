"""
Permutations

Write a function that takes in an array of
unique integers and returns an array of all
permutations of those integers in no
particular order.
If the input array is empty, the function
should return an empty array.
Sample Input
array = [1, 2, 3]


Sample Output
[
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]

"""
# O(n*n!) time, O(n*n!) space
def getPermutations(array):
	resultPermutations = []
	permutationHelper(0,array,resultPermutations)
	return resultPermutations

def permutationHelper(i,array,resultPermutations):
	# 如果走到array最后一个数字
	if i == len(array) - 1:
		resultPermutations.append(array[:])
	else:
		for j in range(i,len(array)):
			swap(array,i,j)
			permutationHelper(i+1,array,resultPermutations)
			swap(array,i,j)

def swap(array,i,j):
	array[i],array[j] = array[j],array[i]

###################

# upper Bound: O(n^2 * n!) time , O(n * n!) space
# average: O(n * n!) time, O(n * n!) space
def getPermutations(array):
	resultPermutations = []
	permutationHelper(array,[],resultPermutations)
	return resultPermutations

def permutationHelper(array,currentPermutation,resultPermutations):
	# 如果输入前面不动的部分序列为空，并且给的后半部分序列不为空
	if not len(array) and len(currentPermutation):
	#if len(array)==0 and len(currentPermutation) != 0:
		resultPermutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			# 新序列等于序列从index头到i，加上index的i+1到结尾
			newArray = array[:i] + array[i+1:]
			newPermutation = currentPermutation + [array[i]]
			permutationHelper(newArray,newPermutation,resultPermutations)



