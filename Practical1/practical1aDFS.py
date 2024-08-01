def depth_first_search(graph, start):
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

depth_first_search(graph, 'A')