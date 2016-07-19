"""Project Euler Problem 2

Return the sum of the even valued terms of the Fibonacci sequences
below four million"""


def fib_sum(u_l):
    """Merges the two loops into one"""

    fib_seq = [1, 1]
    term = 0
    total = 0
    while term <= u_l:
        term = fib_seq[-1] + fib_seq[-2]
        if term <= u_l:
            fib_seq.append(term)
        if term % 2 == 0:
            total += term
    return total
    

def main():
    """Run desired function"""
    print(fib_sum(4e6))

if __name__ == '__main__':
    main()
