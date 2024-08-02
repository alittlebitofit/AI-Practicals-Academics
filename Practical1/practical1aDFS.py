# DFS Algorithm Explanation
# 1. Initialization:
# 	- Start from a given node (source or root).
# 	- Use a stack to keep track of the nodes to be visited.
# 	- Maintain a set to keep track of visited nodes to avoid revisiting and processing the same node again.

# 2. Process:
# 	- Push the starting node onto the stack.
# 	- While the stack is not empty:
# 		- Pop a node from the stack.
# 		- If the node has not been visited:
# 			- Mark it as visited.
# 			- Process the node (e.g., print its value or perform some operation).
# 			- Push all its adjacent nodes (neighbors) that have not been visited onto the stack.


# DFS Characteristics
# - Space Complexity: O(V) where V is the number of vertices, due to the stack and visited set.
# - Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges, since each vertex and edge is processed once.
# - Applications:
# 	- Finding connected components in a graph.
# 	- Topological sorting.
# 	- Solving puzzles and games (like mazes).



def dfs_traversal_algorithm(graph, start):
	stack = [start]

	visited = set()

	while stack:
		current = stack.pop()

		if current not in visited:
			visited.add(current)

			print(current, end=" ")

			for neighbor in graph[current]:
				if neighbor not in visited:
					stack.append(neighbor)


graph = {
	'A': ['B', 'C'],
	'B': ['D', 'E'],
	'C': ['F'],
	'D': [],
	'E': ['F'],
	'F': [],
}

dfs_traversal_algorithm(graph, 'A')