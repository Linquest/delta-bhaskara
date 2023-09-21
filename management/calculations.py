import math


def delta(a, b, c):
    return b**2 - 4*a*c


def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return 'Delta Negativo'
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f'x1={x1:.2f}, x2={x2:.2f}'


print(bhaskara(7, 3, 4))
print(bhaskara(1, 5, 2))
print(bhaskara(3, 10, 2))
