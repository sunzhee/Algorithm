"""
Task Assignment

You're given an integer k representing a number of workers
and an array of positive integers representing durations of
tasks that must be completed by the workers. Specically,
each worker must complete two unique tasks and can only
work on one task at a time. The number of tasks will always
be equal to 2k such that each worker always has exactly
two tasks to complete. All tasks are independent of one
another and can be completed in any order. Workers will
complete their assigned tasks in parallel, and the time taken
to complete all tasks will be equal to the time taken to
complete the longest pair of tasks (see the sample output for
an explanation).
Write a function that returns the optimal assignment of tasks
to each worker such that the tasks are completed as fast as
possible. Your function should return a list of pairs, where
each pair stores the indices of the tasks that should be
completed by one worker. The pairs should be in the
following format: [task1, task2] , where the order of
task1 and task2 doesn't matter. Your function can
return the pairs in any order. If multiple optimal assignments
exist, any correct answer will be accepted.
Note: you'll always be given at least one worker (i.e., k will
always be greater than 0).



Sample Input
k = 3
tasks = [1, 3, 5, 3, 1, 4]

Sample Output
[
 [0, 2], // tasks[0] = 1, tasks[2] = 5 | 1 + 5 = 6
 [4, 5], // tasks[4] = 1, tasks[5] = 4 | 1 + 4 = 5
 [1, 3], // tasks[1] = 3, tasks[3] = 3 | 3 + 3 = 6

] 

// The fastest time to complete all tasks is 6.
// Note: there are multiple correct answers for this sa
// The following is an example of another correct answe
// [
// [2, 4],
// [0, 5],
// [1, 3]
// [


"""

# O(n*log(n)) time, because of sorting | O(n) space, for store the dict
def taskAssignment(k, tasks):
	resultPairedTasks = []
	sortedTasks = sorted(tasks)
	# we create a dict for original task and dur pair
	taskDurToIndex = getTaskDurToIndex(tasks)
	for index in range(k):
		# this is the smallest duration,first index, very left one
		task1Dur = sortedTasks[index]
		# get the real index from dict, may have two or more index
		# so we need an queue
		indexWithTask1Dur = taskDurToIndex[task1Dur]
		# we get one index from this duration
		# 为什么这里pop()之后，字典变量跟着也被pop掉了？？
		task1Index = indexWithTask1Dur.pop()
		
		# this is the biggest duration, last index
		# actual length->(len(tasks) -1) - index :  very right one
		task2Dur = sortedTasks[len(tasks) - 1 - index]
		indexWithTask2Dur = taskDurToIndex[task2Dur]
		task2Index = indexWithTask2Dur.pop()

		print(taskDurToIndex)
		
		resultPairedTasks.append([task1Index,task2Index])
		
	return resultPairedTasks
	
	
def getTaskDurToIndex(tasks):
	taskDurToIndex = {}
	for index,taskDur in enumerate(tasks):
		# if there is same duration in tasks, we append index to the same duration array
		# we can pop the index, and dont care about task sequence.
		if taskDur in taskDurToIndex:
			taskDurToIndex[taskDur].append(index)
		# if not in the dict, just add it
		else:
			taskDurToIndex[taskDur] = [index]

	return taskDurToIndex

