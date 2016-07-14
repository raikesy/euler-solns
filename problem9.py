'''Project Euler Problem 9

Current plan of attack is to generate all possible sets of a, b, c
which is true for a + b + c = 1000 and a < b < c, testing each one
against a^2 + b^2 = c^2
    a's lowest possible value is 1
    This means b's lowest possible value is 2
    In this case, c would be 997, which is therefore c's highest Value
    b's highest value is 499 (c = 500, a = 1)
    c's lowest value is 334 (b = 333, a = 332)
    Summary: c: 334-997, b: 2-499, a: 1-332
'''

def main():
    for a in range(334):
        for b in range(a, int((1000 - a)/2)):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a*b*c)


if __name__ == '__main__':
    main()
