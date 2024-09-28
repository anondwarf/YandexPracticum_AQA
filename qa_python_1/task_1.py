import re

# Наша строка
string_example = '1h 45m,360s,25m,30m 120s,2h 60s'

# Использована библиотека re, по причине возможности разделить строку по нескольким параметрам
list_example = re.split('[, ]', string_example)

# Объявил переменную в которой будет храниться итоговое значение минут
result = 0

# Цикл проходит по элементам списка list_example
for item in list_example:

    """
    Условие проверяет наличие в элементе списка list_example подстрок
    'h' - часы
    'm' - минуты
    's' - секунды
    В зависимости от вхождения, в переменную хранящую итоговое значение минут добавляется результат вычислений
    """

    if 'h' in item:
        # Убираем из строки последний символ, преобразуем строку в число и умножаем на 60 - получаем минуты
       result += int(item[:-1]) * 60
    elif 'm' in item:
        # Убираем из строки последний символ и получаем минуты
        result += int(item[:-1])
    else:
        # Убираем из строки последний символ производим целочисленное деление на 60 - получаем минуты
        result += int(item[:-1]) // 60

# Вывод результата подсчета общего кол-ва минут в переданной строке
print(f'Общее количество минут: {result}m')