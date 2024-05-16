bread = 27.5
orange = 43
fish = 152.8
wine = 99.99

num_bread = 1
num_orange = 0.85
num_fish = 1.63
num_wine = 2

price_bread = bread * num_bread
price_orange = orange * num_orange
price_fish = fish * num_fish
price_wine = wine * num_wine
total = price_bread + price_orange + price_fish + price_wine

str_bread = 'Хліб'
str_orange = 'Апельсини'
str_fish = 'Риба'
str_wine = 'Вино'
str_total = 'До сплати'

print(f'|{"Список покупок":^50}|')
print(f"|{'=' * 50}|")
print(f"|{'Товар'} {'Кількість':^35} {'Ціна':>8}|")
print(f"{'|'} {'|':>50}")
print(f"|{str_bread} {num_bread:^32.2f} {price_bread:>12.2f}|")
print(f"|{str_orange} {num_orange:^23.2f} {price_orange:>16.2f}|")
print(f"|{str_fish} {num_orange:^32.2f} {price_orange:>12.2f}|")
print(f"|{str_wine} {num_wine:^32.2f} {price_wine:>12.2f}|")
print()
print(f"|{str_total:>35}:{total:>14.2f}|")

