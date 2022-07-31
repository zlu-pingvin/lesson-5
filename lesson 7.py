# s = input()
# print(s[0], s[3])
# print(s[-1], s[-2])

# s = input()
# for i in s:
#     print(i)

# s = input()
# [print(True) if s[0] == s[-1] else print(False)]

# s = input()
# print(s[:10])  # в первой строке первые 10 символов
# print(s[-10:])  # последние 10 символов
# print(s[::2])  # все символы стоящие на четных местах
# print(s[2::3])  # каждый третий символ

# s = input()
# print(s[::-1])

# s = input().split()
# [print(s[0]) if len(s[0]) >= len(s[1]) else print(s[1])]

# s = input().split()
# if s[0] >= s[1]:
#     print(s[0])
# else:
#     print(s[1])

# s = input()
# if '(' in s and ')' in s:
#     l = s.find('(')
#     s = s[:l] + '*' + s[l:]
#     r = s.rfind(')') + 1
#     s = s[:r] + '*' + s[r:]
#     print(s)
# else:
#     print(s)

# s = input()
# s = s.replace('(', '*(', 1)
# s = s[::-1].replace(')', '*)', 1)
# print(s[::-1])

# s = input()
# print(s.count('+'), s.count('-'), sep='\n')

# n = int(input())
# x = bin(n)
# print(x[2:])

# s = "8" * 68
# while "222" in s or "888" in s:
#     if "222" in s:
#         s = s.replace("222", "8", 1)
#     else:
#         s = s.replace("888", "2", 1)
# print(s)

# s = '1' + '8' * 80
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s:
#         s = s.replace('18', '2', 1)
#     elif '288' in s:
#         s = s.replace('288', '3', 1)
#     elif '3888' in s:
#         s = s.replace('3888', '1', 1)
#     else:
#         print('alarm')
#         break
# print(s)

# s = '1' + '8' * 80
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s:
#         s = s.replace('18', '2', 1)
#     elif '288' in s:
#         s = s.replace('288', '3', 1)
#     else:
#         s = s.replace('3888', '1', 1)
# print(s)

# s = '1' * 100
# while '111' in s:
#     if '111' in s:
#         s = s.replace('111', '2', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#         elif '333' in s:
#             s = s.replace('333', '1', 1)
# print(s)

# s = '1' * 200 + '7' * 57
# while '1111' in s:
#     s = s.replace('1111', '7', 1)
#     s = s.replace('77', '1', 1)
# print(s)


# def algor(n):
#     """функция алгоритм"""
#     b = bin(n)[2:]  # двоичная запись числа n типа str
#     if n % 2 == 0:
#         b += "01"
#     else:
#         b += "10"
#     rezultat = int(b, 2)  # превращаем двоичное в десятичное
#     return rezultat
#
#
# for i in range(1, 1000000):
#     if algor(i) > 102:
#         print(algor(i))
#         break

# def avtomat(n):
#     """функция автомат"""
#     b = bin(n)[2:]  # двоичная запись числа n типа str
#     b = "0" * (8 - len(b)) + b  # делаем запись восьмибитной
#     s = ""
#     for digit in b:  # находим обратный код числа
#         if digit == "0":
#             s += "1"
#         else:
#             s += "0"
#     rezultat = int(s, 2)  # превращаем двоичное в десятичное
#     answer = rezultat - n  # из нового вычитается исходное
#     return answer
#
#
# x = int(input())
# for i in range(0, 256):
#     if avtomat(i) == x:
#         print(i)

# def alg(n):
#     bin_n = bin(n)[2:]
#     if n % 2 == 0:
#         bin_n += '00'
#     else:
#         bin_n += '11'
#     r = int(bin_n, 2)
#     return r
#
#
# n = 0
# for i in range(100):
#     if alg(i) < 94:
#         n = i
# print(n)

# def alg(n):
#     y = int(bin(n)[2:])
#     x = 0
#     while y > 0:
#         x += y % 10
#         y //= 10
#     z = (bin(n)[2:]) + str(x % 2)
#     return z
#
# def alg_2(z):
#     x = 0
#     l = z
#     while l > 0:
#         x += l % 10
#         l //= 10
#     p = str(z) + str(x % 2)
#     return p
#
#
# n = 0
# z = int(alg(n))
# r = int(alg_2(z))
# # print(z)
# # print(r)
#
# for i in range(1, 1000):
#     # n += 1
#     alg(n)
#     # print(alg(n))
#     if int((alg_2(int(alg(n)))), 2) > 55:
#         print(int((alg_2(int(alg(n)))), 2))
#         break
#         # print(int(alg_2(int(alg(n)))))
#     n += 1

# def alg(n):
#     y = int(bin(n)[2:])
#     x = 0
#     while y > 0:
#         x += y % 10
#         y //= 10
#     z = int((bin(n)[2:]) + str(x % 2))
#     q = 0
#     u = z
#     while z > 0:
#         q += z % 10
#         z //= 10
#     p = int(str(u) + str(q % 2))
#     r = int(str(p), 2)
#     return r
#
# n = int(input())
# print(alg(n))

# def avtomat(n):
#     a = str(n // 100)
#     b = str(n // 10 % 10)
#     c = str(n % 10)
#     if a <= b <= c and a != 0:
#         x = a + b
#         y = c + b
#     return int(y) - int(x)
#
#
# n = int(input())
# print(avtomat(n))

# def avtomat(n):
#     list = []
#     for j in n:
#         list.append(j)
#
#     list = sorted(list)
#
#     a = list[2] + list[1]
#     if list[0] != '0':
#         b = list[0] + list[1]
#     else:
#         b = list[1] + list[0]
#     return int(a) - int(b)
#
# x = int(input())
# answer = 0
# for i in range(100, 1000):
#     if avtomat(str(i)) == x:
#         answer = i
# print(answer)

# count = 0
# for s1 in "АКРУ":
#     for s2 in "АКРУ":
#         for s3 in "АКРУ":
#             for s4 in "АКРУ":
#                 for s5 in "АКРУ":
#                     count += 1
#                     if count == 355:
#                         print(s1 + s2 + s3 + s4 + s5)

# count = 0
# for s1 in 'ABCDX':
#     for s2 in 'ABCDX':
#         for s3 in 'ABCDX':
#             for s4 in 'ABCDX':
#                 for s5 in 'ABCDX':
#                     if (s1 + s2 + s3 + s4 + s5).count('X') == 1:
#                         count += 1
                        # print(s1 + s2 + s3 + s4 + s5)
                    # elif (s1 + s3 + s4 + s5).count('X') == 1:
                    #     count += 1
                    #     print(s1 + s3 + s4 + s5)
                    # elif (s1 + s2 + s4 + s5).count('X') == 1:
                    #     count += 1
                    #     print(s1 + s2 + s4 + s5)
                    # elif (s2 + s3 + s4 + s5).count('X') == 1:
                    #     count += 1
                    #     print(s2 + s3 + s4 + s5)
                    # elif (s1 + s2 + s3 + s4).count('X') == 1:
                    #     count += 1
                    #     print(s1 + s2 + s3 + s4)
# count = count / 5
# print(str(count)[0:3])

# count = 0
# for s1 in 'ABCDX':
#     for s2 in 'ABCDX':
#         for s3 in 'ABCDX':
#             for s4 in 'ABCDX':
#                 s = s1 + s2 + s3 + s4
#                 if s.count('X') == 1:
#                     count += 1
# print(count)

# count = 0
# for s1 in 'КОР':
#     for s2 in 'КОР':
#         for s3 in 'КОР':
#             for s4 in 'КОР':
#                 for s5 in 'КОР':
#                     count += 1
#                     if count == 237:
#                         print(s1 + s2 + s3 + s4 + s5)

# s = 'а г и л м о р т'
# s = sorted(s)
# print(*s)

def abc():
    count = 0
    for s1 in 'АГИЛМОРТ':
        for s2 in 'АГИЛМОРТ':
            for s3 in 'АГИЛМОРТ':
                for s4 in 'АГИЛМОРТ':
                    count += 1
                    print(s1 + s2 + s3 + s4)
                    if 'ИГ' in s1 + s2 + s3 + s4:
                        # print(count)
                        return count


print(abc())


