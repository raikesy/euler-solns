"""Returns the sum of the even valued terms of the Fibonacci sequences
below four million"""


def fib_sum1(u_l=4e6):
    """Basic solution using conditions and loops"""

    # Generate Fibonacci sequence
    fib_seq = [1, 1]
    term = 0
    while term <= u_l:
        term = fib_seq[-1] + fib_seq[-2]
        if term <= u_l:
            fib_seq.append(term)
    print(fib_seq)

    # Sum up even values
    total = 0
    for value in fib_seq:
        if value % 2 == 0:
            total += value
    return total


def fib_sum2(u_l=4e6):
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
    # print(fib_seq)
    return total


def main():
    """Run desired function"""
    print(fib_sum1())

if __name__ == '__main__':
    main()
