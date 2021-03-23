"""

Tournament Winner

There's an algorithms tournament taking place in which teams of
programmers compete against each other to solve algorithmic
problems as fast as possible. Teams compete in a round robin,
where each team faces o against all other teams. Only two
teams compete against each other at a time, and for each
competition, one team is designated the home team, while the
other team is the away team. In each competition there's always
one winner and one loser; there are no ties. A team receives 3
points if it wins and 0 points if it loses. The winner of the
tournament is the team that receives the most amount of points.
Given an array of pairs representing the teams that have
competed against each other and an array containing the results
of each competition, write a function that returns the winner of
the tournament. The input arrays are named competitions
and results , respectively. The competitions array has
elements in the form of [homeTeam, awayTeam] , where each
team is a string of at most 30 characters representing the name
of the team. The results array contains information about the
winner of each corresponding competition in the
competitions array. Specically, results[i] denotes the
winner of competitions[i] , where a 1 in the results
array means that the home team in the corresponding
competition won and a 0 means that the away team won.
It's guaranteed that exactly one team will win the tournament
and that each team will compete against all other teams exactly
once. It's also guaranteed that the tournament will always have
at least two teams.


Sample Input
competitions = [
 ["HTML", "C#"],
 ["C#", "Python"],
 ["Python", "HTML"],
]
results = [0, 0, 1]


Sample Output
"Python"
// C# beats HTML, Python Beats C#, and Python Bea
// HTML - 0 points
// C# - 3 points
// Python - 6 points

"""

competitions =[
 ["HTML", "C#"],
 ["C#", "Python"],
 ["Python", "HTML"],
]

results = [0, 0, 1]



def tournamentWinner(competitions, results):

	#use Current Best Team to record the highest score, 
	#so we dont need traverse the scores list again for highest score team
	currentBestTeam = ""
	scores = {currentBestTeam:0}
	
	for index, competition in enumerate(competitions):
		result = results [index]
		#this is a python way to get items from hash-table
		#same as:
		#homeTeam = competition[0]
		#awayTeam = competition[1]
		homeTeam,awayTeam = competition
		
		if result == 1:
			winningTeam = homeTeam
		else:
			winningTeam = awayTeam
		
		#add winning team into the scores list, if this winning team not in the scores list
		#if team never win, that team wont be appeared in the scores list
		if winningTeam not in scores:
			scores[winningTeam] = 0
			
		scores[winningTeam] = scores[winningTeam] + 3
		
		#compare the current best team with the new winning team's score
		#record the highest score team in currentBestTeam
		if scores[winningTeam] > scores[currentBestTeam] :
			currentBestTeam = winningTeam
			
	return currentBestTeam


print ("input competitions:",competitions)
print ("input results:",results)
print ("output winner is:",tournamentWinner(competitions,results))