my_dict = {}
for _ in range(int(input())): # Вводим кол-во стран
    country, *cities = input().split() # Вводим страны и города, первое слово будет ключ, а последующие значениями
    my_dict[country] = cities # Добавляем в словарь и присваиваем к переменной cities

for _ in range(int(input())): # Вводим кол-во городов
    city = input() # Перечисляем города
    for country, cities in my_dict.items():# Проходим по ключ-значениям словаря, items возвращает объект и получаем
        # ключ-значение
        if city in cities: # Если введённый город есть в значениях cities
            print(country) # Выводит страну этого города