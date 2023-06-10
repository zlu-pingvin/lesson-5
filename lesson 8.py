# list = []
# for i in range(1, 51):
#     list.append(i ** 2)
# print(list)

# list = []
# for i in range(int(input())):
#     list.append(int(input()))
# print(list)

# print([int(input()) for i in range(int(input()))])

# list = []
# plus = []
# for i in range(10):
#     n = input()
#     list.append(int(n))
#     if int(n) > 0:
#         plus.append(int(n))
# print(list)
# print(*plus, sep='\n')

# n = input().split()
# a = []
# for i in n:
#     a.append(int(i))
# print(a)

n = input()
s = []
x = 0
if len(n) < 4:
    print(n)
elif len(n) > 5:
    for i in n:
        s.append(i)
        if len(s) == 1:
            s.append(',')
            x = len(s)
        if x + 3 == len(s):
            s.append(',')
            x = len(s)
elif len(n) == 5:
    for i in n:
        s.append(i)
        if len(s) == 2:
            s.append(',')
elif len(n) == 4:
    for i in n:
        s.append(i)
        if len(s) == 1:
            s.append(',')
s = ''.join(s)
s.replace(' ', '')
if s[-1] == ',':
    print(s[:-1])


    elif len(n) > 5:
        n = reversed(n)
        for i in n:
            s.append(i)
            if len(s) == 1:
                s.append(',')
                x = len(s)
            if x + 3 == len(s):
                s.append(',')
                x = len(s)
        if s[-1] == ',':
            return s[:-1]
        else:
            return s

