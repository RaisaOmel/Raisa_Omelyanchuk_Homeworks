#2.	Вы разрабатываете систему управления магазином продуктов.
# У вас есть класс Product, представляющий продукт.
# Каждый продукт имеет имя, цену и количество на складе.
# Вам нужно реализовать методы для инициализации и обновления информации о продуктах.

#Ваша задача - создать методы класса Product, которые позволяют устанавливать начальные
# значения для продуктов и обновлять информацию о них.

# Кроме того, вы должны создать метод calculate_total_price,
# который вычисляет общую стоимость продуктов на складе.

class Product:
    def __init__(self,name,price,number):
        global dct
        self.name=name
        self.price=price
        self.number=number
        dct[self.name]=(self.price,self.number)

    def set_product(self, price=0,number=0):
        global dct
        if price!=0:
            self.price=price
        if number!=0:
            self.number=number
        dct[self.name] = (self.price, self.number)

    @staticmethod
    def calculate_total_price():
        global dct
        return sum([val[0]*val[1] for val in dct.values()])

dct={}
prod1=Product('apple',3.50,250)
print(dct)
prod2=Product('herry',23.50,30)
prod1.set_product(0,150)
print(dct)
print(f'на складе товара на сумму {Product.calculate_total_price()}')