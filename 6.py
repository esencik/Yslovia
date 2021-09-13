(a, b) = eval(input('Введите значения a и b через запятую: '))
c = a // b
c = ((c + 2) // (c + 1)) % 2
d = (c + 1) % 2
res = a * c + b * d
print(res)