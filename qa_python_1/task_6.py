types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

'''
Метод удаления дубликатов в словарях.
Проверяет наличие значения списка из словаря в созданном списке, если значение отсутствует - добавляет его в список 
уникальных значений и в временный список, после итерации по value словаря collection, в словарь result по key collection
добавляется созданный нами список temp, после temp обнуляется, по окончанию итераций по словарю collection, возвращаем
полученный список result
'''
def remove_duplicate(collection):
    uniq = []
    temp = []
    result = {}

    for key,value in collection.items():
        for i in value:
            if i not in uniq:
                uniq.append(i)
                temp.append(i)

        result[key] = temp
        temp = []

    return result

'''
Метод соединения 2ух словарей по типу {значение ключа первого словаря: значение ключа второго словаря}.
Проверяет что если ключ из первого словаря == ключу из второго словаря, то в result добавляем запись
'''
def combining_dictionaries(types, tickets):
    result = {}

    for key_types,value_types in types.items():
        for key_tickets,value_tickets in tickets.items():
            if key_types == key_tickets:
                result[value_types] = value_tickets

    return result


print(combining_dictionaries(types, remove_duplicate(tickets)))
