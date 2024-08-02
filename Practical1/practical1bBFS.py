# BFS Algorithm Explanation
# 1. Initialization:
# 	- Start from a given node (source or root).
# 	- Use a queue to keep track of the nodes to be visited.
# 	- Maintain a set to keep track of visited nodes to avoid revisiting and processing the same node again.

# 2. Process:
# 	- Enqueue the starting node onto the queue.
# 	- While the queue is not empty:
# 		- Dequeue a node from the queue.
# 			- If the node has not been visited:
# 				- Mark it as visited.
# 				- Process the node (e.g., print its value or perform some operation).
# 				- Enqueue all its adjacent nodes (neighbors) that have not been visited onto the queue.


# BFS Characteristics
# - Space Complexity: O(V) where V is the number of vertices, due to the queue and visited set.
# - Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges, since each vertex and edge is processed once.
# - Applications:
# 	- Finding the shortest path in an unweighted graph.
# 	- Level-order traversal of a tree.
# 	- Finding connected components in a graph.


def bfs_traversal_algorithm(graph, start):
	queue = [start]
	visited = set()

	while queue:
		current = queue.pop(0)

		if current not in visited:
			visited.add(current)
			print(current, end=" ")

			for child in graph[current]:
				if child not in visited:
					queue.append(child)


graph = {
	'A': ['B', 'C'],
	'B': ['D', 'E'],
	'C': ['F'],
	'D': [],
	'E': ['F'],
	'F': [],
}

bfs_traversal_algorithm(graph, 'A')