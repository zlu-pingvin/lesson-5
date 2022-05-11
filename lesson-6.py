# def lines():
#     print('*' * 20)
#
#
# lines()

# def lines(n):
#     return ('*' * n)
#
#
# for i in range(3):
#     n = int(input())
#     print(lines(n))

# def y(x):
#     return ((5 * x ** 4) + (3 * x ** 3) + (x ** 2) + (4 * x) - 4)
#
#
# x = 4
# print(y(x))
# x = 5
# print(y(x))
# x = 10
# print(y(x))

# def f(x):
#     if x > 0:
#         return 0
#     elif x < 0:
#         return x ** 2
#
#
# print(f(x = int(input())))

# def line(x):
#     """ процедура line(x) рисует горизонтальную линию звездочек длины х"""
#     print(x * "*")
#
#
# def resta(a, b):
#     """ процедура resta(a, b) рисует прямоугольник с помощью символа *
#     размерами а на b """
#     line(b)
#     for i in range(a - 2):
#         print("*"+" "*(b - 2) + "*")
#     line(b)
#
#
# x, y = map(int, input().split())
# resta(x, y)

# def dlina(x1, y1, x2, y2):
#     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#
#
# def dlina(x2, y2, x3, y3):
#     return ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
#
#
# def dlina(x1, y1, x3, y3):
#     return ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
#
#
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
#
# a = dlina(x1, y1, x2, y2)
# b = dlina(x2, y2, x3, y3)
# c = dlina(x1, y1, x3, y3)
#
# def s(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
#
# print(s(a, b, c))

# def per(a1, b1, c1):
#     return a1 + b1 + c1
#
# def per(a2, b2, c2):
#     return a2 + b2 + c2
#
#
# a1, b1, c1 = map(int, input().split())
# a2, b2, c2 = map(int, input().split())
#
# first_p = per(a1, b1, c1)
# second_p = per(a2, b2, c2)

def per(a, b, c):
    return a + b + c

# a, b, c = map(int, input().split())
print(per(a, b, c = map(int, input().split())))




