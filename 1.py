# Ввод:
# 6
# Курск
# Калуга
# Анапа
# Анапа
# Абинск
# Курск
def count(cities):
    citi = set(cities)
    return len(citi)

n = int(input("Введите количество городов: "))

cities = []
print("Введите названия городов:")
for _ in range(n):
    city = input()
    cities.append(city)

result = count(cities)
print("Количество городов, названия которых повторяются:", result)

#Самая недооценённая задача..