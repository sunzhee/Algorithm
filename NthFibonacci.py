"""
Nth Fibonacci
The Fibonacci sequence is dened as follows: the rst number of
the sequence is 0 , the second number is 1 , and the nth
number is the sum of the (n - 1)th and (n - 2)th numbers. Write a
function that takes in an integer n and returns the nth
Fibonacci number.
Important note: the Fibonacci sequence is often dened with its
rst two numbers as F0 = 0 and F1 = 1 . For the purpose of
this question, the rst Fibonacci number is F0 ; therefore,
getNthFib(1) is equal to F0 , getNthFib(2) is equal to
F1 , etc..


Sample Input #1
n = 2
Sample Output #1
1 

Sample Input #2
n = 6
Sample Output #2
5 //0,1,1,2,3,5
"""



"""
O(2^n) Time ,O(n) Space
most brutal way, recursive
def getNthFib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return getNthFib(n - 1) + getNthFib(n - 2)
"""


#O(n) Time, O(n) space
#put all the calulated Fibnacci number in a hashtable
#if we have already calculated, then just get it from hashtable
#so we don't have to calulate multiple times
FibDict = {1:0,2:1}
def getNthFib(n):
	if n in FibDict:
		return FibDict[n]
	else:
		temp = getNthFib(n - 1) + getNthFib(n - 2)
		FibDict[n] = temp
	return FibDict[n]


#O(n) Time,O(1) Space
#the best way, do not use recursive
#we only remember the last two fibnacci number, because we don't need others.
#and begin calculate from 3
def getNthFib3(n):
	lastTwo = [0,1]
	#counter must begin with 3,we already have Fib(1) and Fib(2) in lastTwo[] 
	counter = 3
	while counter <= n:
		#exchange the lastTwo, put current as n-1, put n-1 as n-2,and drop n-2
		#and then move forward to next counter
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1
	#only the Fib(1) need return lastTwo[0], the very first one
	if n == 1:
		return lastTwo[0]
	#all other condition,we need return lastTwo[1]
	else:
		return lastTwo[1]

print("input:",6)
print("output:",getNthFib(6))