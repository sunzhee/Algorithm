"""
Ambiguous Measurements
This problem deals with measuring cups that
are missing important measuring labels.
Specically, a measuring cup only has two
measuring lines, a Low (L) line and a High (H)
line. This means that these cups can't
precisely measure and can only guarantee
that the substance poured into them will be
between the L and H line. For example, you
might have a measuring cup that has a Low
line at 400ml and a high line at 435ml .
This means that when you use this
measuring cup, you can only be sure that
what you're measuring is between 400ml
and 435ml .
You're given a list of measuring cups
containing their low and high lines as well as
one low integer and one high integer
representing a range for a target
measurement. Write a function that returns
a boolean representing whether you can use
the cups to accurately measure a volume in
the specied [low, high] range (the range is inclusive).

Note that:
Each measuring cup will be
represented by a pair of positive
integers [L, H] , where
0 <= L <= H .
You'll always be given at least one
measuring cup, and the low and
high input parameters will always
satisfy the following constraint:
0 <= low <= high .
Once you've measured some liquid, it
will immediately be transferred to a
larger bowl that will eventually
(possibly) contain the target
measurement.
You can't pour the contents of one
measuring cup into another cup.


Sample Input
measuringCups = [
 [200, 210],
 [450, 465],
 [800, 850],
]
low = 2100
high = 2300

用杯子测量出来的结果只要能落在low和high之间，即为True，否则为False

Sample Output
true
// We use cup [450, 465] to measure four volumes:
// First measurement: Low = 450, High = 465
// Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
// Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
// Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860
// Then we use cup [200, 210] to measure two volumes:
// Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
// Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280
// We've measured a volume in the range [2200, 2280].
// This is within our target range, so we return `true`.
// Note: there are other ways to measure a volume in the target range.

"""
def ambiguousMeasurements(measuringCups, low, high):
	memoization = {}
	return canMeasureInRange(measuringCups,low,high,memoization)


def canMeasureInRange(measuringCups,low,high,memoization):
	# 创建一个目标low high的组合
	# 先检查字典里是否已经计算过这个组合，如果计算过则直接返回结果True or False
	memoLowHighPairs = getLowHighPair(low,high)
	if memoLowHighPairs in memoization:
		return memoization[memoLowHighPairs]
	
	# base case之一，如果超过底线，说明无法测量，返回False
	if low <= 0 and high <= 0:
		return False
	
	# 设置一个变量，用来记录每一次计算的返回值，存放于字典中
	canMeasure = False
	for cup in measuringCups:
		cupLow,cupHigh = cup
		# 能测量，break跳出循环，返回True
		if low <= cupLow and cupHigh <= high:
			canMeasure = True
			break
			
		# 核心递归，用low high减去cup的值带入到新的case里面，继续递归
		# 每一层递归调用for循环三次，使用三个杯子
		canMeasure = canMeasureInRange(measuringCups,low - cupLow,high - cupHigh,memoization)
		if canMeasure:
			break
			
	# 记录low high组合的结果，一般来说这里应该都是False，因为一旦有了True就可以不用计算，直接返回了
	memoization[memoLowHighPairs] = canMeasure
	return canMeasure

	
def getLowHighPair(low,high):
	return str(low) + "-" + str(high)