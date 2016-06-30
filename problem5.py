'''Find the smallest positive number that is evenly divisible by every 
number between 1 and 20'''


def main(upper):
    # Generate a list to test against that skips factors of already
    # tested numbers
    # full_list = list(range(upper, step=-1))



    test_value = upper
    flag = True
    while flag:
        for divisor in range(upper, 1, -1):
            if test_value % divisor != 0:
                break
        else:
            flag = False
            answer = test_value
        if test_value % 1000000 == 0:
            print('Current test: ', test_value)
        test_value += upper
    print(answer)

if __name__=="__main__":
    main(20)

# Someone else's much more efficient solution
# i = 1                           # i starts at one and eventually becomes answer
# for k in (range(1, 21)):        # k goes from 1 to 20
#     if i % k > 0:               # tests if i goes into 1-20
#         for j in range(1, 21):  # as soon as a non-factor is found
#             if (i*j) % k == 0:  # multiply by the lowest number to make it a factor
#                 i *= j          # continue checking the next numbers
#                 break
# print(i)