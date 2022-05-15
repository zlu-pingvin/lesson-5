import random

def password():  # Генератор безопасных паролей
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
    pswrd = ''
    for i in range(12):

        pswrd += random.choice(chars)
        # random.shuffle(pswrd)
    return pswrd

# n = int(input())
# for i in range(10):
#     print(password())

# import random

def qwerty():
    n = random.randint(1, 6)
    flag = True
    if n <= 3:
        flag = True
        return 'кверти'
    else:
        return 'пщ пщ'

if __name__ == '__main__':
    print(qwerty())

# import speedtest
#
# test = speedtest.Speedtest()
# download = test.download()
# upload = test.upload()
#
# dwn = round((download/1024)/1024, 2)
# upl = round((upload/1024)/1024, 2)
#
# print(f'Download speed: {dwn} Mb/s')
# print(f'Upload speed: {upl} Mb/s')


# # шрифт цезаря https://stepik.org/lesson/352860/step/10?unit=336821
# len_s = []
# f = input('Введите фразу \n').split()
# s = ' '.join(f)
#
# # f = [str(i) for i in f]
# # print(f)
# rus_low = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# eng_low = 'abcdefghijklmnopqrstuvwxyz'
# eng_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# symbol = '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "'
#
# n_d = input('Если нужно зашифровать текст, нажми "+", если нужно дешифровать текст, нажми "-" \n')
# n_l = input('Выберите язык алфавита: русский - нажмите "r", английский - нажмите "e" \n')
# rot = len_s
#
# n = 0  # кол-во букв: ру 32, англ 25
# if n_l == 'r':
#     n = 32
# elif n_l == 'e':
#     n = 26  # чому 26?
#
# for a in range(len(f)):
#     count = 0  # количество символов в каждом слове
#     for b in f[a]:
#         for c in b:
#             if c.isalpha():
#                 count += 1
#     len_s.append(count)
#     # print(count)
# # print(s)
# # print(len_s)
#
#
#
#     len_s.append(count)
#     for i in range(len(f)):
#         if s[i].isalpha():
#             if s[i] == s[i].upper():
#                 for j in range(n):
#                     if n == 32:
#                         if s[i] == rus_up[j]:
#                             # text.extend([rus_up[(j + rot) % n]])
#                             print(*[rus_up[(j + rot) % n]], end='')
#                     elif n == 26:  # !!!! 26 !!!!
#                         if s[i] == eng_upp[j]:
#                             # text.extend([eng_upp[(j + rot) % n]])
#                             print(*[eng_upp[(j + rot) % n]], end='')
#             elif s[i] == s[i].lower():
#                 for j in range(n):
#                     if n == 32:
#                         if s[i] == rus_low[j]:
#                             # text.extend([rus_low[(j + rot) % n]])
#                             print(*[rus_low[(j + rot) % n]], end='')
#                     elif n == 26:
#                         if s[i] == eng_low[j]:
#                             # text.extend([eng_low[(j + rot) % n]])
#                             print(*[eng_low[(j + rot) % n]], end='')
#         else:
#             # text.extend(f[i])
#             print(s[i], end='')
#
#
#
# # n = input()
# # # ищем длину слов переводим в словарь в виде чисел
# # s = n
# # for j in n:
# #     if j in '*,.!@"-':
# #         s = s.replace(j, '')
# # g = [len(i) for i in s.split()]
# # print(s)
# # print(g)


# n = int(input())  # Перевод из десятичной системы счисления в двоичную
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(b)

# https://stepik.org/lesson/311434/step/10?unit=293862
# https://inf-ege.sdamgia.ru/test?theme=260



