# 9
"""Создать 4 фрукта.
Апельсин, яблоко, мандарин, банан
У всех фруктов есть сорт, список витаминов, цена, имя
У апельсина, мандарина, банана есть метод очистить
У яблока метод порезать
У банана есть характеристика: кол-во калия
Создать 4 объекта фрукта и использовать все доступные методы и характеристики
При вызове метода очистить, должно писаться имя фрукта
Например:
apple = Apple("sort", [a,b,c], 120, "apple")
apple.clear()
>>"apple очищен"
"""
class Fruits:
    def __init__(self,sort,vitamins,price,name):
        if vitamins is None:
            vitamins=[]
        self.name=name
        self.sort=sort
        self.vitamins=vitamins
        self.price=price

    def clear(self):
        pass

    def cut(self):
        pass
    def get_vitamin(self,vitamin):
        if vitamin:
            if self.vitamins.count(vitamin)==0:
                self.vitamins.append(vitamin)

    def del_vitamin(self,vitamin):
        if vitamin:
            self.vitamins.remove(vitamin)
class Apple(Fruits):
    def cut(self):
        print(f'{self.name} порезан')

class Banana(Fruits):
    def __init__(self,sort,vitamins,price,name,kalium=''):
        super().__init__(sort,vitamins,price,name)
        self.kalium=kalium

    def clear(self):
        print(f'{self.name} очищен')
class Orange(Fruits):
    def clear(self):
        print(f'{self.name} очищен')

class Mandarin(Fruits):
    def clear(self):
        print(f'{self.name} очищен')

apple=Apple('цитрон',['a','d','c'], 8,'apple')
apple.cut()
apple.clear()
banana=Banana('желтый',['c','e'], 5,'banana',0)
banana.cut()
banana.clear()
mandarin=Mandarin('красный',['a','c'], 6,'mandarin')
mandarin.cut()
mandarin.clear()
orange=Orange('зеленый',['a','c','e'], 7,'orange')
orange.cut()
orange.clear()
