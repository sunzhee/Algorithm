"""
Lowest Common Manager

You're given three inputs, all of which are
instances of an OrgChart class that have a
directReports property pointing to their
direct reports. The rst input is the top
manager in an organizational chart (i.e., the
only instance that isn't anybody else's direct
report), and the other two inputs are reports
in the organizational chart. The two reports
are guaranteed to be distinct.
Write a function that returns the lowest
common manager to the two reports.



// From the organizational chart below.
topManager = Node A
reportOne = Node E
reportTwo = Node I

 	  A
 	/   \
   B     C
  / \   / \
  D  E  F  G
 / \
H   I

Sample Output
Node B

"""

def getLowestCommonManager(topManager, reportOne, reportTwo):
	return getOrgInfo(topManager,reportOne,reportTwo).lowestCommonManager

class OrgInfo:
	def __init__(self,lowestCommonManager,numImportantReporters):
		self.lowestCommonManager = lowestCommonManager
		self.numImportantReporters = numImportantReporters

def getOrgInfo(manager,reportOne,reportTwo):
	numberImportantReports = 0
	
	for directReport in manager.directReports:
		orgInfo = getOrgInfo(directReport,reportOne,reportTwo)
		if orgInfo.lowestCommonManager is not None:
			return orgInfo
		numberImportantReports += orgInfo.numImportantReporters
		
	if manager == reportOne or manager == reportTwo:
		numberImportantReports += 1
		
	lowestCommonManager = manager if numberImportantReports == 2 else None
	
	return OrgInfo(lowestCommonManager,numberImportantReports)
	
	
	
# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
