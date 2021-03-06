"""
Move Element To End
You're given an array of integers and an integer. Write a function
that moves all instances of that integer in the array to the end of
the array and returns the array.
The function should perform this in place (i.e., it should mutate
the input array) and doesn't need to maintain the order of the
other integers.

Sample Input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output
[1, 3, 4, 2, 2, 2, 2, 2]


"""


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2



#O(n) time, O(1) space, n is the array length
def moveElementToEnd(array, toMove):
	i = 0
	j = len(array) - 1
	while i < j:
		# 这里是edge情况，右边全都是toMove数字，需要循环移动右边指针，直到没有toMove为止。
		while i < j and array[j] == toMove:
			j = j - 1
		if array[i] == toMove:
			array[i],array[j] = array[j],array[i]
		i = i + 1
		
	return array

print("input array:",array,"\ntoMove:",toMove)
print(moveElementToEnd(array,toMove))
