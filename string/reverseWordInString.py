"""
Reverse Words In String

Write a function that takes in a string of
words separated by one or more whitespaces
and returns a string that has these words in
reverse order. For example, given the string
"tim is great" , your function should
return "great is tim" .
For this problem, a word can contain special
characters, punctuation, and numbers. The
words in the string will be separated by one
or more whitespaces, and the reversed string
must contain the same whitespaces as the
original string. For example, given the string
"whitespaces 4" you would be
expected to return "4 whitespaces" .
Note that you're not allowed to to use any
built-in split or reverse
methods/functions. However, you are
allowed to use a built-in join
method/function.
Also note that the input string isn't
guaranteed to always contain words.

Sample Input
string = "AlgoExpert is the best!"

Sample Output
"best! the is AlgoExpert"

"""

# O(n) time, O(n) space
# 先把全部字符串翻转过来，此时word字母顺序是反的，所以再一个一个找空格隔开的word，把每一个word再反转成正序
def reverseWordsInString(string):
	# 字符串没法操作，所以将字符串换成数组
	characters = [char for char in string]
	# 把整个字符串倒过来
	reverseListRange(characters,0,len(characters)-1)
	
	startOfWord = 0
	while startOfWord < len(characters):
		endOfWord = startOfWord
		# endOfWord 不停的 +1 ，范围是0到len(characters)，直到找到空格为止
		# 这样就可以找出word
		while endOfWord < len(characters) and characters[endOfWord] != " ":
			endOfWord += 1
		# 因为所有字母都是逆序，所以把这一段word的字母反转成正序
		reverseListRange(characters,startOfWord,endOfWord -1) # -1是因为最后一个是空格，跳过
		# 找下一个word之前，要把开始位置设置为当前结束位置+1，跳过空格
		startOfWord = endOfWord + 1
	return "".join(characters)
	
def reverseListRange(list,start,end):
	while start < end:
		list[start],list[end] = list[end],list[start]
		start += 1
		end -= 1
		
