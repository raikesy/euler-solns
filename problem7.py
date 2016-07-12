'''Solve Euler Problem 7, finding the 10 001st prime number'''

# Approach 1: run a prime checker against numbers from 1 onwards and
# keep count until the 10 001st is found. The only question is how to 
# efficiently check for primes.
# Divide by 2, 3, NOT 4, 5, NOT 6, 7 etc

def is_prime(n):
    '''v2, only test odd numbers up to root(n) inclusive'''
    divisors = [2]
    divisors.extend(list(range(3, int(n ** 0.5) + 1, 2)))
    for i in divisors:
        if not n % i:
            return False
    return True


def main():
    '''v1, tests all numbers for primality'''
    prime_no = 10001
    prime_count = 0
    test_number = 0
    while prime_count < prime_no:
        test_number += 1
        if is_prime(test_number):
            prime_count += 1
    print(test_number)

if __name__ == "__main__":
    main()
        
        
