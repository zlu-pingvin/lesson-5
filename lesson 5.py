# n = int(input())
# count = 0
# while n != 0:
#     if len(str(n)) == 1:
#         if n % 3 == 0:
#             count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if n % 7 == 0 and n % 10 == 0:
#         count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if n % 6 == 0 or n % 11 == 0:
#         count += n
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# for i in range(n):
#     z = int(input())
#     if z % 6 == 0:
#         count += z
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if n % 4 == 0 and n % 10 == 2:
#         count += n
#     n = int(input())
# print(count)

# n = int(input())
# summ = 0
# count = 0
# while n != 0:
#     if len(str(n)) == 3:
#         count += 1
#         summ += n
#     n = int(input())
# [print('NO') if count == 0 else print(summ / count)]

# n = int(input())
# max = 0
# for i in range(n):
#     if n % 5 == 0:
#         if n > max:
#             max = n
#     n = int(input())
# print(max)

# n = int(input())
# min = 30001
# for i in range(n):
#     z = int(input())
#     if z % 3 == 0:
#         if z < min:
#             min = z
# print(min)

# n = int(input())
# min = 30001
# for i in range(n):
#     z = int(input())
#     if z % 2 == 0:
#         if z < min:
#             min = z
# print(min)

# n = int(input())
# max = 0
# count = 0
# summ = 0
# for i in range(n):
#     z = int(input())
#     if z > max:
#         max = z
#     count += 1
#     summ += z
# print(summ / count)
# [print('YES') if max > 59 else print('NO')]

# n = int(input())
# min = 0
# count = 0
# summ = 0
# for i in range(n):
#     z = int(input())
#     if z <= 40:
#         min += 1
#     count += 1
#     summ += z
# print(summ / count)
# [print('YES') if min > 1 else print('NO')]

# n = int(input())
# max = 0
# count = 0
# min = 1000
# for i in range(n):
#     z = int(input())
#     if z > max:
#         max = z
#     if z < min:
#         min = z
#     if z <= 30:
#         count += 1
# print(max - min, count, sep='\n')

# n = int(input())
# summ = 0
# count = 0
# while n != 0:
#     count += 1
#     if n % 2 == 0:
#         summ += n
#     n = int(input())
# print(count, summ, sep='\n')

# n = int(input())
# summ = 0
# count_min = 0
# count_max = 0
# while n != 0:
#     summ += n
#     if n > 0:
#         count_max += 1
#     if n < 0:
#         count_min += 1
#     n = int(input())
# print(summ, count_max - count_min, sep='\n')

# count = 0
# for i in range(10):
#     z = int(input())
#     if z % 3 == 0 and z % 10 == 5:
#         count += 1
# print(count)

# n = int(input())
# zero = 0
# min = 99
# for i in range(n):
#     z = int(input())
#     if z < min and z > 0:
#         min = z
#     if z < -10:
#         zero += 1
# print(min)
# [print('YES') if zero > 0 else print('NO')]

# n = int(input())
# count = 0
# while n != 0:
#     if n % 5 == 0 or n % 9 == 0:
#         count += 1
#     n = int(input())
# print(count)

# n, m = int(input()), int(input())
# count = 0
# for i in range(n, m + 1):
#     if i % 2 == 0:
#         count += 1
# print(count)

