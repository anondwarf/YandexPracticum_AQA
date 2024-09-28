world_champions = {2002: 'Бразилия', 2006: 'Италия', 2010: 'Испания', 2014: 'Германия', 2018: 'Франция',
                   2022: 'Аргентина'}

country = 'Италия'

# цикл перебирает ключи и значения коллекции world_champions и выводит на экран
for key, value in world_champions.items():
    print(key, '-', value)

# проверка наличия country в коллекции world_champions и вывод результата на экран
if country in world_champions:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')