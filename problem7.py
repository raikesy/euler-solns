'''Solve Euler Problem 7, finding the 10 001st prime number'''

def is_prime(test_num):
    '''Test a number for primality.

    v3, test divisible by 2 or 3 then 6k+/-1'''
    if test_num == 1:
        return False
    if test_num in (2, 3):
        return True
    if not (test_num % 2 and test_num % 3):
        return False
    k = 1
    divisor = 6 * k - 1
    while divisor <= test_num ** 0.5:
        if not (test_num % divisor and test_num % (divisor + 2)):
            return False
        k += 1
        divisor = 6 * k - 1
    return True


def prime_generator(nth):
    '''Generate the nth prime number

    v2, only tests 6k+/-1'''
    first_two = 2, 3
    if nth < 3:
        return first_two[nth - 1]

    prime_count = 2
    k = 1
    pos_min = -1
    while prime_count < nth:
        test_num = 6 * k + pos_min
        if is_prime(test_num):
            prime_count += 1
        pos_min *= -1
        if pos_min < 0:
            k += 1
    return test_num


def main():
    print(prime_generator(10001))


if __name__ == "__main__":
    main()
