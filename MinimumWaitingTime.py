"""
Minimum Waiting Time
You're given a non-empty array of positive integers representing
the amounts of time that specic queries take to execute. Only
one query can be executed at a time, but the queries can be
executed in any order.
A query's waiting time is dened as the amount of time that it
must wait before its execution starts. In other words, if a query is
executed second, then its waiting time is the duration of the rst
query; if a query is executed third, then its waiting time is the
sum of the durations of the rst two queries.
Write a function that returns the minimum amount of total
waiting time for all of the queries. For example, if you're given
the queries of durations [1, 4, 5] , then the total waiting
time if the queries were executed in the order of [5, 1, 4]
would be (0) + (5) + (5 + 1) = 11 . The rst query of
duration 5 would be executed immediately, so its waiting time
would be 0 , the second query of duration 1 would have to
wait 5 seconds (the duration of the rst query) to be executed,
and the last query would have to wait the duration of the rst
two queries before being executed.

Sample Input
queries = [3, 2, 1, 2, 6]

Sample Output
17

"""


queries = [4, 3, 1, 1, 3, 2, 1, 8]
queries = [3, 2, 1, 2, 6]

#O(nlogn) time , O(1) space, n the queries's length, nlogn because of the sort time
def minimumWaitingTime(queries):
	totalWaitingTime = 0
	queries.sort()
	
	#this enumerate(queries) takes out the array's id and array's item at each loop
	#same as below
	#for idx,duration in enumerate(queries):
	#	print(idx,duration)
	for i in range(len(queries)):
		#print(i,queries[i])
		totalWaitingTime += (len(queries) - (i + 1)) * queries[i]
	return totalWaitingTime

print("input:",queries)
print("output:",minimumWaitingTime(queries))