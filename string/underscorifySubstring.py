"""
Underscorify Substring

Write a function that takes in two strings: a
main string and a potential substring of the
main string. The function should return a
version of the main string with every
instance of the substring in it wrapped
between underscores.

If two or more instances of the substring in
the main string overlap each other or sit side
by side, the underscores relevant to these
substrings should only appear on the far left
of the leftmost substring and on the far right
of the rightmost substring. If the main string
doesn't contain the other string at all, the
function should return the main string intact.

Sample Input
string = "testthis is a testtest to see if testestest it work"
substring = "test"

Sample Output
"_test_this is a _testtest_ to see if _testestest_ it works"

"""

# O(n + m) time, O(n) space
# 时间复杂度会因为输入的string发生很大变化，主要是find substring这个过程，最复杂的情况为O(n + m)简单的可以到O(n)
def underscorifySubstring(string, substring):
	locationsWithcollapse = getLocations(string,substring)
	locations = collapse(locationsWithcollapse)
	return underscorify(string,locations)

def getLocations(string,substring):
	locations = []
	startIndex = 0
	while startIndex < len(string):
		nextIndex = string.find(substring,startIndex)
		if nextIndex != -1: # -1 表示没有找到substring
			locations.append([nextIndex,nextIndex + len(substring)])
			startIndex = nextIndex + 1
		else: # 等于 -1 ，搜索结束
			break
	return locations

def collapse(locations):
	if not len(locations): # 如果是空的，直接返回空
		return locations
	newLocations = [locations[0]]
	previous = newLocations[0]
	for i in range(1,len(locations)):
		current = locations[i]
		if current[0] <= previous[1]:
			previous[1] = current[1]
		else:
			newLocations.append(current)
			previous = current
	return newLocations

def underscorify(string,locations):
	locationsIndex = 0
	stringIndex = 0
	inBetweenUnderscores = False
	finialChars = []
	i = 0 # 用来标记每一个location的坐标是前面的还是后面的
	while stringIndex < len(string) and locationsIndex < len(locations):
		if stringIndex == locations[locationsIndex][i]:
			finialChars.append("_")
			inBetweenUnderscores = not inBetweenUnderscores
			if not inBetweenUnderscores:
				locationsIndex += 1
			i = 1 if i == 0 else 0
		finialChars.append(string[stringIndex])
		stringIndex += 1
	if locationsIndex < len(locations):
		finialChars.append("_")
	elif stringIndex < len(string):
		finialChars.append(string[stringIndex:])
			
	return "".join(finialChars)
	
	
	
	
	
	
	
	
	
