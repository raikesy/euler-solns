def sum_of_sq(upper):
    return sum([x ** 2 for x in range(upper + 1)])


def sq_of_sum(upper):
    return sum(range(upper+1)) ** 2


def main():
    top = 100
    print(sq_of_sum(top)-sum_of_sq(top))

if __name__ == '__main__':
    main()
