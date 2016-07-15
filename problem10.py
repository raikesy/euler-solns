'''Project Euler Problem 10

Find the sum of every prime under 2 million'''
import problem7 as p7

def prime_sum(upper):
    i = 1
    p_sum = 0
    current_prime = 0
    while True:
        current_prime = p7.prime_generator(i)
        if current_prime >= upper:
            break
        p_sum += current_prime
        i += 1
    return p_sum


def main():
    print(prime_sum(10000))


if __name__ == "__main__":
    main()
