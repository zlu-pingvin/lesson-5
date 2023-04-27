# n = 'q', '2'
# print(*n)
# n = list(n)
# print(n)

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# print(arr)

# n = [i ** 2 for i in range(1, 51)]
# print(n)

# a = [1, 3, 4, 52, 6, 71, 2, 3, 99]
# s = 0
# for i in range(len(a)):
#     s += a[i]
# print(s)

# a = [1, 4, 4, 52, 6, 71, 2, 3, 99]
# s = 0
# for i in a:
#     s += i
# print(s)

# arr = []
# dig = []
# for i in range(10):
#     n = int(input())
#     arr.append(n)
#     if n > 0:
#         dig.append(n)
# print(arr)
# print(*dig, sep='\n')

# s = input().split()
# arr = []
# for i in s:
#     arr.append(int(i))
# print(arr)

# a = [1, 3, 4, 52, 6, 71, 2, 3, 99]
# a.sort()
# print(a)

# a = [1, 3, 4, 52, 6, 71, 2, 3, 99]
# a.sort(reverse=True)
# print(a)

# n = int(input())
# s = input().split()
# arr = []
# for i in range(n):
#     arr.append(int(s[i]))
# arr.reverse()
# print(*arr)

# n = int(input())  # Последовательность Фибоначчи
# arr = [1, 1]
# for i in range(3, n + 1):
#     q = arr[-1] + arr[-2]
#     arr.append(q)
# print(*arr)

# n = int(input())
# arr1 = []
# arr2 = []
# for i in range(n):
#     q = int(input())
#     arr1.append(q)
#     arr2.append(q * 2)
# print(*arr1 + arr2)

# s = input().split()
# a = 0
# b = 1
# for i in s:
#     a += int(i)
#     b *= int(i)
# print(a)
# print(b)

# def fibonacci(num):
#     # Починаємо з двох перших чисел в послідовності
#     fib_list = [0, 1]
#
#     # Додаємо наступні числа до послідовності
#     while fib_list[-1] + fib_list[-2] <= num:
#         fib_list.append(fib_list[-1] + fib_list[-2])
#
#     # Повертаємо послідовність
#     return fib_list
#
#
# print(fibonacci(100))

# s = input().split()
# a = []
# b = []
# for i in s:
#     if int(i) > 0:
#         a.append(i)
#     elif int(i) < 0:
#         b.append(i)
# print(*a + b)

# s = input().split()
# a = []
# b = []
# for i in s:
#     if int(i) % 2 == 0:
#         a.append(i)
#     elif int(i) % 2 != 0:
#         b.append(i)
# print(*a + b)

# print(divmod(10, 3))

# import math
# sin = math.radians(666)
# cos = math.radians(6 * 6 * 6)
#
# print(math.sin(sin) + math.cos(cos))
# print('0_o')
# print(math.sin(666) + math.cos(6 * 6 * 6))
# print(math.sin(666))
# print(math.cos(6 * 6 * 6))

# import random

# a = []
# for i in range(20):
#     a.append(random.randint(-10000, 10000))
# print(a)

# a = []
# n = 4
# for i in range(0, n):
#     a.append(int(input()))
# for j in a:
#     if a[j] + a[j - 1] % 2 == 0 and a[j] + a[j - 1] % 4 != 0:
#         print(a[j - 1], a[j])

# a = []
# n = 4
# x = 0
# for i in range(0, n):
#     a.append(int(input()))
# for j in range(0, len(a)):
#     if (a[j] + a[j - 1]) % 2 == 0 and (a[j] + a[j - 1]) % 4 != 0:
#         x += 1
# print(x)

# a = []
# n = 40
# k = 0
# for i in range(0, n):
#     a.append(int(input()))
# for j in range(1, len(a)):
#     if (a[j] * a[j - 1]) > 0 and (a[j] + a[j - 1]) % 7 == 0:
#         k += 1
# print(k)

# a = []  # ліст
# b = [0]  # сума сусідніх елементів з а
# n = 30
# y = 0  # нібільша сума з b
# x = 0  # номер елемента b (пари з а)
# for i in range(0, n):
#     a.append(int(input()))
# for j in range(1, len(a)):
#     b.append(a[j] + a[j - 1])
# for k in range(len(b)):
#     if b[k] > y:
#         y = b[k]
#         x = k
# print(x)

# q = 0
# list = []
# for i in range(30):
#     list.append(int(input()))
# n = max(list)
# for j in list:
#     if j == n:
#         q += 1
# print(q)

# a = list(int(input()) for _ in range(30))
# x = 0
# n = []
# for i in range(2, len(a)):
#     if a[i] + a[i - 1] + a[i - 2] > x:
#         x = a[i] + a[i - 1] + a[i - 2]
#         n = [a[i]], [a[i - 1]], [a[i - 2]]
# print(*n[2], *n[1], *n[0], sep='\n')

# l = []
# x = 1000000 ** 11
# n = 0
# for i in range(1, 21):
#     l = input().split()
#     for j in range(10):
#         l[j] = (int(l[j]))
#     if sum(l) < x:
#         x = sum(l)
#         n = i
# print(n)

# a = []
# N = 2000
# i = 0
# k = 0
# for j in range(0, N):
#     a.append(int(input()))
#     if a[j] % 2 == 0:
#         i += 1
#     else:
#         k += 1
# if sum(a) % 2 == 0:
#     print(i)
# else:
#     print(k)

# a = []
# n = 6
# max = -21
# for i in range(0, n):
#     a.append(int(input()))
#     if a[i] > max and a[i] < 0:
#         max = a[i]
# print(max)

# n = 30
# a = [int(input()) for i in range(n)]
# j = [i for i in a if len(str(i)) == 3 and i % 7 == 0]
# if not j:
#     print('Не найдено')
# else:
#     print(min(j))

# n = 30
# k = 0
# a = [int(input()) for i in range(n)]
# for j in range(n):
#     if len(str(a[j])) == 2 and '9' in str(a[j]):
#         k += 1
# print(k)

# import animalsay
# import animals

# from animals import Animals
# animal = Animals('cat')
# print(animal.image())

# n = 30
# k = 1
# a = [int(input()) for i in range(n)]
# for j in range(n):
#     if a[j] % 2 != 0 and a[j] % 3 == 0:
#         k *= a[j]
# print(k)

# n = 2014
# k = 0
# a = [int(input()) for i in range(n)]
# for j in range(n):
#     if len(str(a[j])) == 3 and a[j] % 10 == 9 and a[j] % 100 != 99:
#         k += a[j]
# if k > 0:
#     print(k)
# else:
#     print(-1)

# a = []
# for i in range(1020, 6950+1):
#     if i % 3 == 0 and i % 7 != 0 and i % 19 != 0 and i % 27!= 0:
#         a.append(i)
# print(len(a))
# print(max(a))

# a, b = int(input()), int(input())
# n = []
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 7 != 0 and i % 13 != 0 and i % 19 != 0 and i % 27 != 0:
#         n.append(i)
# print(len(n), max(n), sep='\n')

# arr = [1, 3, 5, 0 , 7, 4]
# for j in range(len(arr)):
#     for i in range(1, len(arr)):
#         if arr[i] < arr[i - 1]:
#             arr[i], arr[i - 1] = arr[i - 1], arr[i]
# print(arr)

# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])
# a.sort()
# print(*a)

# a = [int(i) for i in input().split()]  ## !!! ліст в інт
# print(*sorted(a))

# a = [int(i) for i in input().split()]
# a.sort(reverse=True)
# print(*a)

# a = [int(i) for i in input().split()]
# a.sort(reverse=True)
# b = [int(k) for k in input().split()]
# b.sort(reverse=True)
# if a[2] > b[2]:
#     print('А')
# elif a[2] < b[2]:
#     print('Б')
# else:
#     print('одинаковый')

# l = [int(input()) for i in range(10)]
# a = l[:4]
# a.sort()
# b = l[4:6]
# c = l[6:]
# c.sort(reverse=True)
# print(*a + b + c, sep='\n')

# l = [int(i) for i in input().split()]
# l.sort(reverse=True)
# a = []
# for i in l:
#     if i % 3 == 0:
#         a.append(i)
# if len(a) < 3:
#     print('нет ответа')
# else:
#     print(a[2])

# l = [input() for i in range(11)]
# l.sort()
# n = l[5]
# print(n[4:])

# a = [int(i) for i in input().split()]
# b = [int(j) for j in input().split()]
# a.sort()
# b.sort()
# if a == b:
#     print('да')
# else:
#     print('нет')

# a, b = input(), input()
# x = []
# y = []
# [x.append(i) for i in a]
# [y.append(j) for j in b]
# x.sort()
# y.sort()
# if x == y:
#     print('да')
# else:
#     print('нет')

# a = [int(i) for i in input().split()]
# a.sort(key=abs)
# print(*a)

# a = input().split()
# a.sort(key=len, reverse=True)
# print(*a)

