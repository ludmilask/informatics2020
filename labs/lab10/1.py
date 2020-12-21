import multiprocessing
import argparse


def factorize(n):
    div = 2
    divs = []
    while (n != 1):
        while (n % div == 0):
            n //= div
            divs.append(div)
        div += 1
    return divs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs='*')
    numbers = vars(parser.parse_args())['n']

    pool = multiprocessing.Pool()
    divisors_of_each = pool.map(factorize, numbers)
    pool.close()

    for number, divisors in zip(numbers, divisors_of_each):
        print(number, ":", *divisors, sep=" ")
