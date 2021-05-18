"""
Balanced Brackets

Write a function that takes in a string made
up of brackets ( ( , [ , { , ) , ] , and } )
and other optional characters. The function
should return a boolean representing
whether the string is balanced with regards
to brackets.
A string is said to be balanced if it has as
many opening brackets of a certain type as it
has closing brackets of that type and if no
bracket is unmatched. Note that an opening
bracket can't match a corresponding closing
bracket that comes before it, and similarly, a
closing bracket can't match a corresponding
opening bracket that comes after it. Also,
brackets can't overlap each other as in
[(]) .



Sample Input
string = "([])(){}(())()()"

Sample Output
true // it's balanced

"""

# O(n) time, O(n) space
def balancedBrackets(string):
	openingBrackets = "([{"
	closingBrackets = ")]}"
	matchingBracket ={ ")":"(" , "]":"[" , "}":"{" }
	bracketStack = []
	
	for char in string:
		if char in openingBrackets:
			bracketStack.append(char)
		if char in closingBrackets:
			# 这里不要用 is None，因为stack赋值之后，pop出去，虽然stack目前没有值，但不等于None
			if len(bracketStack) == 0:
				return False
			elif matchingBracket[char] != bracketStack[-1]:
				return False
			else:
				bracketStack.pop()
	if len(bracketStack) != 0:
		return False
	else:
		return True
				
