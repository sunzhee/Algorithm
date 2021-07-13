"""
Laptop Rentals

You're given a list of time intervals during
which students at a school need a laptop.
These time intervals are represented by pairs
of integers [start, end] , where
0 <= start < end . However, start and
end don't represent real times; therefore,
they may be greater than 24 .
No two students can use a laptop at the same
time, but immediately after a student is done
using a laptop, another student can use that
same laptop. For example, if one student rents
a laptop during the time interval [0, 2] ,
another student can rent the same laptop
during any time interval starting with 2 .
Write a function that returns the minimum
number of laptops that the school needs to
rent such that all students will always have
access to a laptop when they need one.


Sample Input
times =
[
 [0, 2],
 [1, 4],
 [4, 6],
 [0, 4],
 [7, 8],
 [9, 11],
 [3, 10],
]

Sample Output 
3

"""

# O(n*log(n)) time, O(n) space
def laptopRentals(times):
	if len(times) == 0:
		return 0
	
	usedLaptop = 0
	startTime = sorted([interval[0] for interval in times])
	endTime = sorted([interval[1] for interval in times])
	
	startIterator = 0
	endIterator = 0
	
	while startIterator < len(times):
		if startTime[startIterator] >= endTime[endIterator]:
			usedLaptop -= 1
			endIterator +=1
		
		usedLaptop += 1
		startIterator += 1
			
	return usedLaptop



#######################

import heapq as hq

def laptopRentals(times):
	if len(times) == 0:
		return 0
	
	times.sort(key = lambda x: x[0])
	timesWhenLaptopIsUsed = []
	# heapq 没有用第二个元素排序的功能，所以要建立一个数组元素，把第二个值放在第一位，然后数组值放在第二位
	# 这样就可以按照我们需要的值进行堆排序了
	# 原times[0] = [0,2]
	# timesHeapElement = [2,[0,2]]
	timesHeapElement = [times[0][1],times[0]]
	hq.heappush(timesWhenLaptopIsUsed,timesHeapElement)
	#print(timesHeapElement)
	for index in range(1,len(times)):
		currentInterval = times[index]

		if timesWhenLaptopIsUsed[0][0] <= currentInterval[0]:
			hq.heappop(timesWhenLaptopIsUsed)
		
		timesHeapElement = [times[index][1],times[index]]
		hq.heappush(timesWhenLaptopIsUsed,timesHeapElement)
	return len(timesWhenLaptopIsUsed)