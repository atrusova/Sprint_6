import random as r


def generate_phone_number():
    return f'+7{r.randint(1000000000, 9999999999)}'


names = ['Валера', 'Иван', 'Инокентий', 'Гена', 'Женя', 'Саша']
surnames = ['Пеньков', 'Иванов', 'Березкин', 'Сидоров', 'Рохин', 'Васильев']
addresses = ['Ленинский 1', 'Гурзуфская 5', 'Щорса 8', 'Соснова 9', 'Фрунзе 17']
metro = [1, 5, 16, 40, 115]


def generate_order_info():
    order_dict_info = {
        'name': r.choice(names),
        'surname': r.choice(surnames),
        'address': r.choice(addresses),
        'metro': r.choice(metro),
        'phone': generate_phone_number(),
        'comment': 'позвонить за 15 мин'
    }
    return order_dict_info
