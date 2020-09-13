array = [int(i) for i in input().split()]
squares = set()
for i in range(len(array)):
    squares.add(array[i]**2)
result = list(squares).sort()
for i in squares:
    print(i, end = ' ')