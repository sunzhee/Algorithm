"""
Waterfall Streams

You're given a two-dimensional array that represents the
structure of an indoor waterfall and a positive integer that
represents the column that the waterfall's water source
will start at. More specifically, the water source will start
directly above the structure and will flow downwards.
Each row in the array contains 0 s and 1 s, where a 0
represents a free space and a 1 represents a block that
water can't pass through. You can imagine that the last
row of the array contains buckets that the water will
eventually flow into; thus, the last row of the array will
always contain only 0 s. You can also imagine that there
are walls on both sides of the structure, meaning that
water will never leave the structure; it will either be
trapped against a wall or flow into one of the buckets in
the last row.
As water flows downwards, if it hits a block, it splits evenly
to the left and right-hand side of that block. In other
words, 50% of the water flows left and 50% of it flows
right. If a water stream is unable to flow to the left or to
the right (because of a block or a wall), the water stream
in question becomes trapped and can no longer continue
to flow in that direction; it effectively gets stuck in the
structure and can no longer flow downwards, meaning
that 50% of the previous water stream is forever lost.
Lastly, the input array will always contain at least two
rows and one column, and the space directly below the
water source (in the first row of the array) will always be
empty, allowing the water to start flowing downwards.
Write a function that returns the percentage of water
inside each of the bottom buckets after the water has
flowed through the entire structure.
You can refer to the first 4.5 minutes of this question's
video explanation for a visual example.

Sample Inputs:

array = [
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0]
]
source = 3

Sample Output
[0, 0, 0, 25, 25, 0, 0]

"""

# O(w ** 2 * h) time, O(w) space, w is width, h is height of array
def waterfallStreams(array, source):
	rowAbove = array[0][:] # 把最顶上row[0]全部copy下来
	rowAbove[source] = -1 # use -1 represent water
	
	for row in range(1,len(array)):
		currentRow = array[row][:] # 把currentRow copy下来
		
		for idx in range(len(rowAbove)):
			valueAbove = rowAbove[idx]
			
			hasWaterAbove = valueAbove < 0
			currentIsBlock = currentRow[idx] == 1
			
			if not hasWaterAbove: # 如果上面没有水，continue 下一个
				continue
			if not currentIsBlock: # 能走到这一步说明上面有水，而且当前不是block，所以让水流下去
				currentRow[idx] += valueAbove # 要用当前值加上上面的值，因为有可能两股水流合并在一起，加两次
				continue
			
			splitWater = valueAbove / 2 # 走到这里说明上面有水，当前是一个block，于是分水
			
			rightIdx = idx # 水往右走的情况
			while rightIdx + 1 <len(rowAbove):
				rightIdx += 1
				if rowAbove[rightIdx] == 1:
					break #说明旁边上面这个有block，水走不了，停止
				if currentRow[rightIdx] != 1:
					currentRow[rightIdx] += splitWater #说明current这里没有阻碍，分水值加上当前值，因为有可能其他水流合并在一起
					break #用break是因current这里已经是空的，没有block，水会流下去，所以不需要继续循环了
				# 以上两种情况都不是的话，说明当前还是一个block，继续执行rightIdx += 1，水往右走直到找到空地流下去
				
			leftIdx = idx # water goes to left 道理同上
			while leftIdx - 1 >= 0:
				leftIdx -= 1
				if rowAbove[leftIdx] == 1:
					break
				if currentRow[leftIdx] != 1:
					currentRow[leftIdx] += splitWater
					break
		rowAbove = currentRow
		
	finialPercentages = list(map(lambda x: x * -100, rowAbove))
	
	return finialPercentages
				
				
				



