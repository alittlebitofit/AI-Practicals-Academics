# 2b Write a program to solve tower of Hanoi problem.

# For n == 1
# - Move from source to target

# For n > 1
# - Move n-1 from source to auxiliary
# - Then move nth from source to target
# - Then move n-1 from auxiliary to target


# Time Complexity
# The time complexity of the Tower of Hanoi problem can be analyzed based on the number of moves required to solve the puzzle.

# For n disks, the recurrence relation for the number of moves 
# T(n) can be expressed as:
# T(n) = 2*T(n−1)+1

# This relation indicates that to move n disks, we need to:

# Move n-1 disks.
# Move one disk (the largest one).
# Move n-1 disks again.

# By expanding this recurrence relation, we get:
# T(n)=2(2T(n−2)+1)+1
# T(n)=4T(n−2)+2+1
# T(n)=4(2T(n−3)+1)+2+1
# T(n)=8T(n−3)+4+2+1

# Continuing this expansion, we can generalize:

# T(n)=2^k*T(n−k) + 2^(k−1) + 2^(k−2) + ... + 2 + 1

# When 𝑘=𝑛:

# 𝑇(𝑛)=2^𝑛 * T(n-n) + 2^(n-1) + 2^(n-1) + ... + 2 + 1
# 𝑇(n)=2^n T(0) + 2^(𝑛−1) + 2^(𝑛−2) + ... + 2 + 1

# Since 𝑇(0)=0:

# T(n)=2^n −1

# Therefore, the time complexity of the Tower of Hanoi algorithm is 
# O(2^n).

# Space Complexity
# The space complexity of the Tower of Hanoi algorithm is determined by the maximum depth of the recursion stack.

# In each recursive call, we make two recursive calls with 
# n−1 disks. The depth of the recursion stack is therefore n (one for each disk).

# Thus, the space complexity of the Tower of Hanoi algorithm is O(n).

# Summary
# Time Complexity: 𝑂(2^𝑛)
# Space Complexity: 𝑂(𝑛)
# These complexities reflect the exponential nature of the problem,
# where the number of moves grows exponentially with the number of disks, while the space required is linear in the number of disks.

def toh(n, source, target, auxiliary):
	if n > 0:
		toh(n-1, source, auxiliary, target)
		print(f'Move disk {n} from {source} to {target}')
		toh(n-1, auxiliary, target, source)

toh(
	n=4,
	source='A',
	target='C',
	auxiliary='B',
)