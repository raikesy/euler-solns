"""Project Euler Problem 3"""


def largest_prime_factor(starting_number=600851475143):
    """Find the largest prime factor of 600851475143"""
    test_number = starting_number
    test_factor = 2
    while test_number > test_factor:
        if test_number % test_factor == 0:
            test_number = int(test_number / test_factor)
            test_factor = 2
        else:
            test_factor += 1
    largest_factor = test_factor
    print("Largest Prime Factor: {:d}".format(largest_factor))


def main():
    """Runs largest_prime_factor"""
    largest_prime_factor()
    return 0

if __name__ == '__main__':
    main()
