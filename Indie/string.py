# l = 'Я стану крутым программистом!'
# print(l, l, l, sep='\n')

# l = 'Я стану крутым программистом!\n'
# print(l * 3)

# print('W' * 777)

# print('Лев Николаевич Толстой написал "Война и мир"')

# a, b = input(), input()
# print(a, b, sep='\n')

# a, b, c = input(), input(), input()
# print(c, b, a, sep='\n')

# a = input() + ' '
# print(a * 4)

# print(len(input()))

# a, b = input(), input()
# print(b + a)

# print(input() * 3)

# ord()

# a, b, c = input().split()
# print(f'Simvol code {a} is {ord(a)}.')
# print(f'Simvol code {b} is {ord(b)}.')
# print(f'Simvol code {c} is {ord(c)}.')

# s = input()
# print(s[-1])

# s = input()
# print(s[0:4])

# s = input()
# print(s[-4:])

# s = input()
# print(s[0::2])

# s = input()
# # print(s[1::2])

# s = input()
# print(s[::-1])

# s = input()
# l = s[::-1]
# print(l[::3])

# s = input()
# l = s[-1]+s[:-1]
# print(l)

# s = input()
# print(s.lower())

# a, b = input(), input()
# print(a.upper() == b.upper())

# s = input().lower()
# s = s[:3].upper()+s[3:-3]+s[-3:].upper()
# print(s)

# s = input()
# print(s.swapcase())

# s = input().title()
# print(s.swapcase())

# s = input()
# print(s.count('e') + s.count('E'))

# s = input()
# print(s.find('a'))

# s = input()
# print(s.replace(' ', ','))

# s = input()
# s = s.replace('w', '')
# s = s.replace('z', '')
# print(s)

# s = input()
# s = s.replace('', 'z')
# print(s[:-1])

# s = input().lower().replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
# s = s.replace('', '.')
# print(s[:-1])

# l = input().split()
# print(len(l))

# list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
# l = '-'.join(list_strings)
# print(l)

# s = input().lower()
# print(s.startswith('mam'))

# s = input()
# postfix = input()
# print(s.endswith(postfix))

# s, prefix, postfix = input(), input(), input()
# print(s.startswith(prefix) and s.endswith(postfix))

# s = input()
# print(s.isdigit())

# s = input()
# print(s.isupper())

# s = input()
# print(s.islower())

# d = input()
# print(d.ljust(10, '-'))

# d = input()
# print(d.rjust(10, '!'))

# d = 'qwerty'
# print(d.rjust(10))

# d = 'qwerty'
# print(d.rjust(15, '-'))

# d = input()
# print(d.center(15, '_'))

# d = '123'
# print(d.zfill(15))

# d = input()
# print(d.rjust(10, '0'))

# S.strip()

# s = input()
# print(s.strip('-_!?'))

# s = input()
# print(s.lstrip('-_!?'))

# print(hex(171))

# a, b, c = int(input()), int(input()), int(input())
# a = hex(a)[2:].rjust(2, '0').upper()
# b = hex(b)[2:].rjust(2, '0').upper()
# c = hex(c)[2:].rjust(2, '0').upper()
# print(f'#{a}{b}{c}')

# s = """dfg df df
# dfgddf  dfgd gd
# dfgfdg dg"""
# print(s)

# a = "abc\tdef"
# print(a)

# print('/\\_/\\')
# print('>^,^<')
# print(' / \\')
# print('(|_|)_/')

# print('/\\_/\\\n>^,^<\n / \\\n(|_|)_/')

# print('   /~~~\\')
# print('  //^ ^\\\\')
# print(' (/(_*_)\\)')
# print("_/' '*' '\\_")
# print(' (/_)^(_\\)')


# print("  /~~~\ \n //^ ^\\\ \n(/(_*_)\) \n_/''*''\_\n(/_)^(_\)")

# s = input()
# print("""Что Вы сказали? {0}? Какое интересное слово""".format(s))

# a, b = input(), input()
# print("""Здравствуйте, {1} {0}!""".format(a, b))

# b = int(input())
# a = b - 1
# c = b + 1
# print("""Для числа {1} предыдущим будет число {0}.
# Для числа {1} следующим будет число {2}.""".format(a, b, c))

# print(f'Мое имя {input()}!')

# n = input().upper()
# y = int(input())
# print(f'Hello {n}. You are {y} years old.')

# n = input()
# y = int(input())
# print(f'{n}, вам исполнится 77 лет в {y + 77}')

# n = int(input())
# print(f'{n} сек - это {n // 60} мин. {n % 60} сек.')

# a, b = map(int, input().split())
# print(f'Разрешение экрана: {a} x {b}.')
# print(f'Общее количество пикселей = {a * b}.')

# a, b = int(input()), int(input())
# print(f'{a} / {b} = {a / b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} % {b} = {a % b}')

# x, y, z = int(input()), int(input()), int(input())
# print(f"""
# Vector A({x}, {y}, {z})
# Vector B({x + 5}, {y + 5}, {z + 5})
# """)

# a = float(input())
# b = int(input())
# print(f"""
# Current dollar rate is {a}. You want to buy {b} dollars
# You must pay {a * b}
# """)

# x, y = int(input()), int(input())
# print(f'Точка({x = }, {y = })')

# number_pi = 3.141592653589793
# print(f'{number_pi:.6f}')

# b = float(input())
# print(f'{b:.2f}')

# n = 12345
# print(f'{n:8d}')
# print(f'{n:,d}')
# print(f'{n:_d}')

# print(f'Число\t\tКвадрат\t\tКуб')
# for x in range(1, 11):
#    print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')

# b = int(input())
# print(f'{b:010d}')

# n = int(input())
# print(f'{n:-^15}')

# text = input()
# print(f"|{text:&^20}|")
# print(f"|{text:&>20}|")
# print(f"|{text:&<20}|")

# my_list = [1] * 77
# print(my_list)

# my_list = ['q', 'w', 't'] * 15
# print(my_list)

# my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# print(min(my_list), max(my_list))

# b = list(map(int, input('Введите значения: ').split()))

# my_list = list(map(int, input().split()))
# print(777 in my_list)

# n = list(map(int, input().split()))
# print(sum(n) / len(n))

# a = list(map(int, input().split()))
# print(a[::-1])

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1] = 'Сверхъестественное'
# top[2] = 'Настоящий детектив'
# print(top)

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# n = int(input())
# print(months[n - 1])

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.append(111)
# numbers.append(222)
# numbers.append(789)
# numbers.append(201)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.insert(5, 111)
# numbers.insert(8,222)
# numbers.insert(0, 789)
# numbers.insert(11, 201)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
# numbers.extend(extra)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# deleted = []
# deleted.append(numbers.pop())
# deleted.append(numbers.pop(0))
# deleted.append(numbers.pop(12))
# deleted.append(numbers.pop(7))
# print(numbers)
# print(sum(deleted))

# numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# numbers.remove(3)
# numbers.remove(5)
# numbers.remove(7)
# numbers.remove(9)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.sort(reverse=True)
# print(numbers)

# a = list(map(int, input().split()))
# a.reverse()
# print(a)

# a = list(map(int, input().split()))
# n = a.count(999)
# print(n)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# copy_numbers = numbers.copy()
# print(copy_numbers)

# s = input().upper().replace('', '-')
# s = s[0:s.index(' ') - 1] + ' ' + s[s.index(' ') + 2::]
# s = s[1:-1]
# print(s)

# s = input()
# a = s[0]
# b = s.index(' ') + 1
# c = a + '.' + s[b] + '.'
# d = s[::-1]
# d = d.index(' ')[::-1]
# e = s[d::-1]
#
# print(d)
# print(e)
# print(s)
# print(a, b)
# print(c)
# # print(d + ' ' + c)

# a, b, c = input().split()
# print(f'{c} {a[0]}.{b[0]}.')

# s = input()
# print(s.replace(' ', '\n', 999))

# a = 50000  # банк
# b = 2000  # ставка
# a -= b # -2000, ставка. Далі йде підсумок: або  банк + (ставка помножена на коеф), або банк - ставка
# a += b * 1.78  # ЛАЦІО
# print(a, 'ЛАЦІО')
# a -= b
# a += b * 1.89  # КОПЕНГАГЕН
# print(a, 'КОПЕНГАГЕН')
# a -= b
# a += b * 1.97  # РЕД СТАР
# print(a, 'РЕД СТАР')
# a -= b
# print(a, 'аллоа')
# a -= b
# a += b * 1.83  # ЧЕСТЕРФІЛД
# print(a, 'ЧЕСТЕРФІЛД')
# a -= b
# a += b * 1.86  # ГРУЗІЮ
# print(a, 'ГРУЗІЮ')
# a -= b
# a += b * 1.97  # СЛОВЕНІЮ
# print(a, 'СЛОВЕНІЮ')
# a -= b
# print(a, 'еспаньол')
# a -= b
# a += b * 1.75  # ЗАКАТЕКАС
# print(a, 'ЗАКАТЕКАС')
# a -= b
# a += b * 2.08  # АЛЬБАСЕТЕ
# print(a, 'АЛЬБАСЕТЕ')
# a -= b
# print(a, 'литву')
# a -= b
# print(a, 'мажейкю')
# a -= b
# a += b * 1.7  # РІТАС
# print(a, 'РІТАС')
# a -= b
# a += b * 1.81  # БЕНФІКУ
# print(a, 'БЕНФІКУ')
# a -= b
# print(a, 'барселону')
# a -= b
# a += b * 1.72  # РАПІД
# print(a, 'РАПІД')
# a -= b
# print(a, 'мідтьюланд')
# a -= b
# a += b * 1.87  # ОДІШІ
# print(a, 'ОДІШІ')
# a -= b
# print(a, 'крайову')
# print()
# print(a, ' - банк після 19 ставок по 2000')
# print('Банк збільшився на', (a / 50000 * 100) - 100, '%', 'або на', 19 / ((a / 50000 * 100) - 100), 'в середньому % на день' )
# print(6460, ' - профіт за 19 днів')
# print((a - 50000) / 19, ' - профіт в середньому за день')