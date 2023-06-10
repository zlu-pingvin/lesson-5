# a, b = int(input()), int(input())
# q = a + b  # +
# w = a - b  # -
# e = a * b  # *
# r = a / b  # /
# t = a // b  # //
# y = a % b  # %
# u = (a ** 10 + b ** 10) ** 0.5
# print(q, w, e, r, t, y, u, sep='\n')

# v, z = float(input()), float(input())
# n = v / (z * z)
# if n < 18.5:
#     print('Недостаточная масса')
# elif n > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

# s = len(input()) * 60
# r = s // 100
# k = s % 100
# print(f"{r} р. {k} коп.")

# s = input().split()
# print(len(s))

# year = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# x = int(input()) % 12
# print(year[x])
#
# y = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
# x = int(input()) % 12
# print(y[x - 8])

# s = input()
# if len(s) == 5:
#     print(int(s[::-1]))
# else:
#     print(s[0] + s[:0:-1])
#
# 1 000 000 000 000 000
# 1 5 9 13 17 21 25

# def mln(n):
#     s = []
#     x = 0
#     if len(n) < 4:
#         return n
#     elif len(n) == 4:
#         for i in n:
#             s.append(i)
#             if len(s) == 1:
#                 s.append(',')
#         return s
#     elif len(n) == 5:
#         for i in n:
#             s.append(i)
#             if len(s) == 2:
#                 s.append(',')
#         return s
#     elif len(n) > 5:
#         n = reversed(n)
#         for i in n:
#             s.append(i)
#             x += 1
#             if x % 3 == 0:
#                 s.append(',')
#         return reversed(s)
#
#
# n = input()
# o = mln(n)
# o = ''.join(o)
# # o.replace(' ', '')
# if o[0] == ',':
#     print(o[1:])
# else:
#     print(o)

# l = ['1', '2', '3', '4', '5']
# l = ''.join(l)
# print(l)

# 92
# # 64
# print(2 ** 6)
# # 28
# print(2 ** 4)
# # 16
#
# print(2 ** 3)  # 8
# 6 + 4 + 3

# 44
print(2 ** 5)
# 12
print(2 ** 3)
# 8
print(2 ** 2)

