'''Solve Euler Problem 7, finding the 10 001st prime number'''

# Approach 1: run a prime checker against numbers from 1 onwards and
# keep count until the 10 001st is found. The only question is how to 
# efficiently check for primes.
# Divide by 2, 3, NOT 4, 5, NOT 6, 7 etc

def is_prime(test_value):
    '''v1, pure brute force'''
    for i in range(2,test_value):
        if test_value % i == 0:
            return False
    return True


def main():
    prime_no = 10
    prime_count = 0
    test_number = 1
    while prime_count < prime_no:
        if is_prime(test_number):
            prime_count += 1
        test_number += 1
    print(test_number)

if __name__ == "__main__":
    main()
        
        
