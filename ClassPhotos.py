"""
Class Photos
It's photo day at the local school, and you're the photographer
assigned to take class photos. The class that you'll be
photographing has an even number of students, and all these
students are wearing red or blue shirts. In fact, exactly half of the
class is wearing red shirts, and the other half is wearing blue
shirts. You're responsible for arranging the students in two rows
before taking the photo. Each row should contain the same
number of the students and should adhere to the following
guidelines:
All students wearing red shirts must be in the same row.
All students wearing blue shirts must be in the same row.
Each student in the back row must be strictly taller than
the student directly in front of them in the front row.
You're given two input arrays: one containing the heights of all
the students with red shirts and another one containing the
heights of all the students with blue shirts. These arrays will
always have the same length, and each height will be a positive
integer. Write a function that returns whether or not a class
photo that follows the stated guidelines can be taken.
Note: you can assume that each class has at least 2 students


Sample Input
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

Sample Output
true
"""


redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]


#O(nlogn) time, O(1)space, n is the number of students
def classPhotos(redShirtHeights, blueShirtHeights):
	#sort as tallest in the first
	redShirtHeights.sort(reverse = True)
	blueShirtHeights.sort(reverse = True)
	
	#if tallest in Red is shorter than tallest in Blue, then Red must be the first row
	#else tallest in Blue is shorter than tallest in Red, then Blue must be the first row
	if redShirtHeights[0] < blueShirtHeights[0]:
		firstRow = "Red"
	else:
		firstRow = "Blue"
	
	#check one by one, if any red taller than blue,if yes,
	#since red is first row and taller then blue then return false
	#else is the on the contrary 
	for i in range(len(redShirtHeights)):
		if firstRow == "Red":
			if redShirtHeights[i] >= blueShirtHeights[i]:
				return False
		else:
			if blueShirtHeights[i] >= redShirtHeights[i]:
				return False
			

	return True

print("input:","\nredShirtHeights:",redShirtHeights,"\nblueShirtHeights:",blueShirtHeights)
print("output:",classPhotos(redShirtHeights,blueShirtHeights))