"""
Min Rewards

Imagine that you're a teacher who's just
graded the nal exam in a class. You have a
list of student scores on the nal exam in a
particular order (not necessarily sorted), and
you want to reward your students. You decide
to do so fairly by giving them arbitrary
rewards following two rules:
1. All students must receive at least one
reward.
2. Any given student must receive strictly
more rewards than an adjacent student
(a student immediately to the left or to
the right) with a lower score and must
receive strictly fewer rewards than an
adjacent student with a higher score.
Write a function that takes in a list of scores
and returns the minimum number of rewards
that you must give out to students to satisfy
the two rules.
You can assume that all students have
dierent scores; in other words, the scores
are all unique.


Sample Input
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]


Sample Output
25

"""


# O(n^2) time, O(n) space
# 从第二个开始比较，第二个i和他前一个 j = i-1比较，如果scores i比j大，那么reward[i] +1 就行了
# 如果score i比j小，那么就要从i的前一个一直循环到数组初始，给每一个数值用max公式赋值
# 这个公式很重要，整个题目的核心算法 max(reward[j],reward[j+1]+1)
def minRewards(scores):
	# 初始化，全部给1
	rewards = [1 for _ in scores]

	for i in range(1,len(scores)):
		j = i - 1
		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >=0 and scores[j] > scores[j+1]:
				rewards[j] = max(rewards[j],rewards[j+1] + 1)
				j -=1
	return sum(rewards)

# O(n) time, O(n) space
# 先从左到右循环一遍，从第二个开始，只要当前的i比左边的i-1 score大，那i就+1
# 再从右到左循环一遍，从倒数第二个开始，只要当前的i比右边的i+1大，那就套用max公式
# 核心max公式 rewards[i] = max(rewards[i],rewards[i+1]+1)
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1,len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
	for i in reversed(range(len(scores)-1)):
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i],rewards[i+1] + 1)
	return sum(rewards)
			


