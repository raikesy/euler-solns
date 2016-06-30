"""Solve Project Euler problem 4.

Find the largest palindromic number made from the product of two 3-digit
numbers. (913*993 not 924*962 or 995*583)

Times:
    v1.0, gen all products, check all products, select biggest = 7.8 seconds
    v1.1, merge factor and product lists into a list of tuples = 7.4 seconds
    v2.0 gen all products, sort by size, select first          = 3.1 seconds

    """


def number_gen(digits=3):
    """Generate the product of every combination of 2 x-digit numbers."""
    factor_lb = 10 ** (digits - 1)
    factor_ub = 10 ** digits - 1
    factor_pool = range(factor_ub, factor_lb - 1, -1)

    pp_list = []
    for i in factor_pool:
        for j in range(factor_ub, i - 1, -1):
            pp_list.append((i, j, i * j))

    return pp_list

    # def combinations_with_replacement(iterable, r):
    #     # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    #     pool = tuple(iterable)
    #     n = len(pool)
    #     if not n and r:
    #         return
    #     indices = [0] * r
    #     yield tuple(pool[i] for i in indices)
    #     while True:
    #         for i in reversed(range(r)):
    #             if indices[i] != n - 1:
    #                 break
    #         else:
    #             return
    #         indices[i:] = [indices[i] + 1] * (r - i)
    #         yield tuple(pool[i] for i in indices)


def palindrome_checker(test_value):
    """Check to see if a number is a palindrome."""
    num_string = str(test_value)
    num_length = len(num_string)
    half_length = int(num_length / 2)
    first_half = num_string[:half_length]
    second_half = num_string[:-(half_length + 1):-1]

    return first_half == second_half


def main(print_flag=False):
    """Solve problem."""
    full_list = number_gen()
    full_list.sort(key=lambda full_tuple: full_tuple[2], reverse=True)

    for full_tuple in full_list:
        if palindrome_checker(full_tuple[2]):
            answer = full_tuple[2]
            factors = full_tuple[:2]
            break

    # result_list = []
    # for full_tuple in full_list:
    #     result_list.append(palindrome_checker(full_tuple[2]))

    # pal_list = []
    # for i, result in enumerate(result_list):
    #     if result:
    #         pal_list.extend(full_list[i])

    # answer = max(pal_list[2::3])
    # index = pal_list.index(answer)
    # factors = pal_list[index - 2:index]

    if print_flag:
        print("{} which is the product of {}".format(answer, factors))
    else:
        return answer


if __name__ == '__main__':
    import timeit
    # print(timeit.timeit(main, number=10))
    # main(True)
    print(timeit.timeit("combinations_with_replacement(i,r)", "import itertools" number=10))
