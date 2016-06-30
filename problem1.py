""" Return the sum of all multiples of 3 or 5 below 1000 """


def multiples(upper_limit=1000):
    """Uses a conditional loop"""
    result = 0
    for i in range(upper_limit):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


def multiples2(upper_limit=1000):
    """Uses the sum and range functions with custom step sizes

    Multiples of 15 will be counted twice so are subtracted from the
    total"""
    sum3 = sum(range(0, upper_limit, 3))
    sum5 = sum(range(0, upper_limit, 5))
    sum15 = sum(range(0, upper_limit, 15))
    result = sum3 + sum5 - sum15
    return result


def multiples3(upper_limit=999):
    """Uses mathematical formulae for arithmetic series"""

    # S_n = n/2*(a_1 + a_n)
    # a_n is the last term, which we don't immediately know
    # nth term given by a_n = a_1 + (n - 1)*d
    # So n = int((l - a_1)/d + 1) where l is the upper limit
    # In our case a_1 == d
    # So n = int(l/d)
    # a_n = d + (int(l/d)-1)*d = d*int(l/d)
    # So S_n = int(l/d)/2*(d + d*int(l/d))
    # Simplified: d*int(l/d)*(1+int(l/d))/2

    def arith_sum(d, l):
        S = d * int(l / d) * (1 + int(l / d)) / 2
        return S

    sum3 = arith_sum(3, upper_limit)
    sum5 = arith_sum(5, upper_limit)
    sum15 = arith_sum(15, upper_limit)
    result = sum3 + sum5 - sum15
    return result


def multiples4(l=999):
    """Fully simplified version of multiples3"""
    T = (3 * int(l / 3) * (1 + int(l / 3)) / 2 + 5 * int(l / 5) *
         (1 + int(l / 5)) / 2 - 15 * int(l / 15) * (1 + int(l / 15)) / 2)
    return T


def main():
    """Run desired function"""
    import timeit
    print(timeit.timeit(multiples4, number=10000))
    print(multiples4())

if __name__ == '__main__':
    main()
