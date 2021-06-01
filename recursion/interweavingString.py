"""
Interweaving Strings

Write a function that takes in three strings
and returns a boolean representing whether
the third string can be formed by
interweaving the rst two strings.
To interweave strings means to merge them
by alternating their letters without any
specic pattern. For instance, the strings
"abc" and "123" can be interwoven as
"a1b2c3" , as "abc123" , and as
"ab1c23" (this list is nonexhaustive).
Letters within a string must maintain their
relative ordering in the interwoven string.


Sample Input
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

Sample Output
true


"""
# O(2^(n+m)) time, n is len(one),m is len(two), O(n+m) space
def interweavingStrings(one, two, three):
	if len(three) != len(one) + len(two):
		return False
	return interwavingHelper(one,two,three,0,0)

def interwavingHelper(one,two,three,idx1,idx2):
	idx3 = idx1 + idx2
	# base case, finished comparision
	# 走到最后，比较完毕返回
	if idx3 == len(three):
		return True
	# 如果idx1还没比较完，同时对应的字符相等，那么继续往下，否则忽略这个序列，不可能是这个组合
	if idx1 < len(one) and one[idx1] == three[idx3]:
		# 如果能走完返回都是true，那么返回true
		# 只要能走完一遍，都返回true就可以，有可能有多种方法inter weaving，但是后续我们不需要计算了
		if interwavingHelper(one,two,three,idx1 + 1,idx2) == True:
			return True
	
	if idx2 < len(two) and two[idx2] == three[idx3]:
		return interwavingHelper(one,two,three,idx1,idx2 + 1)
	
	# 如果上面两个比较没true结果，则返回false
	return False