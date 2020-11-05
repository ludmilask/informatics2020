array = [float(i) for i in input().split()]
squares = set()
for i in array:
    squares.add(i**2)
result = sorted(list(squares))
for i in result:
    print(i, end = ' ')