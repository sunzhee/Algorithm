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
	hq.heappush(timesWhenLaptopIsUsed,times[0])
	#print(timesWhenLaptopIsUsed)
	for index in range(1,len(times)):
		currentInterval = times[index]

		if timesWhenLaptopIsUsed[0][1] <= currentInterval[0]:
			#print(timesWhenLaptopIsUsed[0])
			#print(currentInterval[0])
			hq.heappop(timesWhenLaptopIsUsed)

		hq.heappush(timesWhenLaptopIsUsed,currentInterval)
		print(timesWhenLaptopIsUsed)
	return len(timesWhenLaptopIsUsed)