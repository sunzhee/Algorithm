"""
Longest Palindromic Substring

Write a function that, given a string,
returns its longest palindromic
substring.
A palindrome is dened as a string
that's written the same forward and
backward. Note that single-character
strings are palindromes.
You can assume that there will only be
one longest palindromic substring.


Sample Input
string = "abaxyzzyxf"

Sample Output
"xyzzyx"



"""
# O(n^2) time , O(n) space
def longestPalindromicSubstring(string):
	# 保存的是最长palindrom的起始和结束index
	currentLongest = [0,1]
	# 从第2个开始比较，分两种情况，奇数情况，就在i为中心，左右开始扩展比较，i-1,i+1，
	#     偶数情况就在i前面的空白作为中心，i-1和i开始扩展比较
	for i in range(1,len(string)):
		odd = getLongestPalindromFrom(string,i-1,i+1)
		even = getLongestPalindromFrom(string,i-1,i)
		# 比较odd和even两种情况下，哪个回文更长
		#     lambda表达式翻译为，比较 odd[1]-odd[0] 和 even[1]-even[0]，找出差值最大的那个odd 或者是even 返回作为结果，返回结果也还是一个数组，不是单独数字
		longest = max(odd,even,key=lambda x: x[1] - x[0])
		# 同上，比较currentLongest和longest
		currentLongest = max(longest,currentLongest,key=lambda x:x[1] - x[0])
	# 遍历一遍之后，返回最长的那个注意，最后要+1
	return string[currentLongest[0]:currentLongest[1]+1]

		
		
def getLongestPalindromFrom(string,leftIdx,rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1,rightIdx-1]