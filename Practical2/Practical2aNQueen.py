# 2a Write a program to simulate 4-Queen / N-Queen problem.

# N-Queen Problem Characteristics:
# - Time Complexity: The time complexity of the N-Queen problem is O(N!), as there are N choices for the first queen, N-1 choices for the second, and so on.
# - Space Complexity: The space complexity is O(N^2) for storing the board.

""" Test definition - START """
class TestNQueen:
	def test_is_safe_column_pass():
		board = [
		    ["Q", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		]

		assert Board.is_safe(board, row=1, col=1) == True


	def test_is_safe_column_fail():
		board = [
		    ["Q", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		]

		assert Board.is_safe(board, row=1, col=0) == False


	def test_is_safe_upper_left_diagonal_pass():
		board = [
		    ["Q", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		]

		assert Board.is_safe(board, row=1, col=2) == True


	def test_is_safe_upper_left_diagonal_fail():
		board = [
		    ["Q", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		]

		assert Board.is_safe(board, row=1, col=1) == False


	def test_is_safe_upper_right_diagonal_pass():
		board = [
		    ["Q", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		]

		assert Board.is_safe(board, row=1, col=2) == True


	def test_is_safe_upper_right_diagonal_fail():
		board = [
		    [".", "Q", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		    [".", ".", ".", "."],
		]

		assert Board.is_safe(board, row=1, col=0) == False

	def run_all_tests():
		for attribute_name in dir(TestNQueen):
			attribute = getattr(TestNQueen, attribute_name)
			if callable(attribute):
				try:
					attribute()
				except:
					pass
""" Tests definition - END """








""" N-Queen algorithm - START """
class Board:
	def is_safe(board, row, col):

		"""
			board: Chess board
			row: Row of the chess board
			col: Column of the chess board
		"""

		# Check for column. Meaning keep the column constant, and row changing.
		for i in range(row, -1, -1):
			if board[i][col] == "Q":
				return False

		# Upper-left diagonal
		for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
			if board[i][j] == "Q":
				return False

		# Upper-right diagonal
		for i,j in zip(range(row, -1, -1), range(col, len(board))):
			if board[i][j] == "Q":
				return False

		# At this point, it is safe to place the queen in the specified cell.
		return True


	# Recursive function
	def solve_nqueen(board, row):

		"""
			board: Chess board
			row: Row of the chess board
		"""

		# If row becomes equal to the size of the board (in any dimension),
		# that means all queens have been placed safely.
		# Solution has been found.
		if row == len(board):
			return True


		# This runs recursively.
		# Meaning, column will start from the beginning for each row.
		for col in range(len(board)):
			# If it is safe to place a Queen in the cell, place it.
			# Otherwise, continue to check for the next column in the next iteration.
			if Board.is_safe(board, row, col):
				board[row][col] = "Q"

				# Recursively call the function passing the next row.
				# If it returns True for all the rows, then solution has been found.
				if Board.solve_nqueen(board, row+1):
					return True

				# Otherwise, lift the queen.
				# Trace back and check from the next column.
				else:
					board[row][col] = "."

		return False

""" N-Queen algorithm -	END """






#Test runs
TestNQueen.run_all_tests()






#Actual run
def main():
	try:
		N = int(input("Enter size of the N-Queen problem: "))
		assert N > 0
	except ValueError:
		print("Enter an integer genius")
		print()
		main()
		return
	except AssertionError:
		print("Not the size of your brain bruh")
		print()
		main()
		return

	board = [["."] * N for _ in range(N)]

	if not Board.solve_nqueen(board, row=0):
		print(f"No solution for {N}-queen problem.")
	else:
		print(f"{N}-Queen Problem Solution:")
		print("".join(["|"] + ["-"] * len(board) * 3 + ["|"]))
		for row in board:
			print("|", end="")
			for val in row:
				print(f" {val} ", end="")
			print("|")
		print("".join(["|"] + ["-"] * len(board) * 3 + ["|"]))

if __name__ == "__main__":
	main()
