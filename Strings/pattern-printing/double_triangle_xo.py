pattern = 'x o '
def printing_awessome(n):
    print_upper(n)
    print_core(n)
    print_lower(n)

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
    for i in range(n-1, -1, -1):
        print(' '*(n-i-1) + "".join([pattern[j%4] for j in range(i)]))

if __name__ == '__main__':
    ns = [7, 2, 5, 6, 1, 8, 15]
    for n in ns:
        print("n = ", n)
        print_upper(n)
        print_core(n)
        print_bottom(n)