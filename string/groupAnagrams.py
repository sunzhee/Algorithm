"""
Group Anagrams

Write a function that takes in an array of
strings and groups anagrams together.
Anagrams are strings made up of exactly the
same letters, where order doesn't matter. For
example, "cinema" and "iceman" are
anagrams; similarly, "foo" and "ofo" are
anagrams.
Your function should return a list of anagram
groups in no particular order.

Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Sample Output
[  ["foo"],  ["flop", "olfp"],  ["oy", "yo"],  ["act", "cat", "tac"] ]
"""

# O(w * n*log(n)) time, O(w * n) space
# w is the number of words, n is the longest word's length
# 遍历一次，每个单词先排序成字母顺序，然后用一个哈希列表保存起来，一样的就添加到value里，没有的就新创建一个key:value,然后输出所有的values即可
def groupAnagrams(words):
	anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		# print(word) yo,act....cat...
		# print(sortedWord) yo,act....act...
		if sortedWord in anagrams:
			# 如果在hashtable anagrams里面的话，在同样key下面添加这个新的word，排序前的word，cat等
			anagrams[sortedWord].append(word)
		else:
			# 如果没有，则添加一个新的key value配对
			anagrams[sortedWord] = [word]
	print(anagrams.values())
	# 最后输出的时候要做成list形式
	return list(anagrams.values())

		
		
