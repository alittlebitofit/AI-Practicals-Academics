# 2b Write a program to solve tower of Hanoi problem.

# For n == 1
# - Move from source to target

# For n > 1
# - Move n-1 from source to auxiliary
# - Then move nth from source to target
# - Then move n-1 from auxiliary to target

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