'''Project Euler Problem 12

Find the first triangular number with 500 divisors'''
def triangular_generator(nth):
    '''Return the nth triangular number'''
    t = 0
    for i in range(nth):
        t += i + 1
    return t


def divisor_count(product):
    '''Return the number of divisors of a number
    
    Includes 1 and itself'''
    count = 0
    for i in range(int(product ** 0.5)):
        if not product % (i + 1):
            count += 2
    return count


def main():
    i = 0
    divisors_needed = 500
    while divisor_count(triangular_generator(i)) <= divisors_needed:
        i += 1
    print(triangular_generator(i))


if __name__ == "__main__":
    main()
