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



def main():
    print(sum(sieve(60000)))


if __name__ == "__main__":
    main()
