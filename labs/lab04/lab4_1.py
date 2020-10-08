def author(_author):
    def wrapper(function):
        function._author = _author
        return function
    return wrapper

@author("Captain Friedrich Von Schoenvorts")
def add2(num: int) -> int:
    return num + 2

print(add2._author)
