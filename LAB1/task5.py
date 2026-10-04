distance = float(input())
consumption = float(input())
price_per_liter = float(input())

fuel = distance * consumption / 100
cost = fuel * price_per_liter

print(f"Топливо: {fuel:.2f} л")
print(f"Стоимость: {cost:.2f} руб")