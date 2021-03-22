"""
Non-Constructible Change

Given an array of positive integers representing the values of
coins in your possession, write a function that returns the
minimum amount of change (the minimum sum of money) that
you cannot create. The given coins can have any positive integer
value and aren't necessarily unique (i.e., you can have multiple
coins of the same value).
For example, if you're given coins = [1, 2, 5] , the
minimum amount of change that you can't create is 4 . If you're
given no coins, the minimum amount of change that you can't
create is 1 .


Sample Input
coins = [5, 7, 1, 1, 2, 3, 22]

Sample Output
20


"""


myOwncoins = [1,1,1,1,1]
myOwncoins = [5, 7, 1, 1, 2, 3, 22]


def nonConstructibleChange(coins):
	coins.sort()
	currentChange = 0
	for coin in coins:
		if (coin <= currentChange + 1):
			currentChange = currentChange + coin
		else:
			return currentChange + 1
	return currentChange + 1

print("input:",myOwncoins)
print("output:",nonConstructibleChange(myOwncoins))