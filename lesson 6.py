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

# def per(a, b, c):
#     return a + b + c

# a, b, c = map(int, input().split())
# print(per(a, b, c = map(int, input().split())))


# def per(x, y, z):
#     return x + y + z
#
# def s(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# a, b, c = map(int, input().split())
# e, f, d = map(int, input().split())
# first = per(a, b, c) + per(e, f, d)
# second = s(a, b, c) + s(e, f, d)
# print(first)
# print(second)

# def per(x, y, z):
#     return x + y + z
#
# def s(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
#
# a, b, c = map(int, input().split())
# d, e, f = map(int, input().split())
#
# first = per(a, b, c) + per(d, e, f)
# second = s(a, b, c) + s(d, e, f)
#
# print(first)
# print(second)

# def s():
#     for i in range(100, 1000):
#         i = str(i)
#         a = str(i[0])
#         b = str(i[1])
#         c = str(i[2])
#         if int(a) + int(b) + int(c) == 10:
#             print(i)
#
#
# s()

# def summ(a, b):
#     x = int(a[0]) + int(a[1])
#     y = int(b[0]) + int(b[1])
#     if x > y:
#         print('в первом числе сумма цифр больше')
#     elif x < y:
#         print('во втором числе сумма цифр больше')
#     else:
#         print('сумма цифр в числах одинакова')
#
# a, b = input().split()
# summ(a, b)


# def sh(n, m):
#     count = 0
#     for i in range(n, m + 1):
#         i = str(i)
#         a, b, c = str(i[0]), str(i[1]), str(i[2])
#         x, y, z = str(i[3]), str(i[4]), str(i[5])
#         if int(a) + int(b) + int(c) == int(x) + int(y) + int(z):
#             count += 1
#     print(count)
#
# n, m = map(int, input().split())
# sh(n, m)

# def cnt():
#     s = int(input())
#     n = 1
#     count = 0
#     while s < 60:
#         s = s + 5
#         n = n * 3
#         count += 1
#         if n == 243:
#             return count
#
#
# print(60 - cnt() * 5)

# s1 = 1
# while True:
#     s = s1
#     n = 1
#     while s <= 60:
#         s = s + 5
#         n = n * 3
#     if n == 243:
#         print(s1)
#         break
#     s1 += 1

# def func(s):
#     n = 1
#     while s < 60:
#         s = s + 5
#         n = n * 3
#     return n
#
#
# x = 0
# while True:
#     x += 1
#     if func(x) == 243:
#         print(x)
#         break

# def func(d):
#     n = 24
#     s = 12
#     while s <= 3004:
#         s = s + d
#         n = n + 3
#     return n
#
#
# x = 0
# while True:
#     x += 1
#     if func(x) == 75:
#         print(x)
#         break

# def func(d):
#     n = 24
#     s = 12
#     while s <= 3004:
#         s = s + d
#         n = n + 3
#     return n
#
# x = 3004
# m = 0
# while True:
#     x -= 1
#     if func(x) == 75:
#         print(x)
#         break

# def func(d):
#     n = 8
#     s = 6
#     while s <= 1800:
#         s = s + d
#         n = n + 7
#     return n
#
#
# x = 0
# count = 0
# while x <= 1800:
#     x += 1
#     if func(x) == 57:
#         count += 1
# print(count)

# def func(x):
#     L = 0
#     M = 1
#     while x > 0:
#         L = L + 1
#         M = M * (x % 8)
#         x = x // 8
#     return L, M
#
#
# x = 0
# for i in range(1, 1000000):
#     L, M = func(i)
#     if L == 3 and M == 120:
#         x = i
# print(x)

# x = int(input())
# def func(x):
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 2
#         if c == 0:
#             a = a + 1
#         else:
#             b = b + 1
#         x = x // 10
#     return a, b
#
#
# x = 0
# for i in range(1, 111111111):
#     a, b = func(i)
#     if a == 3 and b == 2:
#         print(i)
#         break

# https://stepik.org/lesson/421033/step/8?unit=410643

# def func(x):
#     a = 0
#     b = 0
#     while x > 0:
#         y = x % 10
#         if y > 3:
#             a = a+1
#         if y < 8:
#             b = b+1
#         x = x // 10
#     return a, b
#
#
# for x in range(100000):
#     if func(x) == (4, 2) and len(str(x)) == 5:
#         print(x)
#         break

# def func(x):
#     L = 2*x-30
#     M = 2*x+30
#     while L != M:
#         if L > M:
#             L = L - M
#         else:
#             M = M - L
#     return M
#
#
# for x in range(1000, 1000000):
#     if func(x) == 30:
#         print(x)
#         break

# def func(x):
#     S = 5
#     while x > 0:
#         if x % 8 > 4:
#             S = S + (x % 8)
#         else:
#             S = S * (x % 8)
#         x = x // 8
#     return S
#
#
# min = 100000
# for x in range(100, 1000):
#     # n = func(x)
#     if func(x) > 99 and func(x) % 100 == 0:
#         if min > x:
#             min = x
# print(min)

# def func(x):
#     a = 0
#     b = 1
#     while x > 0:
#         a = a + 1
#         if x % 12 != 0:
#             b = b * (x % 12)
#         x = x // 12
#     return a, b
#
#
# count = 0
# for x in range(100):
#     if func(x) == (2, 12):
#         count += 1
# print(count)

# def faktorial(x):
#     if x > 1:
#         f = x * faktorial(x - 1)
#     else:
#         f = 1
#     return f
#
#
# print(faktorial(1))
# print(faktorial(5))
# print(faktorial(6))

# def faktorial(x):
#     if x > 1:
#         f = x * faktorial(x - 1)
#     else:
#         f = 1
#     return f
#
# x = 1
# for i in range(1, 11):
#     print(faktorial(x))
#     x += 1



# def f(x):
#     if x == 1 or x == 2:
#         return 3
#     elif x > 2:
#         return 5 * f(x - 1) - 2 * f(x - 2)
#
# x = int(input())
# print(f(x))

# def f(x):
# #     if x <= 0:
# #         return 0
# #     else:
# #         return x ** 2 + g(x - 1)
# #
# #
# # def g(x):
# #     if x <= 0:
# #         return 1
# #     else:
# #         return x + f(x - 1)
# #
# #
# # print(f(10) + g(10))

# def f(x):
#     if x in (1, 2):
#         return 1
#     return f(x - 1) + f(x - 2)
#
#
# x = int(input())
# print(f(x))

# def f(n):
#     i = 1
#     while i < n:
#         i *= 2
#     if i == n:
#         return 'YES'
#     else:
#         return 'NO'
#
#
# n = int(input())
# print(f(n))

# def f(x):
#     if x == 0:
#         return False
#     else:
#
#         # x = int(input())
#         print(x)
#         x = int(input())
#         f(x)
#         return f(x)


# x = int(input())
# print(f(x))

# def f():
#     n = int(input())
#     if not n:
#         return
#     f()
#     print(n)
#
#
# f()

# def f():
#     n = int(input())
#     if n == 0:
#         return False
#     f()
#     print(n)
# f()

# n = 123
# s = 0
# for i in range(3):
#     s += n % 10
#     n = n // 10
# print(s)

# def f(x):
#     n = 0
#     while x > 0:
#         n += x % 10
#         x = x // 10
#         f(x)
#     return n
#
#
# x = int(input())
# print(f(x))

# def f(n):
#     if n > 0:
#         f(n - 1)
#     print(n)
#
# n = int(input())
# f(n)

# def Rec(a):
#     if a > 0:
#         Rec(a-1)
#     print(a, end="")
#
#
# a = int(input())
# Rec(a)

# def LoopImitation(i, n):
#     print("Hello N", i)
#     if i < n:
#         LoopImitation(i + 1, n)
#
#
# LoopImitation(1, 10)

# def TumbaWords(word, alphabet, n):
#     if n < 1:
#         print(word)
#         return
#     for c in alphabet:
#         TumbaWords(word+c, alphabet, n - 1)
#
#
# n = int(input())
# TumbaWords("", "KLMN", n)

# def f(x):
#     x = x // 10 + x % 10
#     if x > 9:
#         f(x)
#     if x < 10:
#         print(x)
#
#
# x = int(input())
# f(x)

# def f(n):
#     b = ''
#     b = str(n % 2) + b
#     n = n // 2
#     if n > 0:
#         f(n)
#     print(b, end='')
#
# n = int(input())
# f(n)

# def F(x, y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     return F(x+2, y)+F(x*5, y)
# print(F(2, 50))