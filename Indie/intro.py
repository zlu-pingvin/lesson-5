# n = int(input())
# print(n + 1)

# n = int(input())
# print(n * 2)
# print(n / 2)

# n = float(input())
# print(n ** 2)

# a, b = int(input()), int(input())
# print(a + b)

# a, b = float(input()), float(input())
# print(a * b, 2 * (a + b))

# f = float(input())
# c = ((f - 32) * 5) / 9
# print(c)

# a, b = int(input()), int(input())
# print(abs(a) + abs(b))

# b, a = float(input()), float(input())
# print(abs(a - b))

# n = float(input())
# print(round(n, 2), round(n, 3))

# h1, m1, s1 = int(input()), int(input()), int(input())
# h2, m2, s2 = int(input()), int(input()), int(input())
# m1 *= 60
# h1 *= 3600
# m2 *= 60
# h2 *= 3600
# print((h2 + m2 + s2) - (h1 + m1 + s1))

# a, b, c = int(input()), int(input()), int(input())
# print(max((a + b + c), (a * b * c), (a + b * c), (a * b + c), ((a + b) * c), (a * (b + c))))

# a, b, c, d = map(int, input().split())
# print((a + b + c + d) / 4)

# a, b, c, d, e = map(int, input().split())
# print(max(a, b, c, d, e))

# n, a, b = map(int, input().split())
# print((n * a * b) * 2)

# a = int(input())
# x = a / 3
# y = a / 3
# z = x + y
# print(int(x / 2), int(z), int(y / 2))

# x = 3
# y = x + 2
# z = y + 7
# a, b, c = map(int, input().split())
# a *= x
# b *= y
# c *= z
# print(a + b + c)

# a, b = map(int, input().split())
# c = a + b - 1
# x = c - a
# y = c - b
# print(x, y)

# a, b, c = map(int, input().split())
# print(a, b, c, sep=',')

# n = int(input())
# print(f'{n - 1}<{n}<{n + 1}')

# a, b, c = input(), input(), input()
# print(f'{a}---{b}---{c}')

# s = input()
# print(1 , 2, 3, 4, 5, sep=s)

# s = input()
# print(s, end=' - Сказала она!')

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# n, k = int(input()), int(input())
# print(k // n)

# n = int(input())
# print(n % 10)

# n = int(input())
# # print(n % 1000 // 100)

# n = int(input())
# y = 0
# for i in range(2):
#     y += n % 10
#     n = n // 10
# y += n
# print(y)

# n = int(input())
# x = n // 100
# n = n % 100
# x += n // 20
# n = n % 20
# x += n // 10
# n = n % 10
# x += n // 5
# n = n % 5
# x += n
# print(x)

# n = int(input())
# x = 0
# for i in (100, 20, 10, 5):
#     x += n // i
#     n = n % i
# print(x + n)

# n = int(input())
# h = n // 60
# if h > 24:
#     h = h % 24
# m = n % 60
# print(h, m)

# n = int(input())
# if n % 2 == 0:
#     print(n + 2)
# else:
#     print(n + 1)


# 3600
# 60

# n = int(input())
# h = n // 3600 % 24
# n = n % 3600
# m = n // 60
# n = n % 60
# print(f'{h}:{m // 10}{m % 10}:{n // 10}{n % 10}')

# n = int(input())
# n += 1
# print(n)

# n = float(input())
# n *= 1.5
# print(n)

# a = 5
# b = 7
# c = 5
# print(a == b)
# print(a != b)
# print(a == c)

# print(5 > 1 + 7)
# print(6 < -2 - 1)
# print(16 >= 1 + 2 * 3)

# for i in range(0, 11):
#     print(i)
#     print(i % 2 == 0)

# n = int(input())
# print(n > 0)

# n = int(input())
# print(n % 10 == 2)

# n, m = map(int, input().split())
# print(n % 7 == 0 and m % 7 == 0)

# a, b, c = map(int, input().split())
# print(a == b == c)

# n = int(input())
# print(5 < n < 20)

# a, b = input(), input()
# print(a == 'awesome' or b == 'awesome')

# a, b, c = map(int, input().split())
# print(a == b or a == c or b == c)

# n = int(input())
# print(9 < n < 100)

# a, b, c = map(int, input().split())
# print((a ** 2 + b ** 2) == c ** 2 or (a ** 2 + c ** 2) == b ** 2 or (b ** 2 + c ** 2) == a ** 2)

# s = sorted(map(int, input().split()))
# print(*s)

# import math
# n = int(input()) / 10
# n = math.ceil(n)
# print(n)

# import math
# print(math.ceil(int(input())/10))

# import math
# n = int(input())
# print(math.ceil(n / 4))

# import math
# a, b, c = int(input()), int(input()), int(input())
# a = math.ceil(a / 2)
# b = math.ceil(b / 2)
# c = math.ceil(c / 2)
# print(a + b + c)

# import math
# l, w, h = map(int, input().split())
# d = l * h * 2
# k = w * h * 2
# print(math.ceil((d + k) / 16))

