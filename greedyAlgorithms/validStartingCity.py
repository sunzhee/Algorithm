"""
Valid Starting City

Imagine you have a set of cities that are laid
out in a circle, connected by a circular road
that runs clockwise. Each city has a gas
station that provides gallons of fuel, and
each city is some distance away from the
next city.
You have a car that can drive some number
of miles per gallon of fuel, and your goal is to
pick a starting city such that you can ll up
your car with that city's fuel, drive to the next
city, rell up your car with that city's fuel,
drive to the next city, and so on and so forth
until you return back to the starting city with
0 or more gallons of fuel left.
This city is called a valid starting city, and it's
guaranteed that there will always be exactly
one valid starting city.
For the actual problem, you'll be given an
array of distances such that city i is
distances[i] away from city i + 1 .
Since the cities are connected via a circular
road, the last city is connected to the rst
city. In other words, the last distance in the
distances array is equal to the distance
from the last city to the rst city. You'll also
be given an array of fuel available at each
city, where fuel[i] is equal to the fuel
available at city i . The total amount of fuel
available (from all cities combined) is exactly
enough to travel to all cities. Your fuel tank
always starts out empty, and you're given a
positive integer value for the number of
miles that your car can travel per gallon of
fuel (miles per gallon, or MPG). You can
assume that you will always be given at least
two cities.
Write a function that returns the index of the
valid starting city.


Sample Input
distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10


Sample Output
4
"""
# solution 1, brutal force, double loop, check city one by one
#O(n^2) time | O(1) space
def validStartingCity1(distances, fuel, mpg):
	numberOfCities = len(distances)
	
	# check start city one by one, in this for loop
	for startCityIndex in range(numberOfCities):
		milesRemaining = 0
		
		for currentCityIndex in range(startCityIndex, startCityIndex + numberOfCities):
			# can not reach next city, go check next start city
			if milesRemaining < 0:
				continue
			# make sure the index is not out of bound, because it is a cycle
			currentCityIndex = currentCityIndex % numberOfCities
			fuelFromCurrentCity = fuel[currentCityIndex]
			distanceToNextCity = distances[currentCityIndex]
			milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity
			# inner loop finished, we have go around, and miles >= 0, actually can only = 0
			# then, this is the start city
			
		if milesRemaining >= 0:
			return startCityIndex
		
	return -1

# solution 2, smart one
# 只要找到到达某个城市之后，剩余油最少的那个城市，以它作为起点即可。
# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
	numberOfCities = len(fuel)
	milesRemaining = 0

	indexOfStartCity = 0
	milesRemainingOfStartCity = 0
	
	for cityIndex in range(1,numberOfCities):
		distanceFromPreviousCity = distances[cityIndex - 1]
		fuelFromPreviousCity = fuel[cityIndex - 1]
		# 这里是 +=， 因为需要计算从上一个或者上上个city过来还能剩余多少miles
		milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity
		if milesRemaining < milesRemainingOfStartCity:
			milesRemainingOfStartCity = milesRemaining
			indexOfStartCity = cityIndex
	
	return indexOfStartCity



