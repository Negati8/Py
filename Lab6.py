import math

class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель  ноль")

        gcd_val = math.gcd(abs(numerator), abs(denominator))
        
        sign = -1 if (numerator * denominator) < 0 else 1
        
        self.num = sign * (abs(numerator) // gcd_val)
        self.den = abs(denominator) // gcd_val

    def __str__(self) -> str:
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"


    def __add__(self, other):
  
        if isinstance(other, int):
            other = Fraction(other)
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if other.num == 0:
            raise ZeroDivisionError("Деление на ноль")
        return Fraction(self.num * other.den, self.den * other.num)
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den < other.num * self.den
    
    def __le__(self, other):
        return self == other or self < other
        
    def __gt__(self, other):
        return not self <= other
        
    def __ge__(self, other):
        return not self < other

    
    def __float__(self):
        return self.num / self.den


f1 = Fraction(4, 8)  
f2 = Fraction(2, 9)

print(f"Дробь 1: {f1}")
print(f"Дробь 2: {f2}")
print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
print(f"{f1} * {f2} = {f1 * f2}")
print(f"{f1} / {f2} = {f1 / f2}")
print(f" {f1} + 2 = {f1 + 2}")
print(f"{f1} > {f2}? {f1 > f2}") 
print(f"({f1}) = {float(f1)}")


try:
    f_zero = Fraction(1, 0)
except ZeroDivisionError as e:
    print(f"\nОшибка: {e}")