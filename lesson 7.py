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

s = '4' + '8' * 80
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2', 1)
    elif '288' in s:
        s = s.replace('288', '3', 1)
    elif '3888' in s:
        s = s.replace('3888', '1', 1)
    else:
        print('alarm')
        break
print(s)

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