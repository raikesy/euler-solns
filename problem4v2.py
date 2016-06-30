def main():
    max_pal = 0
    for i in range(100, 999):
        for j in range(i, 999):
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                max_pal = max(max_pal, prod)
    # print(max_pal)


if __name__ == "__main__":
    import timeit
    print(timeit.timeit(main, number=10))
