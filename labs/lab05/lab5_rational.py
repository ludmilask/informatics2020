# Поиск наибольшего общего делителя алгоритмом Евклида
def gcd(a, b):
    while a > 0 and b > 0:
        if a > b: 
            a = a % b
        else:
            b = b % a
    return a + b

class Rational:
    nom: int
    denom: int

    def __init__(
        self,
        nom,
        denom,
    ) -> None:
        if denom == 0:
            raise Exception('zero in denom')
        self.nom = nom
        self.denom = denom
        self.reduce()
    
    def reduce(self):
        if self.denom < 0:
            self.nom *= -1
            self.denom *= -1
        gcd_nom_denom = gcd(
            self.nom if self.nom > 0 else -self.nom,
            self.denom
        )
        self.nom = self.nom // gcd_nom_denom
        self.denom = self.denom // gcd_nom_denom

    @classmethod
    def from_str(cls, arg):
        negative = (arg[0] == '-')
        if negative:
            nom, denom = arg[1:].split('/')
        else:
            nom, denom = arg.split('/')
        
        return cls(nom=-int(nom) if negative else int(nom), denom=int(denom))

    def to_float(self):
        return float(self.nom) / float(self.denom)
    
    def __add__(self, second):
        res = Rational(nom = self.nom*second.denom + self.denom*second.nom, denom = self.denom*second.denom)
        res.reduce()
        return res
    
    def __sub__(self, second):
        res = Rational(nom = self.nom*second.denom - self.denom*second.nom, denom = self.denom*second.denom)
        res.reduce()
        return res
        
    def __mul__(self, second):
        res = Rational(nom = self.nom*second.nom, denom = self.denom*second.denom)
        res.reduce()
        return res
        
    def __truediv__(self, second):
        res = Rational(nom = self.nom*second.denom, denom = self.denom*second.nom)
        res.reduce()
        return res


def test_reduce():
    x = Rational(2,2)
    assert x.nom == 1
    assert x.denom == 1
    
    y = Rational(4,6)
    assert y.nom == 2
    assert y.denom == 3


def test_operations():
    x = Rational(12,73)
    y = Rational(17,6)
    
    z = x + y
    assert z.nom == 1313
    assert z.denom == 438
    
    z = x - y
    assert z.nom == -1169
    assert z.denom == 438
    
    z = x * y
    assert z.nom == 34
    assert z.denom == 73
    
    z = x / y
    assert z.nom == 72
    assert z.denom == 1241


def test_cast_to_float():
    x = Rational(1,8)
    as_float = x.to_float()
    assert as_float == 0.125

def test_parse_from_string():
    x = Rational.from_str('2/16')
    assert x.nom == 1
    assert x.denom == 8
    
    y = Rational.from_str('-2/16')
    assert y.nom == -1
    assert y.denom == 8

test_reduce()
test_operations()
test_cast_to_float()
test_parse_from_string()
