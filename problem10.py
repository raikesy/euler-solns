'''Project Euler Problem 10

Find the sum of every prime under 2 million
v2, use a basic sieve of Eratosthenes'''

def sieve(upper):
    '''Return every prime below a given value'''
    prime_list = []
    int_list = list(range(2,upper))
    while int_list:
        prime_list.append(int_list[0])
        int_list = [x for x in int_list if x % prime_list[-1]]
    return prime_list

def sieve2(upper):
    '''Version of sieve that follows Wikipedia's pseudocode

    Avoids using list comprehension which is apparently quite slow
    Further optimisation may be possible using numpy arrays'''
    A = [True] * (upper - 2)    # Don't need bool for 1 or upper'
    for i in range(2, int(upper ** 0.5) + 1):
        if A[i - 2]:
            for j in range(i ** 2, upper, i):
                A[j - 2] = False
    return [x + 2 for x in range(len(A)) if A[x]]

def main():
    print(sum(sieve2(2000000)))


if __name__ == "__main__":
    main()
