neighbours_names = ['Вася', 'Ира', 'Антон', 'Арина', 'Женя']
neighbours_flats = [4, 9, 12, 16, 19]

# Объявлен пустой словарь, его нужно будет наполнить элементами,
# каждый из которых составлен по схеме "квартира: имя"
neighbours =  {}

# Допиши код сюда
for i in range(0, len(neighbours_names)):
    neighbours[neighbours_flats[i]] = neighbours_names[i]
    print(neighbours.get(neighbours_flats[i]) + ' живёт в квартире ' + str(neighbours_flats[i]))