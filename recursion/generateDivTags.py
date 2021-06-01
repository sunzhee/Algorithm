"""
Generate Div Tags

Write a function that takes in a positive
integer numberOfTags and returns a list of
all the valid strings that you can generate
with that number of matched <div></div> tags.
A string is valid and contains matched
<div></div> tags if for every opening tag
<div> , there is a closing tag </div> that
comes after the opening tag and that isn't
used as a closing tag for another opening
tag. Each output string should contain
exactly numberOfTags opening tags and
numberOfTags closing tags.

For example, given numberOfTags = 2 ,
the valid strings to return would be:
["<div></div><div></div>",
"<div><div></div></div>"] .

Note that the output strings don't need to be
in any particular order.


Sample Input
numberOfTags = 3

Sample Output
 [
 "<div><div><div></div></div></div>",
 "<div><div></div><div></div></div>",
 "<div><div></div></div><div></div>",
 "<div></div><div><div></div></div>",
 "<div></div><div></div><div></div>",
 ] 
"""

# time and space complexity is a Catalan number
# O((2n)! / (n! * (n+1)!)) time, O((2n)!/(n! * (n+1)!))
# 卡塔兰数，用于括号组合，或者堆栈组合
def generateDivTags(numberOfTags):
	resultDivTags = []
	recrusiveDivTags(numberOfTags,numberOfTags,"",resultDivTags)
	return resultDivTags

# 利用嵌套递归，正好完成所有排列组合的可能性，是一个很tricky的技巧
def recrusiveDivTags(openTagNumber,closeTagNumber,partialTags,resultDivTags):
	# 添加open tag的条件就是只要大于0
	if openTagNumber > 0:
		newPartialTags = partialTags + "<div>"
		recrusiveDivTags(openTagNumber - 1,closeTagNumber,newPartialTags,resultDivTags)
		
	# 添加close tag的条件就是只要open 小于close
	if openTagNumber < closeTagNumber:
		newPartialTags = partialTags + "</div>"
		recrusiveDivTags(openTagNumber,closeTagNumber - 1,newPartialTags,resultDivTags)
	
	# 走到close为0，说明全部添加完毕，可以返回结果
	if closeTagNumber == 0:
		resultDivTags.append(partialTags)
		