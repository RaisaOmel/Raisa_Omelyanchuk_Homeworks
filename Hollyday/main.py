from dataclasses import dataclass, field
import csv


@dataclass
class Order:
    fio: str
    price: float
    order: dict
    id: int = field(init=False, default=0)
    ID = 0

    def __post_init__(self):
        if self.id == 0:
            Order.ID += 1
            self.id = Order.ID


@dataclass
class Menu:
    name: str
    menu: dict


@dataclass
class Dish:
    name: str
    norm: dict


@dataclass
class Product:
    name: str = ''
    kol: float = 0
    summ: float = 0


@dataclass
class Employee:
    fio: str = ''
    job: str = ''
    salary: float = 0
    id: int = field(init=False, default=0)
    ID = 0

    def __post_init__(self):
        if self.id == 0:
            Employee.ID += 1
            self.id = Employee.ID


sotr = {}
prod = {}
dish = {}
menu = {}
check = {}
try:
    with open('sotrud.csv', 'r', encoding='windows-1251') as file:
        lst = csv.reader(file, delimiter=';')
        for row in lst:
            Employee.ID = int(row[3]) - 1
            sotr[int(row[3])] = Employee(row[0], row[1], float(row[2]))
except:
    print('ошибка с работой файлом сотрудники')

try:
    with open('product.csv', 'r', encoding='windows-1251') as file:
        lst = csv.reader(file, delimiter=';')
        for row in lst:
            prod[row[0]] = Product(row[0], float(row[1]), float(row[2]))
except:
    print('ошибка с работой файлом продукты')

try:
    with open('dish.csv', 'r', encoding='windows-1251') as file:
        lst = csv.reader(file, delimiter=';')
        for row in lst:
            dish[row[0]] = Dish(row[0], eval(row[1]))
except:
    print('ошибка с работой файлом блюд')

try:
    with open('menu.csv', 'r', encoding='windows-1251') as file:
        lst = csv.reader(file, delimiter=';')
        for row in lst:
            menu[row[0]] = Menu(row[0], eval(row[1]))
except:
    print('ошибка с работой файлом меню')

try:
    with open('order.csv', 'r', encoding='windows-1251') as file:
        lst = csv.reader(file, delimiter=';')
        for row in lst:
            Order.ID = int(row[3]) - 1
            check[int(row[3])] = Order(row[0], row[1], eval(row[2]))
except:
    print('ошибка с работой файлом чеки')

ust_tab = 1
ust_menu = 'ланч'

print('Добро пожаловать')
circle = True
while circle:
    print('--------------------')
    print('0....Выход')
    print('1....Установка смены')
    print('2....Сотрудники')
    print('3....Продукты')
    print('4....Блюда(норма)')
    print('5....Меню')
    print('6....Чек')
    print('9....закрытие смены (очистка Чеков)')

    num = input("введите пункт ")
    if num == '0':
        break
    elif num == '9':
        check = {}
    elif num == '1':
        ust_tab = 1
        ust_menu = 'ланч'
        print('укажите сотрудника введя что-нибудь')
        for key, val in sotr.items():
            elem = input(str(val.fio) + ' ')
            if len(elem) > 0:
                ust_tab = val.id
                break
        print('укажите меню введя что-нибудь')
        for key in menu.keys():
            elem = input(str(key) + ' ')
            if len(elem) > 0:
                ust_menu = key
                break
    elif num == '2':
        vvod = True
        while vvod:
            print('----------Сотрудники------------  0....Выход из ввода')
            elem = input('Введите фамилию, имя ')
            if elem.strip() == '0':
                break

            elem1 = input('Введите должность ')
            elem2 = input('Введите оклад ')

            if len(elem) == 0 or len(elem1) == 0 or not elem2.isdigit():
                print('Ошибка ввода')
                continue
            sotr[s.ID] = Employee(elem, elem1, float(elem2))
    elif num == '3':
        vvod = True
        while vvod:
            print('----------Продукты-----------  0....Выход из ввода')
            elem = input('Введите наименование продукта ')
            if elem.strip() == '0':
                break
            else:
                try:
                    elem1 = float(input('Введите количество (грамм, шт) '))
                except:
                    print('ошибка ввода')
                    continue
                try:
                    elem2 = float(input('Введите сумму '))
                except:
                    print('ошибка ввода')
                    continue
                # Проверяем есть ли такой продукт. если есть добавляем. Нет создаем
                p = prod.get(elem, False)
                if not p:
                    p = Product(elem, elem1, elem2)
                    prod[elem] = p
                else:
                    p.kol = round(p.kol + elem1, 3)
                    p.summ = round(p.summ + elem2, 2)

    elif num == '4':
        vvod = True
        while vvod:
            print('----------Блюда-----------  0....Выход из ввода')
            elem = input('Введите наименование ')
            if elem.strip() == '0':
                break
            else:
                dct = {}
                print('укажите состав (вводя норму в грамм) на нужные продукты')
                for key, val in prod.items():
                    elem1 = 0
                    try:
                        elem1 = round(float(input(str(key) + ' норма в грамм ')), 6)
                    except:
                        continue
                    if elem1 > 0:
                        dct[key] = round(elem1, 6)

                if len(dct) > 0:
                    dish[elem] = Dish(elem, dct)

                print(dish)
    elif num == '5':
        vvod = True
        while vvod:
            print('----------Меню-----------  0....Выход из ввода')
            elem = input('Введите наименование ')
            if elem.strip() == '0':
                break
            else:
                try:
                    elem1 = round(float(input('наценка,% ')), 2)
                except:
                    elem1 = 0

                dct = {}
                print('выберите блюда указав цену продажи')
                for key, val in dish.items():
                    elem2 = 0
                    seb = 0
                    for k, norm in val.norm.items():
                        # находим продукт по наименованию
                        p = prod[k]
                        # находим цену продукта
                        if p.kol == 0:
                            cen = p.summ
                        else:
                            cen = round(p.summ / p.kol, 2)

                        seb += round(cen * norm, 2)
                    elem2 += round(seb * (1 + elem1 / 100), 2)
                    try:
                        elem2 = round(float(input(str(key) + ' себестоимость=' + str(seb) + ', с наценкой ' + str(
                            elem2) + '. Продавать будете по цене ')), 2)
                    except:
                        continue

                    if elem2 > 0:
                        dct[key] = round(elem2, 6)

                if len(dct) > 0:
                    menu[elem] = Menu(elem, elem1, dct)

    elif num == '6':
        print(f'пробивает: {sotr[ust_tab].fio} по меню:{ust_menu}')
        dct = {}
        summ = 0
        print('----------Чек № ' + str(Order.ID + 1) + ' ----------- ')
        for key, val in menu[ust_menu].menu.items():
            # находим блюдо
            d = dish[key]
            try:
                elem = int(input(str(d.name) + ' по цене ' + str(val) + ' '))
            except:
                continue

            if elem > 0:
                price = round(elem * val, 2)
                dct[key] = [elem, price]
                summ += price

        if len(dct) > 0:
            print(f'чек на сумму {summ}')
            check[elem] = Order(ust_tab, summ, dct)

try:
    with open('sotrud.csv', 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for key, row in sotr.items():
            lst = []
            lst.append(row.fio)
            lst.append(row.job)
            lst.append(row.salary)
            lst.append(key)
            writer.writerow(lst)
except:
    print('ошибка с работой файлом сотрудники')

try:
    with open('product.csv', 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for key, row in prod.items():
            lst = []
            lst.append(key)
            lst.append(round(row.kol, 3))
            lst.append(round(row.summ, 2))
            writer.writerow(lst)
except:
    print('ошибка с работой файлом продукты')

try:
    with open('dish.csv', 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for key, row in dish.items():
            lst = []
            lst.append(key)
            lst.append(row.norm)
            writer.writerow(lst)
except:
    print('ошибка с работой файлом блюд')

try:
    with open('menu.csv', 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for key, row in menu.items():
            lst = []
            lst.append(key)
            lst.append(row.menu)
            writer.writerow(lst)
except:
    print('ошибка с работой файлом меню')

try:
    with open('order.csv', 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for key, row in check.items():
            lst = []
            lst.append(row.fio)
            lst.append(row.price)
            lst.append(row.order)
            lst.append(key)
            writer.writerow(lst)
except:
    print('ошибка с работой файлом чеки')
