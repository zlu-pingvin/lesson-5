# _str = 'test'
# _int = 2
# _fl = 3.1
# _bl = _fl > 2
# _bl = _fl < _int
# _lst = [1, 2, 3, 4]
# _dict = {'car1': 3, 'car2': 4}
# print(_dict['car1'])
# _tuple = (1, 2, 5, 'test')
# print(_tuple[3], _tuple[2])
#
# num_str = 125
# num_str = str(num_str)
# # print(num_str + 1)
#
# s = 'Hi, my name is Python!'
# s = s.replace('y', 'O')
# s = s.replace('i', '1')
# print(s)
#
# print()
#
# split_test = 'This is a split test'
# split_test = split_test.split()
# print(split_test)
# string_join = ''.join(split_test)
# print(string_join)
# print(len(string_join))
#
# print()
#
# list_append = [1, 2, 3]
# list_append.append(4)
# list_append.append(5)
# print(list_append)
#
# list_extend = [4, 5, 6]
# list_extend.extend([7, 8, 9])
# print(list_extend)
# print(list_extend.index(6))
# print(len(list_extend))
#
# print()
#
# dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
# print(dict_test['car'], dict_test['where'])
# print(dict_test.keys(), dict_test.values())
# print(dict_test.items())

#######
#
# pas = 'password123'
# n = input('Введіть пароль: ')
# if n == pas:
#     print('Ви увійшли в систему')
# else:
#     print('Неправильний пароль')
#
# _dict = {1: 'Понеділок', 2: 'Вівторок', 3: 'Середа', 4: 'Четвер', 5: 'П"ятниця', 6: 'Субота', 7: 'Неділя'}
# n = int(input('Вкажіть число від 1 до 7: '))
# if n < 1 or n > 7:
#     print('Помилка')
# else:
#     print(_dict[n])
#
# n = int(input())
# for i in range(1, 11):
#     print(n * i)
#
# lst = [1, 2, 3, 4, 5]
# summ = 0
# for i in lst:
#     summ += i
# print(summ)
#
# n = int(input())
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)
#
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)
#
# n = 1
# for i in range(1, 123):
#     if n % 1 == 0 and n % i == 0:
#         print(i)
#         n += 1

###############

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst.extend([10, 20])
# lst.remove(10)
# print(lst)
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 0
# for i in lst:
#     n += i
# print(n)
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 0
# for i in lst:
#     n += i * 2
# print(n)
#
# s = ("яблуко", "банан", "апельсин")
# print(s[0], s[1], s[2], sep='\n')
#
# s1 = (1, 2, 3, 4)
# s2 = (5, 6, 7, 8, 9, 14)
# s3 = s1 + s2
# print(s3)
#
# dict = {'ім"я':'Хуан Себастьян', 'команда':'Лаціо', 'вік':25, 'національність':'аргентинець'}
# dict.update({'прізвисько':'Відьмак'})
# print(dict)
# print(dict['команда'], ',', dict['вік'])

#################

# import Calculator
# print(Calculator.add(2, 4))
#
# import Utilities
#
# n = [2, 3, 8, 6]
# print(Utilities.calculate_average(n))
# print(Utilities.find_max(n))

# class Person:
#     name = 'Murloc'
#     species = 'cat'
#     age = 13
#     make_sound = 'miau'
# Animal1 = Person()
# Animal2 = Person()
#
# Animal1.make_sound = 'krya'
# Animal2.make_sound = 'kuvi-kuvi'
# print(Animal1.make_sound)
# print(Animal2.make_sound)
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# n1 = Rectangle(3, 4)
# n2 = Rectangle(int(input()), int(input()))
#
# s = n1.width * n1.height
# print(s)

#############

# class Vehicle:
#     make = 'bmw'
#     model = 'x5'
#     year = 2024
#
# class Car(Vehicle):
#     fuel_type = 'gasoline'
#     start_engine = 'dvs'
#     make = 'hd'
#
# class Motorcycle(Car):
#     _type = 'enduro'
#     make = 'hd'
#
#
# class Bicycle(Motorcycle):
#     wheel_size = 29
#     _type = 'hard tail'
#
# res = Bicycle()
# print(res.year)
# print(res.model)
# print(res.make)

# class Vehicle:
#     """Це базовий клас"""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, color):
#         super().__init__(make, color)
#         self.color = color
#
# class Bicycle(Car):
#     def __init__(self, model, year):
#         super().__init__(year, color)
#         self.model = model
#


