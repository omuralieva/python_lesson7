if __name__ == '__main__':
    a = (1, 2, [1, 4],)                 # создали объкет с ипом данных кортеж
    print(id(a))                        # вывели его id
    a[2].append(3)                      # добавили внего новый элемент
    print(a)                            # вывели измененный объект
    print(id(a))                        # вывели id измененного объекта
    a = (1, 3, [1, 4],)                 # создали другой кортеж
    print(id(a))                        # вывели его id

    print((a.index(3)))
    print((a.count(1)))

    d = {}
    d[1] = 1
    print(d)
    d = {'dict' : 1, 'dictionary' : 2}
    b = dict(short='dict', long='dictionary')
    c = dict([(1, 1), (2, 4)])
    l = dict.fromkeys(['a', 'b'])
    m = dict.fromkeys(['a','b'], 100)

    dict_sample = {'Company': 'Toyota', 'model': 'premio', 'year': '2012'}
    print(dict_sample.get('model'))              # дает доступ к элементам словаря
    print(dict_sample.items())                   # перебирает значение словаря
    print(dict_sample.keys())                    # возвращает ключи в словаре
    dict_sample.pop('year')                      # удаляет заданный ключ
    print(dict_sample)
    dict_sample.popitem()                        # удаляет последний ключ
    print(dict_sample)
    dict_sample_2 = {'Company': 'Toyota', 'model': 'premio', 'year': '2012'}
    del dict_sample_2['model']                   # еще один способ удаления(удобнее, если нужно удалить весь словарь)
    print(dict_sample_2)
    print(dict_sample_2.setdefault('year'))      # возвращает значене заданного ключа
    print(dict_sample_2.setdefault('age'))       # если заданного ключа нет, возвращает "None"
    dict_sample_3 = {'name': 'Ann', 'age': '18'}
    dict_sample_2.update(dict_sample_3)
    print(dict_sample_2)                         # добавляет один словарь в другой
    print(dict_sample_2.values())                # возвращает значения в словаре




