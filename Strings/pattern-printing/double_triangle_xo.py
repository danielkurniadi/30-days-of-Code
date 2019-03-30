pattern = 'x o '
def printing_awessome(n):
	print_upper(n)
	print_core(n)
	print_bottom(n)

def print_upper(n):
	for i in range(n-1):
		print(' '*(n-1) + "".join([pattern[j%4] for j in range(i, -1, -1)]))

def print_core(n):
	if n==1:
		print('x')
		return
	print("".join([pattern[j%4] for j in range(n)]), end='')
	print("".join([pattern[j%4] for j in range(n-2, -1, -1)]))

def print_bottom(n):
	for i in range(n-1, 0, -1):
		print(' '*(n-i) + "".join([pattern[j%4] for j in range(i)]))

if __name__ == '__main__':
	n = int(input().strip())
	printing_awessome(n)
	