"""
Min Number Of Coins For Change

Given an array of positive integers representing coin
denominations and a single non-negative integer n
representing a target amount of money, write a function that
returns the smallest number of coins needed to make change for
(to sum up to) that target amount using the given coin
denominations.
Note that you have access to an unlimited amount of coins. In
other words, if the denominations are [1, 5, 10] , you have
access to an unlimited amount of 1 s, 5 s, and 10 s.
If it's impossible to make change for the target amount, return
-1 .


Sample Input
n = 7
denoms = [1, 5, 10]


Sample Output
3 // 2x1 + 1x5

"""

n = 7
denoms = [1, 5, 10]


#O(d*n) time | O(n) space, d is the denominations, two layer of loop
#outter layer is demoniations, innner loop is given amount n
#base case is: n=0, Min number of coins = 0,
#all other case: MinCoins[n] = min(minCoins[n],1+ minCoins[n - denominations])
def minNumberOfCoinsForChange(n, denoms):
	minCoins = [float("inf") for nums in range(n + 1)]
	minCoins[0] = 0
	for denom in denoms:
		for amount in range(1,n + 1):
			if denom <= amount:
				minCoins[amount] = min(minCoins[amount],minCoins[amount - denom] + 1)
	return minCoins[n] if minCoins[n] != float("inf") else -1


