# 3a. Write a program to implement alpha beta search.

# Sure! Alpha-Beta Pruning is an optimization technique for the Minimax algorithm in game theory.
# It helps to eliminate branches in the game tree that don't need to be explored because they won't
# affect the final decision.

# Complexities
# Time Complexity: The time complexity of the Alpha-Beta Pruning algorithm in the best case is 
# O(b^(m/2)), where b is the branching factor (the average number of child nodes per node) and
# m is the maximum depth of the tree. This is because Alpha-Beta Pruning can effectively cut off
# half of the branches in the best case. In the worst case, it still evaluates 
# O(b^m) nodes, similar to the Minimax algorithm without pruning.

# Space Complexity: The space complexity of the Alpha-Beta Pruning algorithm is 
# O(m), where m is the maximum depth of the tree. This is due to the space required to maintain the recursion stack.

# Summary
# Time Complexity:
# Best case: O(b^(m/2))
# Worst case: O(b^m)

import math

game_tree = {
	'A': ['B', 'C'],
	'B': ['D', 'E'],
	'C': ['F', 'G'],
	'D': [0, 6],
	'E': [2, 3],
	'F': [7, 5],
	'G': [8, 1],
}

def alpha_beta(node, depth, alpha, beta, alpha_player):

	# If you either reach the last depth or the node is a number
	# return the node
	if depth == 0 or not isinstance(node, str):
		return node

	# If it's alpha player's turn
	# initialize max to negative infinity which is the value of alpha at that level
	if alpha_player:
		max_val = -math.inf

		# For every child that has children
		# keep going until you reach the leaf node that returns a number
		for child in game_tree[node]:
			evaluated_val = alpha_beta(child, depth-1, alpha, beta, False)

			# Now update the parent node's value, and also alpha-beta value
			# which is again max value at that level
			max_val = max(max_val, evaluated_val)
			alpha = max(alpha, max_val)

			# If alpha is greater than or equal to beta, then prune akpha's branch
			if alpha >= beta:
				break
		
		# Finally return the max (i.e. alpha value) after all the children are evaluated
		return max_val
	
	# If it's beta player's turn
	# initialize min to positive infinity which is the value of beta at that level
	else:
		min_val = math.inf

		# For every child that has children
		# keep going until you reach the leaf node that returns a number
		for child in game_tree[node]:
			evaluated_val = alpha_beta(child, depth-1, alpha, beta, True)

			# Now update the parent node's value, and also alpha-beta value
			# which is again min value at that level
			min_val = min(min_val, evaluated_val)
			beta = min(beta, min_val)

			# If alpha is greater than or equal to beta, then prune beta's branch
			if alpha >= beta:
				break

		# Finally return the min (i.e. alpha value) after all the children are evaluated
		return min_val
	


# Call the algorithm with the entire tree with initial values
# And it returns the optimal value
optimal_value = alpha_beta('A', 3, -math.inf, math.inf, True)
print(f'The optimal value is {optimal_value}')