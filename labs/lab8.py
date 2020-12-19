class ConsoleIterator:
    def __init__(self):
        self.numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if len(self.numbers) == 0:

                try:
                    split_string = input().split()
                except EOFError:
                    raise StopIteration

                for token in split_string:
                    try:
                        number = int(token)
                    except ValueError:
                        raise StopIteration
                    self.numbers.append(number)

            elif len(self.numbers) != 0:
                return self.numbers.pop(0)


if __name__ == "__main__":
    total_sum = 0

    for number in ConsoleIterator():
        total_sum = total_sum + number

    print(f'Sum of entered numbers is {total_sum}')
