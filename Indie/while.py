# k = 10
# z = 0
# while k <= 14:
#     z = z + k
#     k += 1
# print(z)

# n = 1000
# while n < 2001:
#     print(n)
#     n += 1

# n = 6785
# while n >  194:
#     if n % 5 == 0:
#         print(n)
#     n -= 5

# a, b = map(int, input().split())
# n = 0
# while a <= b:
#     n += 1
#     a *= 3
#     b *= 2
# print(n)

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers:
#     numbers.remove(4)
# print(*numbers)

# s = input()
# print(s)
# while len(s) > 1:
#     s = s[1:-1]
#     print(s)

# n = int(input())
# x = 1
# a = x * x
# while a <= n:
#     a = x * x
#     if a <= n:
#         print(a)
#     x += 1

# a, b = map(int, input().split())
# n = 1
# while a < b:
#     a += (a / 100) * 15
#     n += 1
# print(n)

# n, m = map(int, input().split())
# x = 0
# while n > 0:
#     x += 1
#     n -= 1
#     if x % m == 0:
#         n += 1
# print(x)

# a, b = map(int, input().split())
# n = 0
# x = 0
# while a > 0:
#     x += 1
#     a -= 1
#     n += 1
#     if n == b:
#         a += 1
#         n = 0
# print(x)

# n = int(input())
# x = 0
# while n >= 2:
#     n /= 2
#     x += 1
# if n == 1:
#     print(x)
# else:
#     print('НЕТ')

# n = input()
# z = 0
# x = int(n) * int(n[0])
# while x < 1_000_000_000:
#     x *= int(str(x)[0])
#     if z == x:
#         print(z)
#         break
#     z = x
# if x >= 1_000_000_000:
#     print(x)

# x = 0
# while n := int(input()):
#     x += n
# print(x)

# x = 0
# n = int(input())
# while n != 0:
#     x += n
#     n = int(input())
# print(x)

# s = input()
# x = ''
# while 5 <= len(s) <= 9:
#     x = s
#     s = input()
# print(x)

# n = int(input())
# a = 0
# count = 0
# b = 0
# x = int(input())
# while a <= n:
#     a += x
#     count += 1
#     if a <= n:
#         b = a
#     x = int(input())
# print('Довольно!')
# print(b)
# print(count - 1)

# n, k = map(int, input().split())
# count = 0
# a = 240
# b = a - k  # час на задачі
# task = [5, 15, 30, 50, 75, 105, 140, 180, 225, 275]
# while b >= 0:
#     b -= task[0]
#     del task[0]
#     count += 1
# print(count)

# 5 10 15 20 25 30 35 40 45 50

# n, k = map(int, input().split())
# count = 0
# a = 240
# b = a - k  # час на задачі
# task = [5, 15, 30, 50, 75, 105, 140, 180, 225, 275]
# while b >= 0:
#     b -= task[0]
#     del task[0]
#     count += 1
#     if task == []:
#         break
# print(count)

# https://stepik.org/lesson/625516/step/5?unit=621274

# n, k = map(int, input().split())
# total_time_available = 240  # Общее доступное время
# time_for_journey = k  # Время на дорогу
# tasks = [5 * (i + 1) for i in range(n)]  # Время для каждой задачи
#
# max_tasks_solved = 0
# i = 0
#
# # Пока есть доступное время и есть задачи
# while i < n and total_time_available >= tasks[i] + time_for_journey:
#     max_tasks_solved += 1
#     total_time_available -= tasks[i]
#     i += 1
#
# print(max_tasks_solved)

# n = int(input())
# cub = 0
# cub_in_line = 0
# line = 0
# while cub <= n:
#     line += 1
#     cub_in_line += line
#     cub += cub_in_line
# if cub > n:
#     print(line - 1)
# else:
#     print(line)
# print()
# print()
# print(line, cub_in_line, cub)

# n, m = map(int, input().split())
# a,b = input().split(), input().split()
# x = []
# while len(x) <= n + m:
#     while len(a) > 0:
#         if a[0] >= b[0]:
#             x.append(a[0])
#             del a[0]
#         else:
#             x.append(b[0])
#             del b[0]
#     while len(b) > 0:
#         x.append(b[0])
#         del b[0]
# print(x)

# n, m = map(int, input().split())  ### ###
# a,b = input().split(), input().split()
# x = []
#
# while len(a) > 0 and len(b) > 0:
#     if a[0] <= b[0]:
#         print('a ДО', a)
#         print('x', x)
#         x.append(a[0])
#         del a[0]
#         print('a ПІСЛЯ', a)
#         print('x', x)
#     else:
#         print('b ДО', b)
#         print('x', x)
#         x.append(b[0])
#         del b[0]
#         print('b ПІСЛЯ', b)
#         print('x', x)
# while len(b) > 0:
#     x.append(b[0])
#     del b[0]
#     print('b < 2', b)
#     print('x', x)
# print('x', x)

# n, m = map(int, input().split())
# a,b = input().split(), input().split()
# x = []
# while len(x) < n:
#     x.extend(a)
# while len(x) < m + n:
#     x.extend(b)
# print(x)
# q = 0
# while q < n + m - 1:
#     if x[0 + q] > x[0 + q + 1]:
#         x[0 + q], x[0 + q + 1] = x[0 + q + 1], x[0 + q]
#
#     q += 1
# print(x)



# z = []
# while len(z) < n + m:
#     if len(x) > 1:
#         if x[0] <= x[1]:
#             z.append(x[0])
#             del x[0]
#         else:
#             z.append(x[1])
#             del x[1]
#     else:
#         z.append(x[0])

# print(z)


# n, m = map(int, input().split())  ### ###
# q, w = input().split(), input().split()
# a, b = [], []
#
# while len(q) > 0:
#     a.append(int(q[0]))
#     del q[0]
#
# while len(w) > 0:
#     b.append(int(w[0]))
#     del w[0]
#
# x = []
#
# while len(a) > 0 and len(b) > 0:
#     if a[0] <= b[0]:
#         x.append(a[0])
#         del a[0]
#     else:
#         x.append(b[0])
#         del b[0]
# while len(b) > 0:
#     x.append(b[0])
#     del b[0]
# while len(a) > 0:
#     x.append(a[0])
#     del a[0]
# print(*x)

# o = int(input())
# p = input().split()
# b = []
# k = int(input())
# l = input().split()
# g = []
# x = 0
# while len(b) < o:
#     b.append(int((p[0])))
#     del p[0]
# b.sort()
#
# while len(g) < k:
#     g.append(int((l[0])))
#     del l[0]
# g.sort()
#
# if len(b) > len(g):
#     b, g == g, b
#
# while len(g) > len(b):
#     b.append(-2)
#
# b.append(0)
# g.append(0)
#
# print(b)
# print(g)
#
# while len(b) > 2 and len(g) > 2:
#     if b[0] == g[0] or b[0] == g[0] - 1 or b[0] == g[0] + 1:
#         x += 1
#         del b[0]
#         del g[0]
#     elif b[0] == g[1] or b[0] == g[1] - 1 or b[0] == g[1] + 1:
#         x += 1
#         del b[0]
#         del g[1]
#     elif b[1] == g[0] or b[1] == g[0] -1 or b[1] == g[0] + 1:
#         x += 1
#         del b[1]
#         del g[0]
#     else:
#         del b[0]
#         del g[0]
#
# print(b)
# print(g)
# print(x - 1)

# b m
# o = int(input())
# p = input().split()
# b = []
# k = int(input())
# l = input().split()
# g = []
# x = 0
# while len(b) < o:
#     b.append(int((p[0])))
#     del p[0]
# b.sort()
#
# while len(g) < k:
#     g.append(int((l[0])))
#     del l[0]
# g.sort()
#
# if len(b) < len(g):
#     b, g = g, b
#
# while len(b) > 0 and len(g) > 0:
#     if b[0] == g[0] or b[0] == g[0] or b[0] == g[0] + 1 or b[0] == g[0] - 1:
#         x += 1
#         del b[0]
#         del g[0]
#     else:
#         if b[0] < g[0]:
#             del b[0]
#         else:
#             del g[0]
# print(x)

# n = 4782
# while n > 0:
#     print(n%10)
#     n = n//10

# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)

# n = int(input())
# while n > 0:
#     print(n % 10)
#     n = n // 10

# n = int(input())
# x = 0
# while n > 0:
#     x += n % 10
#     n //= 10
# print(x)

# n = int(input())
# x = 1
# while n > 0:
#     x *= n % 10
#     n //= 10
# print(x)

# n = int(input())
# l = []
# while n > 0:
#     l.append(n % 10)
#     n //= 10
# print(min(l), max(l), sep='\n')

# n = int(input())
# count = 0
# while n > 0:
#     if n % 10 != 0 and n % 10 % 7 == 0:
#         count += 1
#     n //= 10
# print(count)

# n = int(input())
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# b = int(b)
# while b > 0:
#     print(b % 10)
#     b //= 10

# n = int(input())
# a = 1
# while a <= n // 2:
#     if n % a == 0:
#         print(a, end=' ')
#     a += 1
# print(n)

# n = int(input())
# a = 1
# count = 0
# while a <= n // 2:
#     if n % a == 0:
#         count +=1
#     a += 1
# if n == 1 or count > 1:
#     print('No')
# else:
#     print('Yes')

n = int(input())
a = 1
x = 0
while a <= n // 2:
    if n % a == 0:
        x += n // a
    a += 1
print(x + 1)