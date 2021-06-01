"""
Disk Stacking

You're given a non-empty array of arrays
where each subarray holds three integers and
represents a disk. These integers denote each
disk's width, depth, and height, respectively.
Your goal is to stack up the disks and to
maximize the total height of the stack. A disk
must have a strictly smaller width, depth, and
height than any other disk below it.
Write a function that returns an array of the
disks in the nal stack, starting with the top
disk and ending with the bottom disk. Note
that you can't rotate disks; in other words, the
integers in each subarray must represent
[width, depth, height] at all times.
You can assume that there will only be one
stack with the greatest total height.


Sample Input
disks = [
  [2, 1, 2],
  [3, 2, 3],
  [2, 2, 8],
  [2, 3, 4],
  [1, 3, 1],
  [4, 4, 5]
]


Sample Output
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]

// 10 (2 + 3 + 5) is the tallest height

"""
# O(n ** 2) time, O(n) space
# 第二重循环一次次记录堆叠的最大高度，同时也要记录上一个序号，沿着序号一路可以推导回去
def diskStacking(disks):
	disks.sort(key=lambda disk:disk[2])
	heights = [disk[2] for disk in disks]
	sequence = [None for _ in range(len(disks))]
	maxHeightIndex = 0
	for i in range(1,len(disks)):
		currentDisk = disks[i]
		for j in range(0,i):
			otherDisk = disks[j]
			if isValidDimentions(otherDisk,currentDisk):
				if heights[i] <= heights[j] + currentDisk[2]:
					heights[i] = heights[j] + currentDisk[2]
					sequence[i] = j
		if heights[i] >= heights[maxHeightIndex]:
			maxHeightIndex = i
	return buildSequence(disks,sequence,maxHeightIndex)
    

def isValidDimentions(o,c):
	return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSequence(array,sequence,currentIndex):
	result = []
	while currentIndex is not None:
		result.append(array[currentIndex])
		currentIndex = sequence[currentIndex]
	return list(reversed(result))
		
	