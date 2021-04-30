"""
Cycle In Graph

You're given a list of edges representing
an unweighted, directed graph with at least
one node. Write a function that returns a
boolean representing whether the given
graph contains a cycle.
For the purpose of this question, a cycle is
dened as any number of vertices, including
just one vertex, that are connected in a
closed chain. A cycle can also be dened as a
chain of at least one vertex in which the rst
vertex is the same as the last.
The given list is what's called an adjacency
list, and it represents a graph. The number of
vertices in the graph is equal to the length of
edges , where each index i in edges
contains vertex i 's outbound edges, in no
particular order. Each individual edge is
represented by a positive integer that
denotes an index (a destination vertex) in the
list that this vertex is connected to. Note that
these edges are directed, meaning that you
can only travel from a particular vertex to its
destination, not the other way around
(unless the destination vertex itself has an
outbound edge to the original vertex).
Also note that this graph may contain selfloops. A self-loop is an edge that has the
same destination and origin; in other words,
it's an edge that connects a vertex to itself.
For the purpose of this question, a self-loop
is considered a cycle.
For a more detailed explanation, please refer to the
Conceptual Overview section of this question's video
explanation.


Sample Input
edges = [
 [1, 3],
 [2, 3, 4],
 [0],
 [],
 [2, 5],
 [],
]

Sample Output
true
// There are multiple cycles in this graph:
// 1) 0 -> 1 -> 2 -> 0
// 2) 0 -> 1 -> 4 -> 2 -> 0
// 3) 1 -> 2 -> 0 -> 1
// These are just 3 examples; there are more.


test cases:

edges = [
    [],
    [0, 3],
    [0],
    [1, 2]
  ]
True

edges = [
    [1],
    [2, 3, 4, 5, 6, 7],
    [],
    [2, 7],
    [5],
    [],
    [4],
    [0]
  ]
 True

"""

edges = [
 [1, 3],
 [2, 3, 4],
 [0],
 [],
 [2, 5],
 [],
]

# O(v + e) time | O(v) space
# v+e is vertex + edges
def cycleInGraph(edges):
	numberOfNodes = len(edges)
	visited = currentStack = [False for _ in range(numberOfNodes)]
	
	for node in range(numberOfNodes):
		if visited[node]:
			continue
		# DFS, go check node one by one,see if it has cycle
		# only we find cycle, we can break the loop to return True, we can ignor all the rest nodes
		# if we didn't find cycle at this node, we do nothing, continue the for loop for next node.
		hasCycle = containCycle(node,edges,visited,currentStack)
		if hasCycle:
			return True
		#return containCycle(node,edges,visited,currentStack)
	
	return False

def containCycle(node,edges,visited,currentStack):
	visited[node] = True
	currentStack[node] = True
	
	neighbors = edges[node]
	for neighbor in neighbors:
		if not visited[neighbor]:
			hasCycle = containCycle(neighbor,edges,visited,currentStack)
			# if has no cycle, do nothing, go to next neighbor
			if hasCycle:
				return True
		# else,this node is visited, and in current stack, so it must be the ancestor
		# then this edge is a back edge, has cycle
		elif currentStack[neighbor]:
			return True
	# current node move our of the stack, pop out DFS queue
	currentStack[node] = False
	
	return False

print("edges:",edges)
print("contain cycle:",cycleInGraph(edges))