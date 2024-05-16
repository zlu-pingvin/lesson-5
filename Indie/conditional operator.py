# s = input()
# if s == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# n = int(input())
# if n < 20000:
#     print(n)
# else:
#     print(n - (n / 100 * 13))

# a, b = int(input()), int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# a, b, c = map(int, input().split())
# if a + b == c:
#     print('YES')
# else:
#     print('NO')

# a = list(map(int, input().split()))
# if 3 in a:
#     a.remove(3)
# if 5 in a:
#     a.remove(5)
# if 7 in a:
#     a.remove(7)
# if 9 in a:
#     a.remove(9)
# print(a)

# a = 3
# print(a := a + 2)

# if (n := int(input()) <= 10000):
#     print(f'Сумма {n := n} не превышает лимит, проходите')
# else:
#     print(f'Ого! {n := n}! Куда вам столько? Мы заберем {n - 10000}')

# if (s := int(input())) > 10000:
#     print(f'Ого! {s}! Куда вам столько? Мы заберем {s - 10000}')
# else:
#     print(f'Сумма {s} не превышает лимит, проходите')

# if 'walrus' in (s := input()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# if (s := input()) == (t := input()[::-1]):
#     print('YES')
# else:
#     print('NO')

# if (n := input()) == n[::-1]:
#     print('YES')
# else:
#     print('NO')

# if ((a := (int(input()))) + (b := int(input()))) > (c := int(input())) and (a + c) > b and (b + c) > a:
#     print('YES')
# else:
#     print('NO')

# if (len(n := input())) == 6:
#     if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
#         print('YES')
#     else:
#         print('NO')
# if len(n) < 6:
#     n = n.rjust(6, '0')
#     if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
#         print('YES')
#     else:
#         print('NO')

# a, b = input(), input()
# x = ord(a[0]) + int(a[1])
# y = ord(b[0]) + int(b[1])
# if x % 2 == 0 and y % 2 == 0:
#     print('YES')
# elif x % 2 != 0 and y % 2 != 0:
#     print('YES')
# else:
#     print('NO')

# print(text :='Even') if int(input()) % 2 == 0 else print(text :='Odd')

# minimum, maximum = int(input()), int(input())
# [print(minimum, maximum) if minimum < maximum else print(maximum, minimum)]

# s = input()
# print(sentence := 'Вопросительное') if s[-1] == '?' else print(sentence := 'Обычное')

# a, b = input(), input()
# print(experiment := 'Притягиваются') if a != b else print(experiment := 'Отталкиваются')

# a, b = int(input()), int(input())
# if a < b:
#     print('<')
# elif a > b:
#     print('>')
# else:
#     print('=')

# a, b, c = int(input()), int(input()), int(input())
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# n = int(input())
# if n < 2:
#     print(0)
# elif n % 2 == 0:
#     print(int(n / 2))
# else:
#     print(n)

# a, b, c = map(int, input().split())
# if a > b and a > c:
#     if b > c:
#         print(a - c)
#     else:
#         print(a - b)
# if b > a and b > c:
#     if a > c:
#         print(b - c)
#     else:
#         print(b - a)
# if c > b and c > a:
#     if a > b:
#         print(c - b)
#     else:
#         print(c - a)

# a, b = input().lower(), input().lower()
# if a > b:
#     print(1)
# elif b > a:
#     print(-1)
# else:
#     print(0)

# a, b = input().lower(), input().lower()
# if a[-1] == 'ь':
#     if a[-2] == b[0]:
#         print('Good')
#     else:
#         print('Bad')
# else:
#     if a[-1] == b[0]:
#         print('Good')
#     else:
#         print('Bad')

# n = int(input())
# if n % 3 == 0 and n % 5 == 0:
#     print('FizzBuzz')
# elif n % 3 == 0:
#     print('Fizz')
# elif n % 5 == 0:
#     print('Buzz')
# else:
#     print(n)

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)

# n = int(input()) - 1
# m = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# print(m[n])

# n = int(input())
# if n < 2:
#     print('Младенец')
# elif 2 < n < 4:
#     print('Малыш')
# elif 4 <= n < 12:
#     print('Ребенок')
# elif 12 <= n < 19:
#     print('Подросток')
# elif 19 <= n < 65:
#     print('Взрослый человек')
# else:
#     print('Пожилой человек')

# a, b = float(input()), float(input())
# n = input()
# if n not in '+-*/':
#     print('Неизвестно')
# elif n == '+':
#     print(a + b)
# elif n == '-':
#     print(a - b)
# elif n == '*':
#     print(a * b)
# elif n == '/':
#     if b == 0:
#         print('Неизвестно')
#     else:
#         print(a / b)

# a, b = input(), input()
# if len(a) < 7:
#     print('Short')
# elif a != b:
#     print('Difference')
# else:
#     print('OK')

# s = input()
# match s:
#     case '1':
#         print('Совсем еще зеленый студентик')
#     case '2':
#         print('Джун-студент')
#     case '3':
#         print('Мидл-студент')
#     case '4':
#         print('Сеньор-студент')
#     case '5':
#         print('Босс качалки')
#     case _:
#         print('Неизвестный курс')

# digit = int(input("Введите цифру: "))
# match digit:
#     case 0 | 3 | 6 | 9:
#         print("Без остатка делятся на 3")
#     case 1 | 4 | 7:
#         print("При делении на 3 дают остаток 1")
#     case 2 | 5 | 8:
#         print("При делении на 3 дают остаток 2")
#     case  _:
#         print(f"{digit} не является цифрой")

# m = int(input())
# match m:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(31)
#     case 4 | 6 | 9 | 11:
#         print(30)
#     case 2:
#         print(28)

# m = input()
# match m:
#     case 'Овен' | 'Лев' | 'Стрелец':
#         print('Огненный')
#     case 'Телец' | 'Дева' | 'Козерог':
#         print('Земной')
#     case 'Близнецы' | 'Весы' | 'Водолей':
#         print('Воздушный')
#     case 'Рак' | 'Скорпион' | 'Рыбы':
#         print('Водный')


