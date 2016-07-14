'''Solve Euler Problem 7, finding the 10 001st prime number'''

# Approach 1: run a prime checker against numbers from 1 onwards and
# keep count until the 10 001st is found. The only question is how to 
# efficiently check for primes.
# Divide by 2, 3, NOT 4, 5, NOT 6, 7 etc

def is_prime(test_num):
    '''Test a number for primality.
    
    v3, test divisible by 2 or 3 then 6k+/-1'''
    if test_num == 1: return False
    if test_num in (2, 3): return True
    if not (test_num % 2 and test_num % 3):
        return False
    return True


def prime_generator(n):
    '''Generate the nth prime number
    
    v1, tests all numbers for primality'''
    prime_no = n
    prime_count = 0
    test_number = 0
    while prime_count < prime_no:
        test_number += 1
        if is_prime(test_number):
            prime_count += 1
    print(test_number)

def main():
    prime_generator(1)
    prime_generator(10001)

if __name__ == "__main__":
    main()
        
        
