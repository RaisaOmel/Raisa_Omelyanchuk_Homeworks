#Создайте класс Фрукт, его свойствами будет: название фрукта, цвет и размер.
#- создайте метод, который будет выводить название и цвет фрукта
#- создайте абстрактный метод, который будет реализован в классах-потомках
# Также создайте от класса Фрукт несколько потомков для которых будет определено: страна от куда приехал фрукт (private)
#- создайте метод, который будет выводить название фрукта и страну от куда он приехал, цвет, размер (он класса-родителя через super)
#- придумайте любой метод, который бы реализовывал абстрактный метод класса-родителя
from abc import ABC, abstractmethod
class Fruits(ABC):
    NAME='fruits'
    def __init__(self,name,size,color):
        self.name=name
        self.size=size
        self.color=color

    def info(self):
        return f'{self.name} {self.color} цвета'

    @abstractmethod
    def set_ripeness(self):
        pass

class Banan(Fruits):
    def __init__(self,name,size,color,country):
        super().__init__(name,size,color)
        self.__country=country

    def info(self):
        return f"{super().NAME} {self.name} from {self.__country} {self.color} color and {self.size} size"

    def set_ripeness(self,ripeness ):
        self.ripeness=ripeness


class Apple(Fruits):
    def __init__(self, name, size, color, country):
        super().__init__(name, size, color)
        self.__country = country

    def info(self):
        return f"{super().NAME} {self.name} from {self.__country} {self.color} color and {self.size} size"

    def set_ripeness(self, ripeness):
        self.ripeness = ripeness

apple=Apple('apple "Sir"','lange','green','Poland')
apple.set_ripeness('overripe')
print(apple.info(),apple.ripeness)
banan=Banan('banan "Mersy"','average','yellow','Congo')
banan.set_ripeness('unripe')
print(banan.info(),banan.ripeness)