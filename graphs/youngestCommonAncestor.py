"""
Youngest Common Ancestor
You're given three inputs, all of which
are instances of an AncestralTree
class that have an ancestor
property pointing to their youngest
ancestor. The rst input is the top
ancestor in an ancestral tree (i.e., the
only instance that has no ancestor--its
ancestor property points to None
/ null ), and the other two inputs are
descendants in the ancestral tree.
Write a function that returns the
youngest common ancestor to the two
descendants.
Note that a descendant is considered
its own ancestor. So in the simple
ancestral tree below, the youngest
common ancestor to nodes A and B is
node A.


Sample Input
// The youngest common ancestor to
 A
 /
B

Sample Input
// The nodes are from the ancestral tree below.
topAncestor = node A
descendantOne = node E
descendantTwo = node I
        A
     /    \
    B      C
   / \    / \
  D   E   F  G
 / \
H   I


Sample Output
node B


"""

# This is an input class. Do not edit.
class AncestralTree:
	def __init__(self, name):
		self.name = name
		self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDepth(descendantOne,topAncestor)
	depthTwo = getDepth(descendantTwo,topAncestor)
	if depthOne > depthTwo:
		return getAncestor(descendantOne,descendantTwo,(depthOne - depthTwo))
	else:
		return getAncestor(descendantTwo,descendantOne,(depthTwo - depthOne))
	
def getDepth(descendant,topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def getAncestor(lowerDescendant,upperDescendant,diff):
	# 1st while loop bring lower descendant to the same level of upper descendant
	# 2nd while loop let two descendant go up together, until they meet the same ancestor
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1
	while lowerDescendant != upperDescendant:
		lowerDescendant = lowerDescendant.ancestor
		upperDescendant = upperDescendant.ancestor
	return lowerDescendant

